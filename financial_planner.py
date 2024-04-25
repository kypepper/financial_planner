import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Function to calculate Social Security benefits
def calculate_social_security_benefits(user_age, full_retirement_age, annual_income):
    # Calculate the number of years until full retirement age
    years_until_full_retirement = full_retirement_age - user_age
    if years_until_full_retirement <= 0:
        return 0
    
    # Assume the user's current income remains constant until retirement
    estimated_income_until_retirement = annual_income * years_until_full_retirement
    
    # Calculate the estimated Social Security benefits based on the estimated income
    # You can use the Social Security Administration's benefit calculator or formula to estimate benefits
    # For simplicity, we'll use a basic formula or approximation here
    social_security_benefits = estimated_income_until_retirement * 0.3  # Example: Assuming 30% of income
    
    return social_security_benefits

# Function to calculate life expectancy based on current age
def calculate_life_expectancy(current_age):
    # You can use actuarial tables or statistical data to estimate life expectancy
    # For simplicity, we'll assume an average life expectancy of 85 years
    return 85 - current_age

# Financial Planner
st.header("Financial Planner")

monthly_income = st.number_input("Monthly Income:", min_value=0.0, step=100.0)
monthly_expenses = st.number_input("Monthly Expenses:", min_value=0.0, step=100.0)

remaining_balance = monthly_income - monthly_expenses
st.write(f"Remaining Balance: ${remaining_balance:.2f}")

# Expense Tracker
st.header("Expense Tracker")

expenses = {
    "Category": ["Groceries", "Rent", "Utilities", "Entertainment"],
    "Amount": []
}

for category in expenses["Category"]:
    expense = st.number_input(f"{category} Expense:", min_value=0.0, step=10.0)
    expenses["Amount"].append(expense)

expenses_df = pd.DataFrame(expenses)
st.write("### Monthly Expenses Breakdown")
st.write(expenses_df)

# Handle NaN values in expenses DataFrame
expenses_df['Amount'] = expenses_df['Amount'].fillna(0)

# Pie Chart for Expense Breakdown using Plotly
fig = px.pie(expenses_df, values='Amount', names='Category', title='Monthly Expense Breakdown')
st.plotly_chart(fig)

# Goal Tracking
st.header("Goal Tracking")

# Add tools to set financial goals and track progress (ky)

# Retirement Planning
st.header("Retirement Planning")

current_age = st.number_input("Current Age:", min_value=0, step=1)
desired_retirement_age = st.number_input("Desired Retirement Age:", min_value=current_age+1, step=1)
annual_retirement_expenses = st.number_input("Annual Retirement Expenses:", min_value=0.0, step=100.0)

# Calculate estimated Social Security benefits
social_security_benefits = calculate_social_security_benefits(current_age, 67, monthly_income * 12)  # Assuming full retirement age is 67

# Calculate total estimated retirement income including Social Security
total_retirement_income = annual_retirement_expenses + social_security_benefits

# Calculate life expectancy
life_expectancy = calculate_life_expectancy(current_age)

st.write(f"Total Retirement Expenses: ${annual_retirement_expenses:.2f}")
st.write(f"Estimated Social Security Benefits: ${social_security_benefits:.2f}")
st.write(f"Total Retirement Income (including Social Security): ${total_retirement_income:.2f}")
st.write(f"Life Expectancy: {life_expectancy} years")

# Recommended Savings
st.header("Recommended Savings")

savings_recommendation = (monthly_income - monthly_expenses) * 0.2  # Saving 20% of monthly income
st.write(f"Recommended Monthly Savings: ${savings_recommendation:.2f}")

# Goal-Based Savings Calculator
st.header("Goal-Based Savings Calculator")

goal_amount = st.number_input("Goal Amount:", min_value=0.0, step=100.0)
timeframe_years = st.number_input("Timeframe (Years):", min_value=1, step=1)
expected_return = st.number_input("Expected Annual Return (%):", min_value=0.0, step=0.1)

# Calculate monthly savings required to reach the goal
monthly_savings_needed = (goal_amount / (timeframe_years * 12)) / ((1 + expected_return / 100) ** timeframe_years)
st.write(f"Monthly Savings Needed: ${monthly_savings_needed:.2f}")

# Tax Planning Tools
st.header("Tax Planning Tools")
# Add resources and calculators for tax planning
st.write("### Tax Estimation Calculator")

# Get inputs for income, deductions, and tax brackets
income = st.number_input("Total Income:", min_value=0.0, step=100.0)
deductions = st.number_input("Total Deductions:", min_value=0.0, step=100.0)

# Define tax brackets and rates
tax_brackets = {
    "10%": (0, 9875),
    "12%": (9876, 40125),
    "22%": (40126, 85525),
    "24%": (85526, 163300),
    "32%": (163301, 207350),
    "35%": (207351, 518400),
    "37%": (518401, float('inf'))
}

# Calculate tax liability based on income and tax brackets
tax_liability = 0
for rate, (lower, upper) in tax_brackets.items():
    taxable_income = min(upper, max(0, income - deductions)) - lower
    if taxable_income <= 0:
        continue
    tax_liability += taxable_income * (float(rate.strip('%')) / 100)

st.write(f"Estimated Tax Liability: ${tax_liability:.2f}")

# Additional Features
# Add more features based on user feedback and requirements
