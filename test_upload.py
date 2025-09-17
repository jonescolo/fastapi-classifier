import requests

url = "https://langgraph-api-olqa.onrender.com/upload-excel"
file_path = r"C:\Render_2\QIN-Render-Test.xlsx"

with open(file_path, "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())