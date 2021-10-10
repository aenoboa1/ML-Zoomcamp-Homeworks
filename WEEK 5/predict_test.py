# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%


# %%
import requests


# %%
host = 'churn-serving-env-1.eba-s3rq244h.us-east-2.elasticbeanstalk.com'
url = f'http://{host}/predict'


# %%
customer = {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 24,
    "monthlycharges": 29.85,
    "totalcharges": (2 * 29.85 )
}


# %%
response = requests.post(url,json=customer).json()

response


# %%
if response['churn'] == True:
    print('sending promo to %s' %('xyz-123'))


