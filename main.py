from tkinter import *
import tkinter.font as font
from functions import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import string
from tkinter.ttk import Separator, Style


# Main Application Class
class BreadthFirstSearch:

    def __init__(self, master):
        self.master = master
        master.geometry("900x550")
        master.title("Breadth First Search")
        master.configure(bg="white")
        master.iconbitmap("images/bfs-icon.ico")

        # Fonts
        font1 = font.Font(family='Helvetica', size=10, weight='bold')
        font2 = font.Font(family="Times", size=10, slant="italic", weight='bold')
        font3 = font.Font(family="Komika", size=10, slant="italic", weight='bold')
        # Color
        self.color_menu = "#FCA85A"
        self.color_main_content = "#FDE69F"
        self.color_red = "#ED5C5E"
        # Instances
        self.alphabets = list(string.ascii_uppercase + string.ascii_lowercase)
        self.optionButton = False
        self.optionInput = 0
        self.isFileRead = False
        self.isFileSelected = False
        self.listOfFile = list()
        self.filepath = ""
        self.numVertices = 0  # Default at Runtime is 0
        self.column = 0
        self.row = 0
        self.isMatrixValide = True  # To check whether the matrix contains only 1 and 0
        self.NameVertices = list()  # Names Of Vertices
        self.NameVerticesIndex = 0
        self.isNameOk = False
        self.isMatrixOk = False
        self.start = ""
        self.end = ""

        # Images
        self.QuestionImage = PhotoImage(file="images/problem-solving.png")
        self.InputImage = PhotoImage(file="images/input.png")
        self.ChoiceImage = PhotoImage(file="images/choose.png")
        self.ProcessingImage = PhotoImage(file="images/planning.png")
        self.IntroductionImage = PhotoImage(file="images/large.png")
        self.GraphImage = PhotoImage(file="images/graph.png")
        self.UploadImage = PhotoImage(file="images/upload.png")
        self.PathFindingImage = PhotoImage(file="images/road-map.png")
        self.RunImage = PhotoImage(file="images/button_run.png")
        self.ClearImage = PhotoImage(file="images/button_clear.png")

        self.ButtonStart = PhotoImage(file="images/button_start.png")
        self.ButtonValidate = PhotoImage(file="images/button_validate.png")
        self.ButtonOpenFile = PhotoImage(file="images/button_open-file.png")
        self.ButtonReadFile = PhotoImage(file="images/button_read-file.png")
        self.ButtonBack = PhotoImage(file="images/button_back.png")
        self.ButtonNext = PhotoImage(file="images/button_next.png")
        self.ButtonRunAlgorithm = PhotoImage(file="images/button_run-algorithm.png")
        self.ButtonExit = PhotoImage(file="images/button_exit.png")
        self.ButtonReset = PhotoImage(file="images/button_reset.png")

        ## Declaring Frames

        self.frameLeft = Frame(master, bg=self.color_menu)
        self.frameLeft.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        self.frameRight = Frame(master, bg=self.color_main_content)
        self.frameRight.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        # self.frameRight.place_forget()

        self.frameRight1 = Frame(master, bg=self.color_main_content)
        self.frameRight1.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.frameRight1.place_forget()

        self.frameRight2 = Frame(master, bg=self.color_main_content)
        self.frameRight2.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.frameRight2.place_forget()

        self.frameRight4 = Frame(master, bg=self.color_main_content)
        self.frameRight4.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.frameRight4.place_forget()

        self.frameRight3 = Frame(master, bg=self.color_main_content)
        self.frameRight3.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.frameRight3.place_forget()

        self.frameRight4 = Frame(master, bg=self.color_main_content)
        self.frameRight4.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.frameRight4.place_forget()

        ## Putting the menu of the program on the leftframe

        # Question Button
        self.questionButton = MyMenu(self.frameLeft, 0, 0, 1, 0.25, self.color_main_content, self.QuestionImage)
        # Input Button
        self.inputButton = MyMenu(self.frameLeft, 0, 0.25, 1, 0.25, self.color_menu, self.InputImage)
        # Choice Button
        self.choiceButton = MyMenu(self.frameLeft, 0, 0.5, 1, 0.25, self.color_menu, self.ChoiceImage)
        # Processing Button
        self.processingButton = MyMenu(self.frameLeft, 0, 0.75, 1, 0.25, self.color_menu, self.ProcessingImage)

        ## Starting working on the main content => frameRight

        text_intro = "What is Breadth First Search Algorithm ?"
        self.introLabel = LabelFrame(self.frameRight, bg=self.color_main_content, fg=self.color_red, text=text_intro,
                                     bd=0)
        self.introLabel['font'] = font1
        self.introLabel.place(relx=0.01, rely=0.2, relwidth=0.95, relheight=0.45)

        self.textLabel = Label(self.introLabel, text=Text, justify=LEFT, wraplength=180, image=self.IntroductionImage,
                               compound=LEFT, padx=10, bg=self.color_main_content, fg=self.color_red)
        self.textLabel.place(relx=0, rely=0)
        self.textLabel['font'] = font2

        # Button Start

        self.startButton = MyButton(self.frameRight, 0.8, 0.85, 0.2, 0.15, self.color_main_content, self.ButtonStart,
                                    lambda event: self.NextPage(event, self.frameRight, self.frameRight1,
                                                                self.questionButton, self.inputButton))

        ## Starting working on the main content => frameRight1
        text_choice_label = "What is your choice ?"
        self.choicesLabel = LabelFrame(self.frameRight1, bg=self.color_main_content, fg=self.color_red,
                                       text=text_choice_label,
                                       bd=0)
        self.choicesLabel['font'] = font1
        self.choicesLabel.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)

        self.separator1 = Separator(self.frameRight1, orient="horizontal")
        self.separator1.place(relx=0.1, rely=0.25, relheight=0.002, relwidth=0.8)

        self.separator2 = Separator(self.frameRight1, orient="vertical")
        self.separator2.place(relx=0.9, rely=0.1, relheight=0.15, relwidth=0.002)

        self.var1 = IntVar()
        text_choice1 = "PathFinding Problem"
        text_choice2 = "Graph"

        self.optionMenu1 = Radiobutton(self.choicesLabel, text=text_choice1, variable=self.var1, value=1,
                                       bg=self.color_main_content,
                                       activebackground=self.color_main_content)
        self.optionMenu1['font'] = font3
        self.optionMenu1.place(relx=0.07, rely=0)

        self.optionMenu2 = Radiobutton(self.choicesLabel, text=text_choice2, variable=self.var1, value=2,
                                       bg=self.color_main_content,
                                       activebackground=self.color_main_content)
        self.optionMenu2['font'] = font3
        self.optionMenu2.place(relx=0.07, rely=0.3)

        # Pathfinding Section #
        # Section of Pathfinding  Import => self.optionInput = 1

        self.pathLabel = LabelFrame(self.frameRight1, bg=self.color_main_content, fg=self.color_red, bd=0)
        self.pathLabel.place(relx=0.1, rely=0.31, relheight=0.6, relwidth=0.8)
        self.pathLabel.place_forget()

        self.choicesLabelImage1 = Label(self.pathLabel, image=self.PathFindingImage, compound=LEFT,
                                        bg=self.color_main_content)
        self.choicesLabelImage1.place(relx=0, rely=0.1, relwidth=0.3)

        self.choicesLabel2 = Label(self.pathLabel, bg=self.color_main_content, bd=0)
        self.choicesLabel2.place(relx=0.31, rely=0, relwidth=0.69, relheight=1)

        # Entries for the Pathfinding option:

        self.numberOfColumns = Label(self.choicesLabel2, text="The Number of columns ", bg=self.color_main_content,
                                     anchor=W,
                                     fg=self.color_red)
        self.numberOfColumns.place(relx=0.02, rely=0.05, relwidth=0.95, relheight=0.1)
        self.numberOfColumns['font'] = font3

        self.columntext = "Enter the number of columns ( example: 16 ) "
        self.numberOfColumnsEntry = MyEntry(self.choicesLabel2, 0.02, 0.15, 0.95, 0.1, self.color_main_content, "black",
                                            font2, self.columntext)

        self.numberOfRows = Label(self.choicesLabel2, text="The Number of rows ", bg=self.color_main_content, anchor=W,
                                  fg=self.color_red)
        self.numberOfRows.place(relx=0.02, rely=0.3, relwidth=0.95, relheight=0.1)
        self.numberOfRows['font'] = font3

        self.rowtext = "Enter the number of rows ( example: 10 ) "
        self.numberOfRowsEntry = MyEntry(self.choicesLabel2, 0.02, 0.4, 0.95, 0.1, self.color_main_content, "black",
                                         font2, self.rowtext)

        # Adding the validate Button

        self.validateButton = MyButton(self.pathLabel, 0.55, 0.75, 0.2, 0.2, self.color_main_content,
                                       self.ButtonValidate, self.validatePath)

        # Validation text

        self.validatepathText = Label(self.choicesLabel2, text="", bg=self.color_main_content, fg=self.color_red)
        self.validatepathText.place(relx=0.02, rely=0.53, relwidth=0.8, relheight=0.2)
        self.validatepathText['font'] = font2

        # Adding the commands for radio Button

        self.optionMenu1.configure(command=lambda num=1: self.inputChoice(num))
        self.optionMenu2.configure(command=lambda num=2: self.inputChoice(num))

        # Graph Section #

        self.graphLabel = LabelFrame(self.frameRight1, bg=self.color_main_content, fg=self.color_red, bd=0)
        self.graphLabel.place(relx=0.1, rely=0.3, relheight=0.9, relwidth=0.8)
        self.graphLabel.place_forget()
        text_choice_graph = "What is The type of Entry ?"
        self.graphTextLabel = Label(self.graphLabel, text=text_choice_graph, bg=self.color_main_content,
                                    fg=self.color_red,
                                    anchor=W)
        self.graphTextLabel.place(relx=0, rely=0, relwidth=0.8, relheight=0.05)
        self.graphTextLabel['font'] = font1

        # Option type Entry for graph
        text_choice_graph1 = "Number of Vertices"
        text_choice_graph2 = "File Entry (Matrix)"
        self.var2 = IntVar()
        self.optionGraphType1 = Radiobutton(self.graphLabel, text=text_choice_graph1, variable=self.var2, value=1,
                                            bg=self.color_main_content, activebackground=self.color_main_content)
        self.optionGraphType1.place(relx=0.05, rely=0.07, relheight=0.05)
        self.optionGraphType1['font'] = font2

        self.optionGraphType2 = Radiobutton(self.graphLabel, text=text_choice_graph2, variable=self.var2, value=2,
                                            bg=self.color_main_content, activebackground=self.color_main_content)
        self.optionGraphType2.place(relx=0.05, rely=0.15, relheight=0.05)
        self.optionGraphType2['font'] = font2

        self.optionGraphType1.configure(command=lambda num=1: self.graphChoice(num))
        self.optionGraphType2.configure(command=lambda num=2: self.graphChoice(num))

        self.graphLabelImage1 = Label(self.graphLabel, image=self.GraphImage, compound=LEFT,
                                      bg=self.color_main_content)
        self.graphLabelImage1.place(relx=0, rely=0.3, relwidth=0.3)
        self.graphLabelImage1.place_forget()
        self.graphLabelImage2 = Label(self.graphLabel, image=self.UploadImage, compound=LEFT,
                                      bg=self.color_main_content)
        self.graphLabelImage2.place(relx=0, rely=0.3, relwidth=0.3)
        self.graphLabelImage2.place_forget()

        self.graphLabel2 = Label(self.graphLabel, bg=self.color_main_content, bd=0)
        self.graphLabel2.place(relx=0.31, rely=0.3, relwidth=0.69, relheight=1)
        self.graphLabel2.place_forget()

        self.graphLabel3 = Label(self.graphLabel, bg=self.color_main_content, bd=0)
        self.graphLabel3.place(relx=0.31, rely=0.3, relwidth=0.69, relheight=1)
        self.graphLabel3.place_forget()
        # Entry for the graph option:
        # Section of vertices Import => self.optionInput = 2
        self.numberOfVertices = Label(self.graphLabel2, text="The Number of vertices ", bg=self.color_main_content,
                                      anchor=W,
                                      fg=self.color_red)
        self.numberOfVertices.place(relx=0.02, rely=0.05, relwidth=0.95, relheight=0.1)
        self.numberOfVertices['font'] = font3

        self.numVertivesEntryText = "Enter the number of vertices ( example: 10 ) "
        self.numberOfVerticesEntry = MyEntry(self.graphLabel2, 0.02, 0.15, 0.95, 0.1, self.color_main_content, "black",
                                             font2, self.numVertivesEntryText)

        self.validateVerticesButton = MyButton(self.graphLabel2, 0.3, 0.3, 0.3, 0.12, self.color_main_content,
                                               self.ButtonValidate, self.validateVertices)

        self.validateVerticesButtonMessage = Label(self.graphLabel2, text="", bg=self.color_main_content,
                                                   fg=self.color_red)
        self.validateVerticesButtonMessage.place(relx=0.3, rely=0.5, relheight=0.1, relwidth=0.3)
        self.validateVerticesButtonMessage['font'] = font2

        # Section of Matrix Import => self.optionInput = 3
        self.tipText = "Tip: Matrix row should look like: 1 0 1 0 0 1"
        self.tiptext = Label(self.graphLabel3, text=self.tipText, bg=self.color_main_content, fg=self.color_red)
        self.tiptext.place(relx=0, rely=0.04, relheight=0.1, relwidth=1)
        self.tiptext['font'] = font1

        self.titleOfFile = Label(self.graphLabel3, text="No Path Selected..", bg=self.color_main_content)
        self.titleOfFile.place(relx=0.02, rely=0.15, relwidth=0.95, relheight=0.1)
        self.titleOfFile['font'] = font3
        self.openFileButton = MyButton(self.graphLabel3, 0.13, 0.27, 0.3, 0.15, self.color_main_content,
                                       self.ButtonOpenFile, self.OpenFile)

        self.readFileButton = MyButton(self.graphLabel3, 0.55, 0.27, 0.3, 0.17, self.color_main_content,
                                       self.ButtonReadFile,
                                       self.ReadFile)

        self.readMessage = Label(self.graphLabel3, text="", bg=self.color_main_content, fg=self.color_red,
                                 justify=CENTER)
        self.readMessage.place(relx=0.1, rely=0.45, relheight=0.06, relwidth=0.75)
        self.readMessage['font'] = font2

        # Adding the next Button to frameRight1

        self.inputNextButton = MyButton(self.frameRight1, 0.88, 0.9, 0.12, 0.1, self.color_main_content,
                                        self.ButtonNext,
                                        self.InputNext)
        self.inputNextButton.place_forget()

        # Adding The Back Button to frameRight1

        self.inputBackButton = MyButton(self.frameRight1, 0.02, 0.9, 0.1, 0.1, self.color_main_content, self.ButtonBack,
                                        self.InputBack)

        ## Starting working on the main content => frameRight2

        text_name_choice = "Type of vertices name"
        self.nameVerticeOptionLabel = LabelFrame(self.frameRight2, bg=self.color_main_content, fg=self.color_red,
                                                 text=text_name_choice,
                                                 bd=0)
        self.nameVerticeOptionLabel['font'] = font2
        self.nameVerticeOptionLabel.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.15)
        self.var3 = IntVar()
        text_name_option1 = "Numerical"
        text_name_option2 = "Alphabetical"
        text_name_option3 = "Customizable"
        self.optionNameMenu1 = Radiobutton(self.nameVerticeOptionLabel, bg=self.color_main_content, variable=self.var3,
                                           value=1, activebackground=self.color_main_content, text=text_name_option1,
                                           anchor=W)
        self.optionNameMenu1['font'] = font3
        self.optionNameMenu1.place(relx=0.05, rely=0.05, relheight=0.22, relwidth=0.4)

        self.optionNameMenu2 = Radiobutton(self.nameVerticeOptionLabel, bg=self.color_main_content, variable=self.var3,
                                           value=2, activebackground=self.color_main_content, text=text_name_option2,
                                           anchor=W)
        self.optionNameMenu2['font'] = font3
        self.optionNameMenu2.place(relx=0.05, rely=0.35, relheight=0.22, relwidth=0.4)

        self.optionNameMenu3 = Radiobutton(self.nameVerticeOptionLabel, bg=self.color_main_content, variable=self.var3,
                                           value=3, activebackground=self.color_main_content, text=text_name_option3,
                                           anchor=W)
        self.optionNameMenu3['font'] = font3
        self.optionNameMenu3.place(relx=0.05, rely=0.65, relheight=0.22, relwidth=0.4)

        # command of the option menu

        self.optionNameMenu1.configure(command=lambda num=1: self.nameOption(num))
        self.optionNameMenu2.configure(command=lambda num=2: self.nameOption(num))
        self.optionNameMenu3.configure(command=lambda num=3: self.nameOption(num))

        # Name for customizable option

        self.customizableNameOption = LabelFrame(self.frameRight2, bd=0, bg=self.color_main_content, text="")
        self.customizableNameOption.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.55)
        self.customizableNameOption.place_forget()

        text_name = "The name of Vertices"
        self.labelName = Label(self.customizableNameOption, text=text_name, bg=self.color_main_content,
                               fg=self.color_red,
                               anchor=W)
        self.labelName.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.1)
        self.labelName['font'] = font1

        self.text_name_entry = "Enter the name of the Vertices separated by ',' (Max 2 characters by vertex)"

        self.labelNameEntry = MyEntry(self.customizableNameOption, 0.1, 0.1, 0.8, 0.15, self.color_main_content,
                                      "black",
                                      font2, self.text_name_entry)

        self.labelNameMessage = Label(self.customizableNameOption, text="", bg=self.color_main_content,
                                      fg=self.color_red)
        self.labelNameMessage.place(relx=0.1, rely=0.27, relheight=0.13, relwidth=0.5)

        self.validateNameVerticesButton = MyButton(self.customizableNameOption, 0.7, 0.27, 0.2, 0.15,
                                                   self.color_main_content,
                                                   self.ButtonValidate, self.validateCustomizableName)

        self.matrixOfGraphLabel1 = LabelFrame(self.customizableNameOption, bg=self.color_main_content, bd=0)
        self.matrixOfGraphLabel1.place(relx=0.1, rely=0.42, relheight=0.55, relwidth=0.8)

        # Creating The label that contains the text

        self.matrixLabel1 = Label(self.matrixOfGraphLabel1, text="Matrix Entry", bg=self.color_main_content,
                                  fg=self.color_red,
                                  bd=0, anchor=W)
        self.matrixLabel1.place(relx=0, rely=0.05, relheight=0.1, relwidth=0.8)
        self.matrixLabel1['font'] = font1

        self.text_matrix_1 = "Please Enter matrix separated by ','(example: 0010,1101,0101,1111 => 4*4 matrix)"

        self.matrixEntry1 = MyEntry(self.matrixOfGraphLabel1, 0, 0.16, 1, 0.15, self.color_main_content, "black",
                                    font.Font(family="Times", size=9, slant="italic", weight='bold'),
                                    self.text_matrix_1)

        self.validateMatrixMessage1 = Label(self.matrixOfGraphLabel1, bg=self.color_main_content, text="",
                                            fg=self.color_red)
        self.validateMatrixMessage1['font'] = font3
        self.validateMatrixMessage1.place(relx=0, rely=0.37, relheight=0.22, relwidth=0.7)

        self.validateMatrixEntry1 = MyButton(self.matrixOfGraphLabel1, 0.75, 0.35, 0.25, 0.25, self.color_main_content,
                                             self.ButtonValidate,
                                             lambda event: self.validateCustomizableMatrix(event, self.matrixEntry1,
                                                                                           self.validateMatrixMessage1))

        # validation message

        # Starting the code the normal form Name here is Numerical or Alphabetical

        self.matrixOfGraphLabel = LabelFrame(self.frameRight2, bg=self.color_main_content, text="", bd=0)
        self.matrixOfGraphLabel.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.3)
        self.matrixOfGraphLabel.place_forget()

        self.matrixLabel = Label(self.matrixOfGraphLabel, text="Matrix Entry", bg=self.color_main_content,
                                 fg=self.color_red,
                                 bd=0, anchor=W)
        self.matrixLabel.place(relx=0, rely=0.05, relheight=0.1, relwidth=0.8)
        self.matrixLabel['font'] = font1

        #self.text_matrix_1 = "Please Enter matrix separated by ','(example: 0010,1101,0101,1111 => 4*4 matrix)"
        self.matrixEntry = MyEntry(self.matrixOfGraphLabel, 0, 0.18, 1, 0.22, self.color_main_content, "black",
                                   font.Font(family="Times", size=9, slant="italic", weight='bold'), self.text_matrix_1)

        self.validateMatrixMessage = Label(self.matrixOfGraphLabel, bg=self.color_main_content, text="",
                                           fg=self.color_red)
        self.validateMatrixMessage['font'] = font3
        self.validateMatrixMessage.place(relx=0, rely=0.52, relheight=0.22, relwidth=0.7)

        self.validateMatrixEntry = MyButton(self.matrixOfGraphLabel, 0.75, 0.5, 0.25, 0.25, self.color_main_content,
                                            self.ButtonValidate,
                                            lambda event: self.validateCustomizableMatrix(event, self.matrixEntry,
                                                                                          self.validateMatrixMessage))

        # Button of after and back
        self.optionBackButton = MyButton(self.frameRight2, 0.02, 0.9, 0.1, 0.1, self.color_main_content,
                                         self.ButtonBack, self.OptionBack)

        self.optionNextButton = MyButton(self.frameRight2, 0.85, 0.9, 0.15, 0.1, self.color_main_content,
                                         self.ButtonNext, self.OptionNext)
        self.optionNextButton.place_forget()

        ## Starting working on the main content => frameRight3

        # Creating graph container
        self.drawGraphLabel = LabelFrame(self.frameRight3, bd=0, bg=self.color_main_content, text="")
        self.drawGraphLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        # frame graph content

        self.drawgraphtextlabel = Label(self.drawGraphLabel, bg=self.color_main_content, text="Graph Representation",
                                        fg=self.color_red)
        self.drawgraphtextlabel.place(relx=0.05, rely=0, relheight=0.05, relwidth=0.9)
        self.drawgraphtextlabel['font'] = font1

        self.drawGraphContainer = LabelFrame(self.drawGraphLabel, bg="white", bd=0)
        self.drawGraphContainer.place(relx=0.05, rely=0.06, relwidth=0.9, relheight=0.75)

        self.GraphAlgorithmOptionLabel = LabelFrame(self.drawGraphLabel, bg=self.color_main_content, text="", bd=0)
        self.GraphAlgorithmOptionLabel.place(relx=0.05, rely=0.81, relheight=0.11, relwidth=0.9)

        self.textEntry1 = "Enter the Starting Vertex"
        self.GraphAlgorithmEntry1 = MyEntry(self.GraphAlgorithmOptionLabel, 0.05, 0.25, 0.3, 0.4,
                                            self.color_main_content,
                                            self.color_red, font2, self.textEntry1)
        self.textEntry2 = "Enter the Ending Vertex"
        self.GraphAlgorithmEntry2 = MyEntry(self.GraphAlgorithmOptionLabel, 0.36, 0.25, 0.3, 0.4,
                                            self.color_main_content,
                                            self.color_red, font2, self.textEntry2)

        self.GraphAlgorithmButton = MyButton(self.GraphAlgorithmOptionLabel, 0.73, 0.17, 0.27, 0.6,
                                             self.color_main_content,
                                             self.ButtonRunAlgorithm,
                                             self.validateAlgoPar)
        # after and back buttons

        self.processingBackButton = MyButton(self.frameRight3, 0.02, 0.923, 0.1, 0.077, self.color_main_content,
                                             self.ButtonBack, self.ProcessingBack)

        self.processingExitButton = MyButton(self.frameRight3, 0.84, 0.92, 0.15, 0.08, self.color_main_content,
                                             self.ButtonExit, self.Exit)
        self.GraphResetButton = MyButton(self.frameRight3, 0.45, 0.908, 0.12, 1-0.908, self.color_main_content,
                                        self.ButtonReset,
                                        lambda event, frame=self.frameRight3, btn=self.processingButton, type="Graph":
                                        self.reset(event, frame, btn, type))
        ## Starting working on the main content => frameRight3

        # Creating PathFinding container
        self.drawPathLabel = LabelFrame(self.frameRight4, bd=0, bg=self.color_main_content, text="")
        self.drawPathLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Pathfinding content
        self.pathTextLabel = Label(self.drawPathLabel, bg=self.color_main_content, text="The Pathfinding Problem",
                                   fg=self.color_red)
        self.pathTextLabel.place(relx=0.025, rely=0, relheight=0.08, relwidth=0.73)
        self.pathTextLabel['font'] = font2

        self.pathCanvas = Canvas(self.drawPathLabel, bg=self.color_main_content, width=525, height=450, bd=0,
                                 highlightthickness=1)
        self.pathCanvas.place(relx=0.025, rely=0.085)

        self.runButton = MyButton(self.drawPathLabel, 0.825, 0.2, 0.1, 0.1, self.color_main_content, self.RunImage,
                                  lambda event: self.runPath(event))

        self.clearButton = MyButton(self.drawPathLabel, 0.82, 0.4, 0.12, 0.1, self.color_main_content, self.ClearImage,
                                    lambda event: self.clearPath(event))
        self.clearButton.disable()

        self.pathBackButton = MyButton(self.frameRight4, 0.02, 0.923, 0.1, 0.077, self.color_main_content,
                                       self.ButtonBack,
                                       lambda event: self.pathBack(event))

        self.pathExitButton = MyButton(self.frameRight4, 0.85, 0.923, 0.12, 1 - 0.923, self.color_main_content,
                                       self.ButtonExit, self.Exit)
        self.pathResetButton = MyButton(self.frameRight4, 0.45, 0.908, 0.12, 1-0.908, self.color_main_content,
                                        self.ButtonReset,
                                        lambda event, frame=self.frameRight4, btn=self.processingButton, type="Path":
                                        self.reset(event, frame, btn, type))

    def NextPage(self, event, first_frame, second_frame, btn1, btn2):
        first_frame.place_forget()
        second_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        btn1.ChangeBackgroundColor(self.color_menu)
        btn2.ChangeBackgroundColor(self.color_main_content)

    def BackPage(self, event, first_frame, second_frame, btn1, btn2):
        first_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        second_frame.place_forget()
        btn2.ChangeBackgroundColor(self.color_menu)
        btn1.ChangeBackgroundColor(self.color_main_content)

    # Methods  of the Input Page

    def inputChoice(self, num):
        self.inputNextButton.place_forget()
        if num == 1:
            self.graphLabel.place_forget()
            self.pathLabel.place(relx=0.1, rely=0.31, relheight=0.6, relwidth=0.8)
            self.optionInput = 1
        else:
            self.pathLabel.place_forget()
            self.graphLabel.place(relx=0.1, rely=0.31, relheight=0.6, relwidth=0.8)

    def validatePath(self, event):
        try:
            self.column = int(self.numberOfColumnsEntry.get())
            self.row = int(self.numberOfRowsEntry.get())
            text1 = f"Validation complete: \nColumn = {self.column} \nRow = {self.row}"
            self.optionButton = True
            self.validatepathText.configure(text=text1)
            self.inputNextButton.show()
        except ValueError:
            self.optionButton = False
            self.validatepathText.configure(text="")
            messagebox.showerror("Error", "Please Enter A Valid Integer Number")

    def graphChoice(self, num):
        self.inputNextButton.place_forget()
        self.isMatrixOk = False
        if num == 1:
            self.matrixOfGraphLabel1.place(relx=0.1, rely=0.42, relheight=0.55, relwidth=0.8)
            self.matrixLabel.place(relx=0, rely=0.05, relheight=0.1, relwidth=0.8)
            self.matrixEntry.show()
            self.validateMatrixMessage.place(relx=0, rely=0.52, relheight=0.22, relwidth=0.7)
            self.validateMatrixEntry.show()
            self.graphLabelImage1.place(relx=0, rely=0.3, relwidth=0.3)
            self.graphLabel2.place(relx=0.31, rely=0.3, relwidth=0.69, relheight=1)
            self.graphLabelImage2.place_forget()
            self.graphLabel3.place_forget()
            self.optionInput = 2
        else:
            self.graphLabelImage2.place(relx=0, rely=0.3, relwidth=0.3)
            self.graphLabel3.place(relx=0.31, rely=0.3, relwidth=0.69, relheight=1)
            self.graphLabelImage1.place_forget()
            self.graphLabel2.place_forget()
            self.optionInput = 3
            self.matrixOfGraphLabel1.place_forget()
            self.matrixLabel.place_forget()
            self.matrixEntry.place_forget()
            self.validateMatrixMessage.place_forget()
            self.validateMatrixEntry.place_forget()

    def validateVertices(self, event):
        try:
            self.numVertices = int(self.numberOfVerticesEntry.get())
            text = f"Value : {self.numVertices}"
            self.validateVerticesButtonMessage.configure(text=text)
            self.inputNextButton.show()

        except ValueError:
            messagebox.showerror("Error", "Please Enter A Valid Integer Number")
            self.validateVerticesButtonMessage.configure(text="")

    def OpenFile(self, event):
        self.filepath = askopenfilename(initialdir="/", title="Select A File",
                                        filetypes=(("text files", "*.txt"), ('All files', '*.*')))
        if self.filepath != "":
            self.titleOfFile.configure(text=self.filepath)
            self.isFileSelected = True
            self.isFileRead = False
        else:
            self.isFileSelected = False
            self.isFileRead = False

    def squaredMatrix(self, matrix):
        return all(len(row) == len(matrix) for row in matrix)

    def ReadFile(self, event):
        self.listOfFile = list()  # Make sure that the fonction works correctly
        self.isMatrixValide = True  # edit to initial value important!
        if self.isFileSelected and (".txt" in self.filepath):
            with open(self.filepath, "r") as f:
                try:
                    li = [i for i in f.readlines()]
                    self.listOfFile = [[int(i) for i in li[j].split()] for j in range(len(li))]
                    for i in range(len(self.listOfFile)):
                        for j in range(len(self.listOfFile[i])):
                            if self.listOfFile[i][j] not in {1, 0}:
                                self.isMatrixValide = False
                                break  # Not necessary to check all elements if one doesn't respect the condition
                    # Doing condition on whether the matrix is valide or not (contains only 1 and 0)
                    if not self.isMatrixValide:
                        self.readMessage.configure(text="Please enter a matrix where it's elements are 1 or 0")
                    else:
                        if self.squaredMatrix(self.listOfFile):
                            self.readMessage.configure(text="Matrix Saved Successfully")
                            self.inputNextButton.show()
                            self.numVertices = len(self.listOfFile)  # check if this line works !!
                            self.isFileRead = True
                        else:
                            self.readMessage.configure(text="Please enter a squared Matrix")
                except ValueError:

                    messagebox.showerror("Error",
                                         "Please Check if the matrix is valid\nand each element is separated by space")

        else:
            messagebox.showerror("Error", "Please Enter A valid Path to a text file")
            self.titleOfFile.configure(text="No Path Selected..")

    def InputBack(self, event):
        self.frameRight1.place_forget()
        self.frameRight.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        # global self.color_main_content
        self.questionButton.ChangeBackgroundColor(self.color_main_content)
        self.inputButton.ChangeBackgroundColor(self.color_menu)
        self.var1.set(None)
        self.var2.set(None)
        self.graphLabel.place_forget()
        self.pathLabel.place_forget()

    def InputNext(self, event):
        self.var3.set(None)
        self.isMatrixOk = False
        if self.optionInput == 1:
            self.NextPage(event, self.frameRight1, self.frameRight4, self.inputButton, self.processingButton)
            self.test = PathFindingBfs(self.pathCanvas, self.column, self.row, 525, 450)
        elif self.optionInput == 2 or self.optionInput == 3:
            if self.optionInput == 2:
                self.isMatrixOk = False
            else:
                self.isMatrixOk = True
            self.NextPage(event, self.frameRight1, self.frameRight2, self.inputButton, self.choiceButton)
        else:
            pass

    ## Beginning the methods of the third page => frameRight2

    def OptionBack(self, event):
        self.BackPage(event, self.frameRight1, self.frameRight2, self.inputButton, self.choiceButton)

    def OptionNext(self, event):
        if self.isMatrixOk and self.isNameOk:
            self.NextPage(event, self.frameRight2, self.frameRight3, self.choiceButton,
                          self.processingButton)  # change it to next
            self.Graph = DrawGraph(self.drawGraphContainer, self.NameVertices,
                                   self.listOfFile)
        else:
            messagebox.showerror("Error", "Please Check Your Entry")

    def nameOption(self, num):
        if num == 1:
            list1 = list(range(1, self.numVertices + 1))
            list1 = [str(i) for i in list1]
            self.NameVertices = list1
            self.matrixOfGraphLabel.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.3)
            self.customizableNameOption.place_forget()
            self.isNameOk = True
        elif num == 2:
            self.matrixOfGraphLabel.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.3)
            self.customizableNameOption.place_forget()
            if self.numVertices > len(self.alphabets):
                messagebox.showerror("error", "Number Of Names surpassed the limit\nPlease choose other option")
                self.isNameOk = False
            else:
                self.NameVertices = self.alphabets[0:self.numVertices]
                self.isNameOk = True
        else:  # means num = 3
            self.customizableNameOption.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.55)
            self.matrixOfGraphLabel.place_forget()
            self.isNameok = False

        if self.isMatrixOk and self.isNameOk:
            self.optionNextButton.show()
        else:
            self.optionNextButton.place_forget()

    def listCheckLength(self, list1):
        return all(len(element) < 3 for element in list1)

    # validate names of vertices in a list called : self.NameVertices

    def validateCustomizableName(self, event):
        names = self.labelNameEntry.get()
        if len(names) == 0 or names == self.text_name_entry:
            self.labelNameMessage.configure(text="")
            messagebox.showwarning("Warning", "Please Enter Valid Names")
            self.labelNameEntry.insert(0, self.text_name_entry)
            self.isNameOk = False

        else:
            list1 = names.split(",")
            if not self.listCheckLength(list1):
                self.labelNameMessage.configure(text="")
                messagebox.showwarning("Warning", "Please make sure each name has 1 or 2 characters")
                self.labelNameEntry.insert(0, names)
                self.isNameOk = False
            else:
                if len(list1) != self.numVertices:
                    self.labelNameMessage.configure(text="")
                    messagebox.showwarning("Warning", "Number of vertices and names does not match")
                    self.labelNameEntry.insert(0, names)
                    self.isNameOk = False
                else:
                    self.NameVertices = list1
                    self.labelNameMessage.configure(text="Names Saved Successfully")
                    self.isNameOk = True

        if self.isMatrixOk and self.isNameOk:
            self.optionNextButton.show()
        else:
            self.optionNextButton.place_forget()
            # basically this function return the list of names and a boolean variable(self.isNameOk) to know if
            # name is ok

    def validateCustomizableMatrix(self, event, entry1, message):  # was entry1, message
        self.isMatrixValide = True
        message.configure(text="")
        entry = entry1.get()
        if len(entry) == 0 or entry == self.text_matrix_1:
            messagebox.showwarning("Error", "Please Enter A valid matrix")
            entry1.configure(text=self.text_matrix_1)
        else:
            try:
                splited = entry.split(",")  # spliting the string to a list of rows
                list1 = [list(i) for i in splited]  # rows and columns but it's a string
                for i in range(len(list1)):
                    for j in range(len(list1[i])):
                        list1[i][j] = int(list1[i][j])

                # Start the testing on the list

                if not self.squaredMatrix(list1):
                    self.isMatrixOk = False
                    message.configure(text="Please Enter a squared matrix")
                elif len(list1) != self.numVertices:
                    self.isMatrixOk = False
                    messagebox.showwarning("Matrix Dimension Error",
                                           f"Please Enter a matrix of {self.numVertices}x{self.numVertices}")
                else:
                    for i in range(len(list1)):
                        for j in range(len(list1[i])):
                            if list1[i][j] not in {0, 1}:
                                self.isMatrixValide = False
                                break
                    if self.isMatrixValide:
                        self.listOfFile = list1
                        message.configure(text="Matrix Registered successfully")
                        self.isMatrixOk = True
                    else:
                        messagebox.showerror("Error", "All values of the matrix must be either 1 or 0")
                        self.isMatrixOk = False

            except ValueError:
                self.isMatrixOk = False
                messagebox.showwarning("Error", "Please make sure that all elements are either 0 or 1")

        if self.isMatrixOk and self.isNameOk:
            self.optionNextButton.show()
        else:
            self.optionNextButton.place_forget()

    ## Beginning the methods of the third page => frameRight3

    def ProcessingBack(self, event):
        self.BackPage(event, self.frameRight2, self.frameRight3, self.choiceButton, self.processingButton)

    def Exit(self, event):
        self.master.destroy()

    def validateAlgoPar(self, event):
        start = self.GraphAlgorithmEntry1.get()
        end = self.GraphAlgorithmEntry2.get()
        if (start in self.NameVertices and end in self.NameVertices):
            self.start = start
            self.end = end
            if self.end == self.start:
                messagebox.showerror("Matching Name", "Please make sure that the names are different")
            else:
                self.Graph.bfs(self.start, self.end)
                self.Graph.Solution(self.master, font.Font(family="Times", size=10, slant="italic", weight='bold'),
                                    self.ButtonExit)
        else:
            messagebox.showerror("Name Error", "Please Enter A Valid Vertex Name")

    ## Beginning the methods of the fourth page => frameRight4
    def runPath(self, event):
        if self.test.isstartselected and self.test.isendselected:
            self.clearButton.enable()
            self.runButton.disable()
            self.test.bfs(event)

    def clearPath(self, event):
        self.clearButton.disable()
        self.runButton.enable()
        self.test.clear()

    def pathBack(self, event):
        self.BackPage(event, self.frameRight1, self.frameRight4, self.inputButton, self.processingButton)
        self.test.delete()
        self.clearButton.disable()
        self.runButton.enable()

    def reset(self, event, frame, btn, type : str) -> None:
        # Default Values
        self.optionButton = False
        self.optionInput = 0
        self.isFileRead = False
        self.isFileSelected = False
        self.listOfFile = list()
        self.filepath = ""
        self.numVertices = 0
        self.column = 0
        self.row = 0
        self.isMatrixValide = True
        self.NameVertices = list()
        self.NameVerticesIndex = 0
        self.isNameOk = False
        self.isMatrixOk = False
        self.start = ""
        self.end = ""
        self.readMessage.configure(text="")
        self.titleOfFile.configure(text="No Path Selected..")
        self.validatepathText.configure(text="")
        self.validateVerticesButtonMessage.configure(text="")

        self.labelNameMessage.configure(text="")
        self.validateMatrixMessage1.configure(text="")
        self.validateMatrixMessage.configure(text="")

        # Reset RadioButtons
        self.var1.set(None)
        self.var2.set(None)
        self.var3.set(None)

        # Default Entry values
        self.numberOfColumnsEntry.insert(0, self.columntext)
        self.numberOfRowsEntry.insert(0, self.rowtext)
        self.numberOfVerticesEntry.insert(0, self.numVertivesEntryText)
        self.labelNameEntry.insert(0, self.text_name_entry)
        self.matrixEntry1.insert(0, self.text_matrix_1)
        self.matrixEntry.insert(0, self.text_matrix_1)
        self.GraphAlgorithmEntry1.insert(0, self.textEntry1)
        self.GraphAlgorithmEntry2.insert(0, self.textEntry2)

        # Hiding Next Buttons
        self.inputNextButton.place_forget()
        self.optionNextButton.place_forget()

        # Reset of the display to initial status
        self.graphLabelImage1.place_forget()
        self.graphLabel2.place_forget()
        self.graphLabelImage2.place_forget()
        self.graphLabel3.place_forget()
        self.matrixOfGraphLabel.place_forget()
        self.customizableNameOption.place_forget()

        # Resetting the Path Finding Page if needed
        if type == "Path":
            self.test.delete()
            self.clearButton.disable()
            self.runButton.enable()

        # Back to input page
        self.graphLabel.place_forget()
        self.pathLabel.place_forget()
        self.BackPage(event, self.frameRight1, frame, self.inputButton, btn)


