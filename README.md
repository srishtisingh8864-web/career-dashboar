# career-dashboard
# 📊 Career Progression & Promotion Gap Analysis for Retention Optimization

## 🧩 Problem Statement

Employees often leave organizations not due to immediate dissatisfaction, but because of long-term career issues such as delayed promotions, role stagnation, lack of skill development, and unstable management.

Traditional attrition models only predict *who might leave*, but fail to explain *why*.
This project focuses on identifying hidden career progression issues that impact employee retention.

---

## 🎯 Objective

The main objective of this project is to:

* Analyze employee career growth patterns
* Identify promotion stagnation and role stagnation
* Segment employees based on career trajectory
* Provide data-driven retention strategies

---

## 📂 Dataset Description

The dataset includes employee-related information such as:

* Demographics (Age, Gender, Marital Status)
* Job details (Department, Job Role, Job Level)
* Compensation (Monthly Income, Salary Hike)
* Experience (Years at Company, Years in Role)
* Satisfaction metrics (Job Satisfaction, Work-Life Balance)
* Promotion history (Years Since Last Promotion)

---

## ⚙️ Methodology

### 1. Feature Engineering

New metrics were created to capture career progression:

* **Promotion Gap Ratio** = YearsSinceLastPromotion / YearsAtCompany
* **Role Stagnation Index** = YearsInCurrentRole / YearsAtCompany
* **Training Intensity Score** = TrainingTimesLastYear / YearsAtCompany
* **Manager Stability Indicator** = YearsWithCurrManager / YearsAtCompany

---

### 2. Data Preprocessing

* Handled missing values
* Normalized numerical features
* Encoded categorical variables
* Removed outliers

---

### 3. Clustering (Unsupervised Learning)

* Applied **K-Means Clustering**
* Grouped employees based on career progression patterns

---

## 📊 Cluster Insights

* **Cluster 0: Fast Growth Employees**
  Frequent promotions and strong career progression

* **Cluster 1: Stagnant Employees**
  Long time in same role, low promotion rate

* **Cluster 2: High Training but Low Promotion**
  Skilled but not rewarded with promotions

* **Cluster 3: Manager Instability Risk**
  Frequent manager changes affecting growth

---

## 🔍 Key Insights

* Employees with high **promotion gaps** are more likely to leave
* Long tenure in the same role leads to disengagement
* Training alone is not enough without career growth
* Stable management improves retention

---

## 💡 Business Recommendations

* Introduce structured promotion cycles
* Provide role transition opportunities
* Align training programs with promotion pathways
* Improve manager-employee continuity

---

## 🛠️ Tools & Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib / Seaborn
* Streamlit (for dashboard)

---

## 📈 Project Outcome

This project helps identify employees at risk due to career stagnation and enables organizations to take proactive, targeted retention actions.

---

## 🚀 Future Improvements

* Add predictive model for attrition risk
* Integrate real-time HR data
* Build advanced dashboards using Power BI

---

## 📌 Conclusion

Career growth plays a critical role in employee retention. By analyzing promotion gaps and career stagnation, organizations can move from reactive to proactive retention strategies.
