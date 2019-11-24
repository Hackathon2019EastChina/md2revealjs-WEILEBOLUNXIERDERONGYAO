import os
import random
import string
import zipfile
import shutil

from django.shortcuts import *

from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from myapp.models import Document
from myapp.forms import DocumentForm

from . import heading


def handle_md(path: str, unzip_path: str) -> bool:
    shutil.copy(path, unzip_path)
    return heading.get_html(
        os.path.join(unzip_path, os.path.split(path)[1])
    )


def handle_zip(path: str, unzip_path: str) -> bool:
    if zipfile.is_zipfile(path):
        fz = zipfile.ZipFile(path)
        fz.extractall(unzip_path)
        for f in os.listdir(unzip_path):
            if os.path.splitext(f)[1][1:] in ['md']:
                return heading.get_html(
                    os.path.join(unzip_path, f)
                )
    else:
        return False


def handle(path: str, unzip_path: str):
    print(path)
    ext = os.path.splitext(path)[1][1:]
    if ext in ['md']:
        return handle_md(path, unzip_path)
    elif ext in ['zip']:
        return handle_zip(path, unzip_path)
    else:
        return False


def get_random_str() -> str:
    n = 32
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))


def show(request):
    print(request.path)
    path = os.path.join('myapp', 'templates', request.path[1:])
    # response = HttpResponse(open(path), 'r')
    # return response
    # return render(request, 'list.html')
    return render(request, request.path[1:])


def list(request):
    # Handle file upload
    if request.method == 'POST':
        myFile = request.FILES.get("docfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")

        sub_path = get_random_str()
        root = os.path.join('upload', sub_path)
        unzip_path = os.path.join('myapp/templates', sub_path)
        os.mkdir(root)
        os.mkdir(unzip_path)
        # shutil.copytree('revealjs', unzip_path)
        destination = open(os.path.join(root, myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        result = handle(os.path.join(root, myFile.name), unzip_path)
        if result:
            print('===============', sub_path)
            return HttpResponseRedirect('/' + sub_path + '/index.html')
        # return HttpResponse("upload over!")
        # form = DocumentForm(request.POST, request.FILES)
        # if form.is_valid():
        #     newdoc = Document(docfile=request.FILES['docfile'])
        #     newdoc.save()
        #     print(request.FILES['docfile'])
        #
        #     # Redirect to the document list after POST
        #     return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request, 'list.html', {'documents': '', 'form': form})
