# app.py

from flask import Flask, request, jsonify
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import fitz
import nltk
import torch
import os
import tempfile

# Initialize NLTK
#nltk.download('punkt')

app = Flask(__name__)

# Load The Model & Tokenizer
model_checkpoint = 'ahmadhany22/SF-FineTuned-T5'
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)

# Read a PDF file content
def read_pdf(pdf_file):
    document = fitz.open(pdf_file)
    all_text = []
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text()
        all_text.append(text)
    return "\n".join(all_text)

# Preprocess the book and split it into paragraphs of maximum size 1024 words
def split_book(book, paragraph_max_words=1024):
    book_paragraphs = []
    sentences = nltk.sent_tokenize(book)
    current_paragraph = []
    current_word_count = 0
    
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        word_count = len(words)
        
        if current_word_count + word_count <= paragraph_max_words:
            current_paragraph.append(sentence)
            current_word_count += word_count
        else:
            book_paragraphs.append(" ".join(current_paragraph))
            current_paragraph = [sentence]
            current_word_count = word_count
    
    if current_paragraph:
        book_paragraphs.append(" ".join(current_paragraph))
    
    return book_paragraphs

# Summarize the book recursively
def summarize_book(book):
    splited_book = split_book(book)
    summary_list = []
    for paragraph in splited_book:
        inputs = tokenizer(paragraph, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(inputs.input_ids, 
                                     max_length=256,
                                     min_length=40,
                                     length_penalty=2.0,
                                     num_beams=4,
                                     early_stopping=False,
                                     no_repeat_ngram_size=3)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summary_list.append(summary)
    summarized_book = " ".join(summary_list)
    return summarized_book

# Route to handle PDF upload and summarization
@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
            file.save(temp_file.name)
            temp_path = temp_file.name

        # Read the uploaded PDF
        book_content = read_pdf(temp_path)

        # Summarize the book
        summary = summarize_book(book_content)

        # Clean up temporary file
        os.remove(temp_path)

        return jsonify({'summary': summary})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
