import streamlit as st
import requests
import public_ip as ipf

def main():
    if "ip" not in st.session_state:
        con = ':443/back-end'
        st.session_state.ip = "localhost" + con #ipf.get()+':443/back-end' # add if pushing to server
    st.title("Data jobs salary predictor")

    tab1, tab2 = st.tabs(["Predict Salary", "Enter New Data Point"])

    with tab1:
        st.header("Predict Salary")
        
        # Use columns to align input boxes next to each other
        col1, col2, col3 = st.columns(3)
        with col1:
            work_year = st.number_input("Work year:", min_value=0, step=1, key="work_year_tab1")
            employment_type = st.selectbox("Employment type:", ["Full-time", "Part-time", "Contract", "Freelance"],key="employment_type_tab1")
            salary_currency = st.text_input("Salary currency (e.g., USD, EUR):",key = "salary_currency_tab1")
        with col2:
            experience_level = st.selectbox("Experience level:", ["Junior", "Mid-level", "Senior", "Executive"],key = "experience_level_tab1")
            job_title = st.text_input("Job title:",key = "job_title_tab1")
            employee_residence = st.text_input("Employee residence:",key = "employee_residence_tab1")
        with col3:
            company_location = st.text_input("Company location:",key = "company_location_tab1")
            company_size = st.selectbox("Company size:", ["Small", "Medium", "Large"],key = "company_size_tab1")
            remote_ratio = st.slider("Remote ratio in %:", 5, 100, step=5,key = "remote_ratio_tab1")

        if st.button("Predict Salary"):
            prediction_data = {
                "work_year": work_year,
                "experience_level": experience_level,
                "employment_type": employment_type,
                "job_title": job_title,
                "salary_currency": salary_currency,
                "employee_residence": employee_residence,
                "remote_ratio": remote_ratio,
                "company_location": company_location,
                "company_size": company_size
            }
            response = requests.post(f"http://{st.session_state.ip}/predict_salary/", json=prediction_data)
            if response.status_code == 200:
                prediction = response.json().get("predicted_salary")
                st.success(f"Predicted Salary in USD: {prediction}")
            else:
                st.error("Failed to predict salary.")

    with tab2:
        st.header("Enter New Data Point")
        
        # Use columns to align input boxes next to each other
        col1, col2, col3 = st.columns(3)
        with col1:
            work_year = st.number_input("Work year:", min_value=0, step=1)
            employment_type = st.selectbox("Employment type:", ["Full-time", "Part-time", "Contract", "Freelance"])
            salary_currency = st.text_input("Salary currency (e.g., USD, EUR):")
            salary = st.number_input("Salary:", min_value=0.0, step=500.0, key="salary_tab2")
            
        with col2:
            experience_level = st.selectbox("Experience level:", ["Junior", "Mid-level", "Senior", "Executive"])
            job_title = st.text_input("Job title:")
            employee_residence = st.text_input("Employee residence:")
            salary_in_usd = st.number_input("Salary in USD:", min_value=0.0, step=500.0, key="salary_in_usd_tab2")
        with col3:
            company_location = st.text_input("Company location:")
            company_size = st.selectbox("Company size:", ["Small", "Medium", "Large"])
            remote_ratio = st.slider("Remote ratio (0 for on-site, 100 for fully remote):", 5, 100, step=10)
            
            

        if st.button("Submit New Data Point"):
            new_data = {
                "work_year": work_year,
                "experience_level": experience_level,
                "employment_type": employment_type,
                "job_title": job_title,
                "salary": salary,
                "salary_currency": salary_currency,
                "salary_in_usd": salary_in_usd,
                "employee_residence": employee_residence,
                "remote_ratio": remote_ratio,
                "company_location": company_location,
                "company_size": company_size
            }

            response = requests.post(f"http://{st.session_state.ip}/save/", json=new_data)
            if response.status_code == 200:
                st.success("Data point added successfully! Thank you for submitting.")
            else:
                st.error("Failed to add data point.")

if __name__ == "__main__":
    main()