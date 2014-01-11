from setuptools import find_packages, setup

version='0.1'

try:
    long_description = open("README.txt").read()
except:
    long_description = ''

setup(name='trac-WorkflowTicketFieldsPlugin',
      version=version,
      description="Attaches ticket fields to workflow actions exclusively, like the 'Resolution' and 'Owner' fields",
      long_description=long_description,
      author='Ethan Jucovy',
      author_email='ejucovy@gmail.com',
      url='http://trac-hacks.org/wiki/WorkflowActionButtonsPlugin',
      keywords='trac plugin',
      license="BSD",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests*']),
      include_package_data=True,
      zip_safe=False,
      entry_points = """
      [trac.plugins]
      workflow_ticketfields = workflow_ticketfields
      """,
      )

