from config.version import __version__ as version
from setuptools import setup, find_packages


license = open('LICENSE').read()

setup(
    name='hypatia-learn',
    version=version,
    description='Enable peer mentorship!',
    long_description='',
    license=license,
    author='Hypatia Software Org',
    author_email='contact@hypatiasoftware.org',
    url='https://github.com/hypatia-software-org/hypatia-learn',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3',
    install_requires=[
        'django',
    ]
)
