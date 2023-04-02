from PyPDF2 import PdfFileWriter, PdfFileReader


def secure_pdf(file, password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)
    with open(f"encrypted_{file}", "wb") as pdf_file:
        parser.write(pdf_file)
    print(f"Создан... encrypted_{file}")


if __name__ == '__main__':
    file = 'secret.pdf'
    password = '12345'
    secure_pdf(file, password)


# Скрипт ругается и не работает.