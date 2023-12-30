import pandas as pd
import numpy as np

# Load the test set that has been split by goal_info
test_df = pd.read_csv('../testsetbyprompt/testset_single.csv')

# Create an empty DataFrame to store the final test set
final_test_df = pd.DataFrame()

# Group by 'goal_info'
for goal_info, goal_group in test_df.groupby('goal_info'):
    # Get unique episode_ids within this goal_info group
    unique_episodes = goal_group['episode_id'].unique()
    
    # Randomly select one episode_id
    selected_episode_id = np.random.choice(unique_episodes)
    
    # Select all rows from goal_group with the selected_episode_id
    selected_rows = goal_group[goal_group['episode_id'] == selected_episode_id]
    
    # Append to the final test DataFrame
    final_test_df = pd.concat([final_test_df, selected_rows], ignore_index=True)

# Save the final test set
final_test_df.to_csv('../randomepisode/randomepisode_single.csv', index=False)

# Print information
print(f"Total entries in the final test set: {len(final_test_df)}")
print(f"Unique 'goal_info' in the final test set: {final_test_df['goal_info'].nunique()}")
print(f"Unique 'episode_id' in the final test set: {final_test_df['episode_id'].nunique()}")