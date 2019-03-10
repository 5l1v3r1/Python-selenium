from Fixture.application import Application
import pytest

fixture = None

@pytest.fixture
def app(request):
   global fixture
   browser = request.config.getoption("--browser")
   base_Url = request.config.getoption("--baseUrl")
   password = request.config.getoption("--password")
   if fixture is None:
      fixture = Application(browser=browser, base_Url=base_Url, password=password)
   else:
      if not fixture.is_valid():
         fixture = Application(browser=browser, base_Url=base_Url, password=password)
   fixture.session.ensure_Login(username="admin", password="secret")
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
   parser.addoption("--baseUrl", action="store", default="http://localhost:8080/addressbook/")
   parser.addoption("--password", action="store", default="secret")