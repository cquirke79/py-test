from setuptools import setup

setup(
    name="snapshot-analyser30000",
    version="0.1",
    author="CQ",
    author_email="cq@nope.co.nz",
    description="Snapshot analyser is cool",
    license="GPLv3+",
    packages=['shotty'],
    url="https://google.com",
    install_requires=[
    'click',
    'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
