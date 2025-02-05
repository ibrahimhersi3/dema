# Data Pipeline

## Overview

This project is a data pipeline for an e-commerce system. It reads orders and inventory data from CSV files, checks that the orders are properly formatted, and then extracts key product details to combine the orders with the inventory information. The processed data is saved into files and a SQLite database, and the system produces simple reports using SQL queries. The solution is built in Python and can run locally or in a Docker container. 

## The pipeline:

- **Reads** raw orders and inventory CSV files.
- **Validates** the data using [Pydantic](https://pydantic-docs.helpmanual.io/).
- **Transforms** the data by extracting a basic product ID and merging orders with inventory.
- **Saves** intermediate and final outputs (as CSV files and in a SQLite database).
- **Generates** simple reports with SQL queries.

## Project Structure

```plaintext
dema/
├── data/
│   ├── raw/       # Raw CSV files (orders.csv, inventory.csv)
│   └── processed/ # Output CSVs and the SQLite database
├── src/           # Python modules:
│   ├── ingestion.py      # Reads CSV files
│   ├── transform.py      # Transforms and merges data
│   ├── persistence.py    # Saves data to SQLite and CSVs
│   ├── reporting.py      # Runs SQL reports
│   └── validations.py    # Validates data with Pydantic
├── pipeline.py    # Main script to run the whole pipeline
├── requirements.txt  # Python dependencies
├── Docker-compose.yml 
└── Dockerfile     # Containerizes the project
```
## Technologies Used
* **Python 3.9+**: Programming language with type hints.
* **Pandas**: For data ingestion and transformation.
* **SQLAlchemy**: To interact with a SQLite database.
* **Pydantic**: For data validation.
* **Docker**: For containerizing the application.
* **Git & GitHub**: For version control and repository hosting.



## Setup Instructions
### Local Setup

1. Clone the Repository:

```bash
git clone git@github.com:ibrahimhersi3/dema.git
cd dema
```
2. Create and Activate a Virtual Environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies:
```bash
pip install -r requirements.txt
```
4. Run the Pipeline:
```bash
python pipeline.py
```
### Docker Setup

1.Build the Docker Image:
```bash
docker build -t dema:latest .
```
2.Run the Docker Container:
```bash
docker run --rm -v "$(pwd)/data:/app/data" dema:latest
```

## Improvements

* I currently have minimal error handling, I would add more logging and error handling.
* I would write unit tests for core functions.
* I currently use a simple database schema (SQLite) I would * design a more scalable, normalized schema.
* I have no CI/CD integration, I would integrate a CI/CD pipeline for automated testing and deployment.
