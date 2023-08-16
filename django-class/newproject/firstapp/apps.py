# from django.apps import AppConfig
# post_save.connect(check_record_count, sender=Details)


# class FirstappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'firstapp'

#   def ready(self):
#         from .models import Details
#         post_save.connect(check_record_count, sender=Details)
# from django.apps import AppConfig

# class FirstappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'firstapp'

#     def ready(self):
#         from .models import Details
#         from django.db.models.signals import post_save
        # post_save.connect(check_record_count, sender=Details)



# import pandas as pd
# import os

# def check_record_count(sender, instance, **kwargs):
#     if Details.objects.count() % 10 == 0:
#         export_to_csv()

# def export_to_csv():
#     queryset = Details.objects.all()
#     df = pd.DataFrame(list(queryset.values()))
#     current_directory = os.path.dirname(os.path.abspath(__file__))
#     csv_file_path = os.path.join(current_directory, 'data.csv')
#     df.to_csv(csv_file_path, index=False)
    # df.to_csv('data.csv', index=False) 

# from django.apps import AppConfig

# class FirstappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'firstapp'

    # def ready(self):
    #     print("ready method")
        # Import the signal function here to avoid circular import
        # from .models import Details
        # import os
        # import pandas as pd
        # from django.db.models.signals import post_save

        

        # def export_to_csv():
        #     queryset = Details.objects.all()
        #     df = pd.DataFrame(list(queryset.values()))
        #     current_directory = os.path.dirname(os.path.abspath(__file__))
        #     csv_file_path = os.path.join(current_directory, 'data.csv')
        #     df.to_csv(csv_file_path, index=False)
            # df.to_csv('data.csv', index=False)

        # Connect the signal to the function
        # post_save.connect(check_record_count, sender=Details)

        # def check_record_count(sender, instance, **kwargs):
        #     if Details.objects.count() % 10 == 0:
        #         export_to_csv()

from django.apps import AppConfig


# def export_to_csv():
#     import os
#     import pandas as pd
#     from .models import Details  # Move the import here to avoid circular import
#     queryset = Details.objects.all()
#     df = pd.DataFrame(list(queryset.values()))
#     current_directory = os.path.dirname(os.path.abspath(__file__))
#     csv_file_path = os.path.join(current_directory, 'data.csv')
#     df.to_csv(csv_file_path, index=False)

class FirstappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'firstapp'

    # def ready(self):
    #     print("ready")
    #     # Import the function here to avoid circular import
    #     from django.db.models.signals import post_save
        
    #     from .models import Details

    #     def check_record_count(sender, instance, **kwargs):
    #         if Details.objects.count() % 10 == 0:
    #             export_to_csv()

    #     # Connect the signal to the function
    #     post_save.connect(check_record_count, sender=Details)
