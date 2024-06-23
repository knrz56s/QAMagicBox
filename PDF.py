from pypdf import PdfReader
from Keyword import Keyword

class PDF:

    def __init__(self, pdf, doc=""):
        self.pdf = pdf
        self.doc = doc
        self.content = None # pdf content

    def run(self):
        if self.pdf is None and self.doc is None: return

        if self.pdf:
            self.extract()
        KW = Keyword()
        keywords = KW.analysis(self.doc)
        print(keywords)
        self.writeTxt(keywords)
        return

    def extract(self):

        print(">>> extracting words in PDF...")

        # importing required modules 
        #from pypdf import PdfReader 
        
        # creating a pdf reader object 
        reader = PdfReader(self.pdf) 
        
        # printing number of pages in pdf file 
        print(f">>>This pdf has {len(reader.pages)} pages.")
        
        # getting a specific page from the pdf file 
        page = reader.pages[1] 
        
        # extracting text from page 
        text = page.extract_text() 
        print(text)

        self.content = text

        return
    
    def writeTxt(self, keywords):
        print(">>>Writing keywords into txt...")
        try:
            f = open("keywords.txt", 'a')

            for item in keywords:
                 f.write(f"({item[0]}, {item[1]})\n")
            
            import datetime
            # Get current date and time
            current_time = datetime.datetime.now()
            # Format the datetime object as a string
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(formatted_time + '\n')

            f.close()
            print(">>>Data written to keywords.txt successfully.")
        except IOError:
            # Handle IOError (file-related error)
            print("Error: Unable to write to the file.")
        except Exception as e:
            # Handle other exceptions
            print("An error occurred:", e)
    

def main():
    
    doc = '''Abstract—Security policies have different components; firewall, active directory, and IDS are some examples of these components. Enforcement of network security policies to low level security mechanisms faces some essential difficulties. Consistency, verification, and maintenance are the major ones of these difficulties. One approach to overcome these difficulties is to automate the process of translation of high level security policy into low level security mechanisms. This paper introduces a framework of an automation process that translates a high level security policy into low level security mechanisms. The framework is described in terms of three phases; in the first phase all network assets are categorized according to their roles in the network security and relations between them are identified to constitute the network security model. This proposed model extends the organization based access control (OrBAC) model to include not only access control policy but also some other administrative security policies like auditing policy. Besides, it enables matching of each rule of the high level security policy with the corresponding ones of the low level security policy. Through the second phase, the high level security policy is mapped into the network security model. The second phase could be considered as a translation of the high level security policy into an intermediate model level. Finally, the intermediate model level is translated automatically into low level security mechanism. The paper illustrates the applicability of proposed approach through an application example. Keywords: Network security; Security modeling; Security policy; Security management; OrBAC model.'''
    pdf = PDF(pdf=None, doc=doc)
    pdf.run()

if __name__ == '__main__':
    main()