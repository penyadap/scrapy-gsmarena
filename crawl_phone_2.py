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

# Load unlisted URLs
try:
    with open("unlist_urls.txt", "r", encoding="utf-8") as f:
        unlisted = set(line.strip() for line in f)
except FileNotFoundError:
    unlisted = set()

all_new_links = []
total_found = 0
total_skipped = 0

print("=== Memulai proses crawling... ===\n")

for idx, url in enumerate(target_urls, 1):
    print(f"[{idx}/{len(target_urls)}] Memproses: {url}")

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"  ⚠️ Gagal: Status code {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.select("div.makers a[href]")
        print(f"  ✅ Ditemukan {len(links)} link")

        for a in links:
            full_url = urljoin(base_url, a["href"])

            if full_url in unlisted:
                total_skipped += 1
                continue

            all_new_links.append(full_url)
            total_found += 1

    except Exception as e:
        print(f"  ❌ Error saat memproses: {e}")

# Simpan hasil
with open("list_urls.txt", "w", encoding="utf-8") as f:
    for link in all_new_links:
        f.write(link + "\n")

print("\n=== Ringkasan Crawl ===")
print(f"✅ Total link baru disimpan : {total_found}")
print(f"🚫 Total link dilewati     : {total_skipped}")
print(f"📄 Disimpan ke              : list_urls.txt")
