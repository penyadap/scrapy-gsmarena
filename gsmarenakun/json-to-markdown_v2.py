#!/usr/bin/env python3
"""
The csv file must contain a "title" column and any main content should be in a "body" column.
"""

import json
import yaml
import sys
import re
import unicodedata
import os
from pathlib import Path

# Set the path to the source CSV file.
# source = Path('_gsmarena.csv', encoding="utf8")

# daftar data boolean
#
# and key != 'tipe_series'
# and key != 'network_type'
# and key != 'body_dimensions'
# and key != 'body_other'
# and key != 'display_other'
# and key != 'memory_other'
# and key != 'camera_main'
# and key != 'platform_os'
# and key != 'battery_charging'
# and key != 'sound_other'
# and key != 'feature_other'
# and key != 'test_performance'
# and key != 'test_camera'

source = Path('alcatel.json')


class Literal(str):
    pass


def literal_presenter(dumper, content):
    return dumper.represent_scalar("tag:yaml.org,2002:str", content, style="|", default_style='\"')


yaml.add_representer(Literal, literal_presenter)


def slugify(value):
    value = str(value)
    value = unicodedata.normalize('NFKD', value).encode(
        'ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)


def write(path, row):
    file = open(path, 'w', encoding='utf-8')

    print('---', file=file)

    for key, value in row.items():
        if key != 'body' and key != 'brand' and key != 'tipe_series' and key != 'network_type' and key != 'body_dimensions' and key != 'body_other' and key != 'display_other' and key != 'memory_other' and key != 'camera_main' and key != 'platform_os' and key != 'battery_charging' and key != 'sound_other' and key != 'feature_other' and key != 'test_performance' and key != 'test_camera':
            print(f'{key}: "{value}"', file=file)

    # camera_selfie
    # if 'camera_selfie' in row:
    #     camselfie = yaml.dump(row['camera_selfie'])
    #     print(camselfie, file=file)

    # untuk kostum kategori
    if 'brand' in row:
        print('categories:', file=file)
        print("-", row['brand'], file=file)
        print("-", "Smartphone", file=file)

    # untuk kostum tags
    if 'brand' in row:
        print('tags:', file=file)
        print("-", "Ponsel", file=file)
        print("-", "Review", file=file)
        print("-", "Spesifikasi", file=file)

    # tipe_series
    if 'tipe_series' in row:
        print('tipe_series:', file=file)
        series = yaml.dump(row["tipe_series"])
        print(series, file=file)

    # network_type
    if 'network_type' in row:
        print('network_type:', file=file)
        series = yaml.dump(row["network_type"])
        print(series, file=file)

    # body_dimensions
    if 'body_dimensions' in row:
        print('body_dimensions:', file=file)
        series = yaml.dump(row["body_dimensions"])
        print(series, file=file)

    # body_other
    if 'body_other' in row:
        print('body_other:', file=file)
        series = yaml.dump(row["body_other"])
        print(series, file=file)

    # display_other
    if 'display_other' in row:
        print('display_other:', file=file)
        series = yaml.dump(row["display_other"])
        print(series, file=file)

    # memory_other
    if 'memory_other' in row:
        print('memory_other:', file=file)
        series = yaml.dump(row["memory_other"])
        print(series, file=file)

    # camera_main
    if 'camera_main' in row:
        print('camera_main:', file=file)
        series = yaml.dump(row["camera_main"])
        print(series, file=file)

    # platform_os
    if 'platform_os' in row:
        print('platform_os:', file=file)
        series = yaml.dump(row["platform_os"])
        print(series, file=file)

    # battery_charging
    if 'battery_charging' in row:
        print('battery_charging:', file=file)
        series = yaml.dump(row["battery_charging"])
        print(series, file=file)

    # sound_other
    if 'sound_other' in row:
        print('sound_other:', file=file)
        series = yaml.dump(row["sound_other"])
        print(series, file=file)

    # feature_other
    if 'feature_other' in row:
        print('feature_other:', file=file)
        series = yaml.dump(row["feature_other"])
        print(series, file=file)

    # test_performance
    if 'test_performance' in row:
        print('test_performance:', file=file)
        series = yaml.dump(row["test_performance"])
        print(series, file=file)

    # test_camera
    if 'test_camera' in row:
        print('test_camera:', file=file)
        series = yaml.dump(row["test_camera"])
        print(series, file=file)

    print('---', file=file)

    if 'title' in row:
        print(row['title'], file=file)


def main():
    json_file = open(source, newline='', encoding='utf-8')
    content = yaml.safe_load(json_file)

    for row in content["alcatel"]:
        filename = slugify(row['title'])
        path = Path(
            f'./out/{filename}.md')

        if not path.is_file():
            write(path, row)


if __name__ == '__main__':
    main()
