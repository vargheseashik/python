class PyCharm:
    def start(self):
        print("started with PyCharm")
class Vscode:
    def start(self):
        print("started with Vscode")

class Django:
    def execute(self,ide):
        ide.start()


py=Vscode()
dj=Django()
dj.execute(py)