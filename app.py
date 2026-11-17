
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="SmartShelter | DRDO",
    page_icon="🏠",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #101827;
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
div[data-testid="stMetric"] {
    background: #1e293b;
    padding: 20px;
    border-radius: 12px;
}
.stButton button {
    background-color: #16a34a;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🏠 SmartShelter")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Shelter Information",
     "Register", "Emergency Support", "About"]
)

if page == "Dashboard":
    st.title("🏠 SmartShelter")
    st.subheader("Smart Emergency Shelter Management System")
    st.write("A technology-enabled platform for emergency shelter monitoring and management.")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Shelters", "25")
    col2.metric("Available Beds", "450")
    col3.metric("Occupancy", "68%")

    st.divider()
    st.subheader("System Overview")

    data = pd.DataFrame({
        "Category": ["Available", "Occupied"],
        "Beds": [450, 300]
    })

    st.bar_chart(data.set_index("Category"))

    st.info("Welcome to the SmartShelter management dashboard.")

elif page == "Shelter Information":
    st.title("Shelter Information")

    shelters = pd.DataFrame({
        "Shelter": ["Shelter A", "Shelter B", "Shelter C"],
        "Location": ["Chennai", "Coimbatore", "Bengaluru"],
        "Capacity": [200, 150, 100],
        "Available Beds": [80, 60, 40],
        "Status": ["Available", "Available", "Limited"]
    })

    st.dataframe(shelters, use_container_width=True)

elif page == "Register":
    st.title("Shelter Registration")

    with st.form("registration"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=1, max_value=120)
        phone = st.text_input("Contact Number")
        location = st.text_input("Current Location")
        people = st.number_input(
            "Number of People",
            min_value=1,
            max_value=20
        )

        submit = st.form_submit_button("Submit Registration")

        if submit:
            if name and phone and location:
                st.success("Registration submitted successfully!")
            else:
                st.error("Please fill in all required fields.")

elif page == "Emergency Support":
    st.title("🚨 Emergency Support")

    st.warning("Emergency assistance information")

    st.subheader("Emergency Contact")
    st.write("Contact your local emergency response authority.")

    st.subheader("Safety Guidelines")
    st.write("""
    - Stay calm during emergencies.
    - Follow official evacuation instructions.
    - Keep essential medicines and documents.
    - Move to an officially designated safe shelter.
    """)

elif page == "About":
    st.title("About SmartShelter")

    st.write("""
    SmartShelter is a conceptual emergency shelter
    management platform designed to demonstrate:

    - Shelter availability monitoring
    - Occupancy management
    - Registration management
    - Emergency support information
    - Dashboard-based monitoring

    This is a demonstration project and is not an
    official DRDO system.
    """)

st.sidebar.divider()
st.sidebar.caption("SmartShelter | Project Demonstration")
