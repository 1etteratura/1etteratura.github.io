

# models:

#  - one container has many resources, the "final resource" is calculated inside the container

#  - a resource can have many resources, the "final resource" of the resource is calculated inside the resource

class Container:
    def __init__(self, resources):
        self.resources = resources

    def addResource(self, resource):
        self.resources.append(resource)

    def getValues(self):
        return [r.value for i in self.resources]

    def getTotalSum(self):
        return sum(self.getValues())

    def getTotalMultiplication(self):
        return reduce(lambda x, y: x*y, self.getValues())

    def getTotalAverage(self):
        return self.getTotalSum() / len(self.resources)

class Resource:
    def __init__(self, value):
        self.value = value

class CompoundResource(Resource):
    """
    It is a type of container because it contains resources.
    """
    def __init__(self, value, resources):
        super().__init__(value)
        self.resources = resources

    def getValues(self):
        return [r.value for i in self.resources]

    def getTotalSum(self):
        return sum(self.getValues())

    def getTotalMultiplication(self):
        return reduce(lambda x, y: x*y, self.getValues())

    def getTotalAverage(self):
        return self.getTotalSum() / len(self.resources)


if __name__ == '__main__':
    r = Resource(42)
    c = Container([r])
    print(c.resources.value)
