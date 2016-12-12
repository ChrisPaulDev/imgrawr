from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db import models
from django.views.decorators.http import require_http_methods

from .forms import UploadFileForm
from .uploads import handle_uploaded_file
from . import models


def index(request):
    images = models.Image.objects.order_by('-pub_date')
    return render(request, 'home.html', {'images': images})
    
@require_http_methods(["GET"])
def search(request, tag=None):
    images = models.ImagesTags.objects.filter(tag=tag).order_by('-vote')
    queryset = models.Image.objects.filter(id__in=images.values('image')).order_by('-pub_date')
    return render(request, 'search_results.html', {'images': queryset})
    
@csrf_protect
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
        uuid = handle_uploaded_file(request.FILES['file'], str(request.POST['tags']))
        if uuid is not None:
            return HttpResponseRedirect('/view/' + uuid)
        else:
            form = UploadFileForm()
            return render(request, 'upload.html', {'form': form})
    else: #if GET request
        form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})
    
def view_file(request, uuid=None):
    tags = models.ImagesTags.objects.filter(image=uuid) #.replace(".jpg", "")
    return render(request, 'single.html', {'uuid': uuid, 'tags': tags})
    
@require_http_methods(["GET", "POST"])
def upvote(request, tag=None, uuid=None):
    #img_id = uuid.replace(".jpg", "")
    tag_count = models.Tag.objects.filter(tag_text=tag).count()
    vote_count = 0
    if tag_count == 0:
        new_tag = models.Tag.objects.create_tag(tag_text=tag)
        new_tag.save()
        imagetag = models.ImagesTags.objects.create_imagetag(img_id, tag, 1)
        imagetag.save()
        vote_count = 1
    else:
        imagetag = models.ImagesTags.objects.filter(tag=tag, image=uuid)[0]
        imagetag.vote = imagetag.vote + 1
        imagetag.save()
        vote_count = imagetag.vote
        
    from django.http import JsonResponse
    if request.is_ajax():
        response = JsonResponse({'vote_count': str(vote_count)})
        return response
    else:
        response = JsonResponse({'vote_count': str(vote_count)})
        return response
        
