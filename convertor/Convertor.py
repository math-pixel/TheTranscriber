
# Ici on s'inspire du design pattern Strategy :
# https://refactoring.guru/fr/design-patterns/strategy
class Convertor:
    def __init__(self):
        self.convertStrategy = None
        pass

    def setConvertStrategy(self, convertStrategy):
        self.convertStrategy = convertStrategy
        pass

    def convert(self, path):
        return self.convertStrategy.executeConversion(path)