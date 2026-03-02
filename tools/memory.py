import core
import os
import msgpack
import datetime
import re

cached_mem = None

class MemoryTool(core.tool.Tool):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

    # TODO: rewrite in progress
