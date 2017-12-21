#coding: UTF-8

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.psparser import PSLiteral
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdftypes import PDFObjRef
from pdfminer.layout import LAParams, LTTextBoxHorizontal,LTTextBox
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage

from collections import defaultdict, namedtuple

import os
import time

TextBlock= namedtuple("TextBlock", ["x", "y", "text"])

class Parser( object ):
    """Parse the PDF.

    1.  Get the annotations into the self.fields dictionary.

    2.  Get the text into a dictionary of text blocks.
        The key to the dictionary is page number (1-based).
        The value in the dictionary is a sequence of items in (-y, x) order.
        That is approximately top-to-bottom, left-to-right.
    """
    def __init__( self ):
        self.fields = {}
        self.text= {}

    def load( self, open_file ):
        self.fields = {}
        self.text= {}

        try:
            # Create a PDF parser object associated with the file object.
            parser = PDFParser(open_file)
            # Create a PDF document object that stores the document structure.
            doc = PDFDocument(parser)
            # Connect the parser and document objects.
            parser.set_document(doc)
        except Exception as e:
            print("Error parsing {}. {}".format(open_file.name, str(e)))
            return
        # Check if the document allows text extraction. If not, abort.
        #if not doc.is_extractable:
        #    raise PDFTextExtractionNotAllowed
        # Create a PDF resource manager object that stores shared resources.
        rsrcmgr = PDFResourceManager()
        # Set parameters for analysis.
        laparams = LAParams()
        # Create a PDF page aggregator object.
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # Create a PDF interpreter object.
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # Process each page contained in the document.
        for pgnum, page in enumerate(PDFPage.get_pages(open_file, set(), maxpages=0,
                                  password='',
                                  caching=True,
                                  check_extractable=False)):
            interpreter.process_page(page)
            if page.annots:
                self._build_annotations( page )
            txt= self._get_text( device )
            self.text[pgnum+1]= txt

    def _build_annotations( self, page ):
        for annot in page.annots:
            print(type(annot))
            if isinstance( annot, PDFObjRef ):
                annot= annot.resolve()
                #assert annot['Type'].name == "Annot", repr(annot)
                if annot['Subtype'].name == "Widget":
                    if annot['FT'].name == "Btn":
                        assert annot['T'] not in self.fields
                        self.fields[ annot['T'] ] = annot['V'].name
                    elif annot['FT'].name == "Tx":
                        assert annot['T'] not in self.fields
                        self.fields[ annot['T'] ] = annot['V']
                    elif annot['FT'].name == "Ch":
                        assert annot['T'] not in self.fields
                        self.fields[ annot['T'] ] = annot['V']
                        # Alternative choices in annot['Opt'] )
                    else:
                        raise Exception( "Unknown Widget" )
            else:
                raise Exception( "Unknown Annotation" )
    def _get_text( self, device ):
        text= []
        layout = device.get_result()
        for obj in layout:
            print(type(obj))
            if isinstance( obj, LTTextBox):
                if obj.get_text().strip():
                    text.append( TextBlock(obj.x0, obj.y1, obj.get_text().strip()) )
        text.sort( key=lambda row: (-row.y, row.x) )
        return text

if __name__ == "__main__":
    #PDFPATH = "Z:\\20171219"
    PDFPATH='.'
    num = 0
    begtime = time.time()
    pretime = time.time()
    for f in os.listdir(PDFPATH):
        if f.lower().endswith(".pdf"):
            num+=1
            pdf=os.path.join(PDFPATH,f)
            print("Parsing {}".format(pdf))
            parser = Parser()
            parser.load(open(pdf,"rb"))
            with open(f[:-4]+".txt", "w",encoding='UTF-8') as f:
                for k,v in parser.text.items():
                    for x in v:
                        f.write(x.text)
                        f.write("\n\n---\n\n")
            print("{} parsed. timeused {}s".format(pdf, time.time()-pretime))
            pretime=time.time()
    print("All {} Parsed. Used {}s".format(num, time.time()-begtime))
