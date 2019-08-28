from textwrap import dedent

methods = [m for m in dir(str) if not m.startswith("_")]

for method in methods:
    exec(dedent(f"""
        def {method}(s, *args):
            return s.{method}(*args)
        """
        )
    )

from string import *
letters = ascii_letters