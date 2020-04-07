from tla_ingest import populate_from_dir

TYPE_MAPPINGS = {
    'lemma': 'lemma',
    'occurrence': 'occ',
    'text': 'text',
    'ths': 'ths',
}


def main():
    for src_dir, url_path in TYPE_MAPPINGS.items():
        populate_from_dir(
            f'corpus/sample/{src_dir}',
            url_path,
            'http://localhost:8090'
        )

