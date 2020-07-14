import numpy as np
import matplotlib.pyplot as plt
from ROOT import TTree, TFile

class trk:
  px  = 0.0
  py  = 0.0

class vtx:
  x    = 0.0
  y    = 0.0
  trks = []

class event:
  index      = -1
  vtxs_reco  = []
  vtxs_truth = []

def draw_event(event):

  draw_detector()
  draw_vertex(0,0)

  for vx in event.vtxs_reco:
    draw_vertex(vx.x,vx.y,vx.trks,color='red')
  for vx in event.vtxs_truth:
    draw_vertex(vx.x,vx.y,color='blue')

  plt.title("ma,ctau = [15,10]")
  plt.xlabel('x [mm]')
  plt.ylabel('y [mm]')
  plt.savefig(str(event.index)+".png",dpi=500)
  plt.close()

def draw_vertex(x,y,trks=[],size=15,color='black'):
  plt.scatter(x,y,size,color=color, alpha=0.5)
  for tk in trks:
    plt.arrow(x,y,300*tk.px,300*tk.py, head_width=0.0, head_length=0.7, fc='lightblue', ec='black')

def draw_detector():

  draw_circle(33.5)
  draw_circle(50.5)
  draw_circle(88.5)
  draw_circle(125.5)
#  draw_circle(299,'red')


def draw_circle(r,color='blue'):
  theta = np.linspace(0, 2*np.pi, 100)

  x1 = r*np.cos(theta)
  x2 = r*np.sin(theta)


  plt.plot(x1, x2,'--',color=color)
  plt.grid(linestyle='--')

if __name__=="__main__":

  file = TFile('files.root')
  tree = file.Get('outTree')

  index = 0
  for entry in tree: 
    if not (entry.nsecVtx >= 2):
      continue
    if not (entry.truthVtx_maxlinkedRecoVtx_score[0] > 0.5 and entry.truthVtx_maxlinkedRecoVtx_score[1]):
      continue

    ev = event()
    ev.vtxs_reco = []
    ev.index = index
    truth1 = vtx()
    truth2 = vtx()
    truth1.x = entry.truthVtx_x[0]
    truth2.x = entry.truthVtx_x[1]
    truth1.y = entry.truthVtx_y[0]
    truth2.y = entry.truthVtx_y[1]


    ev.vtxs_truth = [truth1,truth2]

    nGoodVtx = 0
    for i in range(0,entry.nsecVtx):
      if(entry.secVtx_pass_mat[i] and entry.secVtx_ntrk[i] >=3 and entry.secVtx_mass[i]/entry.secVtx_maxDR[i]>3):
        nGoodVtx+=1

      reco   = vtx()
      reco.trks = []
      reco.x = entry.secVtx_x[i]
      reco.y = entry.secVtx_y[i]
      
      for j in range(0,entry.secVtx_ntrk[i]):
        reco_trk    = trk()
        reco_trk.px = entry.secVtx_trk_px[i][j]
        reco_trk.py = entry.secVtx_trk_py[i][j]

        reco.trks.append(reco_trk)

      if(entry.secVtx_pass_mat[i] and entry.secVtx_ntrk[i] >=3 and entry.secVtx_mass[i]/entry.secVtx_maxDR[i]>3):
        ev.vtxs_reco.append(reco)

    if nGoodVtx >=2:
      draw_event(ev)
      index += 1

    if index > 10:
      break
