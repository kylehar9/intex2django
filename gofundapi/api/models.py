from django.db import models

class Campaign(models.Model):
    campaign_id = models.IntegerField(primary_key=True, editable=False)
    auto_fb_post_mode = models.TextField()
    category_id = models.IntegerField()
    currencycode = models.TextField()
    current_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    goal = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    donators = models.IntegerField()
    days_active = models.IntegerField(null=True)
    days_created = models.IntegerField(null=True)
    title = models.TextField()
    description = models.TextField()
    has_beneficiary = models.TextField()
    visible_in_search = models.TextField()
    status = models.IntegerField()
    deactivated = models.TextField()
    state = models.TextField()
    is_launched = models.TextField()
    campaign_hearts = models.IntegerField()
    social_share_total = models.IntegerField()
    is_charity = models.TextField()
    campaign_image_url = models.TextField(null=True)
    score = models.DecimalField(max_digits=20, decimal_places=4, default=0)

    # ******Here they are sorted by datatype******
    # campaign_id = models.IntegerField(primary_key=True, editable=False)
    # category_id = models.IntegerField()
    # donators = models.IntegerField()
    # days_active = models.IntegerField()
    # days_created = models.IntegerField()
    # campaign_hearts = models.IntegerField()
    # social_share_total = models.IntegerField()
    # status = models.IntegerField()
    # current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # goal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # auto_fb_post_mode = models.BooleanField()
    # has_beneficiary = models.BooleanField()
    # visible_in_search = models.BooleanField()
    # deactivated = models.BooleanField()
    # is_launched = models.BooleanField()
    # is_charity = models.BooleanField()
    # currencycode = models.TextField()
    # title = models.TextField()
    # description = models.TextField()
    # state = models.TextField()

    # *********This is how I originally had it**********
    # campaign_id = models.IntegerField(primary_key=True, editable=False)
    # auto_fb_post_mode = models.BooleanField()
    # category_id = models.IntegerField()
    # currencycode = models.TextField()
    # current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # goal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # donators = models.IntegerField()
    # days_active = models.IntegerField()
    # days_created = models.IntegerField()
    # title = models.TextField()
    # description = models.TextField()
    # has_beneficiary = models.BooleanField()
    # visible_in_search = models.BooleanField()
    # status = models.IntegerField()
    # deactivated = models.BooleanField()
    # state = models.TextField()
    # is_launched = models.BooleanField()
    # campaign_hearts = models.IntegerField()
    # social_share_total = models.IntegerField()
    # is_charity = models.BooleanField()