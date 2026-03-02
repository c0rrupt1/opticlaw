import os
import yaml
import core

# TODO: replace with better backend

config = core.storage.StorageDict("config", "yaml")

default_config = {
    "api_url": "http://localhost:11434/v1",
    "api_key": "KEY_HERE",
    "model": "MODEL_HERE",
    "channels": ["cli"],
    "modules": ["identity", "memory", "scheduler"],
    "max_turns": 20,
    "context_window": "on"
}

if not config:
    config.load(default_config)
    config.save()

def get(*args, **kwargs):
    """shorthand for accessing config values"""

    return config.get(*args, **kwargs)
