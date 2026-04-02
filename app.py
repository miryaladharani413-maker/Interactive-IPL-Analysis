import streamlit as st
import pandas as pd

# -------- PAGE CONFIG --------
st.set_page_config(page_title="IPL Dashboard", layout="wide")

# -------- TITLE --------
st.title("🏏 Interactive IPL Analytics Dashboard")

# -------- SIDEBAR --------
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ["🏠 Home", "🎯 Prediction", "📊 Analysis", "📈 Performance"])

# -------- DATA --------
data = {
    "Experience":[1,2,3,4,5],
    "TestScore":[50,60,70,80,90],
    "Communication":[5,6,7,8,9],
    "Hire":[0,0,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Experience","TestScore","Communication"]]
y = df["Hire"]

# -------- MODEL --------

score_value = model.score(X, y)

# -------- HOME --------
if option == "🏠 Home":
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Players", len(df))
    col2.metric("Selected", int(sum(y)))
    col3.metric("Rejected", int(len(df) - sum(y)))

# -------- PREDICTION --------
elif option == "🎯 Prediction":
    st.subheader("Player Selection System")

    col1, col2, col3 = st.columns(3)

    with col1:
        exp = st.slider("Experience", 1, 10, 1)
    with col2:
        score = st.slider("Performance Score", 0, 100, 50)
    with col3:
        comm = st.slider("Fitness/Communication", 1, 10, 5)

    if st.button("Predict"):
        result = model.predict([[exp, score, comm]])

        if result[0] == 1:
            st.success("🌟 Selected for IPL Team")
        else:
            st.error("❌ Not Selected")

        st.subheader("Coach Feedback")

        if exp < 2:
            st.warning("Improve experience")
        if score < 70:
            st.warning("Improve performance")
        if comm < 5:
            st.warning("Improve fitness")

# -------- ANALYSIS --------
elif option == "📊 Analysis":
    st.subheader("Dataset")
    st.dataframe(df)

    st.subheader("Statistics")
    st.write(df.describe())

    st.subheader("Feature Importance")
    st.bar_chart(X)

# -------- PERFORMANCE --------
elif option == "📈 Performance":
    st.subheader("Model Performance")

    st.metric("Model Accuracy", round(score_value, 2))
