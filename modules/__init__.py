import core
import core.module

def get_all():
    import modules
    return core.module.load(modules, core.module.Module)
