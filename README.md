# 🛒 Amazon Web Scraper using Selenium & BeautifulSoup

This project is a Python-based web scraper that extracts product information (title, price, and link) from **Amazon.in** using **Selenium** and **BeautifulSoup**, and saves the data to a structured **CSV file**. It's ideal for practicing web scraping and data handling in Python.  

## 🚀 Features

- Extracts **product title**, **price**, and **link**
- Handles **missing data gracefully**
- Saves data to a CSV file for easy access
- Fully automated and easy to run

## 📂 Folder Structure

```bash
📁 Selenium Python Project/
├── 📁 data/ # Folder containing saved HTML files from Amazon
├── 📄 collect.py # Main script to parse HTML and save CSV
├── 📄 requirements.txt # List of dependencies
├── 📄 data.csv # Output file with extracted data
```


## ⚙️ How It Works

1. You save Amazon product page HTML files in the `data/` folder.
2. The script parses each file, extracts the product info, and stores it in a dictionary.
3. All extracted data is saved to `data.csv`.

---

## 🧪 Requirements

- Python 3.x
- Selenium
- BeautifulSoup (bs4)
- Pandas

Install dependencies using:

```bash
pip install -r requirements.txt
```
Or manually:

```bash
pip install selenium beautifulsoup4 pandas
```

---

## ▶️ How to Run
1. Clone this repo:
```bash
git clone https://github.com/AdithyaSalian23/amazon-web-scraper
cd amazon-web-scraper
```
2. Place your Amazon HTML files inside the data/ folder.
   
3. Run the scraper:
```bash
python collect.py
```
4. Check the generated data.csv file for the output. 🎉

---

## 🧠 Skills Used
🐍 Python

🌐 Selenium

🍜 BeautifulSoup

📊 Pandas

💾 Git & GitHub

---

## 📄 License
This project is open-source and free to use under the [MIT License](https://opensource.org/licenses/MIT).
