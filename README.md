# AI-Whole-Book-Summarizer

This project leverages a fine-tuned version of Google's T5 transformer on the BookSum dataset to summarize entire books. The model processes PDF files, cleans and splits the content, and recursively generates summaries until a desired summary length is achieved.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Backend Setup](#backend-setup)
    - [Frontend Setup](#frontend-setup)
4. [Usage](#usage)

## Project Overview

This project is designed to read a book from a PDF file, clean the text to remove noise (such as the table of contents and other unwanted parts), and split the book into fixed-size chunks (1024 words). Each chunk is passed through the T5 model to generate a summary. These individual summaries are then recombined to create a single comprehensive summary of the book. The summarization function is recursively called, treating the combined summary as a new book to be summarized further until it reaches the base case (a summary length of 7 chunks).

Additionally, a website has been created for user interaction, utilizing React for the frontend and Flask for the backend.

## Features

* **PDF Book Summarization**: Automatically summarizes entire books from PDF files.
* **Text Cleaning**: Removes noise such as the table of contents and other unwanted parts.
* **Recursive Summarization**: Refines the summary until a concise version of the book is obtained.
* **User-Friendly Interface**: Provides a web interface for easy interaction with the summarization model.

## Installation

### Prerequisites

- Python 3.7 or higher
- Node.js
- Yarn

### Backend Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/ahmadhanyy/Ai-Whole-Book-Summarizer.git
    cd Ai-Whole-Book-Summarizer/backend
    ```

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Run the Flask app:

    ```sh
    python app.py
    ```

### Frontend Setup

1. Navigate to the frontend directory:

    ```sh
    cd ../frontend
    ```

2. Install the required Node.js packages:

    ```sh
    yarn install
    ```

3. Start the development server:

    ```sh
    yarn dev
    ```

## Usage

1. Upload a PDF book through the web interface.
2. The backend processes the book, cleans the text, splits it into chunks, and generates a summary.
3. The summary is recursively refined until the desired length is achieved.
4. The final summary is returned and displayed to the user.
