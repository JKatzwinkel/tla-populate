import requests
import logging as log
import time

from tla_ingest import populate_from_dir

BACKEND_URL = 'http://localhost:8090'

TYPE_MAPPINGS = {
    'lemma': 'lemma',
    'occurrence': 'occ',
    'text': 'text',
    'ths': 'ths',
}

log.basicConfig(level=log.DEBUG)


def wait_for_connection(url: str):
    connected = False
    ttl = 60
    while not(connected) and ttl > 0:
        try:
            res = requests.get(url)
            connected = True
        except:
            log.info(f'waiting for connection at {url}...')
            time.sleep(4)
            ttl -= 1
    if ttl < 1:
        log.error(f'backend at {url} does not respond!')
    return connected


def main():
    if wait_for_connection(BACKEND_URL):
        for src_dir, url_path in TYPE_MAPPINGS.items():
            log.info(f'ingest {src_dir} documents')
            populate_from_dir(
                f'corpus/sample/{src_dir}',
                url_path,
                BACKEND_URL
            )

