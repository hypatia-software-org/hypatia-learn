from django.conf import settings
import json
import requests
from django.contrib.auth import get_user_model

User = get_user_model()

class CivicrmApi(object):
    @property
    def civicrm_key(self):
        return settings.CIVICRM_KEY
    @property
    def civicrm_api_key(self):
        return settings.CIVICRM_API_KEY

    @property
    def civicrm_url(self):
        return 'https://hypatiasoftware.org/wp-content/plugins/civicrm/civicrm/extern/rest.php'

    
    def get_contact(self, value, field='id'):
        query = {
            'entity':'contact',
            'action':'getsingle',
            field:value,
        }
        return self.query_api(query)


    def get_contact_mentor(self, value, field='id'):
        # Only allow queries of mentor data
        mentor_gid = 11

        query = {
            'entity':'contact',
            'action':'getsingle',
            'group':mentor_gid,
            'return':'contact_id,display_name,custom_5,custom_92,custom_93,image_URL,tag,group',
            field:value,
        }
        return self.query_api(query)


    def get_groupcontact_contacts(self, group):
        query = {
            'entity':'GroupContact',
            'action':'get',
            'group_id':group,
            'status':'Added',
            'return':'contact_id,contact_id.display_name,contact_id.custom_5',
        }
        return self.query_api(query)

    def get_tags(self):
        query = {
            'entity':'tag',
            'action':'get',
            'parent_id':17,
        }
        return self.query_api(query)
        

    
    def query_api(self, query):
        query['key'] = self.civicrm_key
        query['api_key'] = self.civicrm_api_key
        query['json'] = 1

        response = requests.post(self.civicrm_url, data=query)

        data = json.loads(response.text)

        #clean our dict a little:
        if 'tags' in data:
            data['tags'] = data['tags'].split(',')

        return data
        
