import sys
from PyQt4 import QtGui, QtCore
from PIL import Image 
import os
from collections import defaultdict


class ImageDrawPanel(QtGui.QGraphicsPixmapItem):
	def __init__(self, pixmap=None, parent=None, scene=None):
		super(ImageDrawPanel, self).__init__()
		self.parent = parent
		self.rect = set()
		self.startX, self.startY = -1, -1
		self.radius = 10
		self.rectList = defaultdict(lambda : defaultdict(list))

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
		self.rectList[self.parent.imageList.currentItem().text()][self.parent.modelList.currentItem().text()] = [self.startX, self.startY, width, height]
		#remove from canvas
		#print(self.rectList)
		#draw them again	
		for items in self.rectList[self.parent.imageList.currentItem().text()]:
			x,y,w,h = self.rectList[self.parent.imageList.currentItem().text()][items]
						
			rect = painter.drawRect(x, y, w, h)


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
		self.initUI()

	def initUI(self):
		self.DRAW = []
		self.modelList = QtGui.QListWidget(self)
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

		
		self.loadImage()

		self.hbox = QtGui.QHBoxLayout()
		self.hbox.addWidget(self.imageList)
		self.hbox.addWidget(self.view)
		self.hbox.addWidget(self.modelList)

		self.setLayout(self.hbox)    

		self.setGeometry(100, 100, 1200, 650)
		self.setWindowTitle('image annotater')    

	def loadImage(self):	
		self.DRAW = []
		im = Image.open('images/' + self.imageList.currentItem().text())
		im.save('images/' + self.imageList.currentItem().text()[:-4] + '.png')
		pixmap = QtGui.QPixmap('images/' + self.imageList.currentItem().text()[:-4] + '.png')
		#pixmap = pixmap.scaledToWidth(600)
		self.imagePanel.setPixmap(pixmap)
		self.modelList.clear()

		with open('models/' + self.imageList.currentItem().text()[:-4] + '.mod') as f:
			for line in f.readlines():
				if ',n_' in line:
					self.modelList.addItem(line.strip())
					

	def addToDict(self,x,y):
		print(x,y)

	def getCurrentModelItem(self):
		return self.modelList.currentItem().text()

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = ImageDraw()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()