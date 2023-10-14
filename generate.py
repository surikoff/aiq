
import glob
import json
from os import path
from yattag import Doc

OUTPUT_FILE = "visualizations.html"


def main():
    report_images = glob.glob(path.join("results", "*", "*", "*.png"), recursive=True)

    

    doc, tag, text = Doc().tagtext()

    with tag('html'):
        with tag('body'):
            for image in report_images:
                with tag('p'):
                    doc.stag('img', src=image)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(doc.getvalue())

    print(f"{OUTPUT_FILE} собран.")
    
            
if __name__ == "__main__":    
    main()


