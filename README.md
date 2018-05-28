# Challange gittigidiyor
####Author
Umut Ataman - umutataman@gmail.com
####Tools and Frameworks
[PyCharm](https://www.jetbrains.com/pycharm/), [Selenium Webdriver](https://www.seleniumhq.org/projects/webdriver/), [Python 3.6](https://www.python.org/), [Behave](https://behave.readthedocs.io/en/latest/)

## Requirements and Running Project
######Requirements
Please follow steps in order for running the project without an issue

1. pip must be upgraded and virtual env must be created. More details;
[Installing packages using pip and virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
2. Make sure all requirements are install
```
pip install requirements.txt
```

######Running Project 

1. Running test without configuaration, simply send **behave** on terminal
2. To run responsive test; width and height parameters(in pixel) must be added.
```
behave -D width=1920 -D height=1080
behave -D width=414 -D height=736
```

