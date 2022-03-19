from django.shortcuts import render
from django.http import HttpResponseRedirect
from. import resume_scane
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from PyPDF2 import PdfFileReader
import os

 
 
def read_pdf(path):
    try:
        text=''
        path=os.path.join(settings.MEDIA_ROOT, path)
        pdf2=PdfFileReader(path)
        print(path)
        for page in range(pdf2.getNumPages()):
            pages = pdf2.getPage(page)
            #print(page) 
            text += pages.extractText()
        return(text)
    except: None


#module_dir = os.path.dirname(__file__)


def home(request):
	return render(request,'base.html')



# Create your views here.
def new_search(request):
    #Get Data
    new_search = request.POST.get('search')
    dis = request.POST.get('dis')
    output=resume_scane.scan(str(dis),str(new_search))

    

    allout={'out':output,}

    return render(request,'new_search.html',allout)
