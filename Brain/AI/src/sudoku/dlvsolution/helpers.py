import os

from languages.predicate import Predicate
from platforms.desktop.desktop_handler import DesktopHandler
from specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService
from AI.src.constants import DLV_PATH

# make the fact classes here with the correct attributes eg class Edge makes asp fact edge(x, y, value)

class Edge(Predicate):
    predicate_name = "sudoku"

    def __init__(self, x, y, value):
        Predicate.__init__(self, [("x", int), ("y", int), ("value", int)])
        self.x = x
        self.y = y
        self.value = value
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_xOnScreen(self):
        return 500
    
    def get_yOnScreen(self):
        return 500
    
    def get_value(self):
        return self.value
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.value})\n"
    
class X(Predicate):
    predicate_name = "x"

    def __init__(self, x):
        Predicate.__init__(self, [("x", int)])
        self.x = x
    
    def get_x(self):
        return self.x
    
    def __str__(self):
        return f"({self.x})\n"
    
class Y(Predicate):
    predicate_name = "y"

    def __init__(self, y):
        Predicate.__init__(self, [("y", int)])
        self.y = y
    
    def get_y(self):
        return self.y
    
    def __str__(self):
        return f"({self.y})\n"
    
class N(Predicate):
    predicate_name = "n"

    def __init__(self, n):
        Predicate.__init__(self, [("n", int)])
        self.n = n
    
    def get_n(self):
        return self.n
    
    def __str__(self):
        return f"({self.n})\n"
    
class SubGrid(Predicate):
    predicate_name = "subgrid"

    def __init__(self, x, y, a, b):
        Predicate.__init__(self, [("x", int), ("y", int), ("a", int), ("b", int)])
        self.x = x
        self.y = y
        self.a = a
        self.b = b
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_a(self):
        return self.a
    
    def get_b(self):
        return self.b
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.a}, {self.b})\n"


def chooseDLVSystem() -> DesktopHandler:
    try:
        if os.name == 'nt':
            return DesktopHandler(
                DLV2DesktopService(os.path.join(DLV_PATH, "DLV2.exe")))
        elif os.uname().sysname == 'Darwin':
            return DesktopHandler(
                DLV2DesktopService(os.path.join(DLV_PATH, "dlv2.mac_7")))
        else:
            print(f"I will use this ASP Solver: {os.path.join(DLV_PATH, 'dlv2-linux')}")
            return DesktopHandler(
                DLV2DesktopService(os.path.join(DLV_PATH, "dlv2-linux")))
    except Exception as e:
        print(e)


def assert_true(expr, msg=None):
    """Check that the expression is true."""
    if not expr:
        msg = f"{msg}: {(expr)} is not true"
        raise ValueError(msg)
