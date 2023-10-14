
import glob
import json
from os import path, listdir
from yattag import Doc

OUTPUT_FILE = "visualizations.html"


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
                        models = listdir(path.join('results', test))
                        for model in models:
                            with tag('details', style="margin-left: 40px"):
                                with tag('summary'):
                                    text(model)
                                with tag('p'):
                                    report_images = glob.glob(path.join("results", test, model, "*.png"), recursive=True)
                                    for image in report_images:
                                        doc.stag('img', src=image)
                                        with tag('a', href=image.replace(".png", ".txt"), target="_blank"):
                                            text('Open test log')

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(doc.getvalue())

    print(f"{OUTPUT_FILE} собран.")
    
            
if __name__ == "__main__":    
    main()


