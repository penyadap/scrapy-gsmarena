# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


# def conversion(element, response):
#     if element:
#         fo = response.meta['thumb_path'].replace(" ", "_")
#         bar = str(hash(fo))[1:13]
#         element = f"{fo}_min_{bar}.png"
#         #element = datetime.datetime.strptime(s, '%Y/%m/%d')
#     return element


import scrapy
from itemloaders.processors import TakeFirst, MapCompose
import re
import dateutil.parser as dparser
from datetime import datetime
import unicodedata


def os_trim(string):
    try:
        _brackets = re.compile('\(.*?\)|\[.*?\]')
        foo = ','
        data2 = string[0].split(foo, 1)[0]
        bar = '.'
        regex = _brackets.sub(" ", bar)
        complate = data2.split(regex, 1)[0]
        return complate
    except:
        pass


def chipset_trim(string):
    try:
        _brackets = re.compile('\(.*?\)|\[.*?\]')
        # _regex = re.compile(
        #     '(?<![\dA-Z-])(?=[\dA-Z-]{6,})(?:[\d-]+[A-Z]|[A-Z-]+\d)[A-Z\d-]*|[0-9]{6,}')
        foo = _brackets.sub(" ", string[0])
        # bar = _regex.sub("", foo)
        whitespace = (" ".join(foo.split()))
        complate = whitespace.strip()
        return complate

    except:
        pass


