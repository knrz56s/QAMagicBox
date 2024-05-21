from pypdf import PdfReader 
from keybert import KeyBERT

class PDF:

    def __init__(self, pdf):
        self.pdf = pdf
        self.content = ""

    def extract_keywords(self):
        self.extract()
        self.analysis()
        return

    def extract(self):

        print("\nSys >>> extracting words in PDF...\n")

        # importing required modules 
        #from pypdf import PdfReader 
        
        # creating a pdf reader object 
        reader = PdfReader(self.pdf) 
        
        # printing number of pages in pdf file 
        print(f"This pdf has {len(reader.pages)} pages.")
        
        # getting a specific page from the pdf file 
        page = reader.pages[0] 
        
        # extracting text from page 
        text = page.extract_text() 
        print(text)

        self.content = text

        return
    
    def analysis(self):

        print("\nSys >>> Keybert analyzing...\n")

        kw_model = KeyBERT()
        keywords = kw_model.extract_keywords(self.content)
        print(keywords)


        print("\nSys >>> Analysis end.\n")
        return keywords