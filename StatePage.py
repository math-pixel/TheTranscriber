from abc import ABC, abstractmethod


class StatePage(ABC):
    def __init__(self, page):
        self.page = page

    @abstractmethod
    def showDragPage(self):
        pass
    @abstractmethod
    def showLoadingPage(self):
        pass
    @abstractmethod
    def showResultPage(self):
        pass
    




# ---------------------------------------------------------------------------- #
#                                     Drag                                     #
# ---------------------------------------------------------------------------- #
class StateDragPage(ABC):
    def __init__(self, page):
        self.page = page

    def showDragPage(self):
        pass
    
    def showLoadingPage(self):
        print("page de chaargement")
        self.page.updateState(StateLoadingPage(self.page))
    
    def showResultPage(self):
        pass



# ---------------------------------------------------------------------------- #
#                                    Loading                                   #
# ---------------------------------------------------------------------------- #
class StateLoadingPage(ABC):
    def __init__(self, page):
        self.page = page

    def showDragPage(self):
        pass
    
    def showLoadingPage(self):
        pass
    
    def showResultPage(self):
        self.page.updateState(StateResultPage(self.page))



# ---------------------------------------------------------------------------- #
#                                    Result                                    #
# ---------------------------------------------------------------------------- #
class StateResultPage(ABC):
    def __init__(self, page):
        self.page = page

    def showDragPage(self):
        pass
    
    def showLoadingPage(self):
        pass
    
    def showResultPage(self):
        pass
