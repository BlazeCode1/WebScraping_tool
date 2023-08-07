import requests as re
from bs4 import BeautifulSoup as BS
import pandas as pd
import openpyxl as op

url = "https://www.sportsadda.com/football/features/top-10-football-players-of-all-time"

response = re.get(url)

if response.status_code == 200:
    html_content = response.text
else: 
    print("Failed to fetch the website. Status code:",response.status_code)
    exit()
# connect to Document
soup = BS(html_content,"html.parser")
# Find table attribiute
table = soup.find("table")
#After table find tr(row)
table_row = table.find_all("tr")
#initialize lists to store table content
data = []
#loop through the table to collect info
for row in table_row:
    # find all the cells (td elements ) in the current row
    cells = row.find_all("td")
    # exctract the text from each cell and appendt to the data list
    row_data = [cell.text.strip() for cell in cells]
    data.append(row_data)

df = pd.DataFrame(data)
#Exporting the data to an excel file
output_file = "output.xlsx" # specify the output file name
df.to_excel(output_file, index=False, engine='openpyxl')

print("Data exported to Excel successfully.")
