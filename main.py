import re 
from collections import Counter 
from statistics import median, variance
import psycopg2
import random


def parse_colors(html):
    """Extract colors from the provided HTML."""
    color_pattern =  r">\s*(.*?)\s*</td>"
    matches = re.findall(color_pattern, html)
    colors = []
    for row in matches[1:]: # Skip the haeder row
        day_colors = row.split(", ")
        colors.extend(day_colors)
    return colors

def calculate_color_stats(colors):
    """Calculate mean, mode, median, and variance of colors."""
    frequencies = Counter(colors)
    color_counts = list(frequencies.values())
    # calculate mean color using frequency weights as proxy for numeric mean 
    mean_color = max(frequencies, key=lambda color: frequencies[color])

    # mode: most frequently worn color
    mode_color = frequencies.most_common(1)[0][0]

    # median requires sorting by frequency
    sorted_colors = sorted(frequencies.items(), key=lambda x: x[1])
    median_color = median([item[1] for item in sorted_colors])

    # variance using the frequency distribution 
    color_variance = variance(color_counts)

    return mean_color, mode_color, median_color, color_variance

def probability_of_color(colors, target_color):
    """calculate the probality of a color being chosen at random."""
    frequencies = Counter(colors)
    total_colors = len(colors)
    return frequencies[target_color] / total_colors

def create_database():
    """Create the database if it doesn't exist."""
    try:
        conn = psycopg2.connect(
            dbname="postgres",  # Connect to the default 'postgres' database
            user="postgres",
            password="pass123",
            host="localhost",
            port="5432"
        )
        conn.autocommit = True  # Allow CREATE DATABASE without transactions
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'color_analysis'")
        if not cursor.fetchone():  # Check if the database already exists
            cursor.execute("CREATE DATABASE color_analysis;")
            print("Database 'color_analysis' created successfully.")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to create database: {e}")

def save_to_postgresql(colors):
    """
    Save color frequencies to a PostgreSQL database.

    This function takes a list of colors, calculates the frequency of each color,
    and saves the frequencies to a PostgreSQL database. If the database or table
    does not exist, they will be created.

    Args:
        colors (list): A list of color names (strings).

    Raises:
        Exception: If there is an error connecting to the database or executing SQL commands.

    Example:
        colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
        save_to_postgresql(colors)
    """
    """save color frequencies to postgreSQL database."""
    # first, create the database if it doesn't exist
    create_database()
    try:
        conn = psycopg2.connect(
            database="color_analysis",
            user="postgres",
            password="pass123",
            host="localhost",
            port="5432"
        )
        print ("Opened database successfully")

        cursor = conn.cursor()

        # create a table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS color_frequencies (
            color VARCHAR(50),
            frequency INT)"""
        )

        # Insert data 
        frequencies = Counter(colors)
        for color, frequency in frequencies.items():
            cursor.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)", (color, frequency))
        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted to postgreSQL successfully.")
    except Exception as e:
        print(f"Failed to save the data to postgreSQL: {e}")

def recursive_search(lst, target, index=0):
    """Recursive search algorithm for finding a target in a list."""
    if index >= len(lst):
        return -1
    if lst[index] == target:
        return index
    return recursive_search(lst, target, index + 1)

def generate_random_binary():
    """generate a random 4-digit binary number and convert to base 10."""
    binary_number = ''.join(random.choice('01') for _ in range(4))
    return binary_number, int(binary_number, 2)

def sum_fibonacci(n):
    """calculate the sum of the first n Fibonacci numbers."""
    a, b = 0, 1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total
    
# HTMl string
html_content = """
<html>
<head>
<title>Our Python Class exam</title>
</head>
<body>
<h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
<table>
	
	<thead>
		<th>DAY</th><th>COLOURS</th>
	</thead>
	<tbody>
	<tr>
		<td>MONDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>TUESDAY</td>
		<td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
	</tr>
	<tr>
		<td>WEDNESDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
	</tr>
	<tr>
		<td>THURSDAY</td>
		<td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>FRIDAY</td>
		<td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
	</tr>

	</tbody>
</table>

<p>Examine the sequence below very well, you will discover that for every 1s that appear 3 times, the output will be one, otherwise the output will be 0.</p>
<p>0101101011101011011101101000111 <span style="color:orange;">Input</span></p>
<p>0000000000100000000100000000001 <span style="color:orange;">Output</span></p>
<p>
</body>
</html>
"""

# main execution 
colors = parse_colors(html_content)

# analyze color data
mean_color, mode_color, median_color, color_variance = calculate_color_stats(colors)

# probability of red
prob_red = probability_of_color(colors, "RED")

# save to postgreSQL
try:
    save_to_postgresql(colors)
    print("Colors saved to postgreSQL successfully.")
except Exception as e:
    print(f"Failed to save the data to postgreSQL: {e}")

# recursive search example
numbers = [1, 2, 3, 4, 5, 6, 7 ,8, 9]
search_target = 5
search_result = recursive_search(numbers, search_target)

# generate random binary number
binary, base10 = generate_random_binary()
# sum of first 50 Fibonacci numbers
fib_sum = sum_fibonacci(50)

# Output results
print(f"Mean color: {mean_color}")
print(f"Most worn color: {mode_color}")
print(f"Median color: {median_color}")
print(f"Variance of colors: {color_variance}")
print(f"Probability of red: {prob_red}")
print(f"Recursive search result for {search_target}: {search_result}")
print(f"Random binary: {binary}, Base 10: {base10}")
print(f"Sum of first 50 Fibonacci numbers: {fib_sum}")
