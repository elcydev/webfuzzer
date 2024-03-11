from argparse import _ArgumentGroup
from core.models import GroupType, PluginType, SessionBaseModel
from core.plugin import Parser

class CustomHeader(Parser):

    _alias_ = 'CustomHeader'
    _group_type_ = GroupType.INPUT
    _plugin_type_ = PluginType.PARSER

    def parserRequest(self, sb: SessionBaseModel):
     if self.namespace.headers:
        for header in self.namespace.headers:
            try:
               for header in self.namespace.headers:
                  key, value = header.split(':')
                  sb.addHeaders(key=key, value=value)
            except ValueError as e:
                exit("[*] The params -fh {} doesn't have a good format. {}".format(header, e))
     return True

    def initialize(self, main_parser, group):
        return super(CustomHeader, self).initialize(main_parser, group)
    
    def add_arguments(self, group: _ArgumentGroup):
        group.add_argument("-H", 
                           dest="headers", 
                           nargs='+',
                           action='extend',
                           help='"Name:Value", separated by colon. Multiple -fh flags are accepted')
