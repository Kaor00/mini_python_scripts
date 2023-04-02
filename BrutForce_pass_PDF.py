import pikepdf
from tqdm import tqdm


password = [line.strip() for line in open("password_list.txt")]

for password in tqdm(password, "Decrypting PDF"):
    try:
        with pikepdf.open("my_pdf_file.pdf", password=password) as pdf:
            print(f"\n[+] Password found: {password}")
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue
        continue
# НЕ проверено
