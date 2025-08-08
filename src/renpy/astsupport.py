class PyExpr(object):

    expr: str
    filename: str
    linenumber: int
    py: int
    hashcode: str
    column: int

    def __new__(
        cls,
        expr: str,
        filename: str,
        linenumber: int,
        py: int,
        hashcode: str,
        column: int = 0,
    ):
        self = super().__new__(cls)
        self.expr = expr
        self.filename = filename
        self.linenumber = linenumber
        self.py = py
        self.hashcode = hashcode
        self.column = column
        return self

    def get_code(self, **kwargs) -> str:
        return self.expr

    def __str__(self):
        return self.expr
