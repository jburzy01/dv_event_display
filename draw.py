import numpy as np
import matplotlib.pyplot as plt

class trk:
  px  = 0.0
  py  = 0.0

def draw_event():

  fig, ax = plt.subplots(1)
  draw_detector(fig,ax)
  draw_vertex(fig,ax,0,0)
  trk1 = trk()
  trk2 = trk()
  trk1.px = 10
  trk1.py = -50
  trk2.px = 15
  trk2.py = -55
  trks = [trk1,trk2]
  draw_vertex(fig,ax,10,-50,trks,25,'blue')
  plt.show()

def draw_vertex(fig,ax,x,y,trks=[],size=25,color='black'):
  plt.scatter(x,y,size,color=color)
  for trk in trks:
    ax.arrow(x,y,300*trk.px,300*trk.py, head_width=0.0, head_length=0.7, fc='lightblue', ec='black')

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
