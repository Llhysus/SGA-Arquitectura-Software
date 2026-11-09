import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
plt.rcParams['font.family']='DejaVu Sans'
P=[('Estudiante','#F6D9E6'),('Interfaz\nweb','#F2F2F2'),('API REST\n+ Seguridad','#D6E4F5'),('Módulo\nMatrículas','#FDE9C9'),('Módulo\nGestión\nAcadémica','#DDEFD5'),('Módulo\nAuditoría','#E8E8E8'),('PostgreSQL','#F2F2F2')]
X={i:i*1.22+0.8 for i in range(7)}
fig,ax=plt.subplots(figsize=(8.6,10.6)); ax.set_xlim(0,9.2); ax.set_ylim(0,10.6); ax.axis('off')
top=9.95
for i,(n,c) in enumerate(P):
    ax.add_patch(FancyBboxPatch((X[i]-0.52,top),1.04,0.6,boxstyle='round,pad=0.02',fc=c,ec='#444',lw=1))
    ax.text(X[i],top+0.3,n,ha='center',va='center',fontsize=8,fontweight='bold')
    ax.plot([X[i],X[i]],[top,0.35],color='#999',lw=0.8,ls=(0,(4,3)),zorder=0)
y=9.55; dy=0.37
def msg(a,b,t,dash=False,color='#222'):
    global y
    xa,xb=X[a],X[b]
    ax.annotate('',xy=(xb,y),xytext=(xa,y),arrowprops=dict(arrowstyle='-|>',color=color,lw=1,ls='--' if dash else '-',shrinkA=0,shrinkB=0))
    ax.text((xa+xb)/2,y+0.05,t,ha='center',va='bottom',fontsize=7.4,color=color,bbox=dict(fc='white',ec='none',pad=0.6,alpha=0.9))
    y-=dy
def selfmsg(a,t):
    global y
    x=X[a]
    ax.plot([x,x+0.32,x+0.32],[y,y,y-0.2],color='#222',lw=1); ax.annotate('',xy=(x,y-0.2),xytext=(x+0.32,y-0.2),arrowprops=dict(arrowstyle='-|>',color='#222',lw=1,shrinkA=0,shrinkB=0))
    ax.text(x+0.38,y-0.1,t,ha='left',va='center',fontsize=7.4,bbox=dict(fc='white',ec='none',pad=0.6,alpha=0.9)); y-=dy+0.12
def frame(y0,y1,label,xl=0.1,xr=8.6):
    ax.add_patch(Rectangle((xl,y1),xr-xl,y0-y1,fill=False,ec='#B45F06',lw=1.1,ls='-',zorder=2))
    ax.add_patch(Rectangle((xl,y0-0.24),0.45+0.062*len(label),0.24,fc='#FFF2CC',ec='#B45F06',lw=1.1,zorder=3))
    ax.text(xl+0.05,y0-0.12,label,fontsize=7.2,va='center',fontweight='bold',zorder=4)
msg(0,1,'1. Selecciona el grupo y confirma')
msg(1,2,'2. POST /api/matriculas {grupoId} + token')
selfmsg(2,'3. Valida token y rol Estudiante;\n    estudianteId sale del token')
f0=y+0.12; y-=0.45
msg(2,1,'401 / 403 (token inválido o sin permiso)',dash=True,color='#B45F06'); y-=0.08
frame(f0,y+0.05,'opt  [token inválido o rol sin permiso]'); y-=0.15
msg(2,3,'4. registrarMatricula(estudianteId, grupoId)')
msg(3,6,'5. BEGIN (una sola transacción)')
msg(3,4,'6. obtenerYBloquearGrupo(grupoId)')
msg(4,6,'7. SELECT … FOR UPDATE (grupo)')
msg(4,3,'8. grupo bloqueado: cupo_maximo, asignatura, periodo',dash=True)
msg(3,6,'9. ¿duplicada? ¿matrículas del grupo < cupo_maximo?')
f1=y+0.2; y-=0.3
msg(3,6,'ROLLBACK (libera el bloqueo)',color='#B45F06')
msg(3,1,'409 CUPO_AGOTADO / MATRICULA_DUPLICADA',dash=True,color='#B45F06'); y-=0.05
frame(f1,y+0.05,'opt  [cupo agotado o matrícula duplicada]'); y-=0.2
msg(3,6,'10. INSERT matrícula')
msg(3,5,'11. publica evento MatriculaCreada')
msg(5,6,'12. INSERT auditoría (misma transacción)')
msg(3,6,'13. COMMIT (libera el bloqueo)')
msg(3,2,'14. matrícula creada',dash=True)
msg(2,1,'15. 201 Created',dash=True)
msg(1,0,'16. Muestra la confirmación',dash=True)
ax.text(0.1,y-0.1,'Flujos alternos: token inválido o sin permiso → 401/403; cupo agotado o matrícula duplicada → ROLLBACK y 409.',fontsize=7.2,style='italic')
ax.set_ylim(y-0.35,10.6)
plt.savefig('seq.png',dpi=200,bbox_inches='tight',facecolor='white')
print('ok y_end',y)
