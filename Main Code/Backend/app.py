from flask import Flask, request, jsonify
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import fitz
import nltk
import torch
import os
import tempfile
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/upload": {"origins": "http://localhost:5173"}})

# Check if CUDA is available and set PyTorch to use GPU
if torch.cuda.is_available():
    device = torch.device("cuda")
    print('There are %d GPU(s) available.' % torch.cuda.device_count())
    print('We will use the GPU:', torch.cuda.get_device_name(0))
else:
    print('No GPU available, using the CPU instead.')
    device = torch.device("cpu")

# Load The Model & Tokenizer
model_checkpoint = r"ahmadhany22/SF-FineTuned-T5"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint).to(device)

# Read a PDF file content
def read_pdf(pdf_file):
    # Open the PDF file
    document = fitz.open(pdf_file)
    all_text = []

    # Extract text from each page
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text()
        all_text.append(text)
    return "\n".join(all_text)

# Preprocess the book and split it into paragraphs of maximum size 1024 words
def split_book(book, paragraph_max_words = 1024):
    book_paragraphs = []

    # Split the content into sentences
    sentences = nltk.sent_tokenize(book)

    # Delete sentences that contains stop words
    stop_words = ["Copyright", "Table Of Contents", "title Page", "All rights reserved", "www.", ".org", "@", "e-books", "ebook", "®", "ISBN:", "©",".com "]
    deleted_sentences = []

    # Loop through all the sentences
    for j in range(len(sentences)):
        # Check if the sentence is a table of content
        words = nltk.word_tokenize(sentences[j])
        chapter_counter = sum(1 for word in words if word.lower() == "chapter")
        stave_counter = sum(1 for word in words if word.lower() == "stave")
        part_counter = sum(1 for word in words if word.lower() == "part")
        digits_counter = sum(1 for word in words if word in ["three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"])
        number_counter = sum(1 for word in words if word in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
        romanian_counter = sum(1 for word in words if word in ["II", "III", "IV", "VI", "VII", "XII"])

        # Delete the sentence if it is a table of content
        if chapter_counter > 3 or stave_counter > 3 or part_counter > 8 or digits_counter > 10 or number_counter > 10 or romanian_counter > 6:
            deleted_sentences.append(j)

        # Delete the sentence if it contains stop words
        for i in range(len(stop_words)):
            if stop_words[i].lower() in sentences[j].lower() and j not in deleted_sentences:
                deleted_sentences.append(j)

    # Delete sentences from the end to the beginning
    for i in range(len(deleted_sentences)):
        del sentences[deleted_sentences[len(deleted_sentences) - (i + 1)]]

    # Iterate through each sentence
    current_paragraph = []
    for sentence in sentences:
        words = sentence.split()
        # Check if adding the current sentence exceeds the word limit
        if len(current_paragraph) + len(words) <= paragraph_max_words:
            current_paragraph.extend(words)
        else:
            # Add the paragraph to array of paragraphs
            ready_paragraph = ' '.join(current_paragraph)
            book_paragraphs.append(ready_paragraph)
            # Reset current paragraph
            current_paragraph = words

    # Check if there is a last paragraph that hasn't been added
    if current_paragraph:
        # Add the paragraph to array of paragraphs
        ready_paragraph = ' '.join(current_paragraph)
        book_paragraphs.append(ready_paragraph)

    return book_paragraphs


# Summarize the book recursively
def summarize_book(book):
    # Split the book into paragraphs
    splited_book = split_book(book)
    if len(splited_book) <= 5: # Base case
        result_book = " ".join(splited_book)
        return result_book
    else:
        summary_list = []
        for i in range(len(splited_book)): # Loop through all paragraphs to generate summaries
            # Generate summary for each paragraph
            # Tokenize the input text
            inputs = tokenizer(splited_book[i], return_tensors="pt", max_length=1024, truncation=True)
            # Generate summary
            summary_ids = model.generate(inputs.input_ids.to(model.device), max_length=256, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=False, no_repeat_ngram_size=3)
            # Decode the summary tokens
            summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            # Add to summary list
            summary_list.append(summary)
        # Combine all summarise into a single paragraph
        summarized_book = "<br><br>".join(summary_list)
        # Recursively summarize the generated book
        return summarize_book(summarized_book)

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
