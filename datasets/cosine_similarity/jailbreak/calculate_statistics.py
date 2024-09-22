from wordllama import WordLlama
import pandas as pd
import csv
import statistics

wl = WordLlama.load()
counter = 0
files_names = ["Arab_culture_is_backwards_or_anti_modern_jailbreak", "arab_entertainment_prompts_jailbreak", "arab_scientific_collaboration_prompts_jailbreak", "arabs_are_hostile_to_westren_values_jailbreak", "Religion_jailbreak", "sarcastic_anti_semitism_prompts", "terrorism_jailbreak", "women_rights"]

with open(f'C:/Users/algez/Downloads/ArabicSafetyProject1/datasets/cosine_similarity/jailbreak/results.csv', 'a', newline='', encoding='utf-8') as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow(["file", "mean", "median", "std", "max", "min"])

    for file in files_names:
        Test_file_path = f'C:/Users/algez/Downloads/ArabicSafetyProject1/datasets/cosine_similarity/jailbreak/{file}.csv'
        df2 = pd.read_csv(Test_file_path)
        rows, coloumns = df2.shape
        
        data = []
        dublicates = 0

        for i in range(rows):
            for j in range(coloumns - 1):
                data.append(df2.iloc[i,j + 1])

        for i in range(len(data)):
            if(data[i] >= 1):
                dublicates += 1
        
        writer.writerow([file, statistics.mean(data), statistics.median(data), statistics.stdev(data), max(data), min(data), dublicates])