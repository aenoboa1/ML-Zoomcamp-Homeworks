
# %%
import os
import sklearn
import pickle
from flask import request
from flask import Flask
from flask import jsonify

# %%
model_file = input("Input the Filename of the model.bin: ")
dv_file = input("Input the Filename of the dictionary.bin: ")


# %%
def loading_models(dv_file, model_file ):
    with open(dv_file,'rb') as f_in: # read file
        dv = pickle.load(f_in)
    with open(model_file,'rb') as f_in: # read file
        model = pickle.load(f_in)
    return dv,model

# %%
dv,model = loading_models(dv_file,model_file)
# %%

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

