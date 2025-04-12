import streamlit as st

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


# Section: Analytical Questions for Salaries Analysis
st.header("Analytical Questions for Salaries Analysis")

# 1. Best-selling Category
st.subheader("1. Best-selling Category")
st.markdown(
    """
    **Which category is the best-selling in terms of quantity?**  
    <div class="answer">
    - <strong>Best-selling category by vale:</strong> Women’s Wear  <br>
    - <strong>Total Quantity:</strong> 678 
    </div>
    """, unsafe_allow_html=True)



# 2. Highest Revenue Region
st.subheader("2. Highest Revenue Region")
st.markdown(
    """
    **Which region achieved the highest revenue?**  
    <div class="answer">
    - <strong>Region with highest total sales:</strong> Mansoura  <br>
    - <strong>Total Sales:</strong> 64,890.15 EGP
    </div>
    """, unsafe_allow_html=True)



# 3. Month with Highest Sales
st.subheader("3. Month with Highest Sales")
st.markdown(
    """
    **Which month recorded the highest sales?**  
    <div class="answer">
    - <strong>Best sales month:</strong> November  <br>
    - <strong>Total Sales for this month:</strong> 24,937.34 EGP
    </div>
    """, unsafe_allow_html=True)



# 4. Day with Highest Sales
st.subheader("4. Day with Highest Sales")
st.markdown(
    """
    **Which day recorded the highest sales?**  
    <div class="answer">
    - <strong>Day with highest total sales:</strong> 2024-08-31  <br>
    - <strong>Total Sales:</strong> 2,855.21 EGP
    </div>
    """, unsafe_allow_html=True)


# 5. Top Spending Customer
st.subheader("5. Top Spending Customer")
st.markdown(
    """
    **Which customer spent the most on purchases?**  
    <div class="answer">
    - <strong>Customer with highest total sales:</strong> C190  <br>
    - <strong>Total Amount:</strong> 5,610.98 EGP
    </div>
    """, unsafe_allow_html=True)


# 6. Most Frequent Buyer
st.subheader("6. Most Frequent Buyer")
st.markdown(
    """
    **Which customer made the highest number of purchases?**  
    <div class="answer">
    - <strong>Customer with the highest number of purchases:</strong> C099  , C190<br>
    - <strong>Number of Purchases:</strong> 13
    </div>
    """, unsafe_allow_html=True)



# 7. Most Profitable Product
st.subheader("7. Most Profitable Product")
st.markdown(
    """
    **Which product is the most profitable based on total sales?**  
    <div class="answer">
    - <strong>Most profitable product:</strong> Scarf  <br>
    - <strong>Total Sales:</strong> 5,610.98 EGP
    </div>
    """, unsafe_allow_html=True)



# 8. Least Profitable Product
st.subheader("8. Least Profitable Product")
st.markdown(
    """
    **Which product is the least profitable based on total sales?**  
    <div class="answer">
    - <strong>Least profitable product:</strong> T-Shirt  <br>
    - <strong>Total Sales:</strong> 73.47 EGP
    </div>
    """, unsafe_allow_html=True)




# Question 9: Relationship Between Unit Price and Quantity Sold
st.subheader("9. Relationship Between Unit Price and Quantity Sold")
st.markdown(
    """
    <div class="answer">
    There is no relationship between the unit price and quantity sold.
    </div>
    """, unsafe_allow_html=True)


# Question 10: Regional Sales (Bar Chart)
st.subheader("10. Sales Distribution by Region")
st.markdown("**What is the total sales for each region?**")
st.table({
    "Region": ["Mansoura", "Alex", "Tanta", "Madinaty", "New Cairo", "Nasr City"],
    "Total Sales (EGP)": [64890.15, 63305.60, 62583.19, 49515.69, 8845.99, 5549.57]
})


# Question 11:How were sales distributed among different categories throughout the year?
st.subheader("11. How were sales distributed among different categories throughout the year?")


# Question 12: Category Contribution (Pie Chart)
st.subheader("12. Percentage Contribution by Category")
st.markdown("**What is the percentage contribution of sales by each category?**")
st.table({
    "Category": ["Women’s Wear", "Kids’ Wear", "Men’s Wear", "Accessories"],
    "Percentage": ["27.7%", "27.5%", "24.1%", "20.5%"]
})


# Question 13: Order Values (Bar Chart)
st.subheader("13. Average Order Value")
st.markdown(
    """
    **What is the average order value (Total Sales)?**  
    <div class="answer">
    - <strong>Minimum Sales:</strong> 10.83  <br>
    - <strong>Average Sales:</strong> 254.69019  <br>
    - <strong>Maximum Sales:</strong> 798.34
    </div>
    """, unsafe_allow_html=True)


# 14. Total Quantity Sold per Product
st.subheader("14. Total Quantity Sold per Product")
st.markdown("**What is the total quantity sold for each product?**")
st.table({
    "Product Name": ["Polo Shirt", "Scarf", "Jeans", "Socks", "Belt", "Gloves", "Jacket", "Hat", "Dress", "Sweater", "Shorts", "Watch", "Shoes", "Boots", "Sandals", "Skirt", "Blazer", "T-Shirt"],
    "Quantity": [290, 290, 245, 206, 190, 173, 151, 120, 105, 103, 102, 98, 93, 77, 67, 61, 56, 42]
})

# Recommendations
st.subheader("19. Recommendations for Improvement")
st.markdown(
    """
    <div class="answer">
    Based on the trends and patterns extracted from the data, the following recommendations are suggested:<br>
    - <strong>Leverage Strengths:</strong> Focus on the high performance of Women’s Wear, especially in regions with high sales.<br>
    - <strong>Expand Customer Base:</strong> Develop strategies to attract more new customers to balance the overwhelming percentage of repeat buyers.<br>
    - <strong>Seasonal Strategies:</strong> Optimize inventory and promotional activities during peak sales months (May and November).<br>
    - <strong>Reevaluate Underperformers:</strong> Consider revising pricing or marketing strategies for products that are underperforming, such as T-Shirts.
    </div>
    """, unsafe_allow_html=True)

st.divider()
#Note
st.subheader("🔒 Note: Sensitive names and identifiers in the dataset have been anonymized to ensure data privacy.")