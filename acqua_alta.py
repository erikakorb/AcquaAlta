import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import wget
import os
from datetime import datetime


#raccolta ed estrazione dati
nomefile=['venezia','sannicolo','alberoni','pellestrina','chioggia']
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
        df = df.rename({df.columns[1]:'Altezza s.l.m. [cm]'}, axis=1)               # colonna rinominata in previsione della conversione
        df['Altezza s.l.m. [cm]'] = df['Altezza s.l.m. [cm]']*100   # conversione altezza marea da m a cm
        if (nome == 'sannicolo') | (nome=='pellestrina'):
            df = df.rename({df.columns[3]:'Velocità media vento [km/h]'}, axis=1)       # colonna rinominata in previsione della conversione
            df['Velocità media vento [km/h]'] = df['Velocità media vento [km/h]']*3.6    # conversione velocità vento da m/s a km/h
        
        dflist.append(df)        
    return dflist


data =datetime.today().strftime('%Y-%m-%d')
path_data = f'./archivio/{data}/'
os.makedirs(path_data, exist_ok=True)
df_venezia,df_sannicolo,df_alberoni,df_pellestrina,df_chioggia=scarica(nomefile,urls, path_data)



#grafici
plt.rcParams.update({'text.usetex': True, 
                     'font.family': 'Helvetica', 
                     'font.size': 17})
lw = 2

fig, axs=plt.subplots(nrows=2,ncols=2, sharex = True, figsize=(15,15))
fig.suptitle(f'Marea del {data}')


df_venezia.plot(x='Ora', y='Altezza s.l.m. [cm]', color='black', lw=lw, label='Venezia', ax=axs[0][0], grid=True, title='Venezia centro storico').set(ylabel='Altezza marea s.l.m. [cm]')
df_sannicolo.plot(x='Ora', y='Altezza s.l.m. [cm]', color='dodgerblue', lw=lw, label='Punta sabbioni-Lido', ax=axs[1][0])
df_alberoni.plot(x='Ora', y='Altezza s.l.m. [cm]', color='green', lw=lw, label='Lido-Pellestrina', ax=axs[1][0])
df_pellestrina.plot(x='Ora', y='Altezza s.l.m. [cm]', color='saddlebrown', lw=lw, label='Pellestrina-Chioggia', ax=axs[1][0])
df_chioggia.plot(x='Ora', y='Altezza s.l.m. [cm]', color='red', lw=lw, label='Chioggia', ax=axs[1][0], grid=True, title='Bocche di porto e città di Chioggia').set(ylabel='Altezza marea s.l.m. [cm]')
axs[0][0].annotate('Suolo medio', (0.01,0.48), xycoords='axes fraction')
axs[0][0].axhline(100, color='k',linestyle='dotted')
axs[1][0].annotate('Suolo medio', (0.01,0.48), xycoords='axes fraction')
axs[1][0].axhline(100, color='k',linestyle='dotted')

df_sannicolo.plot(x='Ora', y='Velocità media vento [km/h]', color='dodgerblue', lw=lw, label='Punta sabbioni-Lido', ax=axs[0][1])
df_pellestrina.plot(x='Ora', y='Velocità media vento [km/h]', color='saddlebrown', lw=lw, label='Pellestrina-Chioggia', ax=axs[0][1], grid=True, title='Velocità media del vento').set(ylabel='Velocità [km/h]')
df_sannicolo.plot(x='Ora', y='Faro Diga LidoD.Vento med. 10m', color='dodgerblue', lw=lw, label='Punta sabbioni-Lido', ax=axs[1][1])
df_pellestrina.plot(x='Ora', y='D.S.ChioggiaD.Vento med. 10m', color='saddlebrown', lw=lw, label='Pellestrina-Chioggia', ax=axs[1][1], grid=True, title='Direzione media del vento').set(ylabel='Direzione [gradi]')
axs[1][1].annotate('Scirocco', (0.89,0.35), xycoords='axes fraction')
axs[1][1].annotate('Bora', (0.93,0.2), xycoords='axes fraction')


mareamin,mareamax,step = 0,210,10
axs[0][0].axhspan(90, 110, facecolor='yellow', alpha=0.25)
axs[0][0].axhspan(110, 140, facecolor='orange', alpha=0.3)
axs[0][0].axhspan(140, mareamax+step, facecolor='red', alpha=0.3)
axs[1][0].axhspan(90, 110, facecolor='yellow', alpha=0.25)
axs[1][0].axhspan(110, 140, facecolor='orange', alpha=0.3)
axs[1][0].axhspan(140, mareamax+step, facecolor='red', alpha=0.3)
axs[1][1].axhspan(30, 90, facecolor='dodgerblue', alpha=0.15)
axs[1][1].axhspan(100, 150, facecolor='red', alpha=0.15)

axs[0][0].set_ylim(mareamin,mareamax+1)
axs[1][0].set_ylim(mareamin,mareamax+1)
axs[0][0].set_yticks(np.arange(mareamin,mareamax+1,step))
axs[1][0].set_yticks(np.arange(mareamin,mareamax+1,step))
axs[1][1].set_yticks(np.arange(0,351,50))
axs[0][0].set_xlabel(' ')
axs[0][1].set_xlabel(' ')
axs[0][0].grid(ls=':')
axs[0][1].grid(ls=':')
axs[1][0].grid(ls=':')
axs[1][1].grid(ls=':')
axs[0][0].legend(loc='upper left')
axs[1][0].legend(loc='upper left')
plt.tight_layout()
plt.subplots_adjust(bottom=0.1,top=0.9, right=0.96, wspace=0.15, hspace=0.2)
plt.show()
fig.savefig(f'{path_data}{data}.png')
