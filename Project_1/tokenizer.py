import nltk
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import os 
# Download the stopwords and punkt tokenizer models if you haven't already
nltk.download('stopwords')
nltk.download('punkt')

def tokenize_and_count(text):
    # Tokenize words
    words = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalpha() and word not in stop_words]

    # Count occurrences
    word_count = Counter(filtered_words)

    return dict(word_count)

def get_tokenized_data(target):

    comp_files = os.listdir("data/"+target)
    #print(comp_files)
    parsed_data={}

    for comp_file in comp_files:
        full_path = "data/"+target+"/"+comp_file
        comp_name = comp_file.split(".")[0]

        with open(full_path) as fp:
            text  = fp.read()
            word_count_dict = tokenize_and_count(text)
            #print(word_count_dict)
            parsed_data[comp_name] = word_count_dict
        
    return parsed_data

def main():
    # Example
    
    parsed_fraud = get_tokenized_data("fraud")

    print(parsed_fraud)


if __name__ =="__main__":
    main()