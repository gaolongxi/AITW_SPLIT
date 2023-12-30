import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('../all_data/all_general.csv')

# Group by episode_id
grouped = df.groupby('episode_id')

# Print the total number of unique episode groups in the original dataset
print(f"Total number of unique episode groups in the original dataset: {len(grouped)}")

# Determine the number of unique episode IDs for the test set (10%)
test_size = int(np.ceil(len(grouped) * 0.1))

# Randomly select episode IDs for the test set
test_ids = np.random.choice(df['episode_id'].unique(), size=test_size, replace=False)

# Split the DataFrame into test and train sets
test_df = df[df['episode_id'].isin(test_ids)]
train_df = df[~df['episode_id'].isin(test_ids)]

# Print the number of unique episode groups in the test and train sets
print(f"Number of unique episode groups in the test set: {test_df['episode_id'].nunique()}")
print(f"Number of unique episode groups in the train set: {train_df['episode_id'].nunique()}")

# Save the test and train sets
test_df.to_csv('../testset/test_general.csv', index=False)
train_df.to_csv('../trainset/train_general.csv', index=False)