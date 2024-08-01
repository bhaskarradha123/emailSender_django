# from django.shortcuts import render ,HttpResponse
# from django.core.mail import send_mail


# # Create your views here.

# def query(request):
#     if request.method=='POST':
#         name=request.POST['name']
#         email=request.POST['email']
#         query=request.POST['query']
#     # Send confirmation email to user
#         send_mail(
#                 'you query is register',
                
#                 f'Hi  <h3>{name}</h3> \n\nThanks for your query \nMy team will contact you within 24 hrs.\n \nthanks & regards,\nHelp Team.',
             
#                 'dingirani13@gmail.com',
#                 [email],
#                 fail_silently=False,
#             )
#   # Send notification email to yourself
#         send_mail(
#                 'New User Registration',
#                 f'A new user has registered.\n\nUsername: {name}\n\nEmail: {email}\n\n\nMessage: {query}',
#                 'dingirani13@gmail.com',
#                 ['dingirani13@gmail.com'],  # Replace with your email address
#                 fail_silently=False,)



#     return render(request,'query.html')





from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def query(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('query')
        image_url = 'https://i.ytimg.com/vi/gqqi2cqlST8/maxresdefault.jpg'  # Replace with your actual image URL

        # Send confirmation email to user
        send_mail(
            'Your Query is Registered',
            '',  
            'dingirani13@gmail.com',  # This will appear as the "from" email
            [email],
            fail_silently=False,
            html_message=(
                f'<html>'
                f'<body>'
                f'<h3>Hi {name},</h3>'
                f'<p>Thank you for reaching out to us!</p>'
                f'<p>We have received your query and will get back to you within 24 hours.</p>'
                f'<p>In the meantime, feel free to browse our resources:</p>'
                f'<img src="{image_url}" alt="Helpful Resources" style="max-width:100%;height:auto;"/>'
                f'<p>Thank you for your patience and understanding.</p>'
                f'<p>Best regards,<br>Help Team</p>'
                f'</body>'
                f'</html>'
            ),
        )

        # Send notification email to yourself
        send_mail(
            'New User Registration',
            '',  
            'dingirani13@gmail.com',  # This will appear as the "from" email
            ['dingirani13@gmail.com'],  # Replace with your email address
            fail_silently=False,
            html_message=(
                f'<html>'
                f'<body>'
                f'<h3>New User Registration</h3>'
                f'<p> <strong> Username : </strong> <strong style="color: red;"> radha</strong> </p>'
                f'<p><strong>Email: {email}</strong> </p>'
                f'<p><strong>Message:</strong></p>'
                f'<div style="border: 1px solid #ccc; padding: 10px; background-color: #f9f9f9; border-radius: 5px;">'
                f'{query}'
                f'</div>'
                f'</body>'
                f'</html>'
            ),
        )
        return render(request,'thank.html')


    return render(request, 'query.html')

