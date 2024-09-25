import requests

dns_db_url = "https://raw.githubusercontent.com/DnsChanger/dnsChanger-desktop/store/servers_DB.json"


def get_dns_servers() -> list:
    r = requests.get(url=dns_db_url, timeout=30, stream=True)
    return r.json()