# Android in the Wild Data Processing

## Overview

This repository contains a Python script designed to process and analyze data from the "Android in the Wild" (AITW) dataset. The script reads a CSV file containing various columns related to user interactions and splits it into training and testing sets based on unique episode IDs.

## Dataset

The dataset is a CSV file with multiple columns such as `episode_id`, `action_type`, `type_action_text`, `current_activity`, `step_id`, `episode_length`, `android_api_level`, `goal_info`, `device_type`. Each row represents a step in an episode of user interaction.

## Script Functionality

The `split2test.py` script performs the following functions:

- Reads the CSV file into a DataFrame.
- Groups the data by `episode_id`, ensuring all steps of an episode are treated as one unit.
- Randomly splits the dataset into two sets: a training set (90%) and a testing set (10%), with each set containing complete episodes.
- Saves these sets into separate CSV files: `test_xxx.csv` and `train_xxx.csv`.

The `splitbyprompt.py` script performs the following functions:

- Reads the CSV file into a DataFrame.
- Groups the data by `goal_info`, ensuring all steps of an episode are treated as one unit.
- Randomly splits the dataset into two sets: a training set (90%) and a testing set (10%), with each set containing complete episodes.
- Saves these sets into separate CSV files: `testset_xxx.csv` and `trainset_xxx.csv`.
- Each item with the same goal_info(prompt), which may have the same episode_id or not, are organized together in the trainset and the testset.

## Dataset Split Summary

The table below summarizes the split of each CSV file into training and testing sets:

| Dataset Category        | Total Unique Episodes | Unique Episodes in Test Set | Unique Episodes in Train Set |
|----------------------|-----------------------|-----------------------------|------------------------------|
| `SINGLE`          | 26303                 | 2631                        | 23672                        |
| `GENERAL`          | 9477     | 948        | 8529        |
| `GOOGLEAPPS`          | 625523     | 62553        | 562970        |
| `INSTALL`          | 25761     | 2577        | 23184        |
| `WEBSHOPPING`          | 28062     | 2807| 25255        |

| Dataset Category        | Total Unique Prompts | Unique Prompts in Test Set | Unique Prompts in Train Set |
|----------------------|-----------------------|-----------------------------|------------------------------|
| `SINGLE`          | 15366                 | 154                        | 15212                        |
| `GENERAL`          | 546     | 55        | 491        |
| `GOOGLEAPPS`          | 306     | 31        | 275        |
| `INSTALL`          | 689     | 69        | 620        |
| `WEBSHOPPING`          | 13474     | 135| 13339        |

## File Structure in Phoenix

```shell
.
├── all_data
│   ├── all_general.csv
│   ├── all_googleapps.csv
│   ├── all_install.csv
│   ├── all_single.csv
│   └── all_webshopping.csv
├── code
│   ├── split2test.py
│   └── splitbyprompt.py
├── README.md
├── testsetbyepisode
│   ├── test_general.csv
│   ├── test_googleapps.csv
│   ├── test_install.csv
│   ├── test_single.csv
│   └── test_webshopping.csv
├── testsetbyprompt
│   ├── testset_general.csv
│   ├── testset_googleapps.csv
│   ├── testset_install.csv
│   ├── testset_single.csv
│   └── testset_webshopping.csv
├── trainsetbyepisode
│   ├── train_general.csv
│   ├── train_googleapps.csv
│   ├── train_install.csv
│   ├── train_single.csv
│   └── train_webshopping.csv
└── trainsetbyprompt
    ├── trainset_general.csv
    ├── trainset_googleapps.csv
    ├── trainset_install.csv
    ├── trainset_single.csv
    └── trainset_webshopping.csv
```

## How to Run

1. Clone this repository to your local machine.
2. Place your dataset CSV file in the root directory of the cloned repository.
3. Run the script using the command:

   ```shell
   python split2test.py
   python splitbyprompt.py
   ```

4. Check the console for the print outputs and the root directory for the generated CSV files.

## Requirements

- Python 3.x
- Pandas library
- Numpy library

Install the required libraries using:

```shell
pip install pandas numpy
```
