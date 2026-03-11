# 🚗 Used Car Price Prediction Using Machine Learning

This project predicts the **selling price of used cars** using Machine Learning.  
The model is trained using the **CarDekho Used Car Dataset** and deployed using **Streamlit** for interactive predictions.

---

# 📌 Problem Statement

Determining the correct price of a used car is difficult because it depends on many factors such as:

- Car age
- Present market price
- Kilometers driven
- Fuel type
- Transmission type
- Number of previous owners

Incorrect pricing can cause financial loss for sellers or overpayment for buyers.

This project aims to build a **machine learning model that predicts the selling price of a used car based on its features**.

---

# 📊 Dataset

Dataset Name: **CarDekho Used Car Dataset**

Kaggle Link:  
https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho

The dataset contains information about used cars listed on the CarDekho platform.

### Dataset Features

| Feature | Description |
|------|-------------|
| Car_Name | Name of the car |
| Year | Manufacturing year |
| Selling_Price | Selling price of the car |
| Present_Price | Current ex-showroom price |
| Kms_Driven | Distance driven by the car |
| Fuel_Type | Petrol / Diesel / CNG |
| Seller_Type | Dealer or Individual |
| Transmission | Manual or Automatic |
| Owner | Number of previous owners |

---

# 🤖 Machine Learning Model

Model Used:

**Random Forest Regressor**

### Why Random Forest?

- Works well with structured datasets
- Handles nonlinear relationships
- Reduces overfitting
- Provides high prediction accuracy

The model learns patterns between car features and their selling prices to make accurate predictions.

---

# ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Streamlit
- Pickle

---

# 🧠 Project Workflow

The project follows the typical **Machine Learning pipeline**:

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Exploratory Data Analysis (EDA)
5. Model Training
6. Model Evaluation
7. Model Saving using Pickle
8. Deployment using Streamlit

---

# 📊 Data Visualization

Some important visualizations used during the analysis:

- Correlation Heatmap
- Feature Distribution Graphs
- Price vs Feature Relationships

These visualizations help understand the relationships between car features and their prices.

---

# 📂 Project Structure

```
used-car-price-prediction

car data.csv
train_model.py
app.py
model.pkl
model_columns.pkl
requirements.txt
README.md
```

---

# 🧩 Model Training

The model is trained using **Random Forest Regression**.

Steps:

1. Load dataset
2. Perform data preprocessing
3. Encode categorical variables
4. Train model
5. Save trained model using pickle

---

# 💾 Model Saving

The trained model is saved using **Pickle**.

Saved files:

- model.pkl → trained machine learning model  
- model_columns.pkl → training feature columns

This allows the model to be used later in the Streamlit application.

---

# 🌐 Streamlit Web Application

A Streamlit web app is created so users can easily predict car prices.

Users input:

- Present Price
- Kilometers Driven
- Car Age
- Fuel Type
- Transmission Type
- Owner History

The model then predicts the **estimated selling price of the car**.

---

# ▶️ How to Run the Project

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Train the Model

```bash
python train_model.py
```

This will generate:

```
model.pkl
model_columns.pkl
```

### Step 3: Run the Streamlit App

```bash
streamlit run app.py
```

Open your browser and go to:

```
http://localhost:8501
```

---

# 📈 Example Prediction

User Inputs:

```
Present Price: 7.5
Kms Driven: 40000
Car Age: 5
Fuel Type: Petrol
Transmission: Manual
Owner: 0
```

Predicted Output:

```
Estimated Car Price: 5.82 Lakhs
```

---

# 💼 Business Value

This project can be used by:

- Car resale platforms (CarDekho, Cars24, OLX)
- Automobile dealerships
- Individual buyers and sellers

Benefits:

- Accurate car price estimation
- Data-driven pricing decisions
- Reduced negotiation time
- Better market transparency

---

# 🚀 Future Improvements

Possible improvements for this project:

- Use advanced models like **XGBoost**
- Add **more vehicle features**
- Deploy full web application
- Integrate **car image recognition**
- Build a **mobile app version**

---

# 👨‍💻 Author

**Data Science Project**

Used Car Price Prediction using Machine Learning and Streamlit.
