from kivy.core.window import Window
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from maze import *

Window.clearcolor = (0.9, 0.9, 0.9, 0.9)

MazeCreated = False

class Maze(BoxLayout):
    # Maze grid can be edited using self.grid from all methods

    def generateMaze(self):
        global MazeCreated

        if (not MazeCreated):
            (MazeInChar, width, height) = self.readMazefromFile()
            self.remove_widget(self.mazeLabel)
            self.grid = GridLayout(rows = height, cols = width)
            self.add_widget(self.grid)

            for c in MazeInChar:
                if (c == '0'):
                    gridButton = Button(background_normal = '')
                    self.grid.add_widget(gridButton)
                elif (c == '1'):
                    gridButton = Button(background_normal = '', background_color = (0, 0, 0, 10))
                    self.grid.add_widget(gridButton)
                elif (c == '2'):
                    gridButton = Button(background_normal = '', background_color = (100, 50, 100, 10))
                    self.grid.add_widget(gridButton)
            MazeCreated = True

    def generateSolution(self):
        global MazeCreated

        if (MazeCreated):
            (SolutionInChar, width, height) = self.readSolutionfromFile()
            self.remove_widget(self.grid)
            self.grid = GridLayout(rows = height, cols = width)
            self.add_widget(self.grid)

            for c in SolutionInChar:
                if (c == '0'):
                    gridButton = Button(background_normal = '')
                    self.grid.add_widget(gridButton)
                elif (c == '1'):
                    gridButton = Button(background_normal = '', background_color = (0, 0, 0, 10))
                    self.grid.add_widget(gridButton)
                elif (c == '2'):
                    gridButton = Button(background_normal = '', background_color = (255, 0, 0, 10))
                    self.grid.add_widget(gridButton)
    
    def readMazefromFile(self):
        MazeInChar = []
        height = 0
        width = 0

        file = open(self.inputFile.text, "r")
        for lines in file:
            for characters in lines:
                MazeInChar.append(characters)
            height = height + 1
        width = height
        return (MazeInChar, width, height)

    def readSolutionfromFile(self):
        SolutionInChar = []
        height = 0
        width = 0

        (MazeInChar, x, y) = self.readMazefromFile()
        solve(self.inputFile.text)

        file = open("ans.txt", "r")
        for lines in file:
            for characters in lines:
                SolutionInChar.append(characters)
            height = height + 1
        width = height
        return (SolutionInChar, width, height)

    def resetMaze(self):
        global MazeCreated
        
        if (MazeCreated):
            self.remove_widget(self.grid)
            self.mazeLabel = Label(text = 'Input maze file in text box and press generate')
            self.add_widget(self.mazeLabel)
            MazeCreated = False

class MazeProblemSolver(App):
    def build (self):
        return Maze()

if __name__ == "__main__":
    MazeProblemSolver(kv_file = "MazeLayout.kv").run()
