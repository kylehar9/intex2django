from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from api.models import Campaign
import urllib
import json 

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def testInputView(request):
# this view will pull up the submit html template
        return render(request, "index.html", {})

class OneCampaign(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        # campID = request.data['pid']
        campID = json.loads(request.body)
        theCampaign = Campaign.objects.get(campaign_id=campID)
        sent_campaign = {
            "campaign_id": theCampaign.campaign_id,
            "auto_fb_post_mode": theCampaign.auto_fb_post_mode,
            "category_id": theCampaign.category_id,
            "currencycode": theCampaign.currencycode,
            "current_amount": theCampaign.current_amount,
            "goal": theCampaign.goal,
            "donators": theCampaign.donators,
            "days_active": theCampaign.days_active,
            "days_created": theCampaign.days_created,
            "title": theCampaign.title,
            "description": theCampaign.description,
            "has_beneficiary": theCampaign.has_beneficiary,
            "visible_in_search": theCampaign.visible_in_search,
            "status": theCampaign.status,
            "deactivated": theCampaign.deactivated,
            "state": theCampaign.state,
            "is_launched": theCampaign.is_launched,
            "campaign_hearts": theCampaign.campaign_hearts,
            "social_share_total": theCampaign.social_share_total,
            "is_charity": theCampaign.is_charity,
            "campaign_image_url": theCampaign.campaign_image_url,
            "score": theCampaign.score
        }


        return Response({"result": sent_campaign})

class AzureCall(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        # body1 = json.loads(request.body)
        # print(body1)
        formObject = json.loads(request.body)
        
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
                            "Values": [[ formObject['category_id'], formObject['currencycode'], 0, formObject['goal'], formObject['days_active'], formObject['title'], formObject['description'], formObject['has_beneficiary'], formObject['visible_in_search'], formObject['is_charity']]]
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

class CampaignSearch(APIView):
    @csrf_exempt
    def post(self, request, format=None):

        # request = json.dumps(request.data) # Converts request.data from weirdness into a json string
        # searchParams = (json.loads(request)) # Converts json-like string to Python object
        searchParams = (json.loads(request.body)) # For Ty
        
        # We use one of these to load up the result variable to be sent in the Response
        mysearch = {}
        # mysearch = [] # As an array

        order_by = ''

        # order_value = '' # Use later for ORDER BY, if specified

        # if searchParams['order_by']:
        #     order_value = searchParams['order_by']
        

        #********************************************************
        #**************Search a specific goal amount*************
        #********************************************************
        if searchParams['goal']:

            # print("Here is request.smthg:")
            # print(request.data)
            # print("Here it is after json.dumps():")
            # print(request)
            print(searchParams['goal'])
            print(searchParams)



            # goal_amount = searchParams['goal']
            for c in Campaign.objects.raw('SELECT * FROM api_campaign WHERE goal = %s', [searchParams['goal']]):
                # mysearch.append(c.campaign_id) # For an array
                mysearch[c.campaign_id] = {"campaign_id": c.campaign_id, "title": c.title, "goal": c.goal, "donators": c.donators, "current_amount": c.current_amount, "currencycode": c.currencycode, "campaign_hearts": c.campaign_hearts, "days_active": c.days_active} # For an object

            # mysearch= str.encode(json.dumps(mysearch))
            # mysearch = response.read()
            # mysearch = json.loads(mysearch)

        #********************************************************
        #**************Search a goal range **********************
        #********************************************************
        elif searchParams['goal_max'] and searchParams['goal_min']:
            # print(searchParams['goal_max'], searchParams['goal_min'])
            for c in Campaign.objects.raw('SELECT * FROM api_campaign WHERE goal < %s AND goal > %s', [searchParams['goal_max'], searchParams['goal_min']]):
                # Load each Campaign into the Response that lies in this goal range
                mysearch[c.campaign_id] = {"campaign_id": c.campaign_id, "title": c.title, "goal": c.goal, "donators": c.donators, "current_amount": c.current_amount, "currencycode": c.currencycode, "campaign_hearts": c.campaign_hearts, "days_active": c.days_active} # For an object
                # mysearch[c.campaign_id] = [c.campaign_id, c.title, c.goal, c.donators, c.current_amount, c.currencycode, c.campaign_hearts, c.days_active] # For an array
                # mysearch[c.campaign_id] = {"campaign_id": c.campaign_id, "title": c.title, "goal": c.goal}
                # mysearch.append(c.campaign_id)

        #********************************************************
        #**************Search a title ***************************
        #********************************************************
        elif searchParams['title']:

            like_value = '%' + searchParams['title'] + '%' # This will query the DB if a title contains this text, so it becomes %text% 

            for c in Campaign.objects.raw('SELECT * FROM api_campaign WHERE title LIKE %s', [like_value]):
                # mysearch.append(c.campaign_id) # For an array
                mysearch[c.campaign_id] = {"campaign_id": c.campaign_id, "title": c.title, "goal": c.goal, "donators": c.donators, "current_amount": c.current_amount, "currencycode": c.currencycode, "campaign_hearts": c.campaign_hearts, "days_active": c.days_active} # For an object



        #********************************************************
        #**************Search a specific donators count**********
        #********************************************************
        elif searchParams['donators']:

            for c in Campaign.objects.raw('SELECT * FROM api_campaign WHERE donators = %s', [searchParams['donators']]):
                # mysearch.append(c.campaign_id) # For an array
                mysearch[c.campaign_id] = {"campaign_id": c.campaign_id, "title": c.title, "goal": c.goal, "donators": c.donators, "current_amount": c.current_amount, "currencycode": c.currencycode, "campaign_hearts": c.campaign_hearts, "days_active": c.days_active} # For an object

        #********************************************************
        #**************Search donators range **********************
        #********************************************************
        elif searchParams['donators_max'] and searchParams['donators_min']:
            # print(searchParams['goal_max'], searchParams['goal_min'])
            for c in Campaign.objects.raw('SELECT * FROM api_campaign WHERE donators < %s AND donators > %s', [searchParams['donators_max'], searchParams['donators_min']]):
                # Load each Campaign into the Response that lies in this goal range
                mysearch[c.campaign_id] = {"campaign_id": c.campaign_id, "title": c.title, "goal": c.goal, "donators": c.donators, "current_amount": c.current_amount, "currencycode": c.currencycode, "campaign_hearts": c.campaign_hearts, "days_active": c.days_active} # For an object

        #********************************************************
        #**************Search a specific current_amount**********
        #********************************************************
        elif searchParams['current_amount']:

            for c in Campaign.objects.raw('SELECT * FROM api_campaign WHERE current_amount = %s', [searchParams['current_amount']]):
                # mysearch.append(c.campaign_id) # For an array
                mysearch[c.campaign_id] = {"campaign_id": c.campaign_id, "title": c.title, "goal": c.goal, "donators": c.donators, "current_amount": c.current_amount, "currencycode": c.currencycode, "campaign_hearts": c.campaign_hearts, "days_active": c.days_active} # For an object

        #********************************************************
        #**************Search current_amount range **************
        #********************************************************
        elif searchParams['current_amount_max'] and searchParams['current_amount_min']:
            # print(searchParams['goal_max'], searchParams['goal_min'])
            for c in Campaign.objects.raw('SELECT * FROM api_campaign WHERE current_amount < %s AND current_amount > %s', [searchParams['current_amount_max'], searchParams['current_amount_min']]):
                # Load each Campaign into the Response that lies in this goal range
                mysearch[c.campaign_id] = {"campaign_id": c.campaign_id, "title": c.title, "goal": c.goal, "donators": c.donators, "current_amount": c.current_amount, "currencycode": c.currencycode, "campaign_hearts": c.campaign_hearts, "days_active": c.days_active} # For an object

        #********************************************************
        #**************Search a currencycode ********************
        #********************************************************
        elif searchParams['currencycode']:

            for c in Campaign.objects.raw('SELECT * FROM api_campaign WHERE currencycode = %s', [searchParams['currencycode']]):
                # mysearch.append(c.campaign_id) # For an array
                mysearch[c.campaign_id] = {"campaign_id": c.campaign_id, "title": c.title, "goal": c.goal, "donators": c.donators, "current_amount": c.current_amount, "currencycode": c.currencycode, "campaign_hearts": c.campaign_hearts, "days_active": c.days_active} # For an object

        order_by = 'currencycode'

        else:
            print("Made it to else")

        # if searchParams['lets_search'] and order_by:
        #     print("Hello mai fren")



        
        print("Finished")


        return Response({"my_search": mysearch})