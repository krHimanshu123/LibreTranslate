from importlib.metadata import PackageNotFoundError, entry_points, version


class DistributionNotFound(Exception):
    pass


class _Distribution:
    def __init__(self, package_name):
        self.version = version(package_name)


def get_distribution(package_name):
    try:
        return _Distribution(package_name)
    except PackageNotFoundError as error:
        raise DistributionNotFound(str(error)) from error


def iter_entry_points(group, name=None):
    eps = entry_points()

    # Python 3.10+ returns EntryPoints with .select(); older versions may return a dict-like mapping.
    if hasattr(eps, "select"):
        selected = eps.select(group=group)
    else:
        selected = eps.get(group, [])

    for ep in selected:
        if name is None or ep.name == name:
            yield ep
