# -*- coding: UTF-8 -*-

from win32com import client
word = client.Dispatch('Word.Application')

word.Visible = 1
doc = word.Documents.Open( r'G:\Devp\mynotes\tech-notes.docx')   
#print(doc.Content)

newdoc = word.Documents.Add()
#docC = word.Documents.Count
#print(docC)

#myRange = newdoc.Range(0,0)  
#myRange.InsertAfter(doc.Content) 

doc.Content.Copy()
newdoc.Content.Paste()

newdoc.SaveAs(r'g:\x.doc')
newdoc.Close()
doc.Close()

newdoc = word.Documents.Open(r'g:\x.doc')

#word.Selection.Find.ClearFormatting()  
#word.Selection.Find.Replacement.ClearFormatting()  

word.Selection.Find.Execute('systemctl', False, False, False, False, False, True, 1, True, 'XXXXXX', 2)

word.Quit()
