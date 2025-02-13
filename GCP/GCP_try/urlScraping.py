import requests
from bs4 import BeautifulSoup
import re
import json
import time


def extract_starting_integers(s):
    match = re.match(r"(\d+(\.\d+)?)", s)
    if match:
        return float(match.group(1))
    return None

data = {}



url = "https://cloud.google.com/skus/?hl=en&filter=6532-BA4E-165E&currency=USD"

response = requests.get(url)

with open("single.html", "w", encoding="utf-8") as file:
    file.write(response.text)

# print(response.content)

# soup = BeautifulSoup(response.content, 'html.parser')
# # print(soup)
# # row = soup.find('tr', class_='Ewb63', attrs={'ssk': True})
# rows = soup.find_all('tbody')
# print(rows)


# if row:
#     description = row.find('td', class_='RIwBbe bKnY0b')
#     identifier = row.find('td', class_='RIwBbe bKnY0b')
#     cost = row.find('td', class_='RIwBbe wwRvw')
    
#     # Extract the specific content from each block (ensure that the element exists before extracting)
#     if description:
#         description_text = description.find('span', class_='z0U0R').text.strip() if description.find('span', class_='z0U0R') else "Description not found"
#     else:
#         description_text = "Description not found"
        
#     if identifier:
#         identifier_text = identifier.find('span', class_='PO2dsc').text.strip() if identifier.find('span', class_='PO2dsc') else "Identifier not found"
#     else:
#         identifier_text = "Identifier not found"
        
#     if cost:
#         cost_text = cost.find('span').text.strip() if cost.find('span') else "Cost not found"
#     else:
#         cost_text = "Cost not found"

#     # Print the extracted data
#     print(f"Description: {description_text}")
#     print(f"Identifier: {identifier_text}")
#     print(f"Cost: {cost_text}")
# else:
#     print("The row with the ssk attribute was not found.")
    

# print(data)
    
# # cost_elements = row.find('td', class_='RIwBbe wwRvw').find_all('span')
# # costs = [cost.text.strip() for cost in cost_elements]
# # # print(costs)
# # if len(costs) == 1:
# #     print(costs[0])
# #     result = extract_starting_integers(costs[0])
# #     print(result)
# #     costs.insert(0,result)
# #     print(costs)

# #     data[identifier] = {
# #             "description": str(description),
# #             "costs": costs
# #         }
    
    
# # json_data = json.dumps(data, indent=4)
    
    
# # with open('dataTransferSKU.json', 'w', encoding='utf-8') as py_file:
# #     py_file.write(json_data)
    
    
    
    
    
    
    
    
    
    

