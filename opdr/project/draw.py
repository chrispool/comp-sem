import sys
from PyQt4 import QtGui, QtCore
from PIL import Image 
import os
from collections import defaultdict

class MyPopup(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		
		self.label = QtGui.QLabel(" Nieuw model is opgeslagen ", self)
		self.button = QtGui.QPushButton('Close', self)
		self.button.clicked.connect(self.close)
		self.label.setAlignment(QtCore.Qt.AlignCenter)


		self.hbox = QtGui.QHBoxLayout()
		self.hbox.addWidget(self.label)
		self.hbox.addWidget(self.button)

		self.setLayout(self.hbox)  

	def paintEvent(self, e):
		pass


class ImageDrawPanel(QtGui.QGraphicsPixmapItem):
	def __init__(self, pixmap=None, parent=None, scene=None):
		super(ImageDrawPanel, self).__init__()
		self.parent = parent
		self.rect = set()
		self.startX, self.startY = -1, -1
		self.radius = 10
		

		self.pen = QtGui.QPen(QtCore.Qt.SolidLine)
		self.pen.setColor(QtCore.Qt.yellow)
		self.pen.setWidth(5)

		self.brush = QtGui.QBrush(QtCore.Qt.yellow)

	def dd(self):
		return list()

	
	def paint(self, painter, option, widget=None):
		painter.drawPixmap(0, 30, self.pixmap())
		painter.setPen(self.pen)
		#painter.setBrush(self.brush)
		width = self.endX - self.startX
		height = self.endY - self.startY
		self.parent.rectList[self.parent.imageList.currentItem().text()][self.parent.modelList.currentItem().text()] = [self.startX, self.startY, width, height]
		#remove from canvas
		#print(self.rectList)
		#draw them again
		self.parent.geoList.clear()	
		for items in self.parent.rectList[self.parent.imageList.currentItem().text()]:
			x,y,w,h = self.parent.rectList[self.parent.imageList.currentItem().text()][items]
			rect = painter.drawRect(x, y, w, h)
			self.parent.geoList.addItem("{} {} {} {}".format(x,y,w,h))


	def mousePressEvent (self, event):
		self.startX=event.pos().x()
		self.startY=event.pos().y()
		print("point at X{} Y{}".format(self.x,self.y))
		ImageDraw.addToDict(self,self.x,self.y)
		

	def mouseReleaseEvent (self, event):
		print ('mouse moving')
		self.endX=event.pos().x()
		self.endY=event.pos().y()
		self.update()



class ImageDraw(QtGui.QWidget):
	def __init__(self):
		super(ImageDraw, self).__init__()
		#QtCore.QCoreApplication.addLibraryPath(path.join(path.dirname(QtCore.__file__), "plugins"))
		self.coordDict=defaultdict(list)
		self.rectList = defaultdict(lambda : defaultdict(set))
		self.initUI()

	def initUI(self):
		self.DRAW = []
		self.modelList = QtGui.QListWidget(self)
		self.geoList = QtGui.QListWidget(self)
		indir = 'images'
		self.imageList = QtGui.QListWidget(self)
		for root, dirs, filenames in os.walk(indir):
				for f in filenames:
					if f.endswith('jpg'):
						self.imageList.addItem(f)
		self.imageList.setCurrentRow(0)
		self.imageList.currentItemChanged.connect(self.loadImage)

		self.scene = QtGui.QGraphicsScene()
		self.scene.setSceneRect(0, 0, 800, 600)
		self.imagePanel = ImageDrawPanel(scene = self.scene, parent = self)
		self.scene.addItem(self.imagePanel)

		self.view = QtGui.QGraphicsView(self.scene)
		self.button = QtGui.QPushButton('Save model', self)
		self.button.clicked.connect(self.saveNewModel)
		
		self.loadImage()
		self.vbox = QtGui.QVBoxLayout()
		
		self.hbox = QtGui.QHBoxLayout()
		self.hbox.addWidget(self.imageList)
		self.hbox.addWidget(self.view)
		
		self.vbox.addWidget(self.modelList)
		self.vbox.addWidget(self.geoList)
		self.vbox.addWidget(self.button)
		self.hbox.addLayout(self.vbox)
		self.setLayout(self.hbox)    

		self.setGeometry(100, 100, 1200, 650)
		self.setWindowTitle('image annotator')    

	def loadImage(self):	
		self.DRAW = []
		im = Image.open('images/' + self.imageList.currentItem().text())
		im.save('images/' + self.imageList.currentItem().text()[:-4] + '.png')
		pixmap = QtGui.QPixmap('images/' + self.imageList.currentItem().text()[:-4] + '.png')
		pixmap = pixmap.scaledToWidth(800)
		self.imagePanel.setPixmap(pixmap)
		self.modelList.clear()

		with open('models/' + self.imageList.currentItem().text()[:-4] + '.mod') as f:
			for line in f.readlines():
				if ',n_' in line:
					self.modelList.addItem(line.strip())
		self.update()

	def addToDict(self,x,y):
		print(x,y)

	def getCurrentModelItem(self):
		return self.modelList.currentItem().text()

	def saveNewModel(self):
		#first load old model
		model = []
		with open('models/' + self.imageList.currentItem().text()[:-4] + '.mod') as f:
			for line in f.readlines():
					model.append(line.strip())

		#remove last ).
		model[-1] = model[-1][:-2]


      
		geoModel = []
		for items in self.rectList[self.imageList.currentItem().text()]:
			x,y,w,h = self.rectList[self.imageList.currentItem().text()][items]
			d = items.split("d")
			d = "d" + d[1][:1]

			string = "g({}, [{},{},{},{}]),".format(d, int(x), int(y), int(w), int(h))
			geoModel.append(string)
		
		#add opening bracket
		geoModel[0] = "[" + geoModel[0]	
		geoModel[-1] = geoModel[-1][:-1] + ")."
		#create new model, and add geo info
		model = model + geoModel
		f = open("newmodels/" +  self.imageList.currentItem().text()[:-4] + '.mod', 'w')

		for l in model:
			f.write(l + "\n")
		f.close()
		print ("Opening a new popup window...")
		self.w = MyPopup()
		self.w.setGeometry(QtCore.QRect(100, 100, 400, 200))
		self.w.show()
		
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = ImageDraw()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()