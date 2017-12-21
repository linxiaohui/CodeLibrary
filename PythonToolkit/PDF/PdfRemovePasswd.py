# -*- coding: utf-8 -*-
'''
    remove owner password of a pdf file (if possible)

pip install pypdf2

'''

from PyPDF2.pdf import PdfFileWriter, PdfFileReader

def RemovePdfOwnerPassword(inputname, outputname):
    '''
    '''
    inputfile = open(inputname,'rb')
    wrt = PdfFileWriter()
    ipt = PdfFileReader(inputfile)
    try:
        ipt.decrypt("")
    except KeyError as e:
        if e.message == '/Encrypt':
            print("%s is not an encrypted pdf" % inputname)
            return -1
        else:
            raise e
    print(ipt.getDocumentInfo())
    size = ipt.getNumPages()
    i = 0
    while i < size:
        page = ipt.getPage(i)
        #print(page.extractText())
        wrt.addPage(page)
        i = i+1
    fl = open(outputname,"wb")
    wrt.write(fl)
    
    inputfile.close()
    fl.close()
    return 0

def test():
    b = "a.pdf"
    a = "10747756.pdf"
    RemovePdfOwnerPassword(a,b)
    
if __name__ == "__main__":
    test()
