# IEEE_LAT_AM_T_9776
# Title Machine Learning Assisted mm-Wave MIMO Antenna Design with High Isolation for 5G Applications
**Author: Ramasamy R, Rajavel V and Rachit Jain**
Ramasamy R is with the Department of ECE at Ramco Institute of Technology Rajapalayam, Tamil Nadu, India. (e-mail: ramasamy@ritrjpm.ac.in).
Rajavel V is with the Department of ECE at Mepco Schlenk Engineering College Sivakasi, Tamil Nadu, India. (e-mail: rajavelv@mepcoeng.ac.in).
Rachit Jain is with the Department of IT at Prestige Institute of Management & Research, Gwalior, India. (e-mail: rachit.jain@prestigegwl.org and rachit2709@gmail.com ).

This repository contains Python codes for implementing various Machine Learning algorithms (Decision Tree, Random Forest, XGBoost, KNN, and Gradient Boosted Regression) on the dataset alldataset.csv.
The project demonstrates how ML can be applied to optimize and analyze mm-Wave MIMO Antenna Design with High Isolation for 5G Applications.
---
## Dataset

The dataset file **`alldataset.csv`** is required for all scripts and must be placed either in the working directory or uploaded to **Google Drive** for execution in **Google Colab**.

This dataset is required for the following scripts:  
- `1_rama_sr_dt.py` (Decision Tree)  
- `2_rama_sr_gbr.py` (Gradient Boosting Regressor)  
- `3_rama_sr_xg.py` (XGB)  
- `4_rama_sr_knn.py` (KNN)  
- `5_rama_sr_rf.py` (Random Forest)  

**Note:** Place `alldataset.csv` in the **same folder as the scripts** so that the models can read the dataset correctly and execute without errors.

---
**Included Scripts**

| Script            | Related Fig./Table | Description |
|--------------------|--------------------|-------------|
| **1_rama_sr_dt.py**  | Fig 9a / Table IV  | Implements the **Decision Tree (DT)** model to train and predict return loss values. The model achieved **R² = 0.988**, with low error values (**MSE = 0.555, MAE = 0.085, MAPE = 0.004**), and very fast execution (**Fit Time = 0.015s, Predict Time = 0.003s**), indicating reliable and efficient performance. |
| **2_rama_sr_gbr.py** | Fig 9e / Table IV  | Implements the **Random Forest (RF)** ensemble model, capturing complex patterns effectively. It delivered the **best overall accuracy** with **R² = 0.992, MSE = 0.389, MAE = 0.072, MAPE = 0.004**. Although training required more time (**0.808s**), prediction remained fast (**0.032s**), making RF highly dependable for return loss prediction. |
| **3_rama_sr_xg.py**  | Fig 9d / Table IV  | Applies the **K-Nearest Neighbors (KNN)** algorithm to estimate return loss based on nearest neighbor similarity. The model performed well with **R² = 0.990, MSE = 0.450, MAE = 0.116, MAPE = 0.006**. It had the **fastest training time (0.004s)** and quick predictions (**0.008s**), making it efficient for lightweight applications. |
| **4_rama_sr_knn.py** | Fig 9c / Table IV  | Uses the **Extreme Gradient Boosting (XGB)** model, known for handling complex, non-linear data. It achieved **R² = 0.977, MSE = 1.056, MAE = 0.195, MAPE = 0.009**. Training was moderate (**0.094s**), with fast predictions (**0.006s**). While slightly less accurate than RF and DT, XGB still produced dependable results. |
| **5_rama_sr_rf.py**  | Fig 9b / Table IV  | Implements the **Gradient Boosting Regressor (GBR)** for sequential learning. The model obtained **R² = 0.914**, with higher errors (**MSE = 4.021, MAE = 1.287, MAPE = 0.058**), indicating weaker predictive accuracy compared to other models. Training (**0.373s**) and prediction (**0.004s**) times were reasonable, but GBR underperformed relative to RF, DT, and KNN. |

Each script corresponds to a specific machine learning model used for return loss prediction. To reproduce the results reported in **Table IV** and **Figure 9 (a–e)**, simply run the Python files individually.

---
## Requirements

Make sure you have the following Python libraries installed:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost
```
## Machine Learning Models Implemented

The repository includes the following ML models along with their Python import commands:

- **Decision Tree (DT)**  
  ```python
  from sklearn.tree import DecisionTreeRegressor
- **Random Forest (RF)**
  ```python
  from sklearn.ensemble import RandomForestRegressor

- **XGBoost (XGB)**
  ```python
  from xgboost import XGBRegressor
  
- **K-Nearest Neighbors (KNN)**

  ```python
  from sklearn.neighbors import KNeighborsRegressor

- **Gradient Boosted Regressor (GBR)**
  ```python
  from sklearn.ensemble import GradientBoostingRegressor

---
## Model Evaluation Metrics

Each model is evaluated using the following metrics:

- **R²** (Coefficient of Determination)  
- **Mean Squared Error (MSE)**  
- **Mean Absolute Error (MAE)**  
- **Mean Absolute Percentage Error (MAPE)**  
- **Fit Time** (seconds)  
- **Predict Time** (seconds)  
---
## Visualization

- Plots are generated using **Matplotlib** or **Seaborn**.  
- Each figure shows **predicted vs. actual return loss values** across the **32.5–45 GHz range**.  
- All scripts can be executed in **Google Colab** or a **local Python environment**.  

---

## Environment Requirements

- **Python 3.7+** (recommended for compatibility)  
- **Google Colab** or **Jupyter Notebook** for execution in cloud or local environments

---

## Graphical Abstract for proper understanding

This study investigates the design and performance of millimeter-wave (mm-Wave) Multiple-Input Multiple-Output (MIMO) antennas for fifth-generation (5G) applications, with a particular focus on the consequences of incorporating a ring resonator within the antenna system. This study compares two design variations—one with a ring resonator and one without—to assess their impact on enhancing the antenna's performance characteristics. The research employs five machine learning algorithms, namely, Decision Tree, Random Forest, K-Nearest Neighbors (KNN), XG-Boost, and Gradient Boosting Regressor (GBR), to estimate return loss. Among these, the Random Forest algorithm demonstrates superior performance in terms of accuracy, Mean Squared Error (MSE), Mean Absolute Percentage Error (MAPE), Mean Absolute Error (MAE), and R-squared metrics. The proposed MIMO antenna system shows better performance in Envelope Correlation Coefficient (ECC), Diversity Gain (DG), Channel Capacity Loss (CCL) and Total Active Reflection Coefficient (TARC). The results indicate that including a ring resonator in the antenna design significantly improves the antenna's performance, and machine learning algorithms, particularly Random Forest, can effectively predict and optimize critical parameters for antenna design in 5G applications. 



<img width="4420" height="2154" alt="Graphical_abstract" src="https://github.com/user-attachments/assets/79a98a11-ad69-45ad-a48d-0e303982f3ec" />


