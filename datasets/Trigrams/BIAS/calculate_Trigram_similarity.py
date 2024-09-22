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

files_names = ["GROUP1_VS_GROUP2_anti_sematisim", "GROUP1_VS_GROUP2_entertainment_prompts", "GROUP1_VS_GROUP2_hostile_to_values", "GROUP1_VS_GROUP2_Religioun", "GROUP1_VS_GROUP2_scientific_scholar_prompts", "GROUP1_VS_GROUP2_terrorism", "GROUP1_VS_GROUP2_Women_suppressed_bias"]

for file in files_names:

    Test_file_path = f'C:/Users/algez/Downloads/ArabicSafetyProject1/datasets/Group1vsGroup2BiasDataset/{file}.csv'
    df2 = pd.read_csv(Test_file_path)
    data = df2.iloc[:, 0].tolist()

    with open(f'C:/Users/algez/Downloads/ArabicSafetyProject1/datasets/Trigrams/BIAS/{file}.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["prompt"]+["score"]*(len(data)-1))

        for i in tqdm(range(len(data)), desc="Generating Prompts"):
            similarities = []
            for j in range(len(data)):
                if(i != j):
                    similarities.append(trigram_similarity(data[i], data[j]))
            writer.writerow([data[i]] + similarities)