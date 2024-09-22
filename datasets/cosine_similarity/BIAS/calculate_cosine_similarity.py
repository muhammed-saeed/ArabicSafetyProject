from wordllama import WordLlama
import pandas as pd
import csv
from tqdm import tqdm

wl = WordLlama.load()

files_names = ["GROUP1_VS_GROUP2_hostile_to_values"]
for file in files_names:

    Test_file_path = f'C:/Users/algez/Downloads/ArabicSafetyProject1/datasets/Group1vsGroup2BiasDataset/{file}.csv'
    df2 = pd.read_csv(Test_file_path)
    data = df2.iloc[:, 1].tolist()

    with open(f'C:/Users/algez/Downloads/ArabicSafetyProject1/datasets/cosine_similarity/BIAS/{file}.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["prompt"]+["score"]*(len(data)-1))

        for i in tqdm(range(len(data)), desc="Generating Prompts"):
            similarities = []
            for j in range(len(data)):
                if(i != j):
                    similarities.append(wl.similarity(data[i], data[j]))
            writer.writerow([data[i]] + similarities)