class MyEntry:
    def __init__(self, master, relx: float, rely: float, relwidth: float, relheight: float, color, colorf, myFont, text):
        self.master = master
        self.relx = relx
        self.rely = rely
        self.relwidth = relwidth
        self.relheight = relheight
        self.color = color
        self.colorf = colorf
        self.font = myFont
        self.text = text

        self.line_style = Style()
        self.line_style.configure("Line.TSeparator", background="#FDE69F")

        # Placing the button
        self.myEntry = Entry(master, bg=self.color, fg=self.colorf, bd=0)
        self.myEntry.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)
        self.myEntry['font'] = self.font
        self.myEntry.insert(0, text)

        self.separator = Separator(master, orient="horizontal", style="Line.TSeparator")
        self.separator.place(relx=self.relx, rely=self.rely + self.relheight, relheight=0.02, relwidth=self.relwidth)

        # Placeholder Off part

        self.myEntry.bind("<FocusIn>", lambda event: self.PlaceholderOff(event))

        # Placeholder On

        self.myEntry.bind("<FocusOut>", lambda event: self.PlaceholderOn(event))

    def PlaceholderOff(self, event):
        entry = self.myEntry.get()
        if entry == self.text:
            self.myEntry.delete(0, END)

    def PlaceholderOn(self, event):
        entry = self.myEntry.get()
        if len(entry) == 0:
            self.myEntry.insert(0, self.text)

    def get(self):
        return self.myEntry.get()

    def configure(self):
        self.myEntry.configure(text=self.text)

    def place_forget(self):
        self.myEntry.place_forget()
        self.separator.place_forget()

    def show(self):
        self.myEntry.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)
        self.separator.place(relx=self.relx, rely=self.rely + self.relheight, relheight=0.02, relwidth=self.relwidth)

    def insert(self, start, text):
        self.myEntry.delete(0, END)
        self.myEntry.insert(start, text)


