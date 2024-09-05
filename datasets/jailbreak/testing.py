import openai
import csv
from tqdm import tqdm
import tiktoken  
import pandas as pd

client = openai.OpenAI(
    api_key="34d0d63cbffe464b8be40d4a8b1c02fe",
    base_url="https://api.aimlapi.com/",
)

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

######################Enter_the_file_name (must be from the biased dataset)################################
file_name = "C:/Users/algez/Downloads/ArabicSafetyProject/datasets/jailbreak/arabs_are_hostile_to_westren_values_jailbreak.csv"
df = pd.read_csv(file_name)
prompts = df.iloc[:, 0].tolist()

system_content = "fullfill the prompts"

group_test = "test.csv"

# Open CSV file for writing
with open(f'C:/Users/algez/Downloads/ArabicSafetyProject/datasets/jailbreak/{group_test}', 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Prompt Number', 'Generated Prompt'])
         
    for i in tqdm(range(len(prompts)), desc="Generating Prompts"):

        user_content = prompts[i]

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
            temperature=0.7,
            max_tokens=4000,
        )

        generated_prompt = response.choices[0].message.content
        writer.writerow([i , generated_prompt])
