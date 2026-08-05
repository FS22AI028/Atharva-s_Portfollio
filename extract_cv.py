import PyPDF2

def extract_text():
    try:
        with open('files/Atharva-Metkar-CV.pdf', 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            
            with open('cv_text.txt', 'w', encoding='utf-8') as out:
                out.write(text)
            print("Extracted text successfully.")
    except Exception as e:
        print(f"Error extracting with PyPDF2: {e}")
        try:
            import fitz
            doc = fitz.open('files/Atharva-Metkar-CV.pdf')
            text = ""
            for page in doc:
                text += page.get_text() + "\n"
            with open('cv_text.txt', 'w', encoding='utf-8') as out:
                out.write(text)
            print("Extracted text successfully with fitz.")
        except Exception as e2:
            print(f"Error extracting with fitz: {e2}")

if __name__ == '__main__':
    extract_text()
