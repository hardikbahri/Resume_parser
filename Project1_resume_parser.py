import nltk  
import re   #pattern matching
from pdfminer.high_level import extract_text

#pdfminer->Extracting text from pdf
#extract_text-> extracted text as a string

nltk.download('punkt')   #tokenizer
nltk.download('averaged_perceptron_tagger')  #pos for each word
nltk.download('maxent_ne_chunker')    #ner-> named entities
nltk.download('words')
nltk.download('stopwords')

# Extracting text from the pdf
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)  #whole text of the pdf returned as string


# Extracting the names from the text
def extract_names(txt):
    person_names = []

    for sent in nltk.sent_tokenize(txt): #to split the text into sentences.
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))): # Extracting named entities from the text
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':  
                person_names.append(
                    ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())##
                )
    return person_names




#Extracting the phone number
PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]') #makes a regular expression into an obj
# may start with + or (
# start with digit 1-9 
#middle -> 8 or more occcurenes of digits 0-9,etc.
# end with 0-9

def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text) #comapring PHONE REG and text, and finds all occurences

    if phone:
        number = ''.join(phone[0])

        if resume_text.find(number) >= 0 and len(number) < 20:
            return number
    return None




#Extracting email address
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')

def extract_emails(resume_text):
    return re.findall(EMAIL_REG, resume_text)




#Extracting skills
SKILLS_DB = [
    'machine learning',
    'Deep Learning',
    'data science',
    'python',
    'word',
    'excel',
    'English',
    'c',
    'C++',
    'HTML',
    'sql',
    'matlab',
    'javascript',
    'office',
    'React',
    'Node.js',
    'MySQL',
]



def extract_skills(input_text):
    # retrieves a list of english stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))  #english txt file

    # tokenizing involves splitting sentences and words from the body of the text.
    word_tokens = nltk.tokenize.word_tokenize(input_text) #word tokenize


    filtered_tokens = [w for w in word_tokens if w not in stop_words]

    # remove the punctuation
    filtered_tokens = [w for w in word_tokens if w.isalpha()] #it should be alph, not punc or num

    # generate bigrams and trigrams (such as artificial intelligence)
    #below line
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))
    # nltk.everygrams(sequence, min_len, max_len),
    #all possible tokens of 2 and 3 len
    
    # we create a set to keep the results in.
    found_skills = set()

    # we search for each token in our skills database
    for token in filtered_tokens:
        if token.lower() in SKILLS_DB:
            found_skills.add(token)  #unigram

    # we search for each bigram and trigram in our skills database
    for ngram in bigrams_trigrams:
        if ngram.lower() in SKILLS_DB:
            found_skills.add(ngram)
## Adding both tokens and ngrams to found skill set.
    return found_skills




#Extracting Education
RESERVED_WORDS = [
    'school',
    'college',
    'univers',
    'academy',
    'faculty',
    'institute',
    'faculdades',
    'Schola',
    'schule',
    'lise',
    'lyceum',
    'lycee',
    'polytechnic',
    'kolej',
    'ünivers',
    'okul',

]





def extract_education(input_text):
    organizations = []

    # first get all the organization names using nltk
    for sent in nltk.sent_tokenize(input_text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'ORGANIZATION':
                organizations.append(' '.join(c[0] for c in chunk.leaves()))

    # we search for each bigram and trigram for reserved words
    # (college, university etc...)
    education = set()
    for org in organizations:
        for word in RESERVED_WORDS:
            if org.lower().find(word) >= 0: #if lowercase version matches the reserved words
                education.add(org)

    return education


if __name__ == '__main__': #to execute some code only if the file was run directly, and not imported.
    text = extract_text_from_pdf('Resume.pdf')
    education_information = extract_education(text)
    skills = extract_skills(text)
    names = extract_names(text)
    phone_number = extract_phone_number(text)
    emails = extract_emails(text)


if emails:
        print(emails[0])

if names:
        print(names[0] + ' ' + names[1]) # first and second name

if skills:
    print('Skills: ' + str(skills))

if education_information:
    print(education_information)








