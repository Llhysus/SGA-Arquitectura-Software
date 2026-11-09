import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon, Rectangle
plt.rcParams['font.family']='DejaVu Sans'
fig,ax=plt.subplots(figsize=(8.4,9.6)); ax.set_xlim(0,10); ax.set_ylim(0,12.2); ax.axis('off')
ax.add_patch(FancyBboxPatch((3.9,0.15),5.95,11.85,boxstyle='round,pad=0.02,rounding_size=0.25',fc='none',ec='#888',lw=1.2))
ax.text(4.1,11.72,'Sistema de Gestión Académica (SGA)',fontsize=10.5,fontweight='bold',va='center')
U=[('CU-01','Iniciar y cerrar sesión'),('CU-03','Gestionar usuarios y roles'),('CU-04','Gestionar estudiantes'),('CU-05','Gestionar docentes'),('CU-06','Consultar auditoría'),
('CU-07','Gestionar programas y asignaturas'),('CU-08','Gestionar periodos académicos'),('CU-09','Gestionar grupos, cupos, horarios y aulas'),
('CU-10','Consultar reportes'),('CU-02','Buscar y filtrar registros'),('CU-11','Registrar, actualizar y publicar calificaciones'),
('CU-12','Matricularse en un grupo'),('CU-13','Consultar asignaturas matriculadas y horarios'),('CU-14','Consultar calificaciones publicadas')]
y0=11.05; dy=0.76; pos={}
for i,(c,t) in enumerate(U):
    y=y0-i*dy; pos[c]=y
    ax.add_patch(Ellipse((6.95,y),5.4,0.62,fc='white',ec='#222',lw=1,zorder=3))
    ax.text(6.95,y,f'{c} {t}',ha='center',va='center',fontsize=7.6,zorder=4)
def actor(name,y,col):
    ax.add_patch(FancyBboxPatch((0.55,y-0.3),1.7,0.6,boxstyle='round,pad=0.02,rounding_size=0.12',fc=col,ec='#222',lw=1,zorder=3))
    ax.text(1.4,y,name,ha='center',va='center',fontsize=8.5,zorder=4)
    return y
ay={'Administrador':(sum(pos[c] for c in ('CU-03','CU-04','CU-05','CU-06'))/4,'#D6E4F5'),
    'Coordinador\nacadémico':(sum(pos[c] for c in ('CU-07','CU-08','CU-09'))/3,'#DDEFD5'),
    'Docente':(pos['CU-11'],'#FDE9C9'),
    'Estudiante':(sum(pos[c] for c in ('CU-12','CU-13','CU-14'))/3,'#F6D9E6')}
links={'Administrador':['CU-03','CU-04','CU-05','CU-06','CU-10','CU-02'],'Coordinador\nacadémico':['CU-07','CU-08','CU-09','CU-10','CU-02'],'Docente':['CU-11','CU-10','CU-02'],'Estudiante':['CU-12','CU-13','CU-14']}
for n,(y,c) in ay.items():
    for u in links[n]:
        ax.plot([2.25,4.25],[y,pos[u]],color='#555',lw=0.9,zorder=1)
    actor(n,y,c)
# Usuario autenticado + generalización
uy=pos['CU-01']
ax.add_patch(FancyBboxPatch((0.55,uy-0.3),1.7,0.6,boxstyle='round,pad=0.02,rounding_size=0.12',fc='white',ec='#222',lw=1,ls='--',zorder=3))
ax.text(1.4,uy,'Usuario\nautenticado',ha='center',va='center',fontsize=8.5,zorder=4)
ax.plot([2.25,4.25],[uy,pos['CU-01']],color='#555',lw=0.9,zorder=1)
bx=0.25
ys=[v[0] for v in ay.values()]
ax.plot([bx,bx],[min(ys),uy-0.55],color='#555',lw=1,ls='--')
for y in ys: ax.plot([bx,0.55],[y,y],color='#555',lw=1,ls='--')
ax.add_patch(Polygon([[bx-0.14,uy-0.55],[bx+0.14,uy-0.55],[bx,uy-0.28]],closed=True,fc='white',ec='#555',lw=1))
ax.plot([bx,bx],[uy-0.28,uy],color='#555',lw=1,ls='--'); ax.plot([bx,0.55],[uy,uy],color='#555',lw=1,ls='--')
plt.savefig('uc.png',dpi=200,bbox_inches='tight',facecolor='white')
