import numpy as np
import networkx as nx
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.pyplot import figure
from tkinter import Frame, messagebox, Toplevel, Label, LabelFrame, Button, Canvas
matplotlib.use('TkAgg')

# The Text for the definition part of the program
Text = """Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It 
starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'), and explores 
all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. """


# Graph Drawing Class
class DrawGraph:
    def __init__(self, label, listName, listMatrix):
        self.label = label
        self.listName = listName
        self.listMatrix = listMatrix
        self.listsolution = list()

        self.pathFound = False

        self.listforedges = self.matrixtoedges(listMatrix, listName)

        matplotlib.rcParams['toolbar'] = 'None'
        self.f = figure(figsize=(5, 4), dpi=100)
        self.a = self.f.add_subplot(111)

        # networkx functionality
        if self.check_symmetric(self.listMatrix):
            self.G = nx.Graph()
        else:
            self.G = nx.DiGraph()

        nx.spring_layout(self.G)
        self.G.add_nodes_from(self.listName)
        self.G.add_edges_from(self.listforedges)
        nx.draw(self.G, with_labels=1, ax=self.a)

        # Creating the graph
        self.canvas = FigureCanvasTkAgg(self.f, master=label)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(relx=0.05, rely=0, relwidth=0.95, relheight=1)

        self.myframe = Frame(self.label, bd=0, bg="white")
        self.myframe.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.myframe)
        self.toolbar.update()
        self.canvas._tkcanvas.place(relx=0.05, rely=0, relwidth=0.95, relheight=1)

    def check_symmetric(self, list1, rtol=1e-05, atol=1e-08):
        array = np.array(list1)
        return np.allclose(array, array.T, rtol=rtol, atol=atol)

    def matrixtoedges(self, matrix, names):
        list1 = list()
        for i in range(len(names)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    list1.append((names[i], names[j]))
        return list1

    def bfs(self, startNode, endNode):
        self.pathFound = False
        visited = {node: False for node in self.G.nodes}
        queue = [startNode]
        solqueue = [startNode]
        visited[startNode] = True
        result = []
        breaking = False
        while queue:
            cur_node = queue.pop(0)
            cur_var = solqueue.pop(0)
            result.append(cur_node)
            for node in self.G.neighbors(cur_node):
                if not visited[node]:
                    queue.append(node)
                    string = cur_var + " " + node
                    solqueue.append(string)
                    visited[node] = True
                    if node == endNode:
                        breaking = True
                        break
            if breaking:
                break
        # Check if the solqueue is empty or not
        if len(solqueue) != 0:
            self.listsolution = list(solqueue[-1].split())
            if endNode == self.listsolution[-1]:
                self.pathFound = True
            else:
                messagebox.showerror("Path Error", f"There is no path between {startNode} and {endNode}")
        else:
            messagebox.showerror("Path Error", f"There is no path between {startNode} and {endNode}")

    def Solution(self, master, font, image):

        if self.pathFound:
            len1 = len(self.listsolution)
            message = ">>".join(self.listsolution)
            list1 = [[0 for i in range(len1)] for j in range(len1)]
            for i in range(len1 - 1):
                list1[i][i + 1] = 1

            color = "#FDE69F"
            window = Toplevel(master)
            window.geometry("700x500")
            window.configure(bg=color)
            # Label
            label1 = Label(window, text="Solution", bg=color, fg="#ED5C5E")
            label1['font'] = font
            label1.place(relx=0, rely=0, relwidth=1, relheight=0.1)

            label_frame1 = LabelFrame(window, bg="white", bd=0)
            label_frame1.place(relx=0.01, rely=0.11, relwidth=0.98, relheight=0.79)

            mybutton = Button(window, image=image, bg=color, activebackground=color, bd=0)
            mybutton.place(relx=0.8, rely=0.905, relheight=1 - 0.905, relwidth=0.2)
            mybutton.bind("<Button-1>", lambda event: ExitButton(event))

            labelmessage = Label(window, bg=color, text="Path : " + message, bd=0, fg="#ED5C5E")
            labelmessage['font'] = font
            labelmessage.place(relx=0.01, rely=0.905, relwidth=0.8 - 0.01, relheight=1 - 0.905)

            graph = DrawGraph(label_frame1, self.listsolution, list1)

            def ExitButton(event):
                window.destroy()

            window.mainloop()


class PathFindingBfs:
    def __init__(self, myCanvas: Canvas, columns: int, rows: int, width: float, height: float):
        self.Canvas = myCanvas
        self.columns = columns
        self.rows = rows
        self.width = width
        self.height = height
        self.operation = 0

        self.dr = [-1, 1, 0, 0]
        self.dc = [0, 0, 1, -1]
        self.rq = []  # Row Queue
        self.cq = []  # Column Queue
        self.queue = []  # Containing the path
        self.visited = list()  # Visited Matrix
        self.reached = False  # To check if we get to the destination
        self.move_count = 0
        self.nodes_left_in_layer = 1
        self.nodes_in_next_layer = 0
        self.secondarylist = list()

        self.columnwidth = float(self.width / self.columns)
        self.rowheight = float(self.height / self.rows)
        self.isstartselected = False
        self.isendselected = False
        self.startid = 0
        self.endid = 0
        self.barrierlist = list()
        self.operationlist = list()

        self.canvas = Canvas(self.Canvas, height=self.height, width=self.width,
                             bg="#FDE69F")  # Canvas within the canvas
        self.canvas1 = self.Canvas.create_window(0, 0, anchor="nw", window=self.canvas)

        for i in range(self.rows):
            for j in range(self.columns):
                self.x = self.canvas.create_rectangle(0 + j * self.columnwidth, 0 + i * self.rowheight,
                                                      self.columnwidth + j * self.columnwidth,
                                                      self.rowheight + i * self.rowheight)

        # Responsible for choosing the start and end point
        self.canvas.bind("<Double-Button-1>", lambda event: self.start(event))
        # Responsible for Adding Barriers
        self.canvas.bind("<B1-Motion>", lambda event: self.motion(event))
        # Responsible
        self.canvas.bind("<B3-Motion>", lambda event: self.removemotion(event))

    def clear(self):
        # Empty Out the stored variables
        self.rq = []
        self.cq = []
        self.queue = []
        self.reached = False
        self.move_count = 0
        self.nodes_left_in_layer = 1
        self.nodes_in_next_layer = 0
        self.operation = 0
        self.isstartselected = False
        self.isendselected = False
        self.barrierlist = []
        self.startid = 0
        self.endid = 0
        self.operationlist = list()

        for i in range(self.rows):
            for j in range(self.columns):
                id = self.getwidgetid(i, j)
                self.canvas.itemconfig(id, fill="#FDE69F")

    def start(self, event):
        x = event.widget.find_closest(event.x, event.y)  # id of the widget
        if not self.isstartselected:
            self.canvas.itemconfig(x, fill="yellow")
            self.isstartselected = True
            self.startid = x[0]
        elif not self.isendselected:
            self.canvas.itemconfig(x, fill="green")
            self.isendselected = True
            self.endid = x[0]
        elif x[0] == self.startid:
            self.canvas.itemconfig(x, fill="#FDE69F")
            self.isstartselected = False
            self.startid = 0
        elif x[0] == self.endid:
            self.canvas.itemconfig(x, fill="#FDE69F")
            self.isendselected = False
            self.endid = 0

    def motion(self, event):
        if self.isstartselected and self.isendselected:
            x = event.widget.find_closest(event.x, event.y)
            if x[0] not in self.barrierlist and x[0] != self.startid and x[0] != self.endid:
                self.canvas.itemconfig(x, fill="black")
                self.barrierlist.append(x[0])

    def removemotion(self, event):
        x = event.widget.find_closest(event.x, event.y)
        if x[0] in self.barrierlist:
            self.canvas.itemconfigure(x, fill="#FDE69F")
            self.barrierlist.remove(x[0])

    def getlistcoordinates(self, number):
        if not (number % self.columns == 0):
            row = number // self.columns
            column = number % self.columns - 1
        else:
            column = self.columns - 1
            row = (number - 1) // self.columns

        return int(row), int(column)

    def getwidgetid(self, row, column):
        return row * self.columns + column + 1

    def bfs(self, event):
        if self.isstartselected and self.isstartselected:
            # empty the list so that we operate after we make modification
            self.operationlist = [["" for i in range(self.columns)] for j in range(self.rows)]
            # adding the start path
            i, j = self.getlistcoordinates(self.startid)
            self.operationlist[i][j] = "S"
            k, l = self.getlistcoordinates(self.endid)
            self.operationlist[k][l] = "E"
            for i in self.barrierlist:
                n, m = self.getlistcoordinates(i)
                self.operationlist[n][m] = "#"
            i, j = self.getlistcoordinates(self.startid)
            self.Solve(i, j)

    def explore_neighbors(self, r: int, c: int):
        list1 = list()
        for i in range(4):
            rr = r + self.dr[i]
            cc = c + self.dc[i]
            # Skipping the wrong choices
            if rr < 0 or cc < 0:
                continue
            if rr >= self.rows or cc >= self.columns:
                continue
            # Skipping visited locations or blocked cells
            if self.visited[rr][cc]:
                continue
            if self.operationlist[rr][cc] == "#":
                continue
            list1.append(i)
            self.VisitedColor(rr, cc)
            self.operation += 1
            self.rq.append(rr)
            self.cq.append(cc)
            self.visited[rr][cc] = True
            self.nodes_in_next_layer += 1
        # Tracking The Path Of the Solution Part

        if len(list1) != 0:
            path = self.queue.pop(0)
            for i in range(len(list1)):
                if list1[i] == 0:
                    string = path + "U"
                    self.queue.append(string)
                elif list1[i] == 1:
                    string = path + "D"
                    self.queue.append(string)
                elif list1[i] == 2:
                    string = path + "R"
                    self.queue.append(string)
                elif list1[i] == 3:
                    string = path + "L"
                    self.queue.append(string)
        else:
            self.queue.pop(0)

    def Solve(self, sr: int, sc: int):
        self.visited = [[False for i in range(self.columns)] for j in range(self.rows)]
        self.rq.append(sr)
        self.cq.append(sc)
        self.queue.append("")
        self.visited[sr][sc] = True
        while len(self.rq) > 0:  # or self.cq because we add and remove items in the same time
            r = self.rq.pop(0)
            c = self.cq.pop(0)
            if self.operationlist[r][c] == "E":
                self.reached = True
                break
            self.explore_neighbors(r, c)
            self.nodes_left_in_layer -= 1
            if self.nodes_left_in_layer == 0:
                self.nodes_left_in_layer = self.nodes_in_next_layer
                self.nodes_in_next_layer = 0
                self.move_count += 1
        if self.reached:
            k, l = self.getlistcoordinates(self.endid)
            self.backtracking(self.queue[0], k, l)
            text = f"The Shortest Path is {self.move_count} blocks away\nAnd The cells visited are: " \
                   f"{self.operation} ({int((self.operation / (self.columns * self.rows)) * 100)}%)"
            messagebox.showinfo("Solution Details", text)
            return self.move_count
        messagebox.showerror("PathError", "Path Not Found")
        return -1

    def backtracking(self, path: str, r: int, c: int):
        self.ValidateColorSolution(r, c)
        for move in path[-1::-1]:
            if move == "D":
                r -= 1
                self.ValidateColorSolution(r, c)
            elif move == "U":
                r += 1
                self.ValidateColorSolution(r, c)
            elif move == "R":
                c -= 1
                self.ValidateColorSolution(r, c)
            elif move == "L":
                c += 1
                self.ValidateColorSolution(r, c)

    def ValidateColorSolution(self, i: int, j: int):
        id = self.getwidgetid(i, j)
        self.canvas.itemconfig(id, fill="#FCA85A")
        self.canvas.update()
        self.canvas.after(100)

    def VisitedColor(self, i: int, j: int):
        id = self.getwidgetid(i, j)
        self.canvas.itemconfigure(id, fill="red")
        self.canvas.update()

    def delete(self):
        self.clear()
        self.Canvas.delete(self.canvas1)
        self.canvas.destroy()
