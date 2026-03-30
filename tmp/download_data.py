import pandas as pd
import requests

urls = [
    "https://raw.githubusercontent.com/pavansubhasht/ibm-hr-analytics-attrition-dataset/master/WA_Fn-UseC_-HR-Employee-Attrition.csv",
    "https://raw.githubusercontent.com/sharmaroshan/IBM-Employee-Attrition-Analysis/master/WA_Fn-UseC_-HR-Employee-Attrition.csv",
    "https://raw.githubusercontent.com/vitthal-humbe/IBM-Employee-Attrition-Analysis/master/WA_Fn-UseC_-HR-Employee-Attrition.csv",
    "https://raw.githubusercontent.com/tristanga/IBM-HR-Analytics-Employee-Attrition-Performance/master/WA_Fn-UseC_-HR-Employee-Attrition.csv"
]

def download():
    for url in urls:
        print(f"Trying {url}...")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open("data/HR-Employee-Attrition.csv", "wb") as f:
                    f.write(response.content)
                print("Success!")
                return
            else:
                print(f"Failed with status {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    download()
