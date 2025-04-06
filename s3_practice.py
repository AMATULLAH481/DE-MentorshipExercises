import json
import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"C:\Users\HP\.vscode\Jupyter Notebook files\.env")


API_KEY = os.getenv("API_key")
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

# API_1
url = "http://api.football-data.org/v4/competitions/"
response = requests.get(url)
football_data = response.json()
football_data = football_data["competitions"]
df = pd.DataFrame(football_data)

# upload the football data file to S3 in parquet format
wr.s3.to_parquet(
    df=df,
    path=(
        "s3://amatullah-mahmud-bucket/football-API-data-folder/"
        "football_api_data.parquet"
    )
)


# API_2
url = "https://randomuser.me/api/?results=500"
response = requests.get(url)
response.status_code
user_details_data = response.json()
# list collecting our data
female_details = []
male_details = []
date_of_birth = []
first_name = []
last_name = []
full_names = []
user_details_data

for user_details in user_details_data["results"]:
    if user_details["gender"] == "female":
        female_details.append(user_details)
    elif user_details["gender"] == "male":
        male_details.append(user_details)

# convert the female_data list to dataframe
df = pd.DataFrame(female_details)
df = df[["gender", "name", "email"]]

# upload to s3
wr.s3.to_parquet(
    df=df,
    path=(
        "s3://amatullah-mahmud-bucket/random-user-details-folder/"
        "female_details.parquet"
    )
)

# convert the male_data list to dataframe
df = pd.DataFrame(male_details)
df = df[['gender', 'name', 'email']]
df

# upload to s3
wr.s3.to_parquet(
    df=df,
    path=(
        "s3://amatullah-mahmud-bucket/random-user-details-folder/"
        "male_details.parquet"
    )
)

for user_details in user_details_data["results"]:
    date_of_birth.append(user_details["dob"]["date"])

df_birthdate = pd.DataFrame(date_of_birth)
df_birthdate.rename(columns={0: 'date_of_birth'}, inplace=True)

wr.s3.to_parquet(
    df=df_birthdate,
    path=(
        "s3://amatullah-mahmud-bucket/random-user-details-folder/"
        "birthdate_details.parquet"
    )
)

for user_details in user_details_data["results"]:
    first_name.append(user_details["name"]["first"])
    last_name.append(user_details["name"]["last"])

df_firstname = pd.DataFrame(first_name)
df_firstname.rename(columns={0: 'firstname'}, inplace=True)

wr.s3.to_parquet(
    df=df_firstname,
    path=(
        "s3://amatullah-mahmud-bucket/random-user-details-folder/"
        "first_name.parquet"
    )
)

df_lastname = pd.DataFrame(last_name)
df_lastname.rename(columns={0: 'lastname'}, inplace=True)

wr.s3.to_parquet(
    df=df_lastname,
    path=(
        "s3://amatullah-mahmud-bucket/random-user-details-folder/"
        "last_names.parquet"
    )
)

for user_details in user_details_data["results"]:
    full_name = (
        f"{user_details['name']['first']} {user_details['name']['last']}"
    )
    full_names.append(full_name)

df_fullnames = pd.DataFrame(full_names, columns=["full_names"])
df_fullnames

wr.s3.to_parquet(
    df=df_fullnames,
    path=(
        "s3://amatullah-mahmud-bucket/random-user-details-folder/"
        "fullnames.parquet"
        )
)

# senior and manager roles API response
with open("response_data.json", "r") as file:
    response = json.load(file)

job_dict = response['jobs']
print(job_dict)
jobs_list = []
senior_roles = []
manager_roles = []

for job_details in job_dict:
    if "Senior" in job_details['jobTitle']:
        senior_roles.append(job_details['jobTitle'])
    elif "Manager" in job_details['jobTitle']:
        manager_roles.append(job_details['jobTitle'])
    else:
        # print(f" Odd one : {job_details['jobTitle']}")
        continue

df_senior_roles = pd.DataFrame(senior_roles)
df_senior_roles.rename(columns={0: 'senior_roles'}, inplace=True)

wr.s3.to_parquet(
    df=df_senior_roles,
    path=(
        "s3://amatullah-mahmud-bucket/random-user-details-folder/"
        "senior_roles.parquet"
        )
)

df_manager_roles = pd.DataFrame(manager_roles)
df_manager_roles.rename(columns={0: 'manager_roles'}, inplace=True)

wr.s3.to_parquet(
    df=df_manager_roles,
    path=(
        "s3://amatullah-mahmud-bucket/random-user-details-folder/"
        "manager_roles.parquet"
        )
)


# API_3
# url = (
#     f"https://content.guardianapis.com/search"
#     f"?q=Nigeria"
#     f"&from-date=2025-01-01"
#     f"&to-date=2025-12-31"
#     f"&api-key={API_KEY}"
# )
# response = requests.get(url)
nigerian_data = response.json()
nigerian_data

all_articles = []

for page in range(1, 11):  # Since 'pages': 10 in the response
    url = (
        f"https://content.guardianapis.com/search"
        f"?q=Nigeria"
        f"&from-date=2025-01-01"
        f"&to-date=2025-12-31"
        f"&api-key={API_KEY}"
    )
    articles = nigerian_data["response"]["results"]

    if not articles:
        break

    all_articles.extend(articles)
all_articles

df_articles = pd.DataFrame(all_articles)
df_articles = df_articles[["id", "webPublicationDate", "webTitle", "webUrl"]]

wr.s3.to_parquet(
    df=df_articles,
    path=(
        "s3://amatullah-mahmud-bucket/guardian-nigerian-articles/"
        "the_articles.parquet"
        )
)
