import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'gofundapi.settings'
import django
django.setup()
from api.models import Campaign

def main():
    mycamp = Campaign.objects.get(campaign_id=17602)
    print(mycamp.campaign_id, '\n', mycamp.goal, '\n', mycamp.title, '\n', mycamp.description)


if __name__ == '__main__':
    main()