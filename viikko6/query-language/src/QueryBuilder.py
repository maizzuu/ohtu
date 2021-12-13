from matchers import And, PlaysIn, HasAtLeast, All, Not, HasFewerThan, Or


class QueryBuilder():
    def __init__(self):
        self._matchers = []
    
    def add_matcher(self, matcher):
        self._matchers.append(matcher)

    def playsIn(self, team):
        self.add_matcher(PlaysIn(team))
        return self
    
    def hasAtLeast(self, value, attr):
        self.add_matcher(HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self.add_matcher(HasFewerThan(value, attr))
        return self
    
    def build(self):
        r = All(*self._matchers)
        self._matchers.clear()
        return r

    def oneOf(self, *args):
        self._matchers.append(Or(*args))
        return self