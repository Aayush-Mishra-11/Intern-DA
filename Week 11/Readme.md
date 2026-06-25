# Week 11 Customer Segment Profiles
Customer Segmentation & Prediction project.
**Dataset:** 500 customers from `customer_churn.csv`
**Clustering method:** K-Means (k=4), validated vs Hierarchical & DBSCAN
**K-Means silhouette:** 0.1485

---

## Methodology

1. Encoded categorical features (`Contract`, `PaymentMethod`, `PaperlessBilling`).
2. Standardised 7 numerical/coded features.
3. Used the **Elbow method** and **silhouette score** to pick k = 4.
4. Ran K-Means as primary, plus Hierarchical (Ward) and DBSCAN for comparison.
5. Named segments based on tenure, monthly charges, contract type, and seniority.

---

## Segments

### Mid-Spend Traditional Users (Cluster 2)

- **Share of base:** 25.0% (125 customers)
- **Average tenure:** 36.7 months
- **Average monthly charges:** $116.82
- **Average total charges:** $4256
- **% Senior citizens:** 0.0%
- **% Paperless billing:** 0.0%
- **Most common contract:** One year
- **Most common payment method:** Electronic Check
- **Churn rate:** 11.0%

### Senior Digital Switchers (Cluster 1)

- **Share of base:** 23.8% (119 customers)
- **Average tenure:** 35.4 months
- **Average monthly charges:** $108.82
- **Average total charges:** $4488
- **% Senior citizens:** 100.0%
- **% Paperless billing:** 71.0%
- **Most common contract:** Two year
- **Most common payment method:** Credit Card
- **Churn rate:** 6.0%

### Senior Legacy Non-Paperless (Cluster 3)

- **Share of base:** 26.0% (130 customers)
- **Average tenure:** 36.0 months
- **Average monthly charges:** $107.52
- **Average total charges:** $4080
- **% Senior citizens:** 100.0%
- **% Paperless billing:** 25.0%
- **Most common contract:** Month-to-month
- **Most common payment method:** Credit Card
- **Churn rate:** 14.0%

### Young Digital Customers (Cluster 0)

- **Share of base:** 25.2% (126 customers)
- **Average tenure:** 38.0 months
- **Average monthly charges:** $121.33
- **Average total charges:** $4147
- **% Senior citizens:** 0.0%
- **% Paperless billing:** 100.0%
- **Most common contract:** One year
- **Most common payment method:** Bank Transfer
- **Churn rate:** 11.0%


## Clustering Method Comparison

| Method | Silhouette | Clusters |
|---|---|---|
| K-Means (k=4) | 0.1485 | 4 |
| Hierarchical Ward (k=4) | 0.1089 | 4 |
| DBSCAN (eps=1.4, min_samples=8) | 0.6222 | 3 (+ noise) |



📋 Step-by-Step Guide:
Day 1: Clustering Basics - Apply K-Means clustering, determine optimal clusters using Elbow method
Day 2: Advanced Clustering - Try Hierarchical clustering and DBSCAN, compare results
Day 3: Segment Analysis - Analyze cluster characteristics, create customer profiles and names
Day 4: Prediction Models - Build separate Random Forest models for each segment
Day 5: Model Evaluation - Calculate accuracy, precision, recall, F1-score, ROC-AUC for each segment
Day 6: Hyperparameter Tuning - Use Grid Search to optimize Random Forest parameters
Day 7: Business Insights - Create segment-specific strategies, estimate business impact

📊 Sample Output:
CUSTOMER SEGMENTS:
1. Premium Spenders (25%)
2. Budget Conscious (30%)
3. Young Professionals (20%)

MODEL PERFORMANCE:
Premium: 92% accuracy, F1: 0.89
Budget: 88% accuracy, F1: 0.85

📚 Data Source:
https://bit.ly/customer-segmentation-data
