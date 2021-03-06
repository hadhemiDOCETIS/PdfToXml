from tabula import *
import pyPdf,os, time
import pandas as pd
import sys

import warnings 

warnings.filterwarnings("ignore", category=FutureWarning)

filename = sys.argv[1]
pdf = pyPdf.PdfFileReader(open(filename, "rb"))
pag_no = pdf.getNumPages()
name = filename.split('/')[2].split('.')[0]
print('1')


for i in range(0,pag_no):
    pg = pdf.getPage(i)
    
    writer = pyPdf.PdfFileWriter()

    writer.addPage(pg)
    NewPDFfilename ='./PDFModule/'+name+"_Page_"+str(i)+".pdf"
    with open(NewPDFfilename, "wb") as outputStream: 
        writer.write(outputStream)

print('2')

time.sleep(0.2)

for i in range(0,pag_no):
    convert_into('./PDFModule/'+name+'_Page_'+str(i)+'.pdf', './PDFModule/'+name+'_result_'+str(i)+'.csv', output_format = 'CSV')
    convert_into('./PDFModule/'+name+'_Page_'+str(i)+'.pdf', './PDFModule/'+name+'_result_'+str(i)+'.xml', output_format = 'xml')

print('3')

for i in range(0,pag_no):
    try:
        df = pd.read_csv('./PDFModule/'+name+"_result_"+str(i)+".csv")
        if(df.empty):
            print("yes")
        else:
            print("Table found in -----> PAGE"+str(i+1)+" and stored in -----> ./PDFModule/"+name+"_result_"+str(i)+".csv")
    except:
        os.remove('/home/home/Documents/axis/TableExtraction/PDFModule/'+name+'_Page_'+str(i)+'.pdf')
        os.remove('/home/home/Documents/axis/TableExtraction/PDFModule/'+name+'_result_'+str(i)+'.csv')
        os.remove('/home/home/Documents/axis/TableExtraction/PDFModule/'+name+'_result_'+str(i)+'.xml')

        pass

print('4')


