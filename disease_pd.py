import streamlit as st
import pandas as pd
import pickle

import sys
import sklearn

print("Python:", sys.executable)
print("Sklearn:", sklearn.__version__)

model = pickle.load(open("model.pkl", "rb"))

st.title("Disease prediction system")

age = st.selectbox("Enter your age:", range(1, 101))
st.write("Your age is:", age)

bp = st.selectbox("Enter your bp:", range(1, 200))
st.write("Your bp is:", bp)

sg = st.text_input("Enter your sg:")
st.write("Your sg is:", sg)

al= st.selectbox("Enter your al:", range(1, 10))
st.write("Your al is is:", al)

su= st.selectbox("Enter your su:", range(1, 7))
st.write("Your su is:", su)

rbc= st.selectbox("Enter your rbc:", ["normal", "abnormal"])
st.write("Your rbc is:", rbc)

pc= st.selectbox("Enter your pc:", ["normal", "abnormal"])
st.write("Your pc is:", pc)

pcc= st.selectbox("Enter your pcc:", ["present", "notpresent"])
st.write("Your pcc is:", pcc)

ba= st.selectbox("Enter your ba:", ["present", "notpresent"])
st.write("Your ba is:", ba)

bgr= st.text_input("Enter your bgr:")
st.write("Your bgr is:", bgr)

bu= st.text_input("Enter your bu:")
st.write("Your bu is:", bu)

sc= st.text_input("Enter your sc:")
st.write("Your sc is:", sc)

sod= st.text_input("Enter your sod:")
st.write("Your sod is:", sod)

pot= st.text_input("Enter your pot:")
st.write("Your pot is is:", pot)

hemo=st.text_input("Enter your hemo:")
st.write("Your hemo is:", hemo)

pcv= st.text_input("Enter your pcv:")
st.write("Your pcv is:", pcv)

wc= st.text_input("Enter your wc:")
st.write("Your wc is:", wc)

rc= st.text_input("Enter your rc:")
st.write("Your rc is:", rc)

htm= st.selectbox("Enter your htm:", ["Yes", "No"])
st.write("Your htm is:", htm)

dm= st.selectbox("Enter your dm:", ["Yes", "No"])
st.write("Your dm is:", dm)

cad= st.selectbox("Enter your cad:", ["Yes", "No"])
st.write("Your cad is:", cad)

appet= st.selectbox("Enter your appet:", ["Good", "Poor", "Unknown"])
st.write("Your appet is:", appet)

pe= st.selectbox("Enter your pe:", ["Yes", "No", "Unknown"])
st.write("Your pe is:", pe)

ane= st.selectbox("Enter your ane:", ["Yes", "No", "Unknown"])
st.write("Your ane is:", ane)


if st.button("Predict"):

    input_data = pd.DataFrame({
        "age": [age],
        "bp": [bp],
        "sg": [float(sg)],
        "al": [al],
        "su": [su],
        "rbc": [rbc],
        "pc": [pc],
        "pcc": [pcc],
        "ba": [ba],
        "bgr": [float(bgr)],
        "bu": [float(bu)],
        "sc": [float(sc)],
        "sod": [float(sod)],
        "pot": [float(pot)],
        "hemo": [float(hemo)],
        "pcv": [float(pcv)],
        "wc": [float(wc)],
        "rc": [float(rc)],
        "htn": [htm],
        "dm": [dm],
        "cad": [cad],
        "appet": [appet],
        "pe": [pe],
        "ane": [ane]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("CKD Detected")
    else:
        st.success("No CKD Detected")

