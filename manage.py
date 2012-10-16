import os
from cement.core import controller

DIR = os.path.dirname(__file__)
DIR = os.path.abspath(DIR)

from pooldlib import cli
from pooldlib.flask import test
from pooldrest import app


class RootController(cli.RootController):
    class Meta:
        label = 'base'
        description = "Management tools for the Poold.in restful API."


class ServerController(cli.ServerController):
    flask_app = app


class TestController(cli.Controller):

    class Meta:
        label = 'tests'
        description = "Run the pooldrest test suite"

    @controller.expose(hide=True, help='Run the pooldrest test suite')
    def default(self):
        test.run('tests')


class App(cli.App):
    class Meta:
        label = 'pooldwww'
        base_controller = RootController
        handlers = (cli.ShellController,
                    ServerController,
                    TestController)


if __name__ == '__main__':
    App.execute()
