import pdfkit
import os

def pdf_maker(title, html):
    temp_html_file = f"./output_folder/{title}.html"

    with open(temp_html_file, "w") as file:
        file.write(str(html))

    pdfkit.from_file(temp_html_file, f"./output_folder/{title}.pdf", options={"enable-local-file-access": ""})

    os.remove(temp_html_file)