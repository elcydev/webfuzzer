from argparse import ArgumentParser, _ArgumentGroup, Namespace
import pluginlib
from typing import Dict, List
from core.models import GroupType, PluginType, SessionBaseModel

@pluginlib.Parent('parser')
class Parser(object):
    
    _alias_ = "Parser"
    _group_type_ = GroupType.DEFAULT
    main_parser: ArgumentParser = None
    _plugin_type_ = PluginType.PARSER

    def parserRequest(self, sb: SessionBaseModel):
        raise NotImplementedError
    
    def parserResponse(self, sb: SessionBaseModel) -> bool:
        raise NotImplementedError

    @pluginlib.abstractmethod
    def initialize(self, main_parser: ArgumentParser, group: _ArgumentGroup):
        self.main_parser = main_parser
        self.add_arguments(group)
    
    @property
    def getGroupType(self):
        return self._group_type_
  
    @property
    def getPluginType(self):
        return self._plugin_type_
    
    @property
    def namespace(self) -> Namespace:
        return self.main_parser.parse_args()
    
    @property
    def checkNameSpace(self):
        raise NotImplementedError