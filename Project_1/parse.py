
#from matplotlib import pyplot as plt

from tokenizer import get_tokenized_data


def parse_file_to_dict(file_name):
    print("Processing ", file_name)
    with open(file_name) as fp:
        comp_list = fp.readlines()
    line_num=0
    # Parse the data
    parsed_data = {}
    for line in comp_list:
        line = line.strip()
        if len(line) ==0:
            continue
        #print("Line", line_num)
        line_num+=1
    #for line in data.strip().split('\n'):
        company, words = line.split(':')
        word_counts = {}
        for word_count in words.split(';'):
            word, count = word_count.strip().split(' ')
            word_counts[word] = int(count[1:-1])
        parsed_data[company] = word_counts

    # # Display the parsed data
    # for company, word_counts in parsed_data.items():
    #     print(f"{company}:")
    #     for word, count in word_counts.items():
    #         print(f"  {word}: {count}")
    #     print()

    return parsed_data



def get_categorized_words(parsed_data, categories):
    # Categorize words from financial reports
    categorized_words = {}
    for company, words in parsed_data.items():
        categorized_words[company] = {}
        for category, category_words in categories.items():
            categorized_words[company][category] = {}
            for word in category_words:
                if word in words:
                    categorized_words[company][category][word] = words[word]

    # # Display the categorized words
    # for company, categories in categorized_words.items():
    #     print(f"{company}:")
    #     for category, words in categories.items():
    #         if words:
    #             print(f"  {category}:")
    #             for word, count in words.items():
    #                 print(f"    {word}: {count}")
    #     print()

    return categorized_words

import os 


def store_categories_to_files(category, category_words):

    with open("category/"+category+".txt", "w") as f:
        for w in  category_words:
            f.write(w+"\n")



def read_categories_from_files():
    categories = {}

    list_of_cat_files = os.listdir("category")
    for category_file in  list_of_cat_files:
        with open("category/"+category_file) as f:
            category = category_file.split('.')[0]
            categories[category] =[]
            lines = f.readlines()
            for w in lines:
                w = w.strip()
                if len(w)==0:
                    continue

                categories[category].append(w)
    return categories


def plot_word_data(word_data, output_dir="results_nonfraud"):
    # Plotting
    for company, data in word_data.items():
        words = list(data.keys())
        frequencies = list(data.values())
        
        plt.figure(figsize=(15, 6))
        plt.bar(words, frequencies, color='blue')
        plt.title(f"Word Frequency for {company}")
        plt.xlabel("Words")
        plt.ylabel("Frequency")
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.savefig(output_dir+"/"+company+".jpg")
        #plt.show()    


def get_tabular_result(categorized_words, output_file):
    # Convert nested dictionary to DataFrame with desired structure
    df_data = {}

    for company, categories in categorized_words.items():
        for category, words in categories.items():
            if category not in df_data:
                df_data[category] = {}
            df_data[category][company] = ", ".join(f"{word}:{count}" for word, count in words.items())

    df = pd.DataFrame(df_data)#.transpose()

    #print(df)
    df.to_csv(output_file)


import matplotlib.pyplot as plt
import pandas as pd
def main():
    
    # # Parse the data
    # parsed_data = {}

    # #get text from file

    
    # file_name = "Fraud.txt"

    # frauds = parse_file_to_dict(file_name)
    # file_name = "NonFraud.txt"

    # nonfrauds = parse_file_to_dict(file_name)

    frauds = get_tokenized_data("fraud")
    nonfrauds = get_tokenized_data("nonfraud")
    #print(frauds)
    #print(nonfrauds)




    # categories = {
    # 'Deceptive': ['except', 'although', 'however', 'withheld', 'cheating', 'excluding', 'but', 'yet'],
    # 'Litiguous': ['contracts', 'litigations', 'claims', 'settlements', 'sue', 'lawsuit', 'dispute', 'allegation'],
    # 'Uncertain': ['may', 'possible', 'might', 'uncertain', 'depends', 'likely', 'potentially', 'probability'],
    # 'Negative': ['loss', 'decline', 'uncertain', 'drop', 'fall', 'decrease', 'downturn', 'downsize'],
    # 'Financial': ['debt', 'lease', 'security', 'tax', 'equity', 'liability', 'asset', 'balance'],
    # 'Executives': ['president', 'CEO', 'trustee', 'board member', 'director', 'chief', 'officer', 'executive'],
    # 'Audit': ['appeal', 'claimants', 'audit', 'inspection', 'scrutiny', 'review'],
    # 'International': ['global', 'international', 'overseas', 'foreign', 'export', 'import'], # Add country names if needed
    # 'M&A': ['acquisition', 'acquired', 'merger', 'takeover', 'buyout', 'merge', 'purchase', 'deal'],
    # 'Misstatements': ['sustainable', 'renewable', 'margin', 'profit', 'exaggerate', 'overstate', 'inflate', 'misreport'],
    # 'Internal Controls': ['record keeping', 'books', 'accounting', 'collaboration', 'transition', 'ledger', 'document', 'protocol'],
    # 'Bribery': ['millions', 'trillions', 'dollars', 'revenue', 'bribe', 'kickback', 'gift', 'payoff']
    # }

    # for category in categories:
    #     store_categories_to_files(category, categories[category])


    categories = read_categories_from_files()
    print(categories)

    categorized_words_fraud = get_categorized_words(frauds, categories)

    categorized_words_nonfraud = get_categorized_words(nonfrauds, categories)

    plot_word_data(frauds, "results_fraud")
    plot_word_data(nonfrauds, "results_nonfraud")


    get_tabular_result(categorized_words_fraud, "Fraud_result.csv")
    get_tabular_result(categorized_words_nonfraud, "NonFraud_result.csv")

if __name__ == "__main__":
    main()