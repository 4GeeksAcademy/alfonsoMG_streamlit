import streamlit as st
import pickle
from pickle import load



model = load(open("/workspaces/alfonsoMG_streamlit/models/decision_tree_optimized_model.pk", "rb"))

st.title("Diabetes -  Decision Tree Prediction")
st.write("Using the sliders introduce the values above in order to know if you suffer form diabetes or not (according to my model).")

class_dict = {
    "0": "No, according to our model you don't suffer from diabetes.",
    "1": "Yes, I am sorry, it's highly probable that you suffer from diabetes, please go to a doctor."
}

preg_val = st.slider(
                    "Number of Pregnancies",
                    min_value = 0,
                    max_value = 18,
                    step = 1
)

glucose_val = st.slider(
                    "Level of Glucose",
                    min_value = 40,
                    max_value = 200,
                    step = 1
)

bloodp_val = st.slider(
                    "Level of Blood Pressure",
                    min_value = 40,
                    max_value = 200,
                    step = 1
)
skin_val = st.slider(
                    "Skin Thickness",
                    min_value = 1,
                    max_value = 100,
                    step = 1
)

insulin_val = st.slider(
                    "Level of Insulin",
                    min_value = 1,
                    max_value = 850,
                    step = 1
)

bmi_val = st.slider(
                    "BMI",
                    min_value = 1,
                    max_value = 70,
                    step = 1
)

pedigree_val = st.slider(
                    "Diabetes Pedigree",
                    min_value = 0.0,
                    max_value = 3.5,
                    step = 0.2
)

age_val = st.slider(
                    "Age",
                    min_value = 18,
                    max_value = 85,
                    step = 1
)

if st.button("Predict"):
    prediction = str(model.predict([[
                                    preg_val,
                                    glucose_val,
                                    bloodp_val,
                                    skin_val,
                                    insulin_val,
                                    bmi_val,
                                    pedigree_val,
                                    age_val
    ]])
    [0])
    pred_val = class_dict[prediction]
    st.write("Prediction:", pred_val)