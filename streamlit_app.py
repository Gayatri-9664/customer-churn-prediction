import streamlit as st
import math

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")
st.write("Predict whether a customer is likely to churn.")

st.subheader("Customer Information")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior_citizen = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=5)

with col2:
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )
    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )
    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )
    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )
    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )
    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

with col3:
    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )
    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )
    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )
    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ]
    )
    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=85.00
    )
    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=425.00
    )

st.divider()

if st.button("🔍 Predict Churn", use_container_width=True):

    features = [
        1 if gender == "Female" else 0,
        1 if gender == "Male" else 0,

        1 if partner == "No" else 0,
        1 if partner == "Yes" else 0,

        1 if dependents == "No" else 0,
        1 if dependents == "Yes" else 0,

        1 if phone_service == "No" else 0,
        1 if phone_service == "Yes" else 0,

        1 if multiple_lines == "No" else 0,
        1 if multiple_lines == "No phone service" else 0,
        1 if multiple_lines == "Yes" else 0,

        1 if internet_service == "DSL" else 0,
        1 if internet_service == "Fiber optic" else 0,
        1 if internet_service == "No" else 0,

        1 if online_security == "No" else 0,
        1 if online_security == "No internet service" else 0,
        1 if online_security == "Yes" else 0,

        1 if online_backup == "No" else 0,
        1 if online_backup == "No internet service" else 0,
        1 if online_backup == "Yes" else 0,

        1 if device_protection == "No" else 0,
        1 if device_protection == "No internet service" else 0,
        1 if device_protection == "Yes" else 0,

        1 if tech_support == "No" else 0,
        1 if tech_support == "No internet service" else 0,
        1 if tech_support == "Yes" else 0,

        1 if streaming_tv == "No" else 0,
        1 if streaming_tv == "No internet service" else 0,
        1 if streaming_tv == "Yes" else 0,

        1 if streaming_movies == "No" else 0,
        1 if streaming_movies == "No internet service" else 0,
        1 if streaming_movies == "Yes" else 0,

        1 if contract == "Month-to-month" else 0,
        1 if contract == "One year" else 0,
        1 if contract == "Two year" else 0,

        1 if paperless_billing == "No" else 0,
        1 if paperless_billing == "Yes" else 0,

        1 if payment_method == "Bank transfer (automatic)" else 0,
        1 if payment_method == "Credit card (automatic)" else 0,
        1 if payment_method == "Electronic check" else 0,
        1 if payment_method == "Mailed check" else 0,

        senior_citizen,
        tenure,
        monthly_charges,
        total_charges
    ]

    scales = [
        4.9999651554340191e-01,
        4.9999651554340191e-01,
        4.9980520452385879e-01,
        4.9980520452385879e-01,
        4.5806334135287241e-01,
        4.5806334135287241e-01,
        2.9580640983382228e-01,
        2.9580640983382228e-01,
        4.9956346375711325e-01,
        2.9580640983382228e-01,
        4.9419024676735407e-01,
        4.7498263308081523e-01,
        4.9655678824341642e-01,
        4.1065265969377857e-01,
        4.9999714764619141e-01,
        4.1065265969377857e-01,
        4.5233018421894394e-01,
        4.9573657680288391e-01,
        4.1065265969377857e-01,
        4.7709521062363447e-01,
        4.9634383940328530e-01,
        4.1065265969377857e-01,
        4.7556349733761555e-01,
        4.9990953058070564e-01,
        4.1065265969377857e-01,
        4.5593279990003716e-01,
        4.8912104386904226e-01,
        4.1065265969377857e-01,
        4.8751827265531067e-01,
        4.8885546552416703e-01,
        4.1065265969377857e-01,
        4.8779999949382363e-01,
        4.9764760202622643e-01,
        4.0740313640860193e-01,
        4.2794571249109320e-01,
        4.9081878479350327e-01,
        4.9081878479350327e-01,
        4.1394554422079105e-01,
        4.1151427678756247e-01,
        4.7337739179402732e-01,
        4.1786007700019157e-01,
        3.6824683080109444e-01,
        2.4540239643692999e+01,
        3.0105965373777543e+01,
        2.2753838010392733e+03
    ]

    coefficients = [
        0.03270469, 0.02096564, 0.03347188, 0.02021900,
        0.08209089, -0.02350733, 0.01836492, 0.07235312,
        -0.08721590, 0.01836492, 0.13147243, -0.30531533,
        0.42561006, -0.09615207, 0.13982995, -0.09615207,
        -0.00794662, 0.08268046, -0.09615207, 0.05309706,
        0.03364187, -0.09615207, 0.10434390, 0.12994306,
        -0.09615207, 0.00298357, -0.06023192, -0.09615207,
        0.19646604, -0.05361984, -0.09615207, 0.18969339,
        0.34347500, -0.03075357, -0.30743486, -0.04402657,
        0.09870047, -0.04579935, -0.02725365, 0.13062337,
        -0.01154805, 0.07069931, -1.34934059, -0.89392078,
        0.64227770
    ]

    intercept = 0.011159576359318869

    scaled_features = []

    for i in range(len(features)):
        scaled_features.append(features[i] / scales[i])

    linear_value = intercept

    for i in range(len(coefficients)):
        linear_value += coefficients[i] * scaled_features[i]

    probability = 1 / (1 + math.exp(-linear_value))

    churn_percentage = probability * 100

    st.subheader("Prediction Result")

    if probability >= 0.5:
        st.error("⚠️ Customer is likely to churn")
    else:
        st.success("✅ Customer is not likely to churn")

    st.metric(
        "Churn Probability",
        f"{churn_percentage:.2f}%"
    )

    st.progress(probability)

st.divider()

st.subheader("📈 Project Information")

info1, info2, info3, info4 = st.columns(4)

with info1:
    st.metric("Training Records", "7,032")

with info2:
    st.metric("Features", "19")

with info3:
    st.metric("Model Accuracy", "80.38%")

with info4:
    st.metric("ML Model", "Logistic Regression")

st.caption("Dataset: Telco Customer Churn")
st.caption("Customer Churn Prediction | Snowflake ML Project")