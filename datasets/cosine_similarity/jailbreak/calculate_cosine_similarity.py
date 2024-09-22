from wordllama import WordLlama
import pandas as pd
import csv
from tqdm import tqdm

wl = WordLlama.load()

files_names = ["Arab_culture_is_backwards_or_anti_modern_jailbreak", "arab_entertainment_prompts_jailbreak", "arab_scientific_collaboration_prompts_jailbreak", "arabs_are_hostile_to_westren_values_jailbreak", "Religion_jailbreak", "sarcastic_anti_semitism_prompts", "terrorism_jailbreak", "women_rights"]
for file in files_names:

    Test_file_path = f'C:/Users/algez/Downloads/ArabicSafetyProject1/datasets/jailbreak/data/{file}.csv'
    df2 = pd.read_csv(Test_file_path)
    data = df2.iloc[:, 0].tolist()

    with open(f'C:/Users/algez/Downloads/ArabicSafetyProject1/datasets/cosine_similarity/jailbreak/{file}.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["prompt"]+["score"]*(len(data)-1))

        for i in tqdm(range(len(data)), desc="Generating Prompts"):
            similarities = []
            for j in range(len(data)):
                if(i != j):
                    similarities.append(wl.similarity(data[i], data[j]))
            writer.writerow([data[i]] + similarities)
