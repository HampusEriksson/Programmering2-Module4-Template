# Ditt namn
# Din klass
# Datum
# Skapa ett program som använder ett API
# Programmet måste använda sig av input från användaren

# Massor av API finns på: https://github.com/public-apis/public-apis
# Du kan även googla på API

# Du kan behöva köra "pip install requests" i terminalen, precis som i modul 3 för ursina.
import requests


response = requests.get()

if response.status_code == 200:
    pass

else:
    print("Error")
