import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    
    name="scrapy",

    version="1.0.0",                    #TODO: implement versioneer script

    author="Ken Trinh",

    author_email="ctrinh@burlington.com",

    description="Web Scraping Protocol",

    long_description="text/markdown",   #TODO: Need to write a readme

    url="",                             #TODO: relace with GIT URL

    packages=setuptools.find_packages(include=['scrapy', 'scrapy.*', "scrapy.utils.*"]),

    classifiers=[
        "Programming Language :: Python :: 3",

        "License :: MIT License ",
    
        "Operating System :: OS Independent",
    ],

    install_requires=[
        'jupyter==1.0.0',
        'logging==0.4.9.6',
        'lxml==4.8.0',
        'openpyxl==3.0.7',
        'pandas==1.4.2',
        'pytest==7.1.2',
        'PyYAML==5.4.1',
        'requests 2.27.1',
        'tqdm==4.64.0'
    ],

    python_requires=">=3.7"

)