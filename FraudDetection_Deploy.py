import pickle
import streamlit as st
#loading in the model to predict 

pickle_in = open('FraudDataClassifier.pkl', 'rb')
FraudDataClassifier = pickle.load(pickle_in)



def prediction(transactiontype, amount, oldbalanceorg, oldbalancedest, newbalanceorg, newbalancedest): 
    #transaction type
    if transactiontype == 'CASH_IN':
        transactiontype = 0
    elif transactiontype == 'CASH_OUT':
      transactiontype = 1
    elif transactiontype == 'DEBIT' :
      transactiontype = 2
    elif transactiontype == 'PAYMENT' :
      transactiontype = 3
    else:
        transactiontype = 4

    amount = float(amount)
    oldbalanceorg = float(oldbalanceorg)
    oldbalancedest = float(oldbalancedest)
    newbalanceorg = float(newbalanceorg)
    newbalancedest = float(newbalancedest)

    prediction = FraudDataClassifier.predict([[transactiontype, amount, oldbalanceorg, oldbalancedest, newbalanceorg, newbalancedest]])
    return prediction



def main():
    html_temp = ""
    st.title("Fraud Detection")
    st.markdown(html_temp, unsafe_allow_html = True)
    transactiontype = st.text_input("Transaction Type")
    amount = st.text_input("Amount")
    oldbalanceorg = st.text_input("Old Balance Origin")
    oldbalancedest = st.text_input("Old Balance Destination")
    newbalanceorg = st.text_input("New Balance Origin")
    newbalancedest = st.text_input("New Balance Destination")
    result = ""


    if st.button("Predict"):
        result = prediction(transactiontype, amount, oldbalanceorg, oldbalancedest, newbalanceorg, newbalancedest)
        if result == 0:
            st.success('It is not a Fraud Transaction')
        else:
            st.success('It is a Fraud Transaction')


if __name__=='__main__':
    main()