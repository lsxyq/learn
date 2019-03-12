#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
# python如何转换word格式、读取word内容、转成html？
import docx
from win32com import client as wc
word = wc.Dispatch('Word.Application')
doc = word.Documents.Open(r'C:\Users\teacher\Desktop\教案编写规范与示例.doc')
# #使用参数16表示将doc转换成docx
doc.SaveAs(r'C:\Users\teacher\Desktop\5.pdf', 17)
doc.Close()
word.Quit()
"""
wdFormatDocument = 0
wdFormatDocument97 = 0
wdFormatDocumentDefault = 16
wdFormatDOSText = 4
wdFormatDOSTextLineBreaks = 5
wdFormatEncodedText = 7
wdFormatFilteredHTML = 10
wdFormatFlatXML = 19
wdFormatFlatXMLMacroEnabled = 20
wdFormatFlatXMLTemplate = 21
wdFormatFlatXMLTemplateMacroEnabled = 22
wdFormatHTML = 8
wdFormatPDF = 17
wdFormatRTF = 6
wdFormatTemplate = 1
wdFormatTemplate97 = 1
wdFormatText = 2
wdFormatTextLineBreaks = 3
wdFormatUnicodeText = 7
wdFormatWebArchive = 9
wdFormatXML = 11
wdFormatXMLDocument = 12
wdFormatXMLDocumentMacroEnabled = 13
wdFormatXMLTemplate = 14
wdFormatXMLTemplateMacroEnabled = 15
wdFormatXPS = 18
"""