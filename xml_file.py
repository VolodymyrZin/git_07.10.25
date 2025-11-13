import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def find_incoming_by_number(xml_path, target_number):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for group in root.findall('group'):
        number = group.findtext('number')
        if number == str(target_number):
            incoming = group.findtext('timingExbytes/incoming')
            if incoming:
                logging.info(f"group {number} -→ incoming: {incoming}")
                return incoming
            else:
                logging.info(f"group {number} -→ no <incoming>")
                return None

    logging.info(f"group {target_number} not found")
    return None

find_incoming_by_number('groups.xml', 5)


