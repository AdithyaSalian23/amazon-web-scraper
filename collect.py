from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'title': [], 'price': [], 'link': []}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}", "r", encoding="utf-8") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, 'html.parser')

        t = soup.find("h2")
        title = t.get_text(strip=True) if t else "No title found"

        a_tag = soup.find("a", href=True)  
        if a_tag and a_tag["href"].startswith("/"):
            link = "https://www.amazon.in" + a_tag["href"] 
        else:
            link = "No link found"

        p = soup.find("span", attrs={"class": "a-price-whole"})
        price = p.get_text(strip=True) if p else "No price found"

        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)

        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Link: {link}")
        print("-" * 50)

    except Exception as e:
        print(f"Error processing {file}: {e}")

df = pd.DataFrame(data=d)
df.to_csv("data.csv", index=False)

print("Data successfully saved to data.csv ✅")
