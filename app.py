import streamlit as st
import pandas as pd

# -------- PAGE CONFIG --------
st.set_page_config(page_title="IPL Dashboard", layout="wide")

# -------- BACKGROUND IMAGE + BLUR --------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)),
    url("https://images.unsplash.com/photo-1593341646782-e0b495cff86d");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.stApp::before {
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;
    backdrop-filter: blur(8px);
    z-index: -1;
}

/* Title */
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #00ffcc;
}

/* Cards */
.card {
    background-color: rgba(28,34,48,0.8);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 0px 15px black;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: rgba(17,24,39,0.9);
}

/* Text color */
h1, h2, h3, h4, h5, h6, p {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# -------- TITLE --------
st.markdown('<div class="title">🏏 Interactive IPL Analytics Dashboard</div>', unsafe_allow_html=True)

# -------- SIDEBAR --------
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ["🏠 Home", "🎯 Prediction", "📊 Analysis", "📈 Performance"])

# -------- DATA --------
data={
    "Experience":[1,2,3,4,5],
    "TestScore":[50,60,70,80,90],
    "Communication":[5,6,7,8,9],
    "Hire":[0,0,1,1,1]
}

df=pd.DataFrame(data)

X=df[["Experience","TestScore","Communication"]]
y=df["Hire"]

model.fit(X,y)

# -------- HOME --------
if option=="🏠 Home":
    col1,col2,col3 = st.columns(3)

    col1.markdown(f'<div class="card"><h3>Total Players</h3><h2>{len(df)}</h2></div>', unsafe_allow_html=True)
    col2.markdown(f'<div class="card"><h3>Selected</h3><h2>{sum(y)}</h2></div>', unsafe_allow_html=True)
    col3.markdown(f'<div class="card"><h3>Rejected</h3><h2>{len(df)-sum(y)}</h2></div>', unsafe_allow_html=True)

# -------- PREDICTION --------
elif option=="🎯 Prediction":
    st.subheader("Player Selection System")

    col1,col2,col3 = st.columns(3)

    with col1:
        exp = st.slider("Experience",1,10,1)
    with col2:
        score = st.slider("Performance Score",0,100,50)
    with col3:
        comm = st.slider("Fitness/Communication",1,10,5)

    if st.button("Predict"):
        result=model.predict([[exp,score,comm]])

        if result[0]==1:
            st.success("🌟 Selected for IPL Team")
        else:
            st.error("❌ Not Selected")

        st.subheader("Coach Feedback")

        if exp<2:
            st.warning("Improve experience")
        if score<70:
            st.warning("Improve performance")
        if comm<5:
            st.warning("Improve fitness")

# -------- ANALYSIS --------
elif option=="📊 Analysis":
    st.subheader("Dataset")
    st.dataframe(df)

    st.subheader("Statistics")
    st.write(df.describe())

    st.subheader("Feature Importance")

    importance=model.feature_importances_

    imp_df=pd.DataFrame({
        "Feature":X.columns,
        "Importance":importance
    })

    st.bar_chart(imp_df.set_index("Feature"))

# -------- PERFORMANCE --------
elif option=="📈 Performance":
    y_pred=model.predict(X)
    score_value=r2_score(y,y_pred)

    st.metric("Model Score", round(score_value,2))
