#!/usr/bin/env python3

# initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'gofundapi.settings'
import django
django.setup()

# regular imports
from api.models import Campaign
import json

# main script
def main():
    # read JSON file
    with open('campaigns.json', encoding="utf8") as json_file:
        data = json.load(json_file)

    # Create a new Campaign object for each item in the json file
    for c in data['campaigns']:
        cam = Campaign()
        cam.campaign_id = c['campaign_id']
        cam.auto_fb_post_mode = c['auto_fb_post_mode']
        cam.category_id = c['category_id']
        cam.currencycode = c['currencycode']
        cam.current_amount = c['current_amount']
        cam.goal = c['goal']
        cam.donators = c['donators']

        foo = c['days_active'] # temp variable to handle bad value
        try:
            val = int(foo)
        except ValueError:
            val = None
        # Now use val to insert into the database
        cam.days_active = val

        goo = c['days_active'] # temp variable to handle bad value
        try:
            val = int(goo)
        except ValueError:
            val = None
        # Now use val to insert into the database
        cam.days_created = val

        cam.title = c['title']
        cam.description = c['description']
        cam.has_beneficiary = c['has_beneficiary']
        cam.visible_in_search = c['visible_in_search']
        cam.status = c['status']
        cam.deactivated = c['deactivated']
        cam.state = c['state']
        cam.is_launched = c['is_launched']
        cam.campaign_hearts = c['campaign_hearts']
        cam.social_share_total = c['social_share_total']
        cam.is_charity = c['is_charity']
        cam.campaign_image_url = c['campaign_image_url']
        cam.save()


# bootstrap
if __name__ == '__main__':
    main()