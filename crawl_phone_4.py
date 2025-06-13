import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Daftar URL target
target_urls = [
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=27",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=39",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=29",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=54",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=71",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=18",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=61",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=108",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=38",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=89",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=40",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=26",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=76",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=8",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=17",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=42",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=91",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=79",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=101",
    "https://www.gsmarena.com/results.php3?nYearMin=2025&sMakers=16",
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
with open("list_urls.txt", "a", encoding="utf-8") as f:
    for link in all_new_links:
        f.write(link + "\n")

print("\n=== Ringkasan Crawl ===")
print(f"✅ Total link baru disimpan : {total_found}")
print(f"🚫 Total link dilewati     : {total_skipped}")
print(f"📄 Disimpan ke              : list_urls.txt")