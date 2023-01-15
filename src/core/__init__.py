from utilslib import core

from .config import _setup_config
from .depends import _setup_depends
from .tools import _setup_tools

core.config.setup(_setup_config)
core.depends.setup(_setup_depends)
core.tools.setup(_setup_tools)

from .middlewares import register_middlewares

__all__ = ("register_middlewares",)