def thumb_big(string):
    value = string[0]
    value = re.sub(r'[+]', ' Plus', value)
    value = re.sub(r'AT&T', 'ATANDT', value)
    value = re.sub(r'Tel.Me.', 'TELME', value)
    value = re.sub(r'[&]', ' And', value)
    value = unicodedata.normalize('NFKD', value).encode(
        'ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    value = re.sub(r'[-\s]+', '_', value)
    complate = f"/phone/big/{value}_min.png"
    return complate


def thumb_small(string):
    value = string[0]
    value = re.sub(r'[+]', ' Plus', value)
    value = re.sub(r'AT&T', 'ATANDT', value)
    value = re.sub(r'Tel.Me.', 'TELME', value)
    value = re.sub(r'[&]', ' And', value)
    value = unicodedata.normalize('NFKD', value).encode(
        'ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    value = re.sub(r'[-\s]+', '_', value)
    complate = f"/phone/small/{value}_min.png"
    return complate


def permalink(string):
    value = string[0]
    value = re.sub(r'[+]', ' Plus', value)
    value = re.sub(r'AT&T', 'ATANDT', value)
    value = re.sub(r'Tel.Me.', 'TELME', value)
    value = re.sub(r'[&]', ' And', value)
    value = unicodedata.normalize('NFKD', value).encode(
        'ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    value = re.sub(r'[-\s]+', '-', value)
    complate = f"/{value}/"
    return complate


def brand(string):
    complate = string[0].split(' ', 1)
    return complate


def date(string):
    try:
        value = (format(dparser.parse(string[0], fuzzy=True).date()))
        return value
    except:
        value = "2006-01-01"
        return value


class PhoneDataItemLoaderItem(scrapy.Item):
    """
    When using ItemLoader we can define an output and input process per field.
    Since ItemLoader returns lists by default, we can take the first element
    of each list -- the data we want -- with the TakeFirst method.
    We also did some processing with the remove_star_text method. itemloaders.processors.TakeFirst
    """

    item_number = scrapy.Field(output_processor=TakeFirst())
    tipe_series = scrapy.Field(output_processor=MapCompose())
    thumbnail_path = scrapy.Field(output_processor=TakeFirst())

    # head essential
    permalink = scrapy.Field(
        input_processor=permalink, output_processor=TakeFirst())
    thumb_big = scrapy.Field(
        input_processor=thumb_big, output_processor=TakeFirst())
    thumb_small = scrapy.Field(
        input_processor=thumb_small, output_processor=TakeFirst())
    detailed_phone_url = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(output_processor=TakeFirst())
    brand = scrapy.Field(input_processor=brand, output_processor=TakeFirst())
    date = scrapy.Field(input_processor=date, output_processor=TakeFirst())
    released = scrapy.Field(output_processor=TakeFirst())
    announced = scrapy.Field(output_processor=TakeFirst())
    status = scrapy.Field(output_processor=TakeFirst())

    # head platfrom
    os = scrapy.Field(input_processor=os_trim, output_processor=TakeFirst())
    chipset = scrapy.Field(input_processor=chipset_trim,
                           output_processor=TakeFirst())
    gpu = scrapy.Field(output_processor=TakeFirst())

    # network
    network_technology = scrapy.Field(
        output_processor=TakeFirst())
    network_2g = scrapy.Field(
        output_processor=TakeFirst())
    network_3g = scrapy.Field(
        output_processor=TakeFirst())
    network_4g = scrapy.Field(
        output_processor=TakeFirst())
    network_5g = scrapy.Field(
        output_processor=TakeFirst())
    network_speed = scrapy.Field(
        output_processor=TakeFirst())
    network_type = scrapy.Field(
        output_processor=MapCompose())
    network_gprs = scrapy.Field(
        output_processor=TakeFirst())
    network_edge = scrapy.Field(
        output_processor=TakeFirst())

    # body
    body_dimensions = scrapy.Field(
        output_processor=MapCompose())
    body_weight = scrapy.Field(
        output_processor=TakeFirst())
    body_build = scrapy.Field(
        output_processor=TakeFirst())
    body_sim = scrapy.Field(
        output_processor=TakeFirst())
    body_other = scrapy.Field(
        output_processor=MapCompose())

    # display
    display_type = scrapy.Field(
        output_processor=TakeFirst())
    display_size = scrapy.Field(
        output_processor=TakeFirst())
    display_resolution = scrapy.Field(
        output_processor=TakeFirst())
    display_protection = scrapy.Field(
        output_processor=TakeFirst())
    display_other = scrapy.Field(
        output_processor=MapCompose())

    # memory
    memory_cardslot = scrapy.Field(
        output_processor=TakeFirst())
    memory_internal = scrapy.Field(
        output_processor=TakeFirst())
    memory_phonebook = scrapy.Field(
        output_processor=TakeFirst())
    memory_call_record = scrapy.Field(
        output_processor=TakeFirst())
    memory_other = scrapy.Field(
        output_processor=MapCompose())

    # main camera
    camera_main = scrapy.Field(
        output_processor=MapCompose())
    camera_primary = scrapy.Field(
        output_processor=TakeFirst())
    camera_type = scrapy.Field(
        output_processor=TakeFirst())
    camera_main_features = scrapy.Field(
        output_processor=TakeFirst())
    camera_features = scrapy.Field(
        output_processor=TakeFirst())
    camera_main_video = scrapy.Field(
        output_processor=TakeFirst())
    camera_video = scrapy.Field(
        output_processor=TakeFirst())

    # selfie camera
    camera_selfie = scrapy.Field(
        output_processor=TakeFirst())
    camera_secondary = scrapy.Field(
        output_processor=TakeFirst())
    camera_selfie_features = scrapy.Field(
        output_processor=TakeFirst())
    camera_selfie_video = scrapy.Field(
        output_processor=TakeFirst())

    # platfrom
    platform_os = scrapy.Field(
        output_processor=MapCompose())
    platform_chipset = scrapy.Field(
        output_processor=TakeFirst())
    platform_cpu = scrapy.Field(
        output_processor=TakeFirst())
    platform_gpu = scrapy.Field(
        output_processor=TakeFirst())

    # battery
    battery_capacity = scrapy.Field(
        output_processor=TakeFirst())
    battery_standby = scrapy.Field(
        output_processor=TakeFirst())
    battery_talktime = scrapy.Field(
        output_processor=TakeFirst())
    battery_charging = scrapy.Field(
        output_processor=MapCompose())

    # sound
    sound_alert_types = scrapy.Field(
        output_processor=TakeFirst())
    sound_loundspeaker = scrapy.Field(
        output_processor=TakeFirst())
    sound_35mm_jack = scrapy.Field(
        output_processor=TakeFirst())
    sound_other = scrapy.Field(
        output_processor=MapCompose())

    # comms
    comms_wlan = scrapy.Field(
        output_processor=TakeFirst())
    comms_bluetooth = scrapy.Field(
        output_processor=TakeFirst())
    comms_positioning = scrapy.Field(
        output_processor=TakeFirst())
    comms_nfc = scrapy.Field(
        output_processor=TakeFirst())
    comms_radio = scrapy.Field(
        output_processor=TakeFirst())
    comms_usb = scrapy.Field(
        output_processor=TakeFirst())
    comms_infrared_port = scrapy.Field(
        output_processor=TakeFirst())

    # features
    feature_sensors = scrapy.Field(
        output_processor=TakeFirst())
    feature_messaging = scrapy.Field(
        output_processor=TakeFirst())
    feature_browser = scrapy.Field(
        output_processor=TakeFirst())
    feature_java = scrapy.Field(
        output_processor=TakeFirst())
    feature_games = scrapy.Field(
        output_processor=TakeFirst())
    feature_languages = scrapy.Field(
        output_processor=TakeFirst())
    feature_clock = scrapy.Field(
        output_processor=TakeFirst())
    feature_alarm = scrapy.Field(
        output_processor=TakeFirst())
    feature_other = scrapy.Field(
        output_processor=MapCompose())

    # misc
    misc_color = scrapy.Field(
        output_processor=TakeFirst())
    misc_model = scrapy.Field(
        output_processor=TakeFirst())
    misc_sar_as = scrapy.Field(
        output_processor=TakeFirst())
    misc_sar_eu = scrapy.Field(
        output_processor=TakeFirst())

    # tests
    test_performance = scrapy.Field(
        output_processor=MapCompose())
    test_display = scrapy.Field(
        output_processor=TakeFirst())
    test_camera = scrapy.Field(
        output_processor=MapCompose())
    test_loudspeaker = scrapy.Field(
        output_processor=TakeFirst())
    test_batterylife = scrapy.Field(
        output_processor=TakeFirst())
