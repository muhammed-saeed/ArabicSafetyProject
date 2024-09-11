import openai
import os
import pandas as pd
from tqdm import tqdm  # For progress bar
import tiktoken  # Token counting (ensure you have the right tokenizer installed)

# Initialize the OpenAI client
openai.api_key = "1e6fe734c99e4e39860cb9bd1d975175"
client = openai.OpenAI(api_key=openai.api_key, base_url="https://api.aimlapi.com/")

# Define the source and target directories
source_folder = '/Users/muhammedsaeed/Desktop/ArabicSafetyProject/datasets/jailbreak/data'
target_base_folder = '/Users/muhammedsaeed/Desktop/ArabicSafetyProject/datasets/jailbreak/Obfuscation'
target_language = 'Zulu'
language_folder = os.path.join(target_base_folder, target_language)

# Create the target language subfolder if it doesn't exist
os.makedirs(language_folder, exist_ok=True)

# Initialize GPT-4 tokenizer
encoding = tiktoken.encoding_for_model("gpt-4")

# Function to count tokens in a row using GPT-4 tokenizer
def count_tokens(text):
    return len(encoding.encode(text))

# Function to translate a single row using OpenAI GPT
def translate_text_gpt(row_text, max_tokens):
    user_prompt = f"Translate the following text into Zulu:\n\n'{row_text}'"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who translates text into Zulu."},
            {"role": "user", "content": user_prompt},
        ],
        max_tokens=max_tokens+15,
        temperature=0.7
    )
    translation = response.choices[0].message.content
    return translation.strip()

# Function to translate a single CSV file and save it row by row using pandas
def translate_and_save_file(file_path, target_folder):
    file_name = os.path.basename(file_path)
    translated_file_path = os.path.join(target_folder, file_name)

    # Read CSV file into pandas DataFrame
    df = pd.read_csv(file_path)

    # Calculate the max tokens needed for this file
    max_tokens = max(df.apply(lambda row: count_tokens(' '.join(map(str, row))), axis=1)) + 50  # Buffer for the prompt

    # Translate rows with progress tracking
    for i, row in tqdm(df.iterrows(), desc=f"Translating {file_name}", total=len(df)):
        row_text = ' '.join(map(str, row))  # Convert row to a single text string
        translated_row_text = translate_text_gpt(row_text, max_tokens)

        # Ensure that the translated row fits into the DataFrame's structure
        translated_row = [translated_row_text]  # Adjust depending on how you want to handle the translation

        # Check if the number of columns matches
        if len(translated_row) != len(df.columns):
            # Handle the mismatch: either split the translated text or join it into one column
            translated_row = [translated_row_text]  # For simplicity, we store the entire translation as one string

        # Assign translated row back to the DataFrame
        df.iloc[i] = translated_row

    # Save the translated DataFrame to CSV
    df.to_csv(translated_file_path, index=False)

# Process all CSV files in the source folder
csv_files = [file_name for file_name in os.listdir(source_folder) if file_name.endswith('.csv')]
for file_name in tqdm(csv_files, desc="Processing CSV files"):
    file_path = os.path.join(source_folder, file_name)
    translate_and_save_file(file_path, language_folder)

print(f"All CSV files have been translated into Zulu and saved in {language_folder}.")
