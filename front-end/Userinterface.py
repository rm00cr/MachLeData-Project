import streamlit as st
import requests
import public_ip as ipf

# variables for encoding 
expierience = {"Junior":"EN", "Mid-level":"MI", "Senior":'SE', "Executive":"EX"}
employmentstatus = {"Full-time":'FT', "Part-time":'PT', "Contract":'CT', "Freelance":'FL'}
companysize = {"Small":'S', "Medium":'M', "Large":'L'}
# for now hardcoded --> in a real solution make database request
countries = ['NL', 'US', 'GB', 'LT', 'CA', 'ES', 'DE', 'LV', 'BE', 'FR', 'SK',
       'PH', 'IE', 'AU', 'BR', 'IN', 'PL', 'PE', 'AR', 'AT', 'CH', 'NZ',
       'PT', 'RS', 'FI', 'TW', 'NO', 'SV', 'EC', 'CL', 'DO', 'MX', 'CO',
       'SG', 'MT', 'DK', 'ID', 'MY', 'XK', 'CR', 'JP', 'ZM', 'PR', 'AM',
       'LU', 'IT', 'CY', 'RW', 'IL', 'CZ', 'KR', 'ZA', 'EG', 'LB', 'GR',
       'NG', 'BG', 'HU', 'HR', 'KE', 'SE', 'UA', 'TR', 'PK', 'HN', 'RO',
       'VE', 'BM', 'VN', 'GE', 'AE', 'SA', 'OM', 'BA', 'EE', 'UG', 'SI',
       'MU', 'TH', 'QA', 'RU', 'TN', 'GH', 'AD', 'MD', 'UZ', 'HK', 'CF',
       'KW', 'IR', 'AS', 'CN', 'BO', 'DZ', 'IQ', 'JE']
