import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_csv("Telco_Customer_Churn_Dataset.csv")
print(df.head(2))
print(df.shape)
print(df.info())

df["TotalCharges"]=df["TotalCharges"].replace(" ","0")
df["TotalCharges"]=df["TotalCharges"].astype("float")
print(df.info())



null_values=df.isnull().sum()
print(null_values)

print(df.describe())

duplicate_value=df["customerID"].duplicated().sum()
print(duplicate_value)

#NOTE: convert 0 and 1 values of senior citizen to yes/no to make it easier to understand

def conv(value):
    if value==1:
       return "yes"
    else :
        return "no"
df["SeniorCitizen"]=df["SeniorCitizen"].apply(conv)
df["SeniorCitizen"]=df["SeniorCitizen"].astype("object")

    
'''
ax=sns.countplot(data=df,x="Churn")
ax.bar_label(ax.containers[0],fontsize=10,color="Black")
plt.title("Count of Customers by Churn",fontsize=16, color="black", fontweight="bold")
plt.show()

plt.figure(figsize=(4,4))
gb=df.groupby("Churn").agg({'Churn':"count"})
print(gb)
plt.pie(gb["Churn"],labels=gb.index,autopct="%1.2f%%")
plt.title("Percentage of Churned Customers",fontsize=10, color="darkred", fontweight="bold")
plt.show()
#NOTE: from the given pie chart we can conclude that 26.54% of our customers have churned out
#now let's explore the reason behind it



ax=sns.countplot(data=df,x="gender",hue="Churn")
for container in ax.containers:
    ax.bar_label(container,fontsize=10,color="black" )
plt.title("Churn by Gender",fontsize=16,color="darkblue", fontweight="bold")
plt.show()



ax=sns.countplot(data=df,x="SeniorCitizen")
for container in ax.containers:
    ax.bar_label(container,fontsize=10,color="black" )
plt.title("Count of Customers by Senior Citizen ",fontsize=16,color="darkblue", fontweight="bold")
plt.show()



counts = pd.crosstab(df['SeniorCitizen'], df['Churn'])
percentages = counts.div(counts.sum(axis=1), axis=0) * 100

ax = percentages.plot(
    kind='bar',
    stacked=True,
    figsize=(6, 4),
    
)

for container in ax.containers:
    ax.bar_label(container, fmt='%.1f%%', label_type='center')

plt.title("Churn by SeniorCitizen (Percentage)")
plt.xlabel("SeniorCitizen")
plt.ylabel("Percentage")
plt.legend(title="Churn")
plt.tight_layout()
plt.show()

#NOTE: comparative a greater percentage of people in senior citizen category have churned



plt.figure(figsize= (9,4))
sns.histplot(data=df,x="tenure",bins= df["tenure"].max(),hue="Churn")
plt.show()

#NOTE: People who used our services for a long time ave stayed and pople whoe used our serives for #1 or 2 months have churned


ax=sns.countplot(data=df,x="Contract",hue="Churn")
for container in ax.containers:
    ax.bar_label(container,fontsize=10,color="black" )
plt.title("Count of Customers by Contract ",fontsize=16,color="darkblue", fontweight="bold")
plt.show()

#or

counts = pd.crosstab(df['Contract'], df['Churn'])
percentages = counts.div(counts.sum(axis=1), axis=0) * 100

ax = percentages.plot(
    kind='bar',
    stacked=True,
    figsize=(6, 4),
    
)

for container in ax.containers:
    ax.bar_label(container, fmt='%.1f%%', label_type='center')

plt.title("Churn by Contract (Percentage)")
plt.xlabel("Contract")
plt.xticks(rotation=0)
plt.ylabel("Percentage")
plt.legend(title="Churn",bbox_to_anchor=(1,1))
plt.tight_layout()
plt.show()
# NOTE:people who have month to month contract are likely to churn then those who have 1 or 2 years contract

print(df.columns)

features = ['PhoneService', 'MultipleLines', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies']

fig, axs = plt.subplots(3, 3, figsize=(18, 10))

axs = axs.flatten()

for i, feature in enumerate(features):
    sns.countplot(data=df, x=feature, ax=axs[i], palette="Set2",hue=df["Churn"])
    axs[i].set_title(f'Distribution of {feature}', fontsize=14)
    axs[i].set_xlabel('')  # Remove x-label text for clean appearance
    axs[i].set_ylabel('Count', fontsize=12)
    axs[i].tick_params(axis='x', rotation=0)  # Rotate x-axis labels if necessary

# Optimize layout to prevent overlap
plt.tight_layout()

# Display the subplots
plt.show()
# NOTE: Customers without online security, tech support, and backup services show significantly higher churn rates.
#Users with fiber optic internet tend to churn more compared to DSL users.
#Having device protection, online security, and tech support is associated with lower churn.
#Streaming services (TV/movies) and multiple lines show relatively smaller impact on churn compared to security-related features.
'''
plt.figure(figsize=(8,6))
ax=sns.countplot(data=df,x="PaymentMethod",hue="Churn")
for container in ax.containers:
    ax.bar_label(container,fontsize=10,color="black" )
plt.title("CHURN Customers by PaymentMethod",fontsize=16,color="darkblue", fontweight="bold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show() 

# NOTE: CUSTOMER LIKELY TO CHURN WHEN HE IS USING ELECTRONIC CHECK AS PAYMMENT METHOD.


