import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Daftar URL target
target_urls = [
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=62",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=46",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=94",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=120",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=130",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=116",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=123",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=51",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=128",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=129",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=5",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=85",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=23",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=74",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=135",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=49",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=50",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=117",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=84",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=22",
]

base_url = "https://www.gsmarena.com/"

# Baca daftar link yang harus di-skip
try:
    with open("unlist_urls.txt", "r", encoding="utf-8") as f:
        unlisted = set(line.strip() for line in f)
except FileNotFoundError:
    unlisted = set()

# Kumpulan link baru
all_new_links = []

# Loop semua halaman target
for url in target_urls:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for a in soup.select("div.makers a[href]"):
            href = a["href"]
            full_url = urljoin(base_url, href)

            if full_url not in unlisted:
                all_new_links.append(full_url)
    except Exception as e:
        print(f"Error saat memproses {url}: {e}")

# Simpan ke list_urls.txt
with open("list_urls.txt", "w", encoding="utf-8") as f:
    for link in all_new_links:
        f.write(link + "\n")

print(f"{len(all_new_links)} link baru disimpan ke list_urls.txt")
