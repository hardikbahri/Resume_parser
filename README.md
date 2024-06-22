# Resume Information Extraction using Python and NLTK

This Python script uses natural language processing (NLP) techniques to extract relevant information from resume PDFs. It utilizes NLTK (Natural Language Toolkit) for tokenization, part-of-speech tagging, named entity recognition, and more.

## Features

- **Extract Names**: Identifies person names mentioned in the resume.
- **Extract Phone Numbers**: Retrieves phone numbers present in the resume text.
- **Extract Emails**: Finds email addresses mentioned in the resume.
- **Extract Skills**: Identifies skills based on a predefined list and context.
- **Extract Education**: Retrieves educational institutions from the resume text.

## Dependencies

- Python 3.x
- NLTK library (`nltk`)
- PDFMiner library (`pdfminer.six`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. Install dependencies:

   ```bash
   pip install nltk
   pip install pdfminer.six
   ```

3. Download NLTK resources:

   ```bash
   python -m nltk.downloader punkt averaged_perceptron_tagger maxent_ne_chunker words stopwords
   ```

## Usage

1. Place your resume PDF file (`Resume.pdf`) in the project directory.
2. Run the script:

   ```bash
   python resume_parser.py
   ```

3. View extracted information:

   - Extracted Names
   - Phone Number
   - Email Address
   - Skills
   - Education Information

## Example Output

- Extracted Email: `john.doe@example.com`
- Extracted Names: `John Doe`
- Skills: `{'Python', 'Machine Learning', 'Data Science'}`
- Education Information: `{'University of ABC', 'College of XYZ'}`

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

