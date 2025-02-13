from bs4 import BeautifulSoup
import json
import re
import pprint

def extract_starting_integers(s):
    match = re.match(r"(\d+(\.\d+)?)", s)
    if match:
        return float(match.group(1))
    return None

with open('dataTransfer.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

rows = soup.find_all('tr', class_='Ewb63')

data = {}

for row in rows:
    try:
        description = row.find('td', class_='RIwBbe bKnY0b').find('span', class_='z0U0R').text.strip()
        identifier = row.find('td', class_='RIwBbe bKnY0b').find('span', class_='PO2dsc').text.strip()
        cost = row.find('td', class_='RIwBbe wwRvw').find('span').text.strip()
        
# Extract all cost values
        cost_elements = row.find('td', class_='RIwBbe wwRvw').find_all('span')
        costs = [cost.text.strip() for cost in cost_elements]
        # print(costs)
        if len(costs) == 1:
            print(costs[0])
            result = extract_starting_integers(costs[0])
            print(result)
            costs.insert(0,result)
            print(costs)
            # break

        # Store the extracted data in the dictionary
        data[identifier] = {
            "description": str(description),
            "costs": costs
        }
    except:
        continue

json_data = json.dumps(data, indent=4)

with open('dataTransferSKU.json', 'w', encoding='utf-8') as py_file:
    py_file.write(json_data)
    # py_file.write("data = ")
    # pprint.pprint(data, stream=py_file)

print("The JSON data has been saved to output.json")
