from PyQt4.QtCore import *
from PyQt4.QtGui import *
from collections import defaultdict

class ImageDrawPanel(QGraphicsPixmapItem):
	def __init__(self, pixmap=None, parent=None, scene=None):
		super(ImageDrawPanel, self).__init__()
		self.x, self.y = -1, -1
		self.radius = 10
		self.CornerList=[]

		self.pen = QPen(Qt.SolidLine)
		self.pen.setColor(Qt.black)
		self.pen.setWidth(2)

		self.brush = QBrush(Qt.yellow)


	def paint(self, painter, option, widget=None):
		painter.drawPixmap(0, 30, self.pixmap())
		painter.setPen(self.pen)
		painter.setBrush(self.brush)
		if self.x >= 0 and self.y >= 0:
			painter.drawEllipse(self.x-self.radius, self.y-self.radius, self.radius, self.radius)
			self.x, self.y = -1, -1

	def mousePressEvent (self, event):
		self.x=event.pos().x()
		self.y=event.pos().y()
		print("point at X{} Y{}".format(self.x,self.y))
		MainWindow.addToDict(self,self.x,self.y)
		self.update()

	def mouseMoveEvent (self, event):
		print ('mouse moving')
		self.x=event.pos().x()
		self.y=event.pos().y()
		self.update()

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.coordDict=defaultdict(list)
		self.Qlist = QListWidget(self)
		
		self.scene = QGraphicsScene()
		self.scene.setSceneRect(0, 0, 800, 600)

		pixmap, modpath=self.openImage()
		with open(modpath) as f:
			data = f.readlines()
		for line in data:
			if ',n_' in line:
				self.Qlist.addItem(line.strip())

		
		self.imagePanel = ImageDrawPanel(scene = self.scene)
		self.imagePanel.setPixmap(pixmap)
		self.scene.addItem(self.imagePanel)

		self.view = QGraphicsView(self.scene)

		self.edit = QTextEdit()
		self.edit.setText("Please indicate the coordinates \nof corners per item by clicking clockwise,\n starting topleft")

		layout = QHBoxLayout()

		layout.addWidget(self.view)
		layout.addWidget(self.Qlist)
		layout.addWidget(self.edit)

		self.Qlist.currentItemChanged.connect(self.on_item_changed)

		self.widget = QWidget()
		self.widget.setLayout(layout)
		self.entry = QLineEdit(self.widget)
		self.entry.setGeometry(QRect(10,10, 250, 20))
		self.entry.setObjectName("lineEdit")


		self.setCentralWidget(self.widget)
		self.setWindowTitle("Image Draw")
	
	def addToDict(self,x,y):
		print(x,y)
		

	def openImage(self):
		picpath = QFileDialog.getOpenFileName(self, "Open image", ".", "Image Files (*.bmp *.jpg *.png *.xpm)")
		modpath=picpath[:-4]+'.mod'
		return QPixmap(picpath),modpath

	def on_item_changed(self, curr):
		self.d=curr.text()
		self.entry.setText("Click corners of {}".format(self.d))


import sys
if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = MainWindow()
	mainWindow.show()
	sys.exit(app.exec_())