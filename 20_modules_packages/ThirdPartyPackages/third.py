# Distributed via PyPI: Python Package Index
# Installed using pip install package_name

import requests

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())