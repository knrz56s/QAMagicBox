from keybert import KeyBERT

class Keyword:
    def __init__(self) -> None:
        self.keywords = []
    
    
    def analysis(self, doc):

        print(">>> Keybert analyzing...")

        kw_model = KeyBERT()

        for l in range(1, 6):
            keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, l), stop_words=None)

            print(f"{l}: {keywords}")

        self.keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 2), stop_words=None, use_mmr=True, diversity=0.7) # stop_words: filt word


        print(">>> Analysis end.")
        return self.keywords
    
    
def main():
    pass

if __name__ == '__main__':
    main()