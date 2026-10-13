import logging

from maya import cmds

log = logging.getLogger(__name__)

_loaded_plugin_cache: set[str] = set()


def ensure_plugin_loaded(plugin: str) -> None:
    if plugin not in _loaded_plugin_cache:
        if not cmds.pluginInfo(plugin, query=True, loaded=True):
            cmds.loadPlugin(plugin)
            log.info(f"Loaded plugin: {plugin}")
        _loaded_plugin_cache.add(plugin)
