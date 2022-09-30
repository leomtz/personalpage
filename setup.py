from setuptools import setup

setup(
    name='personalpage',
    packages=['personalpage'],
    include_package_data=True,
    install_requires=[
        'flask', 'Flask-SQLAlchemy'
    ],
)