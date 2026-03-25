# Raw Dataset

Due to large file size, datasets are not uploaded directly to GitHub.

Download datasets from the Google Drive links below and place them in this folder.

------------------------------------

Required files:

1. phishing_email.csv
Google Drive link:
PASTE_LINK_HERE

2. spam.csv
Google Drive link:
PASTE_LINK_HERE

3. combined_data.csv
Google Drive link:
PASTE_LINK_HERE

4. enron_data_fraud_labeled.csv
Google Drive link:
PASTE_LINK_HERE

------------------------------------

After downloading, folder structure should look like:

data/raw/
│
├── phishing_email.csv
├── spam.csv
├── combined_data.csv
└── enron_data_fraud_labeled.csv


------------------------------------

Then run preprocessing script:

python src/data_preprocessing.py

This will generate:

data/processed/final_email_dataset.csv
