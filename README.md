# Airline Customer Travel Prediction using Logistic Regression

***Introduction***:
  
  This repository contains a predictive model built using logistic regression to identify customers who are likely to travel with our airline in the upcoming festive season Along with Sentiment Analysis. The model is trained on a dataset comprising 130,000 records and 21 parameters, obtained through web scraping techniques using Python and the Pandas libraries.

  - Current Status 75% Accuracy **(*)** (Improving)

***Skills and Tools***
- Python
- BeautifulSoup
- Requests
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- Scikit-learn

## Usage
- Clone the repository to your local machine.
- Install the required dependencies listed in requirements.txt.
- Run the provided Python scripts to scrape data, analyse, and generate the dashboard.

# Process:

### Data Collection/Extraction
  - Scraped data from Skytrax, an open-source platform, for airline reviews worldwide.
  - The data was obtained from Skytrax Airline Reviews
  - Created custom functions to fetch records alphabetically without missing any parameters in between.
  - Utilized web scraping techniques with BeautifulSoup, Python, and Pandas to gather data on customer behaviour, capturing more than 130K records with 21 parameters using a single Python script.
    
### Data Cleaning and Preprocessing
  - Conducted thorough data cleaning to ensure data quality and consistency.
  - Removed null values, outliers, and inconsistencies in the dataset to prepare it for analysis and modelling.
  - Normalized the 'Route' column to extract the **Origin** and **Destination** for readability and ease of analysis.

### Sentiment Analysis using NLTK
  - Leveraged NLTK library for sentiment analysis to assign sentiment values to each full review and comment.
  - Analyzed the sentiment of customer reviews to gain insights into the overall sentiment of customer feedback.
  - Assigned 3 Sentiment Tones for Each Review, Comment as [Positive, Negative, Neutral]
### Exploratory Data Analysis (EDA)
  - Performed basic data inspection to understand the structure and characteristics of the dataset.
  - Conducted univariate analysis to explore the distribution of individual variables such as customer behaviour, aircraft, Origin, Destination, and ratings.
  - Conducted bivariate analysis to understand the relationships between variables, including how each rating impacts other features and customer behaviour.
### Feature Engineering
  - Converted the 'Flown Date' column to a month to identify festive season months such as Christmas and New Year, facilitating travel behaviour analysis during peak seasons.
  - Utilized NLTK for sentiment analysis to extract sentiments from comments and reviews, reducing memory usage compared to processing large string values
  - Normalising the 'Route' column to extract the **Origin** and **Destination** for readability and ease of analysis
### Model Evaluation
  - Encoding Techniques
    - Employed encoding techniques such as one-hot encoding and target encoding for each categorical column based on their unique values.
  - Data Splitting:
    - Split the dataset into training and testing sets using an 80-20 ratio.
  - Target Variable Design:
    - Designed the target variable based on festive season months identified through EDA (January, February, November, December).
  - Model Building:
    - Built a logistic regression model to predict customer travel for the upcoming festive season.
  - Model Evaluation:
    - Evaluated the model's performance using accuracy as the metric and achieved 75% accuracy.
  - Feature Importance:
    - Identified feature importance within the logistic regression model to understand the factors influencing customer travel predictions.
