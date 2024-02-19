
import glob
import json
from os import path, listdir, scandir
from yattag import Doc
from random import randint

OUTPUT_FILE = "dialogue_tests_en.html"


def main():
    doc, tag, text = Doc().tagtext()

    charts = [entry.path for entry in scandir('graphs_en') if not entry.is_dir()]
    dirs = [entry.path for entry in scandir('graphs_en') if entry.is_dir()]

    with tag('html'):
        with tag('body'):
            for chart, dir in zip(sorted(charts), sorted(dirs)):
                with tag('details'):
                    with tag('summary'):
                        text(dir.split("/")[1])
                    with tag('p'):
                        doc.stag('img', src=f"{chart}?{randint(0, 10000)}")
                        for character in [entry.path for entry in scandir(dir) if not entry.is_dir()]:
                            with tag('details'):
                                with tag('summary'):
                                    text(character.split("/")[1] + ": " + character.split("/")[2].split(".")[0])
                                with tag('p'):
                                    doc.stag('img', src=f"{character}?{randint(0, 10000)}")


    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(doc.getvalue())

    print(f"{OUTPUT_FILE} собран.")
    
            
if __name__ == "__main__":    
    main()


