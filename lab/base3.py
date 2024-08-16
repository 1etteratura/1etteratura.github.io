# all we have are containers, because a resource is just a container with a single value.
# that is: you have a resource which is a numerical value,
# and you have other resources.

class Thing:
    def __init__(self, things):
        self.value = 0
        self.things = things

    def addThing(self, thing):
        self.things.append(thing)

    def getValues(self):
        return [t.value for t in self.things]

    def getTotalSum(self):
        return sum(self.getValues())

    def getTotalMultiplication(self):
        return reduce(lambda x, y: x*y, self.getValues())

    def getValue(self):
        return getTotalMultiplication() * self.value
