from setuptools import setup

REQUIREMENTS = [
    'requests',
    'click',
    'pyfiglet'
]

VERSION = 0.5
REPO_URL = 'https://github.com/trhacknon/toxin'

setup(
    name='toxin',
    packages=['toxin'],
    scripts=['toxin/toxin'],
    version=VERSION,
    description='An LFI (Local File Inclusion) Exploitation Tool',
    author='Ryan Draga',
    author_email='jeremydiliotti@gmail.com',
    url=REPO_URL,
    download_url=F'{REPO_URL}/archive/refs/tags{VERSION}.tar.gz',
    keywords=['LFI', 'Exploit'],
    python_requires='>=3.0',
    install_requires=REQUIREMENTS,
    classifiers=[]
)
