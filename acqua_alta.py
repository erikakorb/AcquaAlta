import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import wget
import os
from datetime import datetime


#raccolta ed estrazione dati
nomefile=['venezia','lido','malamocco','pellestrina','chioggia']
urls=['https://www.comune.venezia.it/sites/default/files/publicCPSM2/stazioni/temporeale/Punta_Salute.html',
      'https://www.comune.venezia.it/sites/default/files/publicCPSM2/stazioni/temporeale/Diga_Sud_Lido.html',
      'https://www.comune.venezia.it/sites/default/files/publicCPSM2/stazioni/temporeale/Diga_Nord_Malamocco.html',
      'https://www.comune.venezia.it/sites/default/files/publicCPSM2/stazioni/temporeale/Diga_Sud_Chioggia.html',
      'https://www.comune.venezia.it/sites/default/files/publicCPSM2/stazioni/temporeale/Chioggia_Citta.html']

def scarica(nomefile,urls,path_data):
    dflist=[]
    for nome, url in zip(nomefile,urls):
        try:
            os.remove(f'{path_data}{nome}.html')
        except OSError:
            pass
        wget.download(url, f'{path_data}{nome}.html')
        df=pd.read_html(f'{path_data}{nome}.html')[0]

        df['Data'] = df['Data'].apply(lambda x: datetime.strptime(x,"%Y-%m-%d %H:%M:%S")) #conversione in formato datetime
        df['Giorno'] = df['Data'].dt.date
        df['Ora'] = df['Data'].dt.strftime('%H:%M')
        df = df.rename({df.columns[1]:'Altezza s.l.m. [m]'}, axis=1)
        
        dflist.append(df)        
    return dflist


data =datetime.today().strftime('%Y-%m-%d')
path_data = f'./archivio/{data}/'
os.makedirs(path_data, exist_ok=True)
df_venezia,df_lido,df_malamocco,df_pellestrina,df_chioggia=scarica(nomefile,urls, path_data)



#grafici
plt.rcParams.update({'text.usetex': True, 
                     'font.family': 'Helvetica', 
                     'font.size': 15})
lw = 2

fig, axs=plt.subplots(nrows=2,ncols=2, sharex = True, figsize=(15,15))
fig.suptitle(f'Marea del {data}')


df_venezia.plot(x='Ora', y='Altezza s.l.m. [m]', color='black', lw=lw, label='Venezia', ax=axs[0][0], grid=True, title='Venezia centro storico').set(ylabel='Altezza acqua s.l.m. [m]')
df_lido.plot(x='Ora', y='Altezza s.l.m. [m]', color='dodgerblue', lw=lw, label='San Nicolò', ax=axs[1][0])
df_malamocco.plot(x='Ora', y='Altezza s.l.m. [m]', color='green', lw=lw, label='Malamocco', ax=axs[1][0])
df_pellestrina.plot(x='Ora', y='Altezza s.l.m. [m]', color='saddlebrown', lw=lw, label='Pellestrina', ax=axs[1][0])
df_chioggia.plot(x='Ora', y='Altezza s.l.m. [m]', color='red', lw=lw, label='Chioggia', ax=axs[1][0], grid=True, title='Bocche di porto e città di Chioggia').set(ylabel='Altezza acqua s.l.m. [m]')

df_lido.plot(x='Ora', y='Faro Diga LidoV.Vento med.10m', color='dodgerblue', lw=lw, label='San Nicolò', ax=axs[0][1])
df_pellestrina.plot(x='Ora', y='D.S.ChioggiaV.Vento med.10m', color='saddlebrown', lw=lw, label='Pellestrina', ax=axs[0][1], grid=True, title='Velocità media del vento').set(ylabel='Velocità [m/s]')
df_lido.plot(x='Ora', y='Faro Diga LidoD.Vento med. 10m', color='dodgerblue', lw=lw, label='San Nicolò', ax=axs[1][1])
df_pellestrina.plot(x='Ora', y='D.S.ChioggiaD.Vento med. 10m', color='saddlebrown', lw=lw, label='Pellestrina', ax=axs[1][1], grid=True, title='Direzione media del vento').set(ylabel='Direzione [gradi]')

axs[0][0].set_ylim(-0.20,1.55)
axs[1][0].set_ylim(-0.20,1.55)
axs[0][0].set_xlabel(' ')
axs[0][1].set_xlabel(' ')
axs[0][0].grid(ls=':')
axs[0][1].grid(ls=':')
axs[1][0].grid(ls=':')
axs[1][1].grid(ls=':')
plt.tight_layout()
plt.subplots_adjust(bottom=0.1,top=0.9, right=0.96, wspace=0.15, hspace=0.2)
plt.show()
fig.savefig(f'{path_data}{data}.pdf')
