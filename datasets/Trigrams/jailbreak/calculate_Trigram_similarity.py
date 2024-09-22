import pandas as pd
import csv
from tqdm import tqdm
import nltk
from nltk.util import ngrams
from collections import Counter


def get_trigrams(text):
    trigrams = list(ngrams(text, 3))
    return trigrams

def trigram_similarity(text1, text2):
    trigrams1 = Counter(get_trigrams(text1))
    trigrams2 = Counter(get_trigrams(text2))

    common_trigrams = sum((trigrams1 & trigrams2).values())

    # Total number of trigrams
    total_trigrams = sum(trigrams1.values()) + sum(trigrams2.values())
    
    if total_trigrams == 0:
        return 0.0
    
    return 2 * common_trigrams / total_trigrams

files_names = ["Arab_culture_is_backwards_or_anti_modern_jailbreak", "arab_entertainment_prompts_jailbreak", "arab_scientific_collaboration_prompts_jailbreak", "arabs_are_hostile_to_westren_values_jailbreak", "Religion_jailbreak", "sarcastic_anti_semitism_prompts", "terrorism_jailbreak", "women_rights"]
for file in files_names:

    Test_file_path = f'C:/Users/algez/Downloads/ArabicSafetyProject1/datasets/jailbreak/data/{file}.csv'
    df2 = pd.read_csv(Test_file_path)
    data = df2.iloc[:, 0].tolist()

    with open(f'C:/Users/algez/Downloads/ArabicSafetyProject1/datasets/Trigrams/jailbreak/{file}.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["prompt"]+["score"]*(len(data)-1))

        for i in tqdm(range(len(data)), desc="Generating Prompts"):
            similarities = []
            for j in range(len(data)):
                if(i != j):
                    similarities.append(trigram_similarity(data[i], data[j]))
            writer.writerow([data[i]] + similarities)