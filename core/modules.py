import core
import re
import inspect

def load(package, base_class):
    """
    Dynamically discovers classes in a package.

    Args:
        package: The root package module (e.g., `import channels; channels`).
        base_class: Only collect classes inheriting from this base.

    Returns:
        A tuple of discovered classes.
    """
    import importlib
    import pkgutil

    discovered = []

    # Ensure the package has a path to iterate
    if not hasattr(package, '__path__'):
        return tuple(discovered)

    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        try:
            # Import the module relative to the package
            module = importlib.import_module(f"{package.__name__}.{modname}")

            for attr_name in dir(module):
                attr = getattr(module, attr_name)

                # Ensure it is a class
                if not isinstance(attr, type):
                    continue

                # Filter by base class if provided (skip the base class itself)
                if base_class:
                    if attr is base_class:
                        continue
                    if not issubclass(attr, base_class):
                        continue

                discovered.append(attr)

        except ImportError as e:
            core.log("warning", f"failed to import {modname}: {e}")
            continue

    return tuple(discovered)

def get_name(obj):
    """converts a name like SchedulerTool to just `scheduler`"""

    name = None
    if inspect.isclass(obj):
        name = obj.__name__
    else:
        name = obj.__class__.__name__

    re_snakecase = re.compile('(?!^)([A-Z]+)')
    name_snakecase = re.sub(re_snakecase, r'_\1', name).lower()

    return name_snakecase
