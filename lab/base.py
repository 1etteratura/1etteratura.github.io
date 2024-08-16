
class Container:
    def __init__(self):
        self._components = {}

    def add_component(self, name, component):
        self._components[name] = component

    def get_component(self, name):
        return self._components.get(name)

    def remove_component(self, name):
        del self._components[name]

    def __iter__(self):
        return iter(self._components)

    def __len__(self):
        return len(self._components)

    def __contains__(self, name):
        return name in self._components

    def __getitem__(self, name):
        return self.get_component(name)

    def __setitem__(self, name, component):
        self.add_component(name, component)

    def __delitem__(self, name):
        self.remove_component(name)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._components})'

    def __str__(self):
        return f'{self.__class__.__name__}({list(self._components)})'

