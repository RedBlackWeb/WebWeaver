from setuptools import setup, find_packages


with open("README.md", 'r') as f:
    description = f.read()

setup(

    name="WebWeaver",
    version="1.1.1",
    packages=find_packages(),
    description='A package used for web crawling',
    author='Shubakar Poda & Nirmal Babu',
    author_email='redblack09062024@gmail.com',
    install_requires=[
        'requests==2.32.3'

    ],
    long_description=description,
    long_description_content_type="text/markdown",

)