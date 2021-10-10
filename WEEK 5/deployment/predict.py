
# %% [markdown]
# Load the model and using it

# %%
import pickle
from flask import request
from flask import Flask
from flask import jsonify
# %%
model_file = 'model_C=1.0.bin'


# %%
with open(model_file,'rb') as f_in: # read file
    (dv,model) = pickle.load(f_in)
    #file open  

app = Flask('churn')

@app.route('/predict',methods=['POST']) # SEND INFORMATION ABOUT CUSTOMER
# SENDING INFORMATION IN JSON FORMAT


def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    churn = y_pred >= 0.5

    result={
        'churn_probabilty': float(y_pred),
        'churn': bool(churn)

    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=9696)

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


X=dv.transform([customer])

y_pred = model.predict_proba(X)[0,1]

print('input',customer)
print('Churn probability',y_pred)