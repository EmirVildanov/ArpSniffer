import re
import urllib.request

OUI_FILE_URL = "http://standards.ieee.org/develop/regauth/oui/oui.txt"
INITIAL_OUI_FILE_NAME = "oui.txt"
CLEAR_OUI_FILE_NAME = "clear_oui.txt"


def download_OUI_file():
    urllib.request.urlretrieve(OUI_FILE_URL, INITIAL_OUI_FILE_NAME)


def get_OUI_info():
    info_lines = []
    with open(INITIAL_OUI_FILE_NAME) as infile:
        for line in infile:
            if re.search("(hex)", line):
                try:
                    mac, vendor = line.strip().split("(hex)")
                except Exception:
                    mac = vendor = ''
                new_info_line = ""
                new_info_line += mac.strip().replace("-", ":").lower()
                new_info_line += " # "
                new_info_line += vendor.strip().replace("'", "`")
                new_info_line += "\n"
                info_lines.append(new_info_line)
    with open(CLEAR_OUI_FILE_NAME, "w") as outfile:
        outfile.writelines(info_lines)


def get_mac_vendor(searching_mac):
    vendor_symbols = searching_mac[0:8]
    with open(CLEAR_OUI_FILE_NAME) as infile:
        for line in infile:
            mac, vendor = line.split(" # ")
            if mac == vendor_symbols:
                return vendor
    return "UNKNOWN"