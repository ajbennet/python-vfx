
import sys
import importlib

from functools import partial
# Package Import
import model
import view

importlib.reload(model)
importlib.reload(view)


def connect(value):
    newValue = partial(model.core, value)
    newValue()


def main():
    interface = view.UI()
    interface.show()


"""
import week5.tweener.controller as controller

reload(controller)

controller.main()

"""
