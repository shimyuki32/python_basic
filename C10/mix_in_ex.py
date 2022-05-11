import pprint

class PrettyMixin:
    def dump(self):
            pprint.pprint(vars(self))