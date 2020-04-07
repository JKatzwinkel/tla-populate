import requests
import time

from tla_ingest import populate_from_dir

BACKEND_URL = 'http://localhost:8090'

TYPE_MAPPINGS = {
    'lemma': 'lemma',
    'occurrence': 'occ',
    'text': 'text',
    'ths': 'ths',
}

def wait_for_connection(url: str):
    connected = False
    while not(connected):
        try:
            res = requests.get(url)
            connected = True
        except:
            print(f'waiting for connection at {url}...')
            time.sleep(4)

def main():
    wait_for_connection(BACKEND_URL)
    for src_dir, url_path in TYPE_MAPPINGS.items():
        print(f'ingest {src_dir} documents')
        populate_from_dir(
            f'corpus/sample/{src_dir}',
            url_path,
            BACKEND_URL
        )

