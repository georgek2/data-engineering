
import requests 
from bs4 import BeautifulSoup 
import pandas as pd

# Step 1: Send an HTTP GET request to the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find the table element containing the population data
table = soup.find('table', {'class': 'wikitable sortable'})

print(table)

# Step 4: Extract the table headers from the table
headers = []
header_row = table.find('tr')
header_cells = header_row.find_all('th')
for cell in header_cells:
    headers.append(cell.text.strip())

# Step 5: Extract the table data rows from the table
data_rows = []
rows = table.find_all('tr')[1:]
for row in rows:
    data_cells = row.find_all('td')
    data = []
    for cell in data_cells:
        data.append(cell.text.strip())
    data_rows.append(data)

# Step 6: Create a DataFrame using the headers and data rows
df = pd.DataFrame(data_rows, columns=headers)

# Step 7: Convert the DataFrame to a formatted array of strings using the to_json() method
formatted_array = df.to_json(orient='records', indent=4)

# Step 8: Return the formatted array of strings
print(formatted_array)





