"""9. Write a Python program to get a list of locally installed Python modules."""

import pkg_resources

installed_packages = {d.project_name: d.version for d in pkg_resources.working_set}

for package, version in installed_packages.items():
    print(package +' - version: '+ version)