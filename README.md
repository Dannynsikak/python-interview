# Color Analysis for T-Shirt Design

This Python project performs an analysis of the color data of dresses worn by Bincom staff throughout the week. The goal is to assist in making informed decisions about the color of T-shirts to produce for the staff based on the color frequencies from a given dataset.

## Features

1. **Mean Color**: Identifies the most frequent color worn throughout the week (treated as the mean color).
2. **Most Worn Color**: Finds the color that was worn the most during the week.
3. **Median Color**: Computes the median color based on the frequency distribution.
4. **Color Variance**: Calculates the variance of the color distribution (BONUS).
5. **Probability of Red**: Computes the probability of a red shirt being selected randomly based on frequency (BONUS).
6. **Save to PostgreSQL**: Stores color frequencies and their corresponding counts in a PostgreSQL database.
7. **Recursive Search**: Implements a recursive algorithm to search for a target number in a list (BONUS).
8. **Random Binary Generator**: Generates a random 4-digit binary number and converts it to base 10.
9. **Sum of Fibonacci Numbers**: Calculates the sum of the first 50 Fibonacci numbers.

## Requirements

- Python 3.x
- `psycopg2` for PostgreSQL database connection.
- A PostgreSQL instance running locally or remotely.

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/Dannynsikak/python-interview.git
cd python-interview

## 2. Install required dependencies i.e

It is recommended to create a virtual environment to manage dependencies.
python3 -m venv .venv
source .venv/bin/activate # On Windows use .venv\Scripts\activate
Then, install the required libraries:
pip install -r requirements.txt
Make sure you have PostgreSQL installed and running locally. You can also configure your database connection in the main.py file by modifying the host, user, password, and database parameters in the psycopg2.connect() method.

## 3. Run the script

To run the program, execute the following command:
python3 main.py
This will perform the analysis on the given HTML data, output the results, and store the color frequencies in a PostgreSQL database.

Project Structure
bash

color-analysis/
│
├── main.py # Main Python script to run the analysis
├── requirements.txt # List of required Python packages
└── README.md # Project documentation
Example Output
After running the script, the following output is generated:

Mean color: BLUE
Most worn color: BLUE
Median color: 3.5
Variance of colors: 60.1625
Probability of red: 0.09090909090909091
Recursive search result for 5: 4
Random binary: 0010, Base 10: 2
Sum of first 50 Fibonacci numbers: 20365011073
The script will also create a PostgreSQL database called color_analysis and save the color frequencies to the color_frequencies table.

Bonus Features
Variance: Calculates the statistical variance of the frequency distribution of the colors.
Probability: Calculates the likelihood of a color (like red) being randomly selected based on its frequency.
Recursive Search: A simple recursive function searches for a target number in a list of integers.
Binary Number Generation: Generates a random 4-digit binary number and converts it to decimal.
Fibonacci Sum: Calculates the sum of the first 50 Fibonacci numbers, as a basic computational task.
