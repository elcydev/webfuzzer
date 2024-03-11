from argparse import _ArgumentGroup
from core.models import GroupType, PluginType, SessionBaseModel
from core.plugin import Parser

class Extension(Parser):

    _alias_ = 'extension'
    _group_type_ = GroupType.INPUT
    _plugin_type_ = PluginType.PARSER

    def parserRequest(self, sb: SessionBaseModel):
        if self.namespace.ext:
            sb.setUrl(sb.getUrl + self.namespace.ext)
    
    def initialize(self, main_parser, group):
        return super(Extension, self).initialize(main_parser, group)
    
    def add_arguments(self, group: _ArgumentGroup):
        group.add_argument("-e", dest="ext", help="Comma separated list of extensions. Extends FUZZ keyword.")