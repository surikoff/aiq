
import glob
import json
from os import path, listdir, scandir
from yattag import Doc
from random import randint

OUTPUT_FILE = "dialogue_tests_en.html"


def main():
    doc, tag, text = Doc().tagtext()

    charts = listdir('graphs_en')

    with tag('html'):
        with tag('body'):
            for chart in charts:
                with tag('p'):
                    doc.stag('img', src=path.join('graphs_en', f"{chart}?{randint(0, 10000)}"))


    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(doc.getvalue())

    print(f"{OUTPUT_FILE} собран.")
    
            
if __name__ == "__main__":    
    main()


