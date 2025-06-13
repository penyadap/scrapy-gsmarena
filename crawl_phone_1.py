import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Daftar URL target
target_urls = [
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=97",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=99",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=57",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=127",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=43",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=77",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=65",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=56",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=60",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=21",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=63",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=109",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=15",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=10",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=81",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=25",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=24",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=100",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=93",
    "https://www.gsmarena.com/results.php3?mode=tablet&nYearMin=2025&sMakers=102",
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
