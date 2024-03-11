from argparse import _ArgumentGroup
from setuptools import Extension
from core.models import GroupType, PluginType, SessionBaseModel
from core.plugin import Parser

class FilterResponseCode(Parser):

    _alias_ = 'FilterResponseCode'
    _group_type_ = GroupType.FILTERS
    _plugin_type_ = PluginType.FILTER

    def parserResponse(self, sb: SessionBaseModel) -> bool:
        if self.namespace.fc:
            if str(sb.getResponse.status_code) in self.namespace.fc.split(','):
                return True
            return False
    
    @property
    def checkNameSpace(self):
        if self.namespace.fc:
            return True
        return False

    def initialize(self, main_parser, group):
        return super(FilterResponseCode, self).initialize(main_parser, group)
    
    def add_arguments(self, group: _ArgumentGroup):
        group.add_argument("-fc", dest="fc", help="Filter HTTP status code from response: 200, 300")