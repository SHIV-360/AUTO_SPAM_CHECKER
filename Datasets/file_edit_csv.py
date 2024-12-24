# import pandas as pd

# # Load the CSV file
# input_file = "spam_ham.csv"  # Replace with your CSV file path
# output_file = "new_spam.csv"  # Replace with the desired output file path

# # Read the CSV file into a DataFrame
# df = pd.read_csv(input_file)

# # Drop the 'id' and 'label_num' columns
# df = df.drop(columns=["id", "label_num"])

# # Save the modified DataFrame to a new CSV file
# df.to_csv(output_file, index=False)

# print(f"Columns 'id' and 'label_num' removed. Updated CSV saved to {output_file}.")


# import pandas as pd

# # Load the CSV file
# input_file = "new_spam.csv"  # Replace with your CSV file path
# output_file = "output.csv"  # Replace with the desired output file path

# # Read the CSV file into a DataFrame
# df = pd.read_csv(input_file)

# # Remove unnecessary spaces from the 'Message' column
# df['Message'] = df['Message'].str.strip()  # Remove leading and trailing spaces
# df['Message'] = df['Message'].replace(r'\s+', ' ', regex=True)  # Remove extra spaces between words

# # Save the modified DataFrame to a new CSV file
# df.to_csv(output_file, index=False)

# print(f"Unnecessary spaces in 'Message' fixed. Updated CSV saved to {output_file}.")


# import pandas as pd

# # Load the CSV file
# input_file = "spamage.csv"  # Replace with your CSV file path
# output_file = "out.csv"  # Replace with the desired output file path

# # Read the CSV file into a DataFrame
# df = pd.read_csv(input_file)

# # Add a new column 'Category' based on the 'spam' column
# df['Category'] = df['spam'].apply(lambda x: 'spam' if x == 1 else 'ham')

# # Remove commas from the 'text' column
# df['text'] = df['text'].apply(lambda x: x.replace(',', '') if isinstance(x, str) else x)

# # Retain only 'Category', 'text', and 'spam' columns, with 'Category' as the first column
# df = df[['Category', 'text', 'spam']]

# # Save the modified DataFrame to a new CSV file
# df.to_csv(output_file, index=False)

# print(f"CSV file updated to remove commas and correctly categorize 'spam' and 'ham'. Saved to {output_file}.")


# import pandas as pd

# # Load the CSV file
# input_file = "out.csv"  # Replace with your CSV file path
# output_file = "output2.csv"  # Replace with the desired output file path

# # Read the CSV file into a DataFrame
# df = pd.read_csv(input_file)

# # Ensure that the 'spam' column is treated as numeric, if not already
# df['spam'] = pd.to_numeric(df['spam'], errors='coerce')

# # Assign 'Category' based on 'spam' column: if spam == 1, then 'spam', else 'ham'
# df['Category'] = df['spam'].apply(lambda x: 'spam' if x == 1 else 'ham')

# # Retain only 'Category' and 'text' columns, remove 'spam'
# df = df[['Category', 'text']]

# # Save the updated DataFrame to a new CSV file
# df.to_csv(output_file, index=False)

# print(f"CSV file updated and saved to {output_file}.")


import pandas as pd

def load_and_clean_csv(file_path):
    try:
        # Attempt to read the CSV
        print(f"Processing file: {file_path}")
        # Open the file with a safer engine, skipping problematic lines
        with open(file_path, 'r', encoding='utf-8') as f:
            # Count valid rows by skipping errors
            df = pd.read_csv(f, engine='python', on_bad_lines='skip')

        # Check for the required columns
        if 'Category' in df.columns and 'Message' in df.columns:
            df = df[['Category', 'Message']]  # Keep only relevant columns
        else:
            print(f"File {file_path} missing required columns. Skipping.")
            return pd.DataFrame(columns=['Category', 'Message'])

        # Clean the 'Message' column: Remove commas, quotes, etc.
        df['Message'] = df['Message'].astype(str).str.replace(r'[,"\'`]', '', regex=True)

        return df
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return pd.DataFrame(columns=['Category', 'Message'])

# File paths
file1 = 'output1.csv'
file2 = 'output.csv'
file3 = 'output2.csv'

# Process files and handle errors
files = [file1, file2, file3]
dataframes = []

for file in files:
    df = load_and_clean_csv(file)
    if not df.empty:
        dataframes.append(df)

# Combine the data from all valid DataFrames
if dataframes:
    combined_df = pd.concat(dataframes, ignore_index=True)
    
    # Save the cleaned and merged file
    output_file = 'new.csv'
    combined_df.to_csv(output_file, index=False)
    print(f"Merged file saved as: {output_file}")
else:
    print("No valid data to merge.")


