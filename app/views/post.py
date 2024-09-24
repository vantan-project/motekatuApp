from django.shortcuts import render,redirect
from django.conf import settings
from ..models import Review
import boto3

def index(request):
    context = {
        'gender': request.user.gender
    }
    return render(request, 'app/post/index.html',context)
def save(request):
    image = request.FILES.get('image', '')
    image_url = None
    if image:
        image_name = f'motekatu-app/{image.name}'  
        s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        s3.upload_fileobj(image, settings.AWS_STORAGE_BUCKET_NAME, image_name)
        image_url = settings.S3_URL + image_name
    name = request.POST['name']
    star = request.POST['star']
    type = request.POST['type']
    comment = request.POST['comment']
    gender = request.user.gender
    review = Review(image=image_url, name=name, star=int(star), type=int(type), comment=comment, gender=gender)
    review.save()
    return redirect('app:review_list', type=type, gender=gender)