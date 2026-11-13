import configparser

import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

def get_config() -> configparser.ConfigParser:

    config = configparser.ConfigParser()

    config_file = BASE_DIR.joinpath('environment.ini')

    if config_file.exists():

        config.read(config_file)

    if not config.has_section('secrets'):

        config.add_section('secrets')

    if not config.has_section('general'):

        config.add_section('general')

    config['secrets']['TELEGRAM_BOT_TOKEN'] = os.getenv(

        'TELEGRAM_BOT_TOKEN',

        config.get('secrets', 'TELEGRAM_BOT_TOKEN', fallback='')

    )

    config['secrets']['CHAT_ID'] = os.getenv(

        'CHAT_ID',

        config.get('secrets', 'CHAT_ID', fallback='')

    )

    config['general']['IP'] = os.getenv(

        'IP',

        config.get('general', 'IP', fallback='127.0.0.1')

    )

    return config
