"""Uploads documents from Elasticsearch into TLA Spring Backend.


Usage:
    populate_spring -d DIR -p ENDPOINT [ -u URL ]

Options:
    -d DIR --dir=DIR                    Specify directory to read TLA documents from (e.g. 'corpus/sample/lemma')
    -p ENDPOINT --endpoint=ENDPOINT     Path segment for batch upload (e.g. lemma, ths...) [default: lemma]
    -u URL --url=URL                    URL of Spring backend [default: http://localhost:8090]

"""
import os
import requests
from docopt import docopt
from tqdm import tqdm
import json


class BatchUpload:
    def __init__(self, name: str, iterator, total: int, url: str):
        self.name = name
        self.iterator = iterator
        self.total = total
        self.url = url

    def run(self):
        self.batch = []
        self.progress_bar = tqdm(
            desc=f'{self.name} --> {self.url}',
            total=self.total,
            ncols=100,
        )
        with self.progress_bar as pb:
            for doc in self.iterator:
                self.batch.append(doc)
                pb.update(1)
                if len(self.batch) > 1000:
                    self.upload()
        if len(self.batch) > 0:
            self.upload()
        self.progress_bar.close()

    def upload(self):
        requests.post(
            self.url,
            json=self.batch
        )
        self.batch = []


def dir_doc_count(srcdir: str) -> int:
    """ counts number of json files in folder
    """
    return len(
        [
            fn
            for fn in os.listdir(srcdir)
            if fn.endswith('.json')
        ]
    )


def dir_iterator(srcdir: str):
    """ returns a generator producing the contents of every json document in a given folder
    """
    for fn in os.listdir(srcdir):
        if fn.endswith('.json'):
            with open(os.path.join(srcdir, fn), 'r') as f:
                yield json.load(f)


def populate_from_dir(srcdir: str, path: str, url: str):
    BatchUpload(
        srcdir,
        dir_iterator(srcdir),
        dir_doc_count(srcdir),
        f'{url}/{path}/batch',
    ).run()


def main(args):
    srcdir = args['--dir']
    if os.path.exists(srcdir) and os.path.isdir(srcdir):
        populate_from_dir(
            srcdir,
            args['--endpoint'],
            args['--url'],
        )

if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)

