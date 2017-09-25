import door_io_mock
import garage

class Server:
    def __init__(self, abstract_door_io):
        self.garage = garage.Garage(abstract_door_io)
    
    def main(self):
        while True:
            input("Press enter to toggle")
            self.garage.toggle()

if __name__ == "__main__":
    server = Server(door_io_mock.Door())
    server.main()
