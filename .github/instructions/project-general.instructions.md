---
description: These are general instructions for this project. Always load these instructions when working on ml-course
# applyTo: 'Describe when these instructions should be loaded by the agent based on task context' # when provided, instructions will automatically be added to the request context when the pattern matches an attached file
---

<!-- Tip: Use /create-instructions in chat to generate content with agent assistance -->

This project is a special project I created for ML course for engineers at FAB.
We have 3 meetings for the course, so the project will have 3 packages - one package per meeting.
In each meetings ther will be many separate packages and / or scripts that will showcase different examples and exercises with solutions.
Here is the general description of the course topics per meeting:

## Meeting 1 - Core Python (Reading Code like a Reviewer):
* Variables, fundamental data types, and how Python stores data in memory.
* Collections (Lists, Dictionaries) and Loops: Validating AI-generated iteration and data-extraction logic.
* Functions: Guiding AI to write modular, reusable code instead of massive, unreadable scripts.
* Modules and packages
* Object oriented programming and classes
* Error handling / exceptions

## Meeting 2 - Deep Data Analysis, Visualization & ML Fundamentals
* Data Wrangling with Pandas & NumPy
* Prompting LLMs to write complex Pandas chaining logic for data cleaning, filtering, and transformation.
* Handling missing sensor values, removing duplicates, and aggregating data by shifts or machines.
* Temporal Data Alignment: Using AI to merge asynchronous FAB sensors, resample time frequencies, and align timestamps.
* Using Matplotlib to build static, publication-ready engineering reports.
* Using Plotly for interactive, web-based, zoomable charts to visually audit dense time-series data and spot anomalies.
* Guiding AI to generate complex charting boilerplate and visual styling.
* Introduction to Machine Learning:
Moving from explicit programming (if/then rules) to pattern recognition from data.
Supervised vs. Unsupervised Learning: Understanding when you have a "ground truth" (e.g., historical failures) versus finding hidden structures.
Regression vs. Classification: Predicting continuous values (pressure) vs. discrete states (pass/fail).
* The Anatomy of Time Series:
Breaking down temporal signals: Trend, Seasonality, Cycles, and Residuals (Noise).
Stationarity and Autocorrelation: Understanding how past machine states influence future states.
AI-Assisted Feature Engineering: Creating lag features and rolling window averages to prepare raw data for ML.

## Meeting 3 - Applied Machine Learning Models for Temporal Data
Temporal Validation Strategies:
Why the standard random train_test_split fails for time series (Data Leakage).
Implementing Walk-Forward Validation and cutoff dates using AI to simulate real-world, future forecasting accurately.
Automated Forecasting with Prophet:
Formatting data and configuring the model to track hourly, daily, or shift-based seasonalities.
Handling FAB-specific events: Adding scheduled maintenance windows or factory shutdowns as custom "shocks."
Interpreting uncertainty intervals for safety margins and operational risk assessment.
Predictive Maintenance with Tree-Based Models:
Using models like XGBoost or LightGBM for robust regression and classification on temporal data.
Feeding engineered "rolling" and "lag" features into these models to predict imminent equipment thresholds.
Unsupervised Anomaly Detection:
Leveraging unsupervised machine learning models to identify hidden equipment faults and irregular sensor behavior without needing a dataset of pre-labeled failures.
Model Evaluation & Interpretation:
Understanding accuracy metrics specifically for time-based data (MAE, MAPE, RMSE).
Prompting AI to help explain model residuals and errors—determining if a model successfully captured the physical laws of the machine or just memorized the noise.



