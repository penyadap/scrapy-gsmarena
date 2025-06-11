import scrapy
from scrapy.loader import ItemLoader
from gsmarenakun.items import PhoneDataItemLoaderItem
import os


class PhoneDataItemLoaderSpider(scrapy.Spider):
    # Nama spider yang akan digunakan saat menjalankan Scrapy
    name = 'gsmarena_single_phone_spider'

    # Daftar domain yang diizinkan untuk diakses oleh spider
    allowed_domains = [
        'www.gsmarena.com'
    ]

    list_urls_file = 'list_urls.txt'
    unlist_urls_file = 'unlist_urls.txt'

    def start_requests(self):
        scraped_urls = set()
        if os.path.exists(self.unlist_urls_file):
            with open(self.unlist_urls_file, 'r') as f:
                scraped_urls = set(line.strip() for line in f if line.strip())

        if os.path.exists(self.list_urls_file):
            with open(self.list_urls_file, 'r') as f:
                urls = [line.strip() for line in f if line.strip()]
        else:
            urls = []

        self.logger.info(f"URL yang akan di-request: {urls}")
        for url in urls:
            if url not in scraped_urls:
                self.logger.info(f"Request: {url}")
                yield scrapy.Request(url=url, callback=self.parse)
            else:
                self.logger.info(f"SKIP: {url} sudah pernah di-scrape.")

    # Konfigurasi khusus untuk spider ini
    custom_settings = {
        'DOWNLOAD_DELAY': 2,  # Menunda permintaan berikutnya selama 2 detik
        'AUTOTHROTTLE_ENABLED': True,  # Mengaktifkan pengaturan throttle otomatis
    }

    # Variabel untuk menghitung jumlah item yang telah diproses
    count = 0

    # Fungsi utama untuk memproses respon dari URL
    def parse(self, response):
        self.logger.info(f"Masuk parse: {response.url}")
        # Cek ulang, skip jika sudah pernah di-scrape (antisipasi duplikasi)
        if os.path.exists(self.unlist_urls_file):
            with open(self.unlist_urls_file, 'r') as f:
                scraped_urls = set(line.strip() for line in f if line.strip())
            if response.url in scraped_urls:
                self.logger.info(f"SKIP (parse): {response.url} sudah pernah di-scrape.")
                return

        self.log(f"I just visited {response.url}")  # Logging URL yang dikunjungi

        # Membuat loader untuk memuat data item
        item_loader = ItemLoader(item=PhoneDataItemLoaderItem(), response=response)
        PhoneDataItemLoaderSpider.count += 1  # Menambah jumlah item yang diproses

        # Menambahkan data langsung dari halaman detail
        item_loader.add_value('item_number', PhoneDataItemLoaderSpider.count)
        item_loader.add_xpath('tipe_series', './/h1/text()')
        item_loader.add_xpath('thumbnail_path', './/a/img/@src')

        item_loader.add_xpath(
            'title', './/h1/text()')
        item_loader.add_xpath(
            'permalink', './/h1/text()')
        item_loader.add_xpath(
            'thumb_big', './/h1/text()')
        item_loader.add_xpath(
            'thumb_small', './/h1/text()')
        item_loader.add_xpath(
            'brand', './/h1/text()')
        item_loader.add_xpath(
            'date', './/span[@data-spec="released-hl"]/text()')
        item_loader.add_xpath(
            'released', './/span[@data-spec="released-hl"]/text()')
        item_loader.add_xpath(
            'announced', './/td[@data-spec="year"]/text()')
        item_loader.add_xpath(
            'status', './/td[@data-spec="status"]/text()')

        # head platfrom
        item_loader.add_xpath(
            'os', './/td[@data-spec="os"]/text()')
        item_loader.add_xpath(
            'chipset', './/td[@data-spec="chipset"]/text()')
        item_loader.add_xpath(
            'gpu', './/td[@data-spec="gpu"]/text()')

        # network
        item_loader.add_xpath(
            'network_technology', './/td/a[@data-spec="nettech"]/text()')
        item_loader.add_xpath(
            'network_2g', './/td[@data-spec="net2g"]/text()')
        item_loader.add_xpath(
            'network_3g', './/td[@data-spec="net3g"]/text()')
        item_loader.add_xpath(
            'network_4g', './/td[@data-spec="net4g"]/text()')
        item_loader.add_xpath(
            'network_5g', './/td[@data-spec="net5g"]/text()')
        item_loader.add_xpath(
            'network_speed', './/td[@data-spec="speed"]/text()')
        item_loader.add_xpath(
            'network_type', './/tr[@data-spec-optional]/td[2]/text()')
        item_loader.add_xpath(
            'network_gprs', './/td[@data-spec="gprstext"]/text()')
        item_loader.add_xpath(
            'network_edge', './/td[@data-spec="edge"]/text()')

        # body
        item_loader.add_xpath(
            'body_dimensions', './/td[@data-spec="dimensions"]/text()')
        item_loader.add_xpath(
            'body_weight', './/td[@data-spec="weight"]/text()')
        item_loader.add_xpath(
            'body_build', './/td[@data-spec="build"]/text()')
        item_loader.add_xpath(
            'body_sim', './/td[@data-spec="sim"]/text()')
        item_loader.add_xpath(
            'body_other', './/td[@data-spec="bodyother"]/text()')

        # display
        item_loader.add_xpath(
            'display_type', './/td[@data-spec="displaytype"]/text()')
        item_loader.add_xpath(
            'display_size', './/td[@data-spec="displaysize"]/text()')
        item_loader.add_xpath(
            'display_resolution', './/td[@data-spec="displayresolution"]/text()')
        item_loader.add_xpath(
            'display_protection', './/td[@data-spec="displayprotection"]/text()')
        item_loader.add_xpath(
            'display_other', './/td[@data-spec="displayother"]/text()')

        # memory
        item_loader.add_xpath(
            'memory_cardslot', './/td[@data-spec="memoryslot"]/text()')
        item_loader.add_xpath(
            'memory_internal', './/td[@data-spec="internalmemory"]/text()')
        item_loader.add_xpath(
            'memory_phonebook', './/th[contains(., "Phonebook")]/following-sibling::td/a/text()')
        item_loader.add_xpath(
            'memory_call_record', './/th[contains(., "Call records")]/following-sibling::td/a/text()')
        item_loader.add_xpath(
            'memory_other', './/td[@data-spec="memoryother"]/text()')

        # main camera
        item_loader.add_xpath(
            'camera_main', './/td[@data-spec="cam1modules"]/text()')
        item_loader.add_xpath(
            'camera_primary', './/td[@data-spec="cameraprimary"]/text()')
        item_loader.add_xpath(
            'camera_type', './/th[contains(., "Main Camera")]/following-sibling::td/a/text()')
        item_loader.add_xpath(
            'camera_main_features', './/td[@data-spec="cam1features"]/text()')
        item_loader.add_xpath(
            'camera_features', './/td[@data-spec="camerafeatures"]/text()')
        item_loader.add_xpath(
            'camera_main_video', './/td[@data-spec="cam1video"]/text()')
        item_loader.add_xpath(
            'camera_video', './/td[@data-spec="cameravideo"]/text()')

        # selfie camera
        item_loader.add_xpath(
            'camera_selfie', './/td[@data-spec="cam2modules"]/text()')
        item_loader.add_xpath(
            'camera_secondary', './/td[@data-spec="camerasecondary"]/text()')
        item_loader.add_xpath(
            'camera_selfie_features', './/td[@data-spec="cam2features"]/text()')
        item_loader.add_xpath(
            'camera_selfie_video', './/td[@data-spec="cam2video"]/text()')

        # platfrom
        item_loader.add_xpath(
            'platform_os', './/td[@data-spec="os"]/text()')
        item_loader.add_xpath(
            'platform_chipset', './/td[@data-spec="chipset"]/text()')
        item_loader.add_xpath(
            'platform_cpu', './/td[@data-spec="cpu"]/text()')
        item_loader.add_xpath(
            'platform_gpu', './/td[@data-spec="gpu"]/text()')

        # battery
        item_loader.add_xpath(
            'battery_capacity', './/td[@data-spec="batdescription1"]/text()')
        item_loader.add_xpath(
            'battery_standby', './/td[@data-spec="batstandby1"]/text()')
        item_loader.add_xpath(
            'battery_talktime', './/td[@data-spec="battalktime1"]/text()')
        item_loader.add_xpath(
            'battery_charging', './/td[contains(., "Charging")]/following-sibling::td/text()')

        # sound
        item_loader.add_xpath(
            'sound_alert_types', './/td[contains(., "Alert types")]/following-sibling::td[@class="nfo"]/text()')
        item_loader.add_xpath(
            'sound_loundspeaker', './/td[contains(., "Loudspeaker")]/following-sibling::td[@class="nfo"]/text()')
        item_loader.add_xpath(
            'sound_35mm_jack', './/td[contains(., "3.5mm jack")]/following-sibling::td/text()')
        item_loader.add_xpath(
            'sound_other', './/td[@data-spec="optionalother"]/text()')

        # comms
        item_loader.add_xpath(
            'comms_wlan', './/td[@data-spec="wlan"]/text()')
        item_loader.add_xpath(
            'comms_bluetooth', './/td[@data-spec="bluetooth"]/text()')
        item_loader.add_xpath(
            'comms_positioning', './/td[@data-spec="gps"]/text()')
        item_loader.add_xpath(
            'comms_nfc', './/td[@data-spec="nfc"]/text()')
        item_loader.add_xpath(
            'comms_radio', './/td[@data-spec="radio"]/text()')
        item_loader.add_xpath(
            'comms_usb', './/td[@data-spec="usb"]/text()')
        item_loader.add_xpath(
            'comms_infrared_port', './/td[contains(., "Infrared port")]/following-sibling::td[@class="nfo"]/text()')

        # features
        item_loader.add_xpath(
            'feature_sensors', './/td[@data-spec="sensors"]/text()')
        item_loader.add_xpath(
            'feature_messaging', './/td[contains(., "Messaging")]/following-sibling::td[@class="nfo"]/text()')
        item_loader.add_xpath(
            'feature_browser', './/td[contains(., "Browser")]/following-sibling::td[@class="nfo"]/text()')
        item_loader.add_xpath(
            'feature_java', './/td[contains(., "Java")]/following-sibling::td[@class="nfo"]/text()')
        item_loader.add_xpath(
            'feature_games', './/td[contains(., "Games")]/following-sibling::td[@class="nfo"]/text()')
        item_loader.add_xpath(
            'feature_languages', './/td[contains(., "Languages")]/following-sibling::td[@class="nfo"]/text()')
        item_loader.add_xpath(
            'feature_clock', './/td[contains(., "Clock")]/following-sibling::td[@class="nfo"]/text()')
        item_loader.add_xpath(
            'feature_alarm', './/td[contains(., "Alarm")]/following-sibling::td[@class="nfo"]/text()')
        item_loader.add_xpath(
            'feature_other', './/td[@data-spec="featuresother"]/text()')

        # misc
        item_loader.add_xpath(
            'misc_color', './/td[@data-spec="colors"]/text()')
        item_loader.add_xpath(
            'misc_model', './/td[@data-spec="models"]/text()')
        item_loader.add_xpath(
            'misc_sar_as', './/td[@data-spec="sar-us"]/text()')
        item_loader.add_xpath(
            'misc_sar_eu', './/td[@data-spec="sar-eu"]/text()')

        # tests
        item_loader.add_xpath(
            'test_performance', './/td[@data-spec="tbench"]/text()')
        item_loader.add_xpath(
            'test_display', './/td[contains(., "Display")]/following-sibling::td[@class="nfo"]/a/text()')
        item_loader.add_xpath(
            'test_camera', './/td[contains(., "Camera")]/following-sibling::td[@class="nfo"]/a/text()')
        item_loader.add_xpath(
            'test_loudspeaker', './/td[contains(., "Loudspeaker")]/following-sibling::td[@class="nfo"]/a/text()')
        item_loader.add_xpath(
            'test_batterylife', './/td[@data-spec="batlife"]/div/a/text()')

        item = item_loader.load_item()
        if item.get('tipe_series'):
            # Tambahkan ke unlist_urls.txt
            with open(self.unlist_urls_file, 'a') as f:
                f.write(response.url + '\n')
            # Hapus dari list_urls.txt
            if os.path.exists(self.list_urls_file):
                with open(self.list_urls_file, 'r') as f:
                    urls = [line.strip() for line in f if line.strip()]
                if response.url in urls:
                    urls.remove(response.url)
                    with open(self.list_urls_file, 'w') as f:
                        for url in urls:
                            f.write(url + '\n')
            yield item
        else:
            self.logger.warning(f"Data kosong untuk {response.url}, tidak disimpan.")

       
