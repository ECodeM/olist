
---

# Olist Seller Performance Analysis

This project evaluates the impact of removing Olist's worst-performing sellers to improve profitability.

## Problem Statement

Olist's team raised the question: **Should Olist remove its worst-performing sellers?** We conducted a detailed analysis based on the available datasets to provide a data-driven recommendation.

## Recommendation

After comprehensive analysis, we recommend removing **5%** of underperforming sellers, totaling **149 sellers** who generated a cumulative loss of **R$1,025,925.81 BRL**. This selective removal focuses on sellers who have been on the platform for over 3 months and consistently causes losses.

## Key Findings

- **Revenue Dependency**: Olist's business model relies on the **R$80.00 BRL monthly seller fee**, contributing to 54% of total revenue. Cutting all underperforming sellers (29% of total) would drastically reduce revenue.
- **Underperforming Sellers**: Of the total 854 underperforming sellers (29% of total sellers), we excluded those in their first 3 months ("honeymoon phase"). This left us with 149 sellers to be removed, mitigating losses without compromising future potential.
- **Impact on IT Costs**: Removing these sellers has barely no impact on IT costs, calculated using the formula:
  
  ```
  IT_costs = α * √n_sellers + β * √n_items
  ```
  where `α = 3157.27` and `β = 978.23`. Total IT costs amounted to approximately **R$500,000 BRL**.

  <img width="1114" alt="Screenshot 2024-09-30 at 4 59 40 PM" src="https://github.com/user-attachments/assets/7ee2a41c-0116-4d52-9db1-d1e4d2f7c953">


## Data and Technical Approach

We processed and analyzed data from 8 uncleaned CSV files, using the following steps:

1. **Data Cleaning**: Handled null values, incoherent entries, and inconsistencies in seller, product, and order data.
2. **Feature Engineering**: Merged datasets to create features relevant to profitability, seller performance, and customer reviews.
3. **Mathematical Models**: Calculated the financial impact of sellers based on order volume, customer reviews, and profitability metrics.
4. **Cost Analysis**: IT and review costs were factored into the decision, where review costs were calculated as:
  
   ```
   {'1 star': 100 BRL, '2 stars': 50 BRL, '3 stars': 40 BRL, '4-5 stars': 0 BRL}
   ```

## Conclusion

By removing **5%** of sellers, Olist can mitigate losses from underperforming sellers while maintaining profit margins and minimizing the impact on operational costs.

---
