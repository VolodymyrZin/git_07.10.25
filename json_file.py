import json
import logging
import time

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='json_zinych.log',
    filemode='a',
)

def is_valid_json_file(filepath):
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        logging.info(f'JSON is valid: {filepath}')
        return True

    except json.JSONDecodeError as e:
        logging.error(f'JSON error in the file {filepath}: {e}')
        return False

    except Exception as e:
        logging.warning(f'Other troubles during reading {filepath}: {e}')
        return False


is_valid_json_file('localizations_en.json')
is_valid_json_file('localizations_ru.json')
is_valid_json_file('login.json')
is_valid_json_file('swagger.json')


