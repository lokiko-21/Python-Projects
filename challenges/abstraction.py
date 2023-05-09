from abc import ABC, abstractmethod
class computer(ABC):
    def codSize(self, size):
        print("Call of duty's full file size is: ", size)
    @abstractmethod
    def download1(self, size):
        pass


class MultiplayerDownload(computer):
    def download1(self, size):
        print("The full game's file size of {}GB with \nMultiplayer exceeds your PC's storage limit of 400GB ".format(size))


obj = MultiplayerDownload()
obj.codSize(450)
obj.download1(450)
