# -*- coding: utf-8 -*-
'''
    remove owner password of a pdf file (if possible)
    Require pyPdf(http://pybrary.net/pyPdf/)
'''

from pyPdf.pdf import PdfFileWriter, PdfFileReader

def RemovePdfOwnerPassword(inputname, outputname):
    '''
    '''
    inputfile = open(inputname,'rb')
    wrt = PdfFileWriter()
    ipt = PdfFileReader(inputfile)
    try:
        ipt.decrypt("")
    except KeyError, e:
        if e.message == '/Encrypt':
            print "%s is not an encrypted pdf" % inputname
            return -1
        else:
            raise e
    print ipt.getDocumentInfo()  
    size = ipt.getNumPages()
    i = 0
    while i < size:
        page = ipt.getPage(i)
        #print page.extractText()
        wrt.addPage(page)
        i = i+1
    fl = open(outputname,"wb")
    wrt.write(fl)
    
    inputfile.close()
    fl.close()
    return 0

def test():
    b = "E:\\test.pdf"
    a = "E:\\DB2_730.pdf"
    RemovePdfOwnerPassword(a,b)
    
if __name__ == "__main__":
    test()
