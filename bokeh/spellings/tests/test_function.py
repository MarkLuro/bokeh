from __future__ import absolute_import, print_function

import unittest

from bokeh.spellings import FunctionHandler
from bokeh.document import Document

from bokeh.plot_object import PlotObject
from bokeh.properties import Int, Instance

class AnotherModel(PlotObject):
    bar = Int(1)

class SomeModel(PlotObject):
    foo = Int(2)
    child = Instance(PlotObject)

class TestFunctionHandler(unittest.TestCase):

    def test_empty_func(self):
        def noop(doc):
            pass
        handler = FunctionHandler(noop)
        doc = Document()
        handler.modify_document(doc)
        if handler.failed:
            raise RuntimeError(handler.error)
        assert not doc.roots

    def test_func_adds_roots(self):
        def add_roots(doc):
            doc.add_root(AnotherModel())
            doc.add_root(SomeModel())
        handler = FunctionHandler(add_roots)
        doc = Document()
        handler.modify_document(doc)
        if handler.failed:
            raise RuntimeError(handler.error)
        assert len(doc.roots) == 2
