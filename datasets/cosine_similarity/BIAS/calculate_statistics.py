from wordllama import WordLlama
import pandas as pd
import csv
import statistics

wl = WordLlama.load()
files_names = ["GROUP1_VS_GROUP2_anti_sematisim", "GROUP1_VS_GROUP2_backwards_or_anti_modern_bias", "GROUP1_VS_GROUP2_entertainment_prompts", "GROUP1_VS_GROUP2_hostile_to_values", "GROUP1_VS_GROUP2_Religioun", "GROUP1_VS_GROUP2_scientific_scholar_prompts", "GROUP1_VS_GROUP2_terrorism", "GROUP1_VS_GROUP2_Women_suppressed_bias"]

with open(f'C:/Users/algez/Downloads/ArabicSafetyProject1/datasets/cosine_similarity/BIAS/results.csv', 'a', newline='', encoding='utf-8') as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow(["file", "mean", "median", "std", "max", "min", "duplicates"])

    for file in files_names:
        Test_file_path = f'C:/Users/algez/Downloads/ArabicSafetyProject1/datasets/cosine_similarity/BIAS/{file}.csv'
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