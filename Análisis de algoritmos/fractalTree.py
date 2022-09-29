from warnings import simplefilter
from numpy_indexed.utility import axis_as_object
import pygame
import math
import random as r
import numpy as np
from PIL import Image
class fractalTree:
	def __init__(self):
		self.SilhouetteMatrix = []
		self.FractalCoords = []
		self.FractalDict = {}
		self.topArboles = {}
		self.InitialParameters = []
		self.cromosomas1Len =[]
		self.cromosomas2Len = []
		self.screen = None
		self.rateMutation = None

	def windowSettings(self,show):
		flag = pygame.HIDDEN
		if(show):
			flag = 0
		pygame.init()
		self.window = pygame.display.set_mode((600, 600), flags = flag)
		pygame.display.set_caption("Fractal Tree")
		self.screen = pygame.display.get_surface()

	def mutacion(self, pBits):
		lista = list(pBits)
		for i in range(self.rateMutation):
			index  = r.randint(0,len(lista)-1)
			if(lista[index]=='1'):
				lista[index]='0'
			else:
				lista[index]='1'
		return ''.join(lista)


	def remplazarTop(self,pDict,pId):
		
		id =0
		notaAct = 9999999

		for dict in self.topArboles:
			if(pDict == self.topArboles[dict]):
				return
			if(self.topArboles[dict]['Nota']<notaAct):
				id = dict
				notaAct = self.topArboles[dict]['Nota']
		
		if(pDict['Nota']>self.topArboles[id]['Nota']):
			del self.topArboles[id]
			self.topArboles[pId] = pDict

	def convertirParamABin(self,cromosomas1,cromosomas2):
		bin1 = ""
		bin2 = ""
		for i in range(len(cromosomas1)):
			
			if(i == 0):
				bin1+=bin(cromosomas1[i])[3:]
				bin2+=bin(cromosomas2[i])[3:]
				self.cromosomas1Len.append(len(bin(cromosomas1[i])[3:]))
				self.cromosomas2Len.append(len(bin(cromosomas2[i])[3:]))
			else:
				bin1+=bin(cromosomas1[i])[2:] 
				bin2+=bin(cromosomas2[i])[2:]
				self.cromosomas1Len.append(len(bin(cromosomas1[i])[2:]))
				self.cromosomas2Len.append(len(bin(cromosomas2[i])[2:]))
			
		return [bin1,bin2]

	def swapBits(self,bin1,bin2):
		rand = r.randint(0,len(bin1))
		aux1 = bin1[:rand]
		aux2 = bin2[:rand]

		mitad1 = bin1[rand:]
		mitad2 = bin2[rand:]

		aux1+=mitad2
		aux2+=mitad1

		r1 = r.randint(0,100)
		r2 = r.randint(0,100)

		if(r1<=4):
			aux2 = self.mutacion(aux2)
		if(r2<=4):
			aux1 = self.mutacion(aux1)
		return [aux2,aux1]


	def Cruces(self):
		parejas = self.Seleccion()
		
		for pair in parejas:
			self.cromosomas1Len=[]
			self.cromosomas2Len=[]
			parametros1 = self.FractalDict[pair[0]]['Parametros']
			parametros2 = self.FractalDict[pair[1]]['Parametros']

			binarios = self.convertirParamABin(parametros1,parametros2)
			binarios = self.swapBits(binarios[0],binarios[1])

			newCromosomas1 = []
			newCromosomas2 = []
			act1=0
			act2=0
			for i in range(len(self.cromosomas1Len)):
				rango1 = self.cromosomas1Len[i]
				rango2 = self.cromosomas2Len[i]
				if(binarios[0][act1:act1+rango1]!=''):
					newCromosomas1.append(int(binarios[0][act1:act1+rango1],2))
				else:
					newCromosomas1.append(0)
				if(binarios[1][act2:act2+rango2]!=''):
					newCromosomas2.append(int(binarios[1][act2:act2+rango2],2))
				else:
					newCromosomas2.append(0)
				act1+=rango1
				act2+=rango2
			newCromosomas1[0] = newCromosomas1[0]*-1
			newCromosomas2[0] = newCromosomas2[0]*-1

			# Arbol nuevo #1
			newCoord1 = self.drawTree(300,599,newCromosomas1[0],newCromosomas1[1],newCromosomas1[2],
				newCromosomas1[3],newCromosomas1[4],newCromosomas1[5],newCromosomas1[6])
			self.FractalCoords = []
			nota1 = self.getScore(self.SilhouetteMatrix,newCoord1)
			arbolDict1 = {'Coordenadas': newCoord1, 'Parametros':newCromosomas1, 'Nota': nota1, 'Padres' : pair}
			self.FractalDict[len(self.FractalDict)] = arbolDict1
			self.remplazarTop({'Nota': nota1},len(self.FractalDict)-1)
			# Arbol nuevo #2
			newCoord2 = self.drawTree(300,599,newCromosomas2[0],newCromosomas2[1],newCromosomas2[2],
				newCromosomas2[3],newCromosomas2[4],newCromosomas2[5],newCromosomas2[6])
			self.FractalCoords = []
			nota2 = self.getScore(self.SilhouetteMatrix,newCoord2)
			arbolDict2 = {'Coordenadas': newCoord2, 'Parametros':newCromosomas2, 'Nota': nota2, 'Padres' : pair}
			self.FractalDict[len(self.FractalDict)] = arbolDict2
			self.remplazarTop({'Nota': nota2},len(self.FractalDict)-1)
			
		if(len(self.FractalDict)<100):
					self.Cruces()

	def Seleccion(self):
		notas = []
		arboles = []
		parejas = []

		for arbol in self.topArboles:
			arboles.append(arbol)
			notas.append(self.topArboles[arbol]['Nota'])
		seleccionados = np.random.choice(arboles , len(self.topArboles), notas)
		
		for i in range(0,len(seleccionados),2):	
			parejas.append([seleccionados[i],seleccionados[i+1]])
		return parejas

	def getScore(self, silhouetteArr, fractalArr):
		a = set(map(tuple,silhouetteArr))
		score = 0
		for i in silhouetteArr:
			if(self.screen.get_at((i[0],i[1])) == (255,255,255,255)):
				score+=1
		if(score == 0):
			score = 1
		return score/len(silhouetteArr)*100

	def getDataFromSilhouette(self, path):
		img = Image.open(path)
		rgbImage = img.convert("RGB")
		im = np.array(rgbImage)
		black = [0, 0, 0]
		X, Y = np.where(np.all(im == black, axis=2))
		self.SilhouetteMatrix = np.column_stack((X, Y))
		return self.SilhouetteMatrix

	def checkImgResolution(self, imgPath):
		im = Image.open(imgPath)
		width, height = im.size

		if([width, height] != [600, 600]):
			return False
		return True		

	def algoritmoGenetico(self, imagePath):
		self.getDataFromSilhouette(imagePath)
		self.PoblacionInicial(300, 599, -90, 13, 15, 9, 1, 6, 1,4)


	def drawTree(self, x1, y1, angle, forkAng, depth, baseLen, lenDec, baseDiam, diamDec):
		if(lenDec >= baseLen):
			lenDec = 0
		elif(diamDec >= baseDiam):
			diamDec = 0
		if depth > 0:
			if(depth>10):
				depth = 10
			x2 = x1 + int(math.cos(math.radians(angle)) * depth * baseLen)
			y2 = y1 + int(math.sin(math.radians(angle)) * depth * baseLen)
			pygame.draw.line(self.screen, (255, 255, 255),
								 (x1, y1), (x2, y2), baseDiam)
			self.drawTree(x2, y2, angle - forkAng, forkAng, depth - 1, baseLen -
						  lenDec, lenDec, baseDiam-diamDec, diamDec)
			self.drawTree(x2, y2, angle, forkAng, depth - 1, baseLen -
			 			  lenDec, lenDec, baseDiam-diamDec, diamDec)
			self.drawTree(x2, y2, angle + forkAng, forkAng, depth - 1, baseLen -
						  lenDec, lenDec, baseDiam-diamDec, diamDec)
			
	def PoblacionInicial(self, x1, y1, angle, forkAng, depth, baseLen, lenDec, baseDiam, diamDec, rateMut):
		self.rateMutation = rateMut	
		self.windowSettings(False)
		for i in range(10):
			rAngle = r.randint(80,angle*-1)*-1
			rforkAng = r.randint(0,forkAng)
			rDepth = r.randint(4,depth)
			rBaseLen = r.randint(4,baseLen)
			rLenDec =  r.randint(0,lenDec)
			rBaseDiam = r.randint(1,baseDiam)
			rDiamDec = r.randint(0,diamDec)
			parametros  = [rAngle, rforkAng, rDepth, rBaseLen, rLenDec, rBaseDiam, rDiamDec]
			self.drawTree(x1, y1, rAngle, rforkAng, rDepth, rBaseLen, rLenDec, rBaseDiam, rDiamDec)
			pygame.display.flip()
			coordenadas = []
			nota = self.getScore(self.SilhouetteMatrix,self.screen)
			arbolDict = {'Coordenadas': coordenadas, 'Parametros':parametros, 'Nota': nota, 'Padres' : None}
			self.FractalDict[i] = arbolDict
			self.topArboles[i] = {'Nota': nota}
			self.FractalCoords = []
			#self.showTree(x1, y1, rAngle, rforkAng, rDepth, rBaseLen, rLenDec, rBaseDiam, rDiamDec)
		self.Cruces()

	def showTree(self, x1, y1, angle, forkAngle, depth, baseLen, lenDec, baseDiam, diamDec):
		self.windowSettings(True)
		self.drawTree(x1, y1, angle, forkAngle, depth,
					  baseLen, lenDec, baseDiam, diamDec)
		pygame.display.flip()
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					running = False

# f = fractalTree()
# m = f.getDataFromSilhouette("silueta.gif")
# f.PoblacionInicial(300,599,-85,8,6,16,1,14,5,4)