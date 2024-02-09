from convertor.ConversionCoordinator import *

converterCoordinator = ConversionCoordinator.getConversionCoordinator()
conversionResult = converterCoordinator.convert('test')
# Ça va print toujours le même truc ici, y pas vraiment de type de conversion
# C'est simplement un exemple pour montrer le squelette de l'idée
DLog.goodlog(conversionResult)