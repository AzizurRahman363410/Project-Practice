from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf #created in step 4
import datetime
# Create your views here.
def home(request):
    return render(request, 'home.html')

class GeneratePDF(View):
    # def get(self, request, *args, **kwargs):
    #     data = {
    #          'today': datetime.date.today(), 
    #          'amount': 39.99,
    #         'customer_name': 'A R SHAKIL',
    #         'order_id': 1233434,
    #     }
    #     pdf = render_to_pdf('invoice.html', data)
    #     return HttpResponse(pdf, content_type='application/pdf')

# another solution directy download pdf

    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
        "invoice_id": 123,
        "customer_name": "A R SHAKIL",
        "amount": 1399.99,
        "today": "Today",}
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            print('File name is : ', filename)
            content = f"inline; filename={filename}"
            
            print('Content one is : ', content)
            download = request.GET.get("download")
            if download:
                content =f"attachment; filename={filename}"
                print('Content is : ', content)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")