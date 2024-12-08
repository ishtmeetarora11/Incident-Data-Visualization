# cis6930fa24-project3

Name: Ishtmeet Singh Arora

## Project Description
The Norman PD Incident Visualization project is a web application designed to visualize police incident data extracted from PDF files or URLs. Users can upload PDF files or provide URLs to PDF documents containing incident reports. The application processes these inputs, extracting incident details such as date, location, and nature of the incidents using text extraction techniques. It then clusters similar incidents using machine learning (KMeans) and displays interactive visualizations built with Bokeh.

The app offers three key visualizations: a scatter plot to show incident clusters, a bar chart of top incident types, and a line graph illustrating the trend of incidents over time. Users can interact with the plots for more details and provide feedback about the visualizations. The app is built using Flask, with Pandas and Scikit-learn handling data manipulation and machine learning, and Bokeh for creating the plots. This project is a valuable tool for analyzing and gaining insights into police incident data in a user-friendly way.

## How to install

```
pipenv install -e .
```

## How to run
Run the following command on terminal

``` bash
pipenv run python app.py
```

The server will start at http://127.0.0.1:5000/

Open a web browser and navigate to http://127.0.0.1:5000/

On the home page, either upload one or more PDF files containing incident data or provide one or more URLs to the PDFs.
Click the Submit button to process the data.


## App.py overview

### Overview

This file is the main entry point for the Norman PD Incident Visualization project. It orchestrates the entire workflow, from data ingestion to visualization and feedback submission. Below is an overview of its key components:

-> Home Route (/): Type: GET and POST

-> Results Route (/results): Type: GET and POST

## Home Route (/):

### Method: GET and POST 

    Purpose: Displays the upload form (index.html) when accessed via GET.
    Handles PDF uploads and URL submissions when accessed via POST.

    Implementation: 

        Data Processing:
            Extracts PDFs from uploaded files or fetches them from URLs using fetchIncidents.
            Uses extractIncidents to parse data and extract structured information (e.g., Date, Nature, Location)
        
        Error Handling:
            Catches exceptions like invalid URLs, missing files, or extraction errors.
            Provides detailed feedback to users through error messages.
        
        Redirection:
            Redirects to /results if data is successfully processed.


## Results Route (/results):

### Method: GET and POST 

    Purpose: Generates visualizations of the processed data and displays them (results.html).
    Accepts and stores user feedback via the form.

    Implementation: 

        Data Retrieval and Validation:
            Retrieves incident data from the session.
            Validates the presence of Date_Time and drops invalid rows.
        
        Data Clustering:
            Converts the Nature field into numerical vectors using TfidfVectorizer.
            Groups similar incidents into clusters using KMeans.
            Reduces the data to two dimensions for plotting using PCA.
        
        Visualization Creation:
            Scatter Plot:
                Visualizes clusters of incidents, color-coded by cluster.
            Bar Chart:
                Shows the top 10 most frequent incident types.
            Time Series Line Graph:
                Displays the trend of incidents over time.
        
        Interactive Features:
            Uses HoverTool to provide details (e.g., Nature, Cluster) when hovering over points.
            Adds legends and dynamic resizing for better usability.
        
        Feedback Form:
            Processes user feedback and displays a success message upon submission.


## Custom Functions

### fetchIncidents

    Fetches data from a given URL using urllib.request.

    Simulates browser-like behavior by setting headers.

    Returns the raw data (PDF binary) fetched from the URL.

### extractIncidents

    Extracts structured data from PDF files using pypdf.

    Parses the extracted text to retrieve details like Date_Time, Incident Number, Nature, etc.

    Handles specific formats of police reports by skipping irrelevant rows (e.g., headers).

    Returns a list of dictionaries, each representing an incident.


## Data Flow

### Overview

    Input Handling:
        Users upload PDF files or provide URLs.
        Files/URLs are processed to extract incident details.

    Data Processing:
        Data is cleaned and transformed into a suitable format for clustering and visualization.

    Visualization:
        Incidents are grouped into clusters, trends are plotted over time, and top incident types are shown in a bar chart.

    Feedback:
        Users can submit feedback, which is logged in the console.


## Bugs and Assumptions

### Assumptions

-> Works on unseen test data by leveraging context and uses sparse matrices and efficient algorithms for large datasets.

-> Logistic Regression works efficiently with sparse data and large feature spaces. It uses linear functions that are computationally less expensive compared to tree-based methods like Random Forest.

-> Logistic Regression models linear decision boundaries, which are often sufficient for text classification tasks. It fits a weighted sum of features to predict class probabilities.

-> The L2 regularization used in Logistic Regression is sufficient to prevent overfitting.

-> TF-IDF provides sufficient feature representation for the classification task.


## Test Cases

### test_preprocess_context_basic.py

test_basic_redaction: Tests the function's ability to replace a single redacted block (█) 
with <redacted> in a typical sentence containing multiple redactions.

test_multiple_redactions: Validates the function's ability to handle sentences with multiple 
redacted blocks of varying lengths.

test_no_redactions: Ensures the function does not alter input text when no redacted blocks are present.

### test_read_and_preprocess_data_basic.py

test_read_and_preprocess_data: Verifies that the function Reads a properly formatted TSV file, Applies the preprocess_context function to the context column, Returns a DataFrame with all required columns and preprocessed content.

### test_split_data_only_validation.py

test_split_data_only_validation: Verifies that the function correctly handles a dataset containing only validation samples.
