from Fixture.application import Application
import pytest
import json
import os.path
import importlib
import jsonpickle
from Fixture.db import DbFixture
from Fixture.orm import ORMFixture

fixture = None
target = None

def load_config(file):
   global target
   if target is None:
      config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
      with open(config_file) as f:
         target = json.load(f)
   return target

@pytest.fixture
def app(request):
   global fixture
   browser = request.config.getoption("--browser")
   web_config = load_config(request.config.getoption("--target"))['web']
   if fixture is None or not fixture.is_valid():
      fixture = Application(browser=browser, base_Url=web_config['baseUrl'])
   fixture.session.ensure_Login(username=web_config['username'], password=web_config['password'])
   return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
   def fin():
      fixture.session.ensure_Logout()
      fixture.destroy()
   request.addfinalizer(fin)
   return fixture


def pytest_addoption(parser):
   parser.addoption("--browser", action="store", default="firefox")
   parser.addoption("--target", action="store", default="target.json")
   parser.addoption("--check_ui", action="store_true")

@pytest.fixture(scope="session")
def db(request):
   db_config = load_config(request.config.getoption("--target"))['db']
   dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
   def fin():
      dbfixture.destroy()
   request.addfinalizer(fin)
   return dbfixture


@pytest.fixture(scope="session")
def orm(request):
   orm_config = load_config(request.config.getoption("--target"))['orm']
   ormfixture = ORMFixture(host=orm_config['host'], name=orm_config['name'], user=orm_config['user'], password=orm_config['password'])
   return ormfixture

def pytest_generate_tests(metafunc):
   for fixture in metafunc.fixturenames:
      if fixture.startswith("data_"):
         Testdata = load_from_module(fixture[5:])
         metafunc.parametrize(fixture, Testdata, ids=[str(x) for x in Testdata])
      elif fixture.startswith("json_"):
         Testdata = load_from_json(fixture[5:])
         metafunc.parametrize(fixture, Testdata, ids=[str(x) for x in Testdata])

def load_from_module(module):
   return importlib.import_module("data.%s" % module).Testdata

@pytest.fixture
def check_ui(request):
   return request.config.getoption("--check_ui")

def load_from_json(file):
   with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
      return jsonpickle.decode(f.read())

