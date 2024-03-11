from argparse import ArgumentParser
from typing import Dict, List

from pluginlib import PluginLoader
import pluginlib
from core.models import GroupType, PluginType, SessionBaseModel
from core.plugin import Parser

import pluginlib

class PluginManager:
  _parser: ArgumentParser = None
  _group_plugins: dict = dict()
  _plugins: Dict[str, Parser] = dict()
  _loader: PluginLoader = None

  def __init__(self, parser: ArgumentParser):
    self._parser = parser

    loader = pluginlib.PluginLoader(paths=['plugins'])
    plugins = loader.plugins
    for group in GroupType:
      self._group_plugins[group.name] = self._parser.add_argument_group(group.value)
    
    for pl_name in plugins.parser:
        inst_pl: Parser = plugins.parser[pl_name]()
        inst_pl.initialize(self._parser, self._group_plugins[inst_pl.getGroupType.name])
        self._plugins[pl_name] = inst_pl

  def setParserRequest(self, gt: GroupType, sb: SessionBaseModel):
    for name, inst_pl in self._plugins.items():
      if inst_pl.getGroupType == gt:
        inst_pl.parserRequest(sb)
        
  def getPlugins(self, pt: PluginType = None) -> List[Parser]:
    if not pt:
      return [inst_pl for name, inst_pl in self._plugins.items()]
    return [inst_pl for name, inst_pl in self._plugins.items() if inst_pl.getPluginType == pt]