import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

# Set the page configuration
st.set_page_config(page_title="Salaries Analysis Report", layout="wide", page_icon="📊")

# Custom CSS to center the content, reduce table width, and style answer text
st.markdown(
    """
    <style>
    .reportview-container .main .block-container{
        margin-left: auto;
        margin-right: auto;
        max-width: 900px;
        padding: 1rem 1rem;
    }
    table {
        max-width: 600px;

    }
    .answer {
        color: #0FA3B1;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        tex
    }
    div[data-baseweb="select"] {
        width: 40% !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the report
st.title("Salaries Analysis Report 📊")


st.image("Image/pexels-pixabay.jpg", width=700)
col1, col2 = st.columns(2)

with col1:
    # Select Language
    lang = st.selectbox("Choose Language For Report", ["English", "Arabic"])

    # Create a sub-row containing two columns for the buttons
    btn_col1, btn_col2 = st.columns(2)

    if lang == "English":
        with open("Report/Salaries_Analysis_Report_EN.pdf", "rb") as file:
            report_data = file.read()
        btn_col1.download_button(
            label="Download Report",
            data=report_data,
            file_name="Salaries_Analysis_Report_EN.pdf",
            mime="application/pdata"
        )
    else:
        with open("Report/Salaries_Analysis_Report_AR.pdf", "rb") as file:
            report_data = file.read()
        btn_col1.download_button(
            label="Download Report",
            data=report_data,
            file_name="Salaries_Analysis_Report_AR.pdf",
            mime="application/pdata"
        )

with col2:
    pass


# Load data from Excel and display it
data = pd.read_csv('./Data/SF Salaries.csv')

st.title('Salaries Analysis Data')
st.dataframe(data)

# Section: Analytical Questions for Salaries Analysis
st.header("Analytical Questions for Salaries Analysis")


# 1. Number of Employees Per Year
st.subheader("1. Number of Employees Per Year")
st.markdown(
    """
    <div class="answer">    
    What is the number of employees for each year? Is the number increasing or decreasing?
    </div> 
    """, unsafe_allow_html=True)
st.table({
    "Year": ["2011", "2012", "2013", "2014"],
    "Number of Employees Per Year": [3387.8, 3434.9, 3615.0, 3668.4]
})
employees_per_year = data.groupby('Year')['EmployeeName'].nunique().reset_index()
employees_per_year.rename(columns={'EmployeeName': 'EmployeeCount'}, inplace=True)

# Draw the graph
fig1 = px.bar(employees_per_year,
    x='Year',
    y='EmployeeCount',
    title='Number of employees per year',
    color='EmployeeCount',
    color_continuous_scale=px.colors.sequential.RdBu)

st.plotly_chart(fig1)

# 2. Mean and Median of TotalPay & TotalPayBenefits Per Year
st.subheader("2. Mean and Median of TotalPay & TotalPayBenefits Per Year")
st.markdown(
    """
    <div class="answer">
    What are the mean and median of TotalPay and TotalPayBenefits for each year?
    </div>
    """, unsafe_allow_html=True)

st.table({
    "Year": ["2011", "2012", "2013", "2014"],
    "TotalPay  ": [71744.103871, 74113.262265, 77611.443142, 75463.918140],
    "TotalPayBenefits": [71744.103871, 100553.229232, 101440.519714, 100250.918884]
})
# Calculate the average for TotalPay and TotalPayBenefits per year
average_pay_per_year = data.groupby('Year')[['TotalPay', 'TotalPayBenefits']].mean().reset_index()

# Draw a graph using lines to illustrate the comparison
fig2 = px.line(average_pay_per_year,
    x='Year',
    y=['TotalPay', 'TotalPayBenefits'],
    title='Average TotalPay and TotalPayBenefits per year')

fig2.update_layout(yaxis_title='Average Salary')

st.plotly_chart(fig2)


# 3. Highest TotalPayBenefits
st.subheader("3. Highest TotalPayBenefits")
st.markdown(
    """
    **Who is the employee with the highest TotalPayBenefits, and how much did they receive?**  
    <div class="answer">
    \n<strong>Employee:</strong> Employee 37403 
    \n<strong>TotalPayBenefits:</strong> $1778487.17 
    </div>
    """, unsafe_allow_html=True)

category_quantity = data.groupby('EmployeeName')['TotalPayBenefits'].sum()
max_category = category_quantity.idxmax()
max_value = category_quantity.max()

# Sort values in descending order and take the top 20
top_20_employees = category_quantity.sort_values(ascending=False).head(20).reset_index()

# Draw the chart
fig3 = px.bar(top_20_employees,
    x='EmployeeName',
    y='TotalPayBenefits',
    title='Top 20 Employees by TotalPayBenefits',
    color='TotalPayBenefits',
    color_continuous_scale=px.colors.sequential.RdBu)

# Improve the horizontal axis layout if names are long
fig3.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig3)

# 4. Most Frequent Job Title
st.subheader("4. Most Frequent Job Title")
st.markdown(
    """
    **Which job title appears the most frequently?**  
    <div class="answer">
    \n<strong>Most common title:</strong> Transit Operator
    \n<strong>It appears:</strong> 7036 times.
    </div>
    """, unsafe_allow_html=True)

# Count the number of occurrences of each job title
job_title_counts = data['JobTitle'].value_counts().reset_index().head(20)
job_title_counts.columns = ['JobTitle', 'Frequency']

# Draw the graph
fig4 = px.bar(job_title_counts,
    x='JobTitle',
    y='Frequency',
    title='Job Title Frequency in Data',
    color='Frequency',
    color_continuous_scale=px.colors.sequential.RdBu)

# Improve the horizontal axis layout if names are long
fig4.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig4)

# 5. OvertimePay = 0
st.subheader("5. Employees with Zero OvertimePay")
st.markdown(
    """
    **How many employees received an OvertimePay of 0?**  
    <div class="answer">
    \n<strong>Number of employees:</strong> 77,321
    </div>
    """, unsafe_allow_html=True)

# 6. Jobs with Salary Over $250,000
st.subheader("6. Job Titles with Salary Over $250,000")
st.markdown(
    """
    <div class="answer">
    Are there any job titles with annual earnings above $250,000? If so, which ones?
    </div> 
    """, unsafe_allow_html=True)

# Filter employees who earn more than $250,000
high_salary_jobs = data[data['TotalPayBenefits'] > 250000]

# Calculate the number of employees in each job title
job_salary_counts = high_salary_jobs['JobTitle'].value_counts().reset_index()
job_salary_counts.columns = ['JobTitle', 'EmployeeCount']
st.dataframe(job_salary_counts)

# Calculate the number of employees in each job
job_salary_counts = high_salary_jobs['JobTitle'].value_counts().reset_index().head(25)
job_salary_counts.columns = ['JobTitle', 'EmployeeCount']

# Draw the graph
fig6 = px.bar(job_salary_counts,
    x='JobTitle',
    y='EmployeeCount',
    title='Jobs Paying More Than $250,000 Annually',
    color='EmployeeCount',
    color_continuous_scale=px.colors.sequential.RdBu)

# Improve the layout of the horizontal axis if the names are long
fig6.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig6)

# 7. Top 10 Jobs by Avg TotalPayBenefits
st.subheader("7. Top 10 Jobs by Average TotalPayBenefits")
st.markdown(
    """
    <div class="answer">
        What are the top 10 job titles based on the average TotalPayBenefits? 
    </div>
    """, unsafe_allow_html=True)
category_quantity = data.groupby('JobTitle')['TotalPayBenefits'].sum().head(10)
max_category = category_quantity.idxmax()
max_value = category_quantity.max()

top_10_jobs = category_quantity.sort_values(ascending=False).head(10).reset_index()
top_10_jobs.columns = ['JobTitle', 'TotalPayBenefits']

st.dataframe(top_10_jobs)
# Draw the graph
fig7 = px.bar(top_10_jobs,
    x='JobTitle',
    y='TotalPayBenefits',
    title='Top 10 Jobs by Average Salary Total Pay Benefits',
    color='TotalPayBenefits',
    color_continuous_scale=px.colors.sequential.RdBu)

st.plotly_chart(fig7)

# 8. Salary Differences Across Years
st.subheader("8. Salary Differences Across Years")
st.markdown(
    """
    <div class="answer">
        Is there a noticeable difference in salaries across the years 2011, 2012, 2013, and 2014?
    </div>
    """, unsafe_allow_html=True)

# Calculate the average of TotalPay and TotalPayBenefits per year
average_pay_per_year = data.groupby('Year')['TotalPay'].mean().reset_index()

average_pay_per_year['TotalPay'] = average_pay_per_year['TotalPay'].apply(lambda x: f"{x:,.2f} $")
st.dataframe(average_pay_per_year)

# Draw a graph using lines to illustrate the comparison
fig8 = px.line(average_pay_per_year,
    x='Year',
    y=['TotalPay'],
    title='Average TotalPay per year')

fig8.update_layout(yaxis_title='Average Salary')

st.plotly_chart(fig8)

# 9. Police Officer Count & Salary
st.subheader("9. Police Officers Count and Average Salary")
st.markdown(
    """
    **How many people have the job title "Police Officer"? What is their average salary?**  
    """, unsafe_allow_html=True)
# Filter Police Officer who received JobTitle = Police Officer
officer_1 = data[(data['JobTitle'] == 'POLICE OFFICER I')]
officer_2 = data[(data['JobTitle'] == 'POLICE OFFICER II')]
officer_3 = data[(data['JobTitle'] == 'POLICE OFFICER III')]

#Calculate the number of these Police Officer
count_1 = len(officer_1)
count_2 = len(officer_2)
count_3 = len(officer_3)

Police_Officer = count_1 + count_2 + count_3

# Print the result
st.markdown(
    """
    <div class="answer">
    - How many people have the title Police Officer
    </div>
    """, unsafe_allow_html=True)
data_table = pd.DataFrame({
    'JobTitle': ['POLICE OFFICER I', 'POLICE OFFICER II', 'POLICE OFFICER III','Total POLICE OFFICER'],
    'Count POLICE OFFICER': [count_1, count_2, count_3,Police_Officer]
})
st.dataframe(data_table)

avg_1 = officer_1['TotalPay'].mean()
avg_2 = officer_2['TotalPay'].mean()
avg_3 = officer_3['TotalPay'].mean()

# Merge all salaries from the three ranks
total_salary_all = pd.concat([officer_1['TotalPay'], officer_2['TotalPay'], officer_3['TotalPay']])

# Calculate the overall mean
avg_4 = total_salary_all.mean()
st.markdown(
    """
    <div class="answer">
    -  What is their average salary?
    </div>
    """, unsafe_allow_html=True)

salary_table = pd.DataFrame({
    'JobTitle': ['POLICE OFFICER I', 'POLICE OFFICER II', 'POLICE OFFICER III','Total POLICE OFFICER Salary'],
    'Avg TotalPay': [f"{avg_1:,.2f} $", f"{avg_2:,.2f} $", f"{avg_3:,.2f} $",f"{avg_4:,.2f} $"]
})
st.dataframe(salary_table)

st.divider()
#Note
st.subheader("🔒 Note: Sensitive names and identifiers in the dataset have been anonymized to ensure data privacy.")