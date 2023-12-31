
import glob
import json
from os import path, listdir, scandir
from yattag import Doc
from random import randint

OUTPUT_FILE = "character_tests.html"


def main():
    doc, tag, text = Doc().tagtext()

    tests = listdir('results')

    with tag('html'):
        with tag('body'):
            for test in tests:
                with tag('details'):
                    with tag('summary'):
                        text(test)
                    with tag('p'):
                        doc.stag('img', src=path.join('results', test, f"models_stat.png?{randint(0, 1000)}"))
                        models = [path.split(entry.path)[-1] for entry in scandir(path.join('results', test)) if entry.is_dir()]
                        for model in models:
                            with tag('details', style="margin-left: 40px"):
                                with tag('summary'):
                                    text(model)
                                with tag('p'):
                                    doc.stag('img', src=path.join('results', test, f"{model}_scores.png?{randint(0, 1000)}"))
                                    report_images = glob.glob(path.join("results", test, model, "*.png"), recursive=True)
                                    for image in report_images:
                                        doc.stag('img', src=f"{image}?{randint(0, 1000)}")


    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(doc.getvalue())

    print(f"{OUTPUT_FILE} собран.")
    
            
if __name__ == "__main__":    
    main()


