import urlparse
import os

from logging import getLogger

from pylons import config
from ckan.common import json

from ckan import plugins as p
import ckan.lib.helpers as h

ignore_empty = p.toolkit.get_validator('ignore_empty')
not_empty = p.toolkit.get_validator('not_empty')

log = getLogger(__name__)

HANDLED_FORMATS = ['csv', 'xls', 'xlsx']

class TableauView(p.SingletonPlugin):
    '''This base class is for view extensions. '''
    p.implements(p.IResourceView, inherit=True)
    p.implements(p.IConfigurer, inherit=True)

    # IConfigurer
    
    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'templates')

    # IResourceView (CKAN >=2.3)

    def info(self):
        return {'name': 'tableau_view',
                'title': 'Tableau',
                'icon': 'plus',
                'iframed': False,
                'default_title': p.toolkit._('Tableau viewer'),
                'schema': {
                    'viz_name': [ignore_empty],
                    'sheet_name': [ignore_empty]
                },
                }

    def can_view(self, data_dict):
        return True

    def view_template(self, context, data_dict):
        return 'tableau/tableau.html'

    def form_template(self, context, data_dict):
        return 'tableau/tableau_form.html'

    def setup_template_variables(self, context, data_dict):
        #log.error('RESOURCE: {0}'.format(data_dict))
        resource_view = data_dict['resource_view']

        return {'viz_name': resource_view.get('viz_name', 'no_viz_name'),
                'sheet_name': resource_view.get('sheet_name', 'no_sheet_name'),
                }


