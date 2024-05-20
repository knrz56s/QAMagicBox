from pypdf import PdfReader 

def pdfExtract(pdf):

    # importing required modules 
    #from pypdf import PdfReader 
    
    # creating a pdf reader object 
    reader = PdfReader(pdf) 
    
    # printing number of pages in pdf file 
    print(len(reader.pages)) 
    
    # getting a specific page from the pdf file 
    page = reader.pages[0] 
    
    # extracting text from page 
    text = page.extract_text() 
    print(text) 

    print("Finish!")

    return