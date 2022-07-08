from django.core.management.base import BaseCommand, CommandError
from crm.models import Client
import requests

class Command(BaseCommand):
    help = 'Adds New Users'

    def handle(self, *args, **options):
        try:
            r = requests.get('https://62c2c06cff594c656764970a.mockapi.io/users')

            for data in r.json()['data']:
                client = Client.objects.update_or_create(
                    cid = data['cid'],
                
                    defaults ={
                        'first_name' : data['first_name'],
                        'last_name' : data['last_name'],
                        'country_code' : data['country_code'],
                        'email' : data['email'],
                        'address' : data['address'],
                        'phone' : data['phone'],
                    }
                )
            
        except:
            raise CommandError('Error adding user')
        self.stdout.write(self.style.SUCCESS("Successfully closed user "))