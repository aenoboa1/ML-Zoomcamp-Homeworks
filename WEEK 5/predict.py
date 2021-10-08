
# %% [markdown]
# Load the model

# %%
import pickle


# %%
model_file = 'model_C=1.0.bin'


# %%
with open(model_file,'rb') as f_in: # read file
    (dv,model) = pickle.load(f_in)
    #file open  


# %%
dv,model # reading the dictionary vector and the model


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
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges": 29.85
}


# %%
X=dv.transform([customer])


# %%
model.predict_proba(X)[0,1]


