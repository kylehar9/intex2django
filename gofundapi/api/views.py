from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def testInputView(request):
# this view will pull up the submit html template
        return render(request, "index.html", {})

def resultsView(request):
# this view receives parameters from the submit html template and calls the API in azure
# this contains API code for Python and Python3 

    # If you are using Python 3+, import urllib instead of urllib2
    #import urllib2.request
    import urllib
    import json 

    # assign all the parameters to variables which you put in the API like the commented code
    # or just put them in directly like I did farther down
    
    # age = str(request.POST['age'])
    # sex = str(request.POST['sex'])
    # bmi = str(request.POST['bmi'])
    # children = str(request.POST['children'])
    # smoker = str(request.POST['smoker'])
    # region = str(request.POST['region'])
    
    # formatting the data into a data object for the API call
    data =  {
                "Inputs": {
                    "input1":
                    {
                        # Test 2:
                        "ColumnNames": ["category_id", "currencycode", "current_amount", "goal", "days_active", "title", "description", "has_beneficiary", "visible_in_search", "is_charity"],
                        "Values": [[ request.POST['category_id'], request.POST['currencycode'], 0, request.POST['goal'], request.POST['days_active'], request.POST['title'], request.POST['description'], request.POST['has_beneficiary'], request.POST['visible_in_search'], request.POST['is_charity']]]
                        # "Values": [[ request.POST['goal'], request.POST['donators']]]
                        
                        # Potentially to-use
                        # "ColumnNames": ["campaign_id", "auto_fb_post_mode", "category_id", "currencycode","current_amount", "goal", "donators", "days_active", "title", "description", "has_beneficiary", "visible_in_search", "state", "campaign_hearts", "is_charity",  "velocity"]
                        # "Values": [ request.POST['campaign_id'], request.POST['auto_fb_post_mode'], request.POST['category_id'], request.POST['currencycode'], request.POST['current_amount'], request.POST['goal'], request.POST['donators'], request.POST['days_active'], request.POST['title'], request.POST['description'], request.POST['has_beneficiary'], request.POST['visible_in_search'], request.POST['state'], request.POST['campaign_hearts'], request.POST['is_charity'], request.POST['velocity']]

                        # "Values": [[ request.POST['age'], request.POST['sex'], request.POST['bmi'], request.POST['children'], request.POST['smoker'], request.POST['region'], "0" ],]

                        # "ColumnNames": ["url", "campaign_id", "auto_fb_post_mode","collected_date","category_id","category","currencycode","current_amount","goal","donators","days_active","days_created","title","description","default_url","has_beneficiary","media_type","project_type","turn_off_donations","user_id","user_first_name","user_last_name","user_facebook_id","user_profile_url","visible_in_search","status","deactivated","state","is_launched","campaign_image_url","created_at","launch_date","campaign_hearts","social_share_total","social_share_last_update","location_city","location_country","location_zip","is_charity","charity_valid","charity_npo_id","charity_name","velocity"]
                        # "ColumnNames": ["age", "sex", "bmi", "children", "smoker", "region", "charges"],
                    }, # in the values array above it may seem weird to put a value for the response var, but azure needs something
                },
                "GlobalParameters": {
                }
            }

    # the API call
    body = str.encode(json.dumps(data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/d7228c50e6944ea1ae1a4cd5d0f15842/services/8ced6f993d1844969db2a8780205da0a/execute?api-version=2.0&details=true'
    api_key = 'htxCbkeJVyLGBy7LKOVzm+JQLZaY3RQHsAGkw/gNS+9/hJanTtBZqgZWe5xYpMgfDP4TD6ScZzrayUNeoppIjw=='
    # Replace my url and api_key with your own values
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
    result = result["Results"]["output1"]["value"]["Values"][0][13]
    #********************************
    # azure send the response as a weird result object. It would be wise to postman to find the 
    # path to the response var value

    return render(request, "results.html", {"result": result}) # this path assumes that this file is in the root directory in a folder named templates
    # the third parameter sends the result (the response variable value) to the template to be rendered