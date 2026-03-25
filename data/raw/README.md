# Raw Dataset

Dataset is large, so not uploaded directly to GitHub.

Download from Google Drive:

https://drive.google.com/drive/folders/1YfoQurISf8GRhqBo_Z5pSn7U7VssEscR

------------------------------------

After downloading, place files inside:

data/raw/

Required files:

- phishing_email.csv
- spam.csv
- combined_data.csv
- enron_data_fraud_labeled.csv

------------------------------------

Then run preprocessing:

python src/data_preprocessing.py

Output file will be created:

data/processed/final_email_dataset.csv

------------------------------------

## Expected folder structure

```
data/
│
├── raw/
│   ├── phishing_email.csv
│   ├── spam.csv
│   ├── combined_data.csv
│   └── enron_data_fraud_labeled.csv
│
└── processed/
```
