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

## Link to Video Describing the Project

https://drive.google.com/file/d/1TT0ih-Rcx53pgkc8-sdfQAB8DYOBkj3n/view?usp=drive_link


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


## Index.html

### Overview

    Purpose:
        Serves as the home page where users can upload PDF files or enter URLs to fetch incident data.

    Structure:
        Header:
            Displays the title "Norman PD Incident Visualization."

    Form:
        Allows users to:
            Upload one or more PDF files via an input field (type="file", multiple).
            Enter one or more PDF URLs via a text input field.
            Uses POST method to send data to the / route.
            Includes an enctype="multipart/form-data" attribute to handle file uploads properly.


## Results.html

### Overview

    Purpose:
        Displays the visualizations created from the incident data and collects user feedback.

    Structure:
        Header:
            Displays the title "Incident Visualizations."
        Visualization Section:
            Renders Bokeh visualizations dynamically using Flask variables (script and div).
            If no visualizations are available, it shows an error message.
        Feedback Form:
            Allows users to submit feedback via a textarea.
            Includes a POST form targeting the /results route.
            If feedback is successfully submitted, it shows a success message.          


## Graphs in the Norman PD Incident Visualization Project

### Scatterplot

    Purpose:
        Groups similar incidents based on the "Nature" field to identify patterns or common types of incidents.

    Features:
        Each point represents an incident, and the color corresponds to its cluster.
        Hover over points to see details like the "Nature" and assigned cluster.
        A legend indicates the cluster numbers.

    Insights:
        Helps visualize patterns or trends in incident types (e.g., identifying recurring or related incidents).

### Bar Chart: Incident Count by Nature

    Purpose:
        Displays the top 10 most frequent types of incidents.

    Features:
        Hover over bars to view the exact count for each type.
        Incident names are displayed along the x-axis for clarity.

    Insights:
        Highlights the most common types of incidents, helping prioritize focus areas for public safety.

### Line Graph: Incidents Over Time

    Purpose:
        Shows how the number of incidents varies over time, helping to identify temporal patterns.

    Features:
        Each data point represents a day's total incidents, connected by a line for trends.
        Hover over points to see the exact date and number of incidents.

    Insights:
        Reveals trends like peaks on specific days or consistent patterns over time.


## Bugs and Assumptions

### Assumptions

-> The app only processes files with the .pdf extension. If a user uploads a non-PDF file or an incorrectly formatted PDF, the app may fail silently or crash.

-> If the uploaded files or fetched URLs do not contain valid incident data, the app redirects to the results page but shows a generic error message.

-> The extractIncidents function assumes a specific structure for the incident PDF files. If the format changes, the extraction logic may fail or produce incorrect results.

-> If clustering fails (e.g., due to insufficient data), the scatter plot generation will throw an exception.

-> The feedback form does not validate the input, allowing users to submit empty or nonsensical feedback.

-> The number of clusters for KMeans is fixed at 4 (n_clusters=4), assuming that this is an appropriate number for the dataset.


## Test Cases

### test_extract_data.py

This test case verifies the functionality of the extractIncidents function. 
It fetches a sample PDF file from a provided URL using urllib.request and extracts incident data using the extractIncidents function. 
The test asserts that the first incident's Date_Time field matches the expected value (10/31/2024 11:44), ensuring the parsing logic accurately processes the provided PDF data.

### test_fetch_data.py

This test case validates the fetchIncidents function by mocking urllib.request.urlopen to simulate an HTTP response without making a real network call. 
It ensures that the function correctly constructs a Request object with the given URL and headers, and properly reads and returns the response (b"Ishtmeet"). This confirms the function's ability to fetch data from a URL as expected.
