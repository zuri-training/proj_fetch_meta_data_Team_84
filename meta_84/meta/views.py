from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from .forms import RegisterForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# the extract

from django.conf import settings
import PIL
from django.core.files.storage import FileSystemStorage
from PIL import Image
from PIL.ExifTags import TAGS
import filetype
from tinytag import TinyTag
from PyPDF2 import PdfFileReader
import docx


# Create your views here.
@login_required(login_url='meta:login')
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        filepath = fs.path(filename)
        filesize = fs.size(filename)
        filesize = str(round(filesize / (1024 * 1024), 2)) + ' ' + 'megabytes(s)'
        uploaded_file_url = fs.url(filename)

        kind = filetype.guess(filepath)
        if kind is None:
            try:
                info_dict = {
                    'File name': filename,
                    'Filesize': filesize,
                    'Creation Date': fs.get_created_time(filename),
                    'Modified Date': fs.get_modified_time(filename),
                    'Accessed Date': fs.get_accessed_time(filename),
                    'File type': filename.split('.')[1].upper(),
                    'File Extension': filename.split('.')[1],
                }
            except:
                info_dict = {
                    'Error': 'The application cannot process this file. Please try again with a different file',

                }
        if kind is not None:


            mimeType = kind.mime
            mimeType = mimeType.split('/')

            if mimeType[0] == 'image':
                try:
                    with Image.open(myfile) as img:
                        info_dict = {
                            'Filename:': filename,
                            'File MIME type:': mimeType,
                            'Image Size:': img.size,
                            'Image Height:': img.height,
                            'Image Width:': img.width,
                            "Image Mode:": img.mode,
                            "Image Palette:": img.palette,
                            'Image is animated:': getattr(img, 'is_animated', False),
                            'Frames in Image:': getattr(img, 'n_frames', 1),
                        }
                        info = {}
                        miro = {}
                        meta = img.getexif()
                        for tag, value in meta.items():
                            if tag in TAGS:
                                info[TAGS[tag]] = value
                        for tag_id in meta:
                            # get the tag name, instead of human unreadable tag id
                            miro[tag] = TAGS.get(tag_id, tag_id)
                            data = meta.get(tag_id)
                        info_dict.update(info)

                        info_dict.update(miro)
                        try:
                            del img.info['exif']
                            info_dict.update(img.info)
                        except:
                            info_dict.update(img.info)

                        # iterating over all EXIF data fields
                        for tag_id in meta:
                            # get the tag name, instead of human unreadable tag id
                            tag = TAGS.get(tag_id, tag_id)
                            data = meta.get(tag_id)
                except:
                    info_dict = {
                        'Error': 'Your' + ' ' + mimeType[
                            0] + ' ' + 'file couldn\'t be processed. Please try a different file'
                    }


            elif mimeType[0] == 'video' or mimeType[0] == 'audio':
                mediafile = TinyTag.get(filepath)
                try:
                    info_dict = {
                        'Title:': mediafile.title,
                        'File MIME type:': mimeType,
                        'Artist:': mediafile.artist,
                        'Filesize:': str((round(mediafile.filesize / (1024 * 1024), 2))) + ' ' + 'megabyte(s)',
                        'Genre:': mediafile.genre,
                        'Year Released:': mediafile.year,
                        'Bitrate:': str(mediafile.bitrate) + ' ' + 'kBits/s',
                        'Composer:': mediafile.composer,
                        'AlbumArtist:': mediafile.albumartist,
                        'Duration:': str((round(mediafile.duration / 60, 2))) + ' ' + 'minute(s)',
                        'Track Total:': str(mediafile.track_total)
                    }
                except:
                    info_dict = {
                        'Error': 'Your' + ' ' + mimeType[
                            0] + ' ' + 'file couldn\'t be processed. Please try a different file'
                    }


            elif mimeType[0] == 'application' and mimeType[1] == 'pdf':
                with open(filepath, 'rb') as f:
                    pdf = PdfFileReader(f)
                    info = pdf.getDocumentInfo()
                    pdfFileNoOfPages = pdf.getNumPages()
                    try:
                        info_dict = {
                            'Author': info.author,
                            'Title': info.title,
                            'File Name': filename,
                            'File Size': filesize,
                            'File MIME type:': mimeType,
                            'Creator': info.creator,
                            'CreationDate': info['/CreationDate'],
                            'Modification Date': info['/ModDate'],
                            'Number of Pages': pdfFileNoOfPages,
                            'Producer': info.producer,
                            'Subject': info.subject,
                            'Encrypted': pdf.isEncrypted,
                        }
                    except:
                        info_dict = {
                            'Error': 'Your' + ' ' + mimeType[
                                1] + ' ' + 'file couldn\'t be processed. Please try a different file'
                        }

            elif mimeType[1] == 'zip' or mimeType[1] == 'docx' or mimeType[1] == 'doc':
                doc = docx.Document(filepath)
                doc_info = doc.core_properties
                try:
                    info_dict = {
                        'Author': doc_info.author,
                        'File Name': filename,
                        'File size': filesize,
                        'Title': doc_info.title,
                        'Category': doc_info.category,
                        'Comments': doc_info.comments,
                        'Content status': doc_info.content_status,
                        'Created': doc_info.created,
                        'Identifier': doc_info.identifier,
                        'Keywords': doc_info.keywords,
                        'Last Modified By': doc_info.last_modified_by,
                        'Language': doc_info.language,
                        'Modified': doc_info.modified,
                        'Subject': doc_info.subject,
                        'Version': doc_info.version,
                    }
                    empty_keys = {k: v for k, v in info_dict.items() if not v}
                    for k in empty_keys:
                        info_dict[k] = 'None'
                except:
                    info_dict = {
                        'Error': 'Your' + ' ' + mimeType[
                            1] + ' ' + 'file couldn\'t be processed. Please try a different file'
                    }
            else:
                try:
                    info_dict = {
                        'File name': filename,
                        'Filesize': filesize,
                        'Creation Date': fs.get_created_time(filename),
                        'Modified Date': fs.get_modified_time(filename),
                        'Accessed Date': fs.get_accessed_time(filename),
                        'File type': filename.split('.')[1].upper(),
                        'File Extension': filename.split('.')[1],
                    }
                except:
                    info_dict = {
                        'Error': 'The application cannot process this file. Please try again with a different file',
                    }
        name_csv = filename.split('.')[0] + '.csv'
        with open('media/csv/' + name_csv, 'w') as f:
            for key in info_dict.keys():
                f.write("%s, %s\n" % (key, info_dict[key]))

        import csv
        print('..................................')
        with open('media/csv/' + name_csv) as csvfile:
            csvReader = csv.reader(csvfile, delimiter=',')
            for row in csvReader:
                print(row)
                fss = FileSystemStorage()
                file_name = fss.save(csvfile.name, csvfile)
                f_url = fss.url(file_name)

                # import pandas as pd
                # pip install panda

                # CSV = pd.read_csv('media/csv/'+ name_csv)

                # html_page = CSV.to_html('media/csv/'+name_csv)

        return render(request, 'meta/dashboard.html', {'uploaded_file_url': uploaded_file_url, 'image_data': info_dict,
                                                  'f_url': f_url, 'file_name': filename, 'file_size': filesize,
                                                  'date_created': fs.get_created_time(filename),
                                                  'file_type': filename.split('.')[1].upper(),
                                                  'file_folder': filename.split('.')[1]})

    return render(request, 'meta/dashboard.html')


class RegisterPage(FormView):
    template_name = 'signup.html'
    form_class = RegisterForm  # django form
    success_url = reverse_lazy('meta:dashboard')

    def form_valid(self, form):
        user = form.save()
        if user is not None:  # if user is authenticated log in the user!
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    # we need to prevent authenticated user from registering!

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('meta:index')  # this is the page it will return instead of signing up
        return super(RegisterPage, self).get(*args, **kwargs)


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    form_class = LoginForm
    redirect_authenticated_user = True  # if user is authenticated they should not be allowed to be in the login page

    def get_success_url(self):  # use this function whenever you need success url in login
        return reverse_lazy('meta:dashboard')
