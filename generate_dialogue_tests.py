
import glob
import json
from os import path, listdir, scandir
from yattag import Doc
from random import randint
from transliterate import slugify
import os

OUTPUT_FILE = "dialogue_tests.html"


def main():
    doc, tag, text = Doc().tagtext()

    charts = listdir('graphs')

    with tag('html'):
        with tag('body'):
            for chart in charts:
                with tag('p'):
                    file_name = chart.split(".")[0]
                    new_file_name = slugify(file_name)
                    print(file_name)
                    os.rename(f"graphs/{chart}", f"graphs/{new_file_name}.png")
                    doc.stag('img', src=path.join('graphs', f"{new_file_name}.png?{randint(0, 10000)}"))


    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(doc.getvalue())

    print(f"{OUTPUT_FILE} собран.")
    
            
if __name__ == "__main__":    
    main()