class MyButton:
    def __init__(self, master, relx: float, rely: float, relwidth: float, relheight: float, color, image, function):
        self.master = master
        self.relx = relx
        self.rely = rely
        self.relwidth = relwidth
        self.relheight = relheight
        self.color = color
        self.image = image
        self.function = function

        self.myButton = Button(master, bg=self.color, image=self.image, activebackground=self.color, bd=0)
        self.myButton.place(relx=self.relx, rely=self.rely, relheight=self.relheight, relwidth=self.relwidth)
        self.myButton.bind("<Button-1>", lambda event: self.function(event))

    def place_forget(self):
        self.myButton.place_forget()

    def show(self):
        self.myButton.place(relx=self.relx, rely=self.rely, relheight=self.relheight, relwidth=self.relwidth)

    def disable(self):
        self.myButton.configure(state=DISABLED)

    def enable(self):
        self.myButton.configure(state=NORMAL)


class MyMenu:
    def __init__(self, master: Frame, relx: float, rely: float, relwidth: float, relheight: float, color,
                 image: PhotoImage):
        self.master = master
        self.relx = relx
        self.rely = rely
        self.relwidth = relwidth
        self.relheight = relheight
        self.color = color
        self.image = image

        # Creating And Placing the Button
        self.myButton = Button(master, bg=self.color, image=self.image, activebackground=self.color, bd=0,
                               command=self.passingNothing, compound=BOTTOM)
        self.myButton.place(relx=self.relx, rely=self.rely, relheight=self.relheight, relwidth=self.relwidth)

    def passingNothing(self):
        # The Button Won't show up unless it has a function
        pass

    def ChangeBackgroundColor(self, color):
        self.myButton.configure(bg=color, activebackground=color)

root = Tk()
BreadthFirstSearch(root)
root.mainloop()
