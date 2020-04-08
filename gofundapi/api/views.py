from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
import urllib
import json 

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def testInputView(request):
# this view will pull up the submit html template
        return render(request, "index.html", {})

class AzureCall(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        # body1 = json.loads(request.body)
        # print(body1)
        # body = json.loads(request)
        
    # this view receives parameters from the submit html template and calls the API in azure
    # this contains API code for Python and Python3 

        # If you are using Python 3+, import urllib instead of urllib2
        #import urllib2.request    
        
        # formatting the data into a data object for the API call
        data =  {
                    "Inputs": {
                        "input1":
                        {
                            # Test 4:
                            "ColumnNames": ["category_id", "currencycode", "current_amount", "goal", "days_active", "title", "description", "has_beneficiary", "visible_in_search", "is_charity"],
                            "Values": [[ request.POST['category_id'], request.POST['currencycode'], request.POST['current_amount'], request.POST['goal'], request.POST['days_active'], request.POST['title'], request.POST['description'], request.POST['has_beneficiary'], request.POST['visible_in_search'], request.POST['is_charity']]]
                        }, 
                    },
                    "GlobalParameters": {
                    }
                }

        # the API call
        body = str.encode(json.dumps(data))
        url = 'https://ussouthcentral.services.azureml.net/workspaces/d7228c50e6944ea1ae1a4cd5d0f15842/services/8ced6f993d1844969db2a8780205da0a/execute?api-version=2.0&details=true'
        api_key = 'htxCbkeJVyLGBy7LKOVzm+JQLZaY3RQHsAGkw/gNS+9/hJanTtBZqgZWe5xYpMgfDP4TD6ScZzrayUNeoppIjw=='
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        # If you are using Python 3+, replace urllib2 with urllib.request
        #req = urllib2.Request(url, body, headers)
        req = urllib.request.Request(url, body, headers) 

        # python3 uses urllib while python uses urllib2
        #response = urllib2.request.urlopen(req)
        response = urllib.request.urlopen(req)

        # this formats the results 
        result = response.read()
        result = json.loads(result) # turns bits into json object

        #******** Need this line********
        # result = result["Results"]["output1"]["value"]["Values"][0][13]
        #********************************
        result = result["Results"]["output1"]["value"]["Values"]

        return Response({"result": result}) # this path assumes that this file is in the root directory in a folder named templates
        # return render(request, "results.html", {"result": result}) # this path assumes that this file is in the root directory in a folder named templates
        # the third parameter sends the result (the response variable value) to the template to be rendered


        # class CreateSale(APIView):
        # '''Creates a sale, including getting a payment intent from Stripe'''
        # @csrf_exempt
        # def post(self, request, format=None):
        #     body = json.loads(request.body)

        #     print(body)

        #     sale = Sale()
        #     sale.name = body['name']
        #     sale.address1 = body['address1']
        #     sale.address2 = body['address2']
        #     sale.city = body['city']
        #     sale.state = body['state']
        #     sale.zipcode = body['zipcode']
        #     sale.total = body['total']
        #     sale.items = body['items']
        #     sale.payment_intent = stripe.PaymentIntent.create(
        #         amount=int(sale.total * 100),
        #         currency = 'usd',
        #     )

        #     sale.save()

        #     return Response({
        #         'sale_id': sale.id, # Make sure you have called sale.save() or it'll be empty
        #         'client_secret': sale.payment_intent['client_secret'],
        #         'name': sale.name,
        #     })