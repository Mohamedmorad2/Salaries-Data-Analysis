# 📊 Salaries Analysis Report


![Image Description](Image/pexels-pixabay.jpg)
This project analyzes a dataset containing detailed information on San Francisco city government employee compensation—covering job titles, departments, base salaries, overtime, and benefits. The analysis reveals trends such as skewed salary distributions.



## 🚀 Features

- Load and view salary data from a CSV file
- Analyze number of employees per year
- Compare mean and median of salaries over the years
- Visualize highest paid employees and job titles
- Filter jobs with salaries over $250,000
- Explore police officers' count and salary stats
- Choose report language (English / Arabic)
- Interactive charts with **Plotly**

## 🗂️ Project Structure

```
project/
├── app.py                     
├── Data/
│   ├── SF Salaries.csv 
│   └──Salaries.csv          
├── Report/
│   ├── Salaries_Analysis_Report_EN.pdf 
│   └── Salaries_Analysis_Report_AR.pdf
└── README.md                   
```

## 🛠️ Requirements

Install dependencies using pip:

```bash
pip install streamlit pandas plotly pillow
```

## ▶️ Run the App

In your terminal, navigate to the project directory and run:

```bash
streamlit run app.py
```

This will launch the app in your browser at `http://localhost:8501`.

## 📁 Data Source

The data used in this dashboard is from a file named `SF Salaries.csv`, located inside the `Data/` folder.

Make sure this file exists before running the app.

## 🧠 Insights Provided

1. Employee counts per year (2011–2014)
2. Trends in total pay and benefits
3. Most frequent job titles
4. Top 10 highest paying job titles
5. Job titles with salaries exceeding $250K
6. Salary analysis of Police Officers by rank
7. Visuals using Plotly for easy understanding

## 📌 Notes

- Employee names in the dataset are anonymized for privacy.
- The data is sourced from the City and County of San Francisco's Open Data Portal.