jobs = ['Customer Success Manager', 'Engineer', 'Applied Scientist',
       'Data Analyst', 'Software Development Engineer',
       'Research Scientist', 'Data Scientist', 'Platform Engineer',
       'Computational Biologist', 'AI Data Scientist',
       'Admin & Data Analyst', 'Cloud Engineer',
       'Data Management Specialist', 'Data Product Owner',
       'Software Engineer', 'Machine Learning Engineer', 'Associate',
       'Data Engineer', 'Product Manager', 'Data Operations Engineer',
       'Business Intelligence Engineer', 'Research Engineer',
       'Analytics Engineer', 'Analyst', 'Actuarial Analyst', 'Manager',
       'Architect', 'Software Developer', 'Member of Technical Staff',
       'BI Analyst', 'AI Engineer', 'Data Governance Analyst',
       'Developer', 'DevOps Engineer', 'Business Intelligence Analyst',
       'Site Reliability Engineer', 'Computational Scientist',
       'Data Management Analyst', 'Data and Reporting Analyst',
       'Solution Architect', 'Data Reporting Analyst', 'Data Architect',
       'Solutions Architect', 'Data Manager', 'Data Reporter',
       'Data Governance', 'Business Intelligence Developer',
       'Solutions Engineer', 'Database Administrator', 'Consultant',
       'Product Analyst', 'Data Specialist', 'Quantitative Developer',
       'Research Assistant', 'BI Developer', 'Quantitative Researcher',
       'Product Designer', 'Machine Learning Scientist',
       'Research Associate', 'Product Owner', 'Insight Analyst',
       'Statistician', 'Engineering Manager', 'Data Analytics Manager',
       'Data Modeler', 'Systems Engineer', 'Data Platform Engineer',
       'Technical Lead', 'Bioinformatician', 'AI Researcher',
       'Data Developer', 'Quantitative Analyst', 'Head of AI',
       'Lead Engineer', 'Prompt Engineer', 'Data Visualization Analyst',
       'Python Developer', 'Analytics Specialist', 'Full Stack Developer',
       'Head of Data', 'AI Governance Lead',
       'Director of Machine Learning', 'AI Architect',
       'Enterprise Account Executive', 'Backend Engineer',
       'DataOps Engineer', 'Data Governance Specialist',
       'System Engineer', 'Data Visualization Engineer', 'AI Developer',
       'Data Governance Lead', 'Business Analyst', 'Tableau Developer',
       'Computer Vision Engineer', 'Account Executive',
       'Product Specialist', 'Data Governance Manager',
       'Business Intelligence', 'Data Operations', 'Data Strategist',
       'Data Quality Specialist', 'Data and Reporting Professional',
       'Robotics Engineer', 'Cloud Database Engineer',
       'Data Integration Engineer', 'Principal Researcher',
       'Research Analyst', 'AI Data Engineer', 'ETL Developer',
       'Bioinformatics Scientist', 'Full Stack Engineer',
       'Postdoctoral Fellow', 'Technology Integrator',
       'Algorithm Developer', 'AI Specialist', 'Data Integrator',
       'Data Lead', 'Business Intelligence Specialist',
       'Encounter Data Management Professional', 'Java Developer',
       'Power BI Developer', 'AI Product Owner',
       'Principal Software Architect', 'Statistical Programmer',
       'Data Operations Specialist', 'Master Data Management',
       'Data Analytics Specialist', 'MLOps Engineer',
       'Data Product Manager', 'Security Researcher',
       'AI Research Scientist', 'Data Operations Analyst',
       'Principal Statistical Programmer', 'Data Team Lead',
       'Data Infrastructure Engineer', 'Big Data Developer',
       'BI Engineer', 'Developer Advocate', 'Postdoctoral Researcher',
       'Tech Lead', 'Data Visualization Specialist',
       'Scala Spark Developer', 'Sales Development Representative',
       'Machine Learning Researcher', 'Power BI', 'AI Scientist',
       'Staff Data Scientist', 'Application Developer',
       'Decision Scientist', 'Cloud Database Administrator',
       'AI Machine Learning Engineer', 'Data Integrity Specialist',
       'Power BI Specialist', 'Analytics Lead', 'GenAI Architect',
       'Lead Data Analysis', 'Data Management Associate',
       'Data Integration Specialist', 'Lead Analyst',
       'Head of Machine Learning', 'Data Management Lead', 'QA Engineer',
       'Data Analytics Consultant', 'Data Quality Analyst',
       'Data Visualization Developer', 'Software Architect',
       'Machine Learning Developer', 'Data Strategy Lead',
       'Data Scientist Associate', 'Data Quality Lead',
       'Data Analytics Lead', 'Business Intelligence Manager',
       'Risk Analyst', 'Marketing Science Partner',
       'Data Reporting Specialist', 'Clinical Data Operator', 'AI Lead',
       'Machine Learning Specialist', 'Research Data Manager',
       'Technical Specialist', 'Applied Research Scientist',
       'Lead Data Management', 'Data Analytics Developer',
       'Machine Learning Architect', 'Machine Learning Lead', 'Stage',
       'Technical Writer', 'Data Quality Engineer',
       'Data Integration Analyst', 'Safety Data Management Specialist',
       'Business Intelligence Lead', 'Data Operations Manager',
       'Big Data Analyst', 'Data Scientist Manager', 'Pricing Analyst',
       'Lead Data Engineer', 'AI Engineering Manager',
       'Backend Developer', 'Data Management Coordinator',
       'Analytics Analyst', 'Controls Engineer',
       'Machine Learning Tech Lead', 'Business Development Manager',
       'Data Management Consultant', 'Business Insights Manager',
       'Power BI Administrator', 'Data Integration Developer',
       'Data Integrity Analyst', 'Platform Data Engineer',
       'Bear Robotics', 'Principal Application Delivery Consultant',
       'Chatbot Developer', 'Artificial Intelligence Engineer',
       'Data Governance Architect', 'Power BI Consultant',
       'Backend Software Engineer', 'AI Product Manager',
       'Data Operations Associate', 'ML Infrastructure Engineer',
       'Cloud Developer', 'Data Operations Lead', 'Fullstack Engineer',
       'Machine Learning Quality Engineer', 'Security Engineer',
       'Databricks Engineer', 'Infrastructure Engineer',
       'Solution Engineer', 'Big Data Engineer',
       'Machine Learning Performance Engineer',
       'Data Analytics Associate', 'Power BI Architect',
       'Machine Learning Platform Engineer', 'AI Solution Architect',
       'Data Scientist Lead', 'Machine Vision Engineer',
       'Data Governance Engineer', 'Machine Learning Model Engineer',
       'Marketing Analyst', 'Data Management Manager',
       'Marketing Analytics Manager', 'Applied AI ML Lead',
       'Data Strategy Manager', 'Machine Learning Manager',
       'Data Product Analyst', 'Data Quality Manager',
       'Elasticsearch Administrator',
       'Machine Learning Infrastructure Engineer', 'People Data Analyst',
       'Frontend Engineer', 'NLP Engineer', 'SAS Developer',
       'Data Analytics Team Lead', 'Machine Learning Modeler',
       'Data Integration Coordinator', 'AI Programmer',
       'Head of Business Intelligence', 'ETL Engineer',
       'AI Research Engineer', 'Business Intelligence Consultant',
       'Robotics Software Engineer', 'AI Software Engineer',
       'Lead AI Engineer', 'AI Software Development Engineer',
       'Master Data Specialist', 'Consultant Data Engineer',
       'Manager Data Management', 'Director of Business Intelligence',
       'Lead Data Scientist', 'CRM Data Analyst', 'BI Data Analyst',
       'Applied Data Scientist', 'Data DevOps Engineer',
       'Quantitative Research Analyst', 'Lead Machine Learning Engineer',
       'Machine Learning Research Engineer', 'Data Analyst Lead',
       'Data Pipeline Engineer', 'Lead Data Analyst',
       'Business Data Analyst', 'Marketing Data Scientist',
       'Deep Learning Engineer', 'Financial Data Analyst',
       'Azure Data Engineer', 'Principal Data Scientist',
       'Staff Data Analyst', 'Machine Learning Software Engineer',
       'Applied Machine Learning Scientist',
       'Principal Machine Learning Engineer', 'Principal Data Engineer',
       'Staff Machine Learning Engineer',
       'Business Intelligence Data Analyst', 'Finance Data Analyst',
       'Software Data Engineer', 'Compliance Data Analyst',
       'Cloud Data Engineer', 'Analytics Engineering Manager',
       'AWS Data Architect', 'Product Data Analyst',
       'Autonomous Vehicle Technician', 'Sales Data Analyst',
       'Applied Machine Learning Engineer', 'BI Data Engineer',
       'Deep Learning Researcher', 'Big Data Architect',
       'Computer Vision Software Engineer', 'Marketing Data Engineer',
       'Data Science Tech Lead', 'Marketing Data Analyst',
       'Principal Data Architect', 'Data Analytics Engineer',
       'Cloud Data Architect', 'Principal Data Analyst']
currency = ['EUR', 'USD', 'GBP', 'CAD', 'PHP', 'INR', 'BRL', 'PLN', 'CHF',
       'TWD', 'NOK', 'SGD', 'AUD', 'JPY', 'DKK', 'CZK', 'HUF', 'MXN',
       'ILS', 'TRY', 'ZAR', 'SEK', 'NZD', 'HKD', 'THB', 'CLP']


def main():
    if "ip" not in st.session_state:
        con = ':443/back-end'
        st.session_state.ip = ipf.get() + con # "localhost"+':443/back-end' # add if pushing to server
    st.title("Data jobs salary predictor")

    tab1, tab2 = st.tabs(["Predict Salary", "Enter New Data Point"])

    with tab1:
        st.header("Predict Salary")
        
        # Use columns to align input boxes next to each other
        col1, col2, col3 = st.columns(3)
        with col1:
            work_year = st.number_input("Work year:", min_value=0, step=1, key="work_year_tab1")
            employment_type = st.selectbox("Employment type:", ["Full-time", "Part-time", "Contract", "Freelance"],key="employment_type_tab1")
            salary_currency = st.selectbox("Salary currency (e.g., USD, EUR):",currency,key = "salary_currency_tab1")
        with col2:
            experience_level = st.selectbox("Experience level:", ["Junior", "Mid-level", "Senior", "Executive"],key = "experience_level_tab1")
            job_title = st.selectbox("Job title:",jobs,key = "job_title_tab1")
            employee_residence = st.selectbox("Employee residence:",countries ,key = "employee_residence_tab1")
        with col3:
            company_location = st.selectbox("Company location:", countries, key = "company_location_tab1")
            company_size = st.selectbox("Company size:", ["Small", "Medium", "Large"],key = "company_size_tab1")
            remote_ratio = st.slider("Remote ratio in %:", 0, 100, step=10,key = "remote_ratio_tab1")

        if st.button("Predict Salary"):
            prediction_data = {
                "work_year": work_year,
                "experience_level": expierience[experience_level],
                "employment_type": employmentstatus[employment_type],
                "job_title": job_title,
                "salary_currency": salary_currency,
                "employee_residence": employee_residence,
                "remote_ratio": remote_ratio,
                "company_location": company_location,
                "company_size": companysize[company_size]
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
            salary_currency = st.selectbox("Salary currency (e.g., USD, EUR):",currency)
            salary = st.number_input("Salary:", min_value=0.0, step=500.0, key="salary_tab2")
        with col2:
            experience_level = st.selectbox("Experience level:", ["Junior", "Mid-level", "Senior", "Executive"])
            job_title = st.selectbox("Job title:",jobs)
            employee_residence = st.selectbox("Employee residence:",countries)
            salary_in_usd = st.number_input("Salary in USD:", min_value=0.0, step=500.0, key="salary_in_usd_tab2")
        with col3:
            company_location = st.selectbox("Company location:",countries)
            company_size = st.selectbox("Company size:", ["Small", "Medium", "Large"])
            remote_ratio = st.slider("Remote ratio (0 for on-site, 100 for fully remote):", 0, 100, step=10)
            
            

        if st.button("Submit New Data Point"):
            new_data = {
                "work_year": work_year,
                "experience_level": expierience[experience_level],
                "employment_type": employmentstatus[employment_type],
                "job_title": job_title,
                "salary": salary,
                "salary_currency": salary_currency,
                "salary_in_usd": salary_in_usd,
                "employee_residence": employee_residence,
                "remote_ratio": remote_ratio,
                "company_location": company_location,
                "company_size": companysize[company_size]
            }

            response = requests.post(f"http://{st.session_state.ip}/save/", json=new_data)
            if response.status_code == 200:
                st.success("Data point added successfully! Thank you for submitting.")
            else:
                st.error("Failed to add data point.")

if __name__ == "__main__":
    main()
