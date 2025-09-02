# all the paths and loading into memory
from pathlib import Path
from markdown import Markdown
from pymarkdown.api import PyMarkdownApi, PyMarkdownApiException

morphe_folder = Path()

phenomena_path = morphe_folder / 'Феномен'
db_path = morphe_folder / 'morphe.db'
anki_output_path = phenomena_path

def load_mds(mds_path):

    mds_path = {}
    mds_content = {}

    for file in phenomena_path.glob('*.md'):
        print(file.name)
        mds_path[file.stem] = file
        mds_content[file.stem] = 
        print(mds)

def check_mds_syntax(mds):
    pass
    
def rename_mds(mds):
    for key,value in mds:
        print(value)

def runtime(do_renaming):

    load_mds(phenomena_path)
    if do_renaming == 1:
        rename_mds(mds)

def deinit():
    pass