from argparse import _ArgumentGroup
from core.models import GroupType, PluginType, SessionBaseModel
from core.plugin import Parser

class FilterResponseHeader(Parser):

    _alias_ = 'FilterResponseHeader'
    _group_type_ = GroupType.FILTERS
    _plugin_type_ = PluginType.FILTER

    def parserResponse(self, sb: SessionBaseModel) -> bool:
     if self.namespace.fh:
        for header in self.namespace.fh:
            try:
                parts = header.split(':')
                if len(parts) < 2:
                    raise ValueError("Invalid header format: {}".format(header))
                
                key, value = parts[0], ':'.join(parts[1:])
                
                if key.strip() not in sb.getResponse.headers.keys():
                    return False
                if not value.strip() in sb.getResponse.headers.values():
                    return False
            except ValueError as e:
                exit("[*] The params -fh {} doesn't have a good format. {}".format(header, e))
     return True

    @property
    def checkNameSpace(self):
        if self.namespace.fh:
            return True
        return False

    def initialize(self, main_parser, group):
        return super(FilterResponseHeader, self).initialize(main_parser, group)
    
    def add_arguments(self, group: _ArgumentGroup):
        group.add_argument("-fh", 
                           dest="fh", 
                           nargs='+',
                           action='extend',
                           help='"Name:Value", separated by colon. Multiple -fh flags are accepted')
