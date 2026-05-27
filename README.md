# 📊 Telco Customer Churn Analysis

## 📌 Project Overview
This project analyzes the **Telco Customer Churn Dataset** to understand customer behavior and identify factors contributing to churn. Using **Pandas, Matplotlib, and Seaborn**, the workflow includes data cleaning, exploratory data analysis (EDA), and visualization to uncover actionable insights for telecom companies.

---

## ⚙️ Steps Performed

### 1. **Data Loading & Inspection**
- Loaded dataset using `pandas.read_csv`.  
- Checked dataset shape, column types, and missing values.  
- Verified duplicates in `customerID`.  

### 2. **Data Cleaning**
- Converted `TotalCharges` column from string to float (handling blank spaces).  
- Transformed `SeniorCitizen` column:  
  - 0 → No  
  - 1 → Yes  

### 3. **Exploratory Data Analysis (EDA)**
- **Churn Distribution:** ~26.54% customers churned.  
- **Churn by Gender:** No significant difference between male and female churn rates.  
- **Churn by Senior Citizen:** Higher churn among senior citizens.  
- **Tenure Analysis:** Short-tenure customers (1–2 months) churn more; long-tenure customers are more loyal.  
- **Contract Type:** Month-to-month contracts have the highest churn; 1- and 2-year contracts reduce churn significantly.  
- **Service Features:** Lack of Online Security, Tech Support, and Backup Services strongly correlates with churn.  
- **Internet Service:** Fiber optic users churn more compared to DSL.  
- **Payment Method:** Customers using Electronic Check are more likely to churn.  

---

## 📈 Key Visualizations
- Churn Count & Percentage  
- Churn by Gender  
- Churn by Senior Citizen (absolute & percentage)  
- Tenure vs Churn (histogram)  
- Contract Type vs Churn  
- Service Features vs Churn (multiple subplots)  
- Payment Method vs Churn  

---

## 🔑 Insights
- **26.54% churn rate** observed.  
- Senior citizens churn more than younger customers.  
- Short-tenure customers (1–2 months) are highly likely to churn.  
- Month-to-month contracts are risky; longer contracts improve retention.  
- Electronic check payment method is strongly associated with churn.  
- Value-added services (security, backup, tech support) reduce churn.  
- Fiber optic internet users show higher churn compared to DSL.  

---

## 📌 Conclusion
This analysis highlights critical factors influencing customer churn. By focusing on **contract type, tenure, payment methods, and value-added services**, telecom companies can design better **retention strategies** and reduce churn rates.

---

## 🛠️ Tech Stack
- **Python** → Data processing and analysis.  
- **Pandas** → Data manipulation and cleaning.  
- **Matplotlib & Seaborn** → Visualization and EDA.  

---

## 🚀 Usage
1. Clone the repository.  
2. Install required libraries (`pandas`, `matplotlib`, `seaborn`).  
3. Run the Jupyter Notebook or Python scripts to reproduce analysis.  
4. Explore visualizations to derive insights.  
