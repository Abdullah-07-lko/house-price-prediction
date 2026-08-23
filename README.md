# 🏠 Bangalore House Price Prediction

A machine learning web application that predicts the estimated price of a house in Bangalore based on **location, total area, number of bedrooms (BHK), and bathrooms**.

The project includes a trained Machine Learning model, a Flask REST API, and a simple HTML/CSS/JavaScript frontend. The complete application is deployed online so anyone can use it.

## 🚀 Live Demo

**Website:**
https://house-price-prediction-2lxr.onrender.com

**Backend API:**
https://house-price-prediction-api-pcvo.onrender.com

---

## 📌 Project Overview

The main goal of this project is to build an end-to-end Machine Learning application rather than only training a model in a notebook.

The workflow is:

```text
User Input
    ↓
Frontend (HTML/CSS/JavaScript)
    ↓
Flask REST API
    ↓
Preprocessing / Feature Creation
    ↓
Trained Linear Regression Model
    ↓
Predicted House Price
    ↓
Frontend
```

The user provides:

* Total area in square feet
* Number of BHK
* Number of bathrooms
* Location

The application then sends these details to the Flask backend, which uses the trained model to generate the estimated price.

---

## 🛠️ Technologies Used

### Machine Learning

* Python
* NumPy
* Pandas
* Scikit-learn
* Linear Regression
* Pickle

### Backend

* Flask
* Flask-CORS
* REST API

### Frontend

* HTML
* CSS
* JavaScript
* jQuery

### Deployment & Tools

* GitHub
* Render
* VS Code
* Postman

---

## 📂 Project Structure

```text
house-price-prediction/
│
├── Client/
│   ├── index.html
│   ├── app.js
│   └── app.css
│
├── Model/
│   ├── House_Prediction_System.ipynb
│   ├── banglore_home_prices_model.pickle
│   └── columns.json
│
├── Server/
│   ├── server.py
│   ├── util.py
│   ├── requirements.txt
│   │
│   └── artifacts/
│       ├── columns.json
│       └── banglore_home_prices_model.pickle
│
└── README.md
```

---

## 🤖 Machine Learning Model

A **Linear Regression** model is used for house price prediction.

The model uses the following main inputs:

* `total_sqft`
* `bath`
* `bhk`
* `location`

The location feature is converted into numerical features using one-hot encoding.

The trained model is saved as a `.pickle` file and loaded by the Flask backend during prediction.

---

## 🔌 API Endpoints

### 1. Get Location Names

**Endpoint:**

```text
GET /get_location_names
```

Example:

```text
https://house-price-prediction-api-pcvo.onrender.com/get_location_names
```

This endpoint returns the available locations that can be selected in the frontend.

---

### 2. Predict House Price

**Endpoint:**

```text
POST /predict_home_price
```

Request parameters:

```text
total_sqft
bhk
bath
location
```

Example:

```text
total_sqft = 1000
bhk = 3
bath = 3
location = 1st Phase JP Nagar
```

Example response:

```json
{
    "estimated_price": 98.58
}
```

The estimated price is displayed in **Lakhs** in the frontend.

---

## 💻 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Abdullah-07-lko/house-price-prediction.git
```

Go inside the project:

```bash
cd house-price-prediction
```

### 2. Install backend dependencies

```bash
cd Server
pip install -r requirements.txt
```

### 3. Start Flask server

```bash
python server.py
```

The backend will run on:

```text
http://127.0.0.1:5000
```

### 4. Run the frontend

Open the `Client` folder and run `index.html` using a local server such as VS Code Live Server.

The frontend communicates with the Flask API to get locations and predictions.

---

## 🌐 Deployment

The project is deployed using **Render**.

### Backend

The Flask backend is deployed as a Render Web Service.

```text
https://house-price-prediction-api-pcvo.onrender.com
```

### Frontend

The HTML/CSS/JavaScript frontend is deployed as a Render Static Site.

```text
https://house-price-prediction-2lxr.onrender.com
```

---

## 🔍 Example

Suppose the user enters:

```text
Area       : 1000 sqft
BHK        : 3
Bathrooms  : 3
Location   : 1st Phase JP Nagar
```

The frontend sends the information to the Flask API.

The backend passes the processed input to the trained model and returns the estimated price.

Example:

```text
Estimated Price: 98.58 Lakh
```

---

## 🎯 Key Learning From This Project

This project helped me understand how to take a Machine Learning model beyond a Jupyter Notebook and turn it into a usable application.

The main concepts covered are:

* Data preprocessing
* Feature engineering
* One-hot encoding
* Linear Regression
* Model serialization using Pickle
* Flask REST APIs
* Frontend and backend communication
* API testing using Postman
* Git and GitHub
* Cloud deployment using Render
* Connecting a deployed frontend with a deployed ML backend

---

## 🔮 Future Improvements

Some possible improvements for the project are:

* Try other regression models and compare their performance.
* Improve data preprocessing and outlier handling.
* Add more property-related features.
* Improve the frontend design and user experience.
* Add proper model evaluation metrics to the application.
* Add a database for storing prediction history.
* Use a production WSGI server such as Gunicorn for the backend.

---

## 👨‍💻 Author

**Abdullah**

Machine Learning | Data Science

GitHub:
https://github.com/Abdullah-07-lko

---

## ⭐ Project

If you find this project useful, feel free to explore the repository and give it a ⭐.
