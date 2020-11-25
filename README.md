<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://proboston.net/">
    <img src="https://proboston.net/assets/images/fb-share.jpg" alt="Proboston logo" width="150">
  </a>

  <h3 align="center">Business ID form app</h3>

  <p align="center">
  Django developer exercise
    <br>
    <a href="https://github.com/johnunar/praggregator/issues">Report Bug</a>
    ·
    <a href="https://github.com/johnunar/praggregator/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
    * [Built With](#built-with)
* [The task](#the-task)
    * [Requirements](#requirements)
    * [Data model](#data-model)
* [Specification](#specification)
    * [Must have](#must-have)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

This Django app has been created as an exercise for Proboston Creative

### Built With
This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)

<!-- THE TASK -->
## The task
Create Django app with a simple form.

### Requirements:
* ModelForm
* Data model is shown in the admin
* New objects cannot be created in the admin

### Data model:
This app has just one Model:

#### Contact
* name: varchar(255), required
* e-mail: varchar(255), not required, validated
* business id: varchar(8), required, validated with ARES

<!-- SPECIFICATION -->
## Specification

#### Must have:
* Form
* Admin
* README
* sqlite (as database should be created by migrate)

<!-- GETTING STARTED -->
## Getting Started
If you want to get a local copy of this app up and running, follow these steps:

### Prerequisites

You need to install python before running 
* [python-3.8.5](https://www.python.org/downloads/)
```shell script
Ubuntu: sudo apt install python3.8
MacOS: brew install python

conda: conda create --name pbform python=3.8
```

### Installation
If you want to run this app locally, you can. 

Good Advise: Use a virtual environment ([pipenv](https://github.com/pypa/pipenv), [anaconda](https://www.anaconda.com/products/individual), ...)

1. Clone the repo
```shell script
git clone https://github.com/johnunar/probostonform.git
```
2. Install requirements from the provided file
```shell script
pip install -r requirements.txt
```
3. Generate a secret key
```shell script
python
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
```
4. Set the environment variables
```shell script
export PROB_DEBUG="True"
export PROB_SECRET_KEY="<Secret_key_from_step_4 >"
```
7. Migrate
```shell script
./manage.py migrate
```
8. Run tests
```shell script
./manage.py test
```
9. Run the development server
```shell script
./manage.py runserver
```
10. If there is anything wrong, do not hesitate and contact me.

<!-- CONTACT -->
## Contact

Jan Unar
* [@JohnnyUnar](https://twitter.com/JohnnyUnar)
* [johnunar@gmail.com](mailto:johnunar@gmail.com)

Project Link: [https://github.com/johnunar/praggregator](https://github.com/johnunar/praggregator)
