# Employee Productivity Prediction using Machine Learning

A web application that leverages a machine learning model to predict the productivity of garment factory workers based on various operational factors.

![Home Page](https://github.com/cw-HX/Employee-Performance-Prediction/blob/main/Code%20Screenshots/Screenshot%202025-08-10%20170807.png?raw=true)

---

### ## Table of Contents
1.  [Abstract](#1-abstract)
2.  [Project Objective](#2-project-objective)
3.  [Technology Stack](#3-technology-stack)
4.  [Application Screenshots](#4-application-screenshots)
5.  [Machine Learning Workflow](#5-machine-learning-workflow)
6.  [Installation and Setup](#6-installation-and-setup)
7.  [Project Structure](#7-project-structure)
8.  [Conclusion](#8-conclusion)

---

### ## 1. Abstract
This project presents a comprehensive system designed to predict the productivity of garment workers using machine learning. By analyzing a range of factors—such as team performance, targeted goals, and financial incentives—we developed a predictive model to forecast worker output. This model is deployed as a user-friendly web application using the Flask framework, allowing managers to input worker-specific data and receive an instant productivity prediction. The primary goal is to provide a data-driven tool that can aid in talent management, resource allocation, and workforce optimization strategies, ultimately enhancing organizational efficiency.

---

### ## 2. Project Objective
The main objectives of this project are:
* To perform a thorough exploratory data analysis (EDA) on the garment worker productivity dataset to uncover key insights.
* To preprocess and clean the data to make it suitable for machine learning.
* To build, train, and evaluate several regression models to find the most accurate predictor of employee productivity.
* To save the best-performing model for future use.
* To develop a web application with a clean and intuitive user interface where users can input data and receive predictions from the trained model.

---

### ## 3. Technology Stack
* **Language:** Python 3.x
* **Libraries:**
    * **Web Framework:** Flask
    * **Machine Learning:** Scikit-learn, XGBoost
    * **Data Manipulation & Analysis:** Pandas, NumPy
    * **Data Visualization:** Matplotlib, Seaborn
* **Development Environment:** Jupyter Notebook, Visual Studio Code

---

### ## 4. Application Screenshots

#### About Page
![About Page](https://github.com/cw-HX/Employee-Performance-Prediction/blob/main/Code%20Screenshots/Screenshot%202025-08-10%20170822.png?raw=true)

#### Prediction Form
![Prediction Form](https://github.com/cw-HX/Employee-Performance-Prediction/blob/main/Code%20Screenshots/Screenshot%202025-08-10%20170836.png?raw=true)

#### Result
![Result](https://github.com/cw-HX/Employee-Performance-Prediction/blob/main/Code%20Screenshots/Screenshot%202025-08-10%20170932.png?raw=true)

---

### ## 5. Machine Learning Workflow
The entire machine learning process was conducted in the `Training files/Employee_Prediction.ipynb` notebook.
1.  **Data Preprocessing:** The dataset was cleaned by handling missing values, converting the `date` column into a `month` feature, and standardizing categorical values in the `department` column.
2.  **Feature Engineering:** Categorical features (`quarter`, `department`, `day`) were encoded into numerical values using a custom `MultiColumnLabelEncoder`.
3.  **Model Training:** The data was split into training (80%) and testing (20%) sets. Three models were trained: Linear Regression, Random Forest, and XGBoost.
4.  **Evaluation:** The **XGBoost Regressor** was selected as the final model due to its superior performance, achieving the highest R2 Score and lowest Mean Squared Error.
5.  **Model Saving:** The trained XGBoost model was serialized and saved to **`gwp.pkl`** using `pickle`.

---

### ## 6. Installation and Setup
To run this project on a local machine, follow these steps:

1.  **Prerequisites:** Ensure you have Python 3 and `pip` installed.

2.  **Clone the Project:** Download or clone the project folder to your local machine.
    ```bash
    git clone <your-repository-url>
    cd Employee_Performance_Project
    ```

3.  **Set up a Virtual Environment (Recommended):**
    ```bash
    # Create a virtual environment
    python -m venv venv

    # Activate it
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

4.  **Install Dependencies:** Install all the required Python libraries.
    ```bash
    pip install flask numpy pandas scikit-learn xgboost
    ```

5.  **Run the Flask Application:**
    ```bash
    # Navigate into the Flask directory
    cd Flask

    # Run the application script
    python app.py
    ```

6.  **Access the Application:** Open your web browser and go to the URL provided in the terminal, which is usually **`http://127.0.0.1:5000`**.

---

### ## 7. Project Structure
The application code is organized within the `Flask/` directory:
```
Flask/
│
├── app.py          # The main backend script
├── gwp.pkl         # The saved machine learning model
└── templates/
    ├── base.html       # The main layout template
    ├── home.html       # The landing page
    ├── about.html      # The project description page
    ├── predict.html    # The user input form
    └── result.html     # The page to display the prediction
```

---

### ## 8. Conclusion
This project successfully demonstrates a complete, end-to-end machine learning pipeline. We have taken a raw dataset, cleaned and processed it, trained and evaluated multiple models, and deployed the best one into a functional and user-friendly web application. The final tool provides a practical solution for predicting employee productivity, offering valuable insights that can help organizations make smarter, data-informed decisions.

---
**Author:** Anupriya Gupta

