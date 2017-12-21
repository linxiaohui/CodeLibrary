# -*- coding: UTF-8 -*-

# http://pythonhosted.org//PyPDF2/index.html

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from PyPDF2.pdf import PdfFileWriter, PdfFileReader, PageObject


def PdfPrettyPrint(inputname, outputname):
    inputfile = open(inputname,'rb')
    wrt = PdfFileWriter()
    ipt = PdfFileReader(inputfile)
    #print ipt.getDocumentInfo()
    pdfnums = ipt.getNumPages()
    #print pdfnums
    i = 0
    while i < pdfnums:
        page = ipt.getPage(i)
        wrt.addPage(page)
        if i+2 < pdfnums:
            page = ipt.getPage(i+2)
            wrt.addPage(page)
        else:
            wrt.addBlankPage()
        if i+1 < pdfnums:
            page = ipt.getPage(i+1)
            page.rotateClockwise(180)
            wrt.addPage(page)
        else:
            wrt.addBlankPage()
        if i+3 < pdfnums:
            page = ipt.getPage(i+3)
            page.rotateClockwise(180)
            wrt.addPage(page)
        else:
            wrt.addBlankPage()
        i = i+4
    fl = open(outputname,"wb")
    wrt.write(fl)
    inputfile.close()
    fl.close()
    return True

if __name__=="__main__":
    iput="D:\\A.pdf"
    output="D:\\B.pdf"
    PdfPrettyPrint(iput, output)