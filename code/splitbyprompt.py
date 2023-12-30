import pandas as pd
import numpy as np

df = pd.read_csv('../all_data/all_webshopping.csv')

goal_info_groups = df.groupby('goal_info')

print(f"Total unique 'goal_info' groups in the original dataset: {len(goal_info_groups)}")

unique_goals = list(goal_info_groups.groups.keys())

np.random.shuffle(unique_goals)

# test_set_size = int(np.ceil(len(unique_goals) * 0.1))
test_set_size = int(np.ceil(len(unique_goals) * 0.01))

test_goals = unique_goals[:test_set_size]

test_df = pd.concat([group for name, group in goal_info_groups if name in test_goals])
train_df = pd.concat([group for name, group in goal_info_groups if name not in test_goals])

print(f"Total unique 'goal_info' groups in the test set: {len(test_df['goal_info'].unique())}")
print(f"Total unique 'goal_info' groups in the train set: {len(train_df['goal_info'].unique())}")

test_df.to_csv('../testsetbyprompt/testset_webshopping.csv', index=False)
train_df.to_csv('../trainsetbyprompt/trainset_webshopping.csv', index=False)
