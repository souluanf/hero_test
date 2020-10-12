<div align="center">
<a href="https://www.companyhero.com" target="_blank">
    <img src="https://www.companyhero.com/companyhero-logo.svg" height="100px" alt="Company Hero"/>
</a>

<h3>Backend Developer Challenge</h3>

<a href="https://www.python.org" target="_blank">
  <img src="https://img.shields.io/badge/devel-Python-brightgreen" alt="Python"/>
</a>

<a href="https://travis-ci.com" target="_blank">
  <img src="https://img.shields.io/badge/ci-Travis-brightgreen" alt="Travis CI"/>
</a>

<a href="https://www.django-rest-framework.org" target="_blank">
  <img src="https://img.shields.io/badge/api-DRF-brightgreen" alt="Django Rest Framework"/>
</a>

<a href="https://www.djangoproject.com" target="_blank">
  <img src="https://img.shields.io/badge/main--framework-Django-brightgreen" alt="Django"/>
</a>

<a href="https://www.docker.com" target="_blank">
  <img src="https://img.shields.io/badge/deploy-Docker|Heroku-brightgreen" alt="Docker"/>
</a>

<a href="https://docs.conda.io/en/latest/miniconda.html" target="_blank">
  <img src="https://img.shields.io/badge/venv-Conda-brightgreen" alt="Conda"/>
</a>

<a href="https://docs.pytest.org/en/latest" target="_blank">
  <img src="https://img.shields.io/badge/coverage-PyTest-brightgreen" alt="PyTest"/>
</a>

<a href="https://opensource.org/licenses/MIT" target="_blank">
  <img src="https://img.shields.io/badge/license-MIT-brightgreen" alt="MIT"/>
</a>

</div>

## TL;DR
##### Front End Application: https://hero-test-lf.herokuapp.com
##### API Postman Documentation: https://documenter.getpostman.com/view/10016660/TVRkb8Aj
##### Continuous Integration Tests: https://travis-ci.com/github/souluanf/hero_test
##### Github Repository: https://github.com/souluanf/hero_test

## Local execution

#### Getting the code

```
$ git clone https://github.com/souluanf/hero_test.git
```

### 1 - Using the Docker
<pre>
$ cd < path/cloned >
$ docker build . -t hero_test
$ docker run -d -p 8030:8030 hero_test
</pre>
Aponte o browser para http://localhost:8030

### 2 -  Without using the docker


Create a virtual environment with your favorite management system (conda, pyenv, virtualenv, etc);

Activate the created environment and install the requirements:
<pre><code> $ pip install -r requirements.txt </code></pre>

Run the server with the following command:
<pre><code> $ python manager.py runserver </code></pre>
Now is ready!

Then point your browser to localhost:8000

###  Default Credentials

<table>
    <thead>
        <tr class="table100-head">
            <th class="column1">USER</th>
            <th class="column2">PASSWORD</th>
        </tr>
    </thead>
    <tbody>
            <tr>
                <td class="column1">test@companyhero.com</td>
                <td class="column2">hero123</td>
            </tr>
    </tbody>
</table>


###  Challenge Description
This is a simple challenge to test your skills on building APIs.
It has to be done using Python and the Django Framework

### Front-end
All resources will be made available on the backend through the REST API. A frontend was developed just for this documentation.

### Coverage
Due to the short time, it was only possible to perform a few tests in order to demonstrate the technique. The package used for the tests was pytest.

### Development Environment

<table>
    <thead>
        <tr class="table100-head">
            <th class="column1">Resource</th>
            <th class="column2">Description</th>
            <th class="column3">Version</th>
        </tr>
    </thead>
    <tbody>
            <tr>
                <td class="column1">Laptop</td>
                <td class="column2">16 GB Memory</td>
                <td class="column3">I7 G7</td>
            </tr>
            <tr>
                <td class="column1">Operating System</td>
                <td class="column2">Ubuntu LTS</td>
                <td class="column3">20.04.1</td>
            </tr>
            <tr>
                <td class="column1">Editor/IDE</td>
                <td class="column2">Pycharm Professional</td>
                <td class="column3">2020.2</td>
            </tr>
            <tr>
                <td class="column1">Virtual Env</td>
                <td class="column2">Conda (Miniconda) </td>
                <td class="column3">4.8.3</td>
            </tr>
            <tr>
                <td class="column1">Graphics Card</td>
                <td class="column2">nVidia GM107 </td>
                <td class="column3">GeForce 940MX</td>
            </tr>
            <tr>
                <td class="column1">Devel</td>
                <td class="column2">Python</td>
                <td class="column3">3.8.3</td>
            </tr>
    </tbody>
</table>
