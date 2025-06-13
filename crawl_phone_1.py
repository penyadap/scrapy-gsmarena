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
