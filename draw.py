import numpy as np
import matplotlib.pyplot as plt

class trk:
  pt  = 0.0
  eta = 0.0
  phi = 0.0
  m   = 0.0

def draw_event():

  fig, ax = plt.subplots(1)
  draw_detector(fig,ax)
  draw_vertex(fig,ax,0,0)
  trks = True;
  draw_vertex(fig,ax,10,-50,trks,25,'blue')
  plt.show()

def draw_vertex(fig,ax,x,y,trks=False,size=25,color='black'):
  plt.scatter(x,y,size,color=color)
  if trks:
    point1 = [x,y]
    point2 = [x+50,y+50]

    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]

    plt.plot(x_values,y_values,color=color)

def draw_detector(fig,ax):

  draw_circle(fig,ax,33.5)
  draw_circle(fig,ax,50.5)
  draw_circle(fig,ax,88.5)
  draw_circle(fig,ax,125.5)
  draw_circle(fig,ax,299,'red')


def draw_circle(fig,ax,r,color='blue'):
  theta = np.linspace(0, 2*np.pi, 100)

  x1 = r*np.cos(theta)
  x2 = r*np.sin(theta)


  ax.plot(x1, x2,'--',color=color)
  plt.grid(linestyle='--')

if __name__=="__main__":
  draw_event()
