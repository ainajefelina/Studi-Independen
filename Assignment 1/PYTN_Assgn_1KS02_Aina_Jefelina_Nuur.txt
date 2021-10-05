# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # import library

# %%
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import folium
cmap = plt.get_cmap('Spectral') #mengimpor warna gradasi
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

# %% [markdown]
# # data kejahatan di london 2008 - 2016
# %% [markdown]
# ## persiapan

# %%
df_crime_london=pd.read_csv('london_crime_by_lsoa.csv') #import data
df_crime_london.shape #mengetahui banyaknya baris dan kolom yang diperoleh


# %%
df_crime_london.describe(include='O').transpose() #mengetahui banyaknya data yang unik dan frekuensinya


# %%
df_crime_london.describe(exclude='O').transpose() #mengetahui deskripsi data secara singkat


# %%
df_crime_london.isnull().any() #mengetahui apakah ada data yang kosong dan ternyata tidak ada data yang kosong


# %%
df_crime_london.info() #mengetahui value dari masing-masing kolom


# %%
#berdasarkan dari data yang kosong dan value dari kolom maka data yang ada sudah benar dan dapat langsung digunakan
df_crime_london.head()

# %% [markdown]
# # total kejahatan per tahun pada 2008 -2016
# %% [markdown]
# ## periapan

# %%
#mengekstrak data yang diperlukan yaitu data kejahatan 'value' tiap tahunnya
tahun = df_crime_london['year'].unique()
total_pertahun = df_crime_london.groupby('year').sum()
total=total_pertahun['value'].to_numpy()

n = len(tahun)
for i in range(n):
    for j in range (0, n-i-1):
        if tahun[j]>tahun[j+1]:
            tahun[j], tahun[j+1] = tahun[j+1], tahun[j]
            total[j], total[j+1] = total[j+1], total[j]

print(tahun)
print(total)

# %% [markdown]
# ## infografis

# %%
df_pertahun = pd.DataFrame({'Tahun':tahun, 'Total':total})
df_pertahun.set_index('Tahun', inplace=True)


# %%
df_pertahun.plot(marker='o', ls='--', lw=2, legend=None, figsize=(10,6))
plt.xlabel('tahun', size=20)
plt.ylabel('total kejahatan per tahun dalam 10.000', size=20)
plt.title('angka kejahatan di London pada 2008-2016', size=25)
plt.xticks(size=20)
values=np.arange(68, 76 , 1)
values_incerment=10000
plt.yticks(values*values_incerment,['%d' %val for val in values], size=20)
plt.show()

# %% [markdown]
# ### kesimpulan
# - dari gambar dapat diketahui terjadi peningkatan kejahatan yang sangat drastis pada tahun 2014 hingga 2016. Hal ini menimbulkan beberapa pertanyaan sebagai berikut:
#    -  kategori kejahatan apa yang menominasi kategori kejahatan?
#     - daerah mana yang mengalami kejatan paling besar pada tahun tersebut?
#  
# %% [markdown]
# # kategori kejahatan berat pada tahun 2014 - 2016
# %% [markdown]
# ## preparasi

# %%
df_crime_london.set_index('year', inplace=True)


# %%
df_14=df_crime_london.loc[[2014]]
df_15=df_crime_london.loc[[2015]]
df_16=df_crime_london.loc[[2016]]


# %%
# kategori berat 2014
kategori= df_14['major_category'].unique()
total_kategori14 = df_14.groupby('major_category').sum()
total_kat_14=total_kategori14['value'].to_numpy()

n = len(kategori)
for i in range(n):
    for j in range (0, n-i-1):
        if kategori[j]>kategori[j+1]:
            kategori[j], kategori[j+1] = kategori[j+1], kategori[j]
            total_kat_14[j], total_kat_14[j+1] =total_kat_14[j+1], total_kat_14[j]

print(kategori)
print(total_kat_14)


# %%
# kategori berat 2015
kategori= df_15['major_category'].unique()
total_kategori15 = df_15.groupby('major_category').sum()
total_kat_15=total_kategori15['value'].to_numpy()

n = len(kategori)
for i in range(n):
    for j in range (0, n-i-1):
        if kategori[j]>kategori[j+1]:
            kategori[j], kategori[j+1] = kategori[j+1], kategori[j]
            total_kat_15[j], total_kat_15[j+1] =total_kat_15[j+1], total_kat_15[j]

print(kategori)
print(total_kat_15)


# %%
# kategori berat 2016
kategori= df_16['major_category'].unique()
total_kategori16 = df_16.groupby('major_category').sum()
total_kat_16=total_kategori16['value'].to_numpy()

n = len(kategori)
for i in range(n):
    for j in range (0, n-i-1):
        if kategori[j]>kategori[j+1]:
            kategori[j], kategori[j+1] = kategori[j+1], kategori[j]
            total_kat_16[j], total_kat_16[j+1] =total_kat_16[j+1], total_kat_16[j]

print(kategori)
print(total_kat_16)


# %%
df_kat_berat=pd.DataFrame({'Kategori': kategori, '2014': total_kat_14, '2015': total_kat_15, '2016': total_kat_16})
df_kat_berat['Total'] = df_kat_berat.sum(axis=1)
df_kat_berat.set_index('Kategori',inplace=True)
df_kat_berat

# %% [markdown]
# ## infografis

# %%
color1= [cmap(i) for i in np.linspace(0, 1, 4)]
ax = df_kat_berat[{'2014','2015','2016'}].plot(kind='area', stacked=True, figsize=(20, 10), color=color1)
ax.set_title('kategori kejahatan berat pada 2014-2016')
ax.set_ylabel('angka kejahatan')
ax.set_xlabel('kategori kejahatan berat')


# %%
color1= [cmap(i) for i in np.linspace(0, 1, 9)]
explode_list=[0, 0.1, 0, 0, 0.1, 0, 0, 0.1, 0] 
df_kat_berat['Total'].plot(kind='pie',
                                         figsize=(15,6),
                                         autopct='%1.1f%%',
                                         startangle=90, 
                                         shadow=True,
                                         pctdistance=1.12,
                                         labels=None,
                                         colors=color1,
                                         explode=explode_list)
plt.legend(labels=df_kat_berat.index, loc='upper left')
plt.title('kategori kejahatan di London pada 2014 - 2016')
plt.axis('equal')
plt.ylabel(None)
plt.show()

# %% [markdown]
# ### kesimpulan
# - Setiap kategori kejahatan tidak selalu terjadi pada setiap tahunnya. Hal ini perlu dianalisis lebih lanjut, apa yang menyebabkan kategori tersebut tidak terjadi pada tahun tersebut
# - ketegori kejahatan di dominasi oleh sexual offences, fraud or forgery, burglary, drugs
# %% [markdown]
# # angka kejahatan pada setiap daerah
# %% [markdown]
# ## preparasi

# %%
df_14.head()


# %%
# total 2014
daerah= df_14['borough'].unique()
angka14 = df_14.groupby('borough').sum()
total_angka14=angka14['value'].to_numpy()

n = len(daerah)
for i in range(n):
    for j in range (0, n-i-1):
        if daerah[j]>daerah[j+1]:
            daerah[j], daerah[j+1] = daerah[j+1], daerah[j]
            total_angka14[j],total_angka14[j+1] =total_angka14[j+1], total_angka14[j]

print(daerah)
print(total_angka14)


# %%
# total 2015
daerah= df_15['borough'].unique()
angka15 = df_15.groupby('borough').sum()
total_angka15=angka15['value'].to_numpy()

n = len(daerah)
for i in range(n):
    for j in range (0, n-i-1):
        if daerah[j]>daerah[j+1]:
            daerah[j], daerah[j+1] = daerah[j+1], daerah[j]
            total_angka15[j],total_angka15[j+1] =total_angka15[j+1], total_angka15[j]

print(daerah)
print(total_angka15)


# %%
# total 2016
daerah= df_16['borough'].unique()
angka16 = df_16.groupby('borough').sum()
total_angka16=angka16['value'].to_numpy()

n = len(daerah)
for i in range(n):
    for j in range (0, n-i-1):
        if daerah[j]>daerah[j+1]:
            daerah[j], daerah[j+1] = daerah[j+1], daerah[j]
            total_angka16[j],total_angka16[j+1] =total_angka16[j+1], total_angka16[j]

print(daerah)
print(total_angka16)


# %%
df_kej_daerah=pd.DataFrame({'Daerah': daerah, '2014': total_angka14, '2015': total_angka15, '2016': total_angka16})
df_kej_daerah['Total'] = df_kej_daerah.sum(axis=1)
df_kej_daerah


# %%
df_kej_daerah_tnp_total=df_kej_daerah.drop('Total', axis=1)
df_kej_daerah_tnp_total.set_index('Daerah', inplace=True)

# %% [markdown]
# ## infografis

# %%
world_geo = r'london_boroughs.json'
world_map = folium.Map(location=[51.5074, 0.1278], zoom_start=9, tile='Mapbox Bright')


# %%
world_map.choropleth(
    geo_data=world_geo,
    data=df_kej_daerah,
    columns=['Daerah', 'Total'],
    key_on='feature.properties.name',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Kejahatan di London')


# %%
world_map.save('LondonCrime.html')
display(world_map)


# %%
color1= [cmap(i) for i in np.linspace(0, 1, 8)]
df_kej_daerah_tnp_total.plot(kind='bar',
                                         figsize=(15,6),
                                         stacked=True,
                                         color=color1)
plt.title('angka kejahatan per daerah pada 2014-2016')
plt.show()

# %% [markdown]
# ### kesimpulan
# - ternyata tiap daerah mengalami peningkatan kejahatan yang berbeda-beda, kejahatan paling tinggi terjadi pada daerah City of London. Hal ini menimbulkan beberapa pertanyaan:
#     - apakah yang menyebabkan kejahatan di daerah City of London mengalami peningkatan tertinggi?
#     - apakah jumlah police code (kantor polisi) mempengaruhi angka kejahatan?
# %% [markdown]
# # hubungan jumlah kantor polisi pada setiap daerah dengan angka kejahatannya
# %% [markdown]
# ## preparasi

# %%
df_crime_london.reset_index(inplace=True)
df_crime_london.set_index('borough', inplace=True)
df_crime_london


# %%
df_Barking=df_crime_london.loc['Barking and Dagenham']
Barking_polisi=len(df_Barking['lsoa_code'].unique())

df_Barnet=df_crime_london.loc['Barnet']
Barnet_polisi=len(df_Barnet['lsoa_code'].unique())

df_Bexley=df_crime_london.loc['Bexley']
Bexley_polisi=len(df_Bexley['lsoa_code'].unique())

df_Brent=df_crime_london.loc['Brent']
Brent_polisi=len(df_Brent['lsoa_code'].unique())

df_Bromley=df_crime_london.loc['Bromley']
Bromley_polisi=len(df_Bromley['lsoa_code'].unique())

df_Camden=df_crime_london.loc['Camden']
Camden_polisi=len(df_Camden['lsoa_code'].unique())

df_City=df_crime_london.loc['City of London']
City_polisi=len(df_City['lsoa_code'].unique())

df_Croydon=df_crime_london.loc['Croydon']
Croydon_polisi=len(df_Croydon['lsoa_code'].unique())

df_Ealing=df_crime_london.loc['Ealing']
Ealing_polisi=len(df_Ealing['lsoa_code'].unique())

df_Enfield=df_crime_london.loc['Enfield']
Enfield_polisi=len(df_Enfield['lsoa_code'].unique())

df_Greenwich=df_crime_london.loc['Greenwich']
Greenwich_polisi=len(df_Greenwich['lsoa_code'].unique())

df_Hackney=df_crime_london.loc['Hackney']
Hackney_polisi=len(df_Hackney['lsoa_code'].unique())

df_Hammersmith=df_crime_london.loc['Hammersmith and Fulham']
Hammersmith_polisi=len(df_Hammersmith['lsoa_code'].unique())

df_Haringey=df_crime_london.loc['Haringey']
Haringey_polisi=len(df_Haringey['lsoa_code'].unique())

df_Harrow=df_crime_london.loc['Harrow']
Harrow_polisi=len(df_Harrow['lsoa_code'].unique())

df_Havering=df_crime_london.loc['Havering']
Havering_polisi=len(df_Havering['lsoa_code'].unique())

df_Hillingdon=df_crime_london.loc['Hillingdon']
Hillingdon_polisi=len(df_Hillingdon['lsoa_code'].unique())

df_Hounslow=df_crime_london.loc['Hounslow']
Hounslow_polisi=len(df_Hounslow['lsoa_code'].unique())

df_Islington=df_crime_london.loc['Islington']
Islington_polisi=len(df_Islington['lsoa_code'].unique())

df_Kensington=df_crime_london.loc['Kensington and Chelsea']
Kensington_polisi=len(df_Kensington['lsoa_code'].unique())

df_Kingston=df_crime_london.loc['Kingston upon Thames']
Kingston_polisi=len(df_Kingston['lsoa_code'].unique())

df_Lambeth=df_crime_london.loc['Lambeth']
Lambeth_polisi=len(df_Lambeth['lsoa_code'].unique())

df_Lewisham=df_crime_london.loc['Lewisham']
Lewisham_polisi=len(df_Lewisham['lsoa_code'].unique())

df_Merton=df_crime_london.loc['Merton']
Merton_polisi=len(df_Merton['lsoa_code'].unique())

df_Newham=df_crime_london.loc['Newham']
Newham_polisi=len(df_Newham['lsoa_code'].unique())

df_Redbridge=df_crime_london.loc['Redbridge']
Redbridge_polisi=len(df_Redbridge['lsoa_code'].unique())

df_Richmond=df_crime_london.loc['Richmond upon Thames']
Richmond_polisi=len(df_Richmond['lsoa_code'].unique())

df_Southwark=df_crime_london.loc['Southwark']
Southwark_polisi=len(df_Southwark['lsoa_code'].unique())

df_Sutton=df_crime_london.loc['Sutton']
Sutton_polisi=len(df_Sutton['lsoa_code'].unique())

df_Tower =df_crime_london.loc['Tower Hamlets']
Tower_polisi=len(df_Tower['lsoa_code'].unique())

df_Waltham =df_crime_london.loc['Waltham Forest']
Waltham_polisi=len(df_Waltham ['lsoa_code'].unique())

df_Wandsworth=df_crime_london.loc['Wandsworth']
Wandsworth_polisi=len(df_Wandsworth['lsoa_code'].unique())

df_Westminster=df_crime_london.loc['Westminster']
Westminster_polisi=len(df_Westminster['lsoa_code'].unique())

print(Barking_polisi, Barnet_polisi, Bexley_polisi, Brent_polisi, Bromley_polisi, 
                                Camden_polisi, City_polisi, Croydon_polisi, Ealing_polisi, Enfield_polisi, 
                                Greenwich_polisi, Hackney_polisi, Hammersmith_polisi, Haringey_polisi,
                                Harrow_polisi, Havering_polisi, Hillingdon_polisi, Hounslow_polisi,
                                Islington_polisi, Kensington_polisi, Kingston_polisi, 
                                Lambeth_polisi, Lewisham_polisi, Merton_polisi, Newham_polisi,
                                Redbridge_polisi, Richmond_polisi, Southwark_polisi, Sutton_polisi, 
                                Tower_polisi, Waltham_polisi, Wandsworth_polisi, Westminster_polisi)


# %%
len_polisi=pd.Series([Barking_polisi, Barnet_polisi, Bexley_polisi, Brent_polisi, Bromley_polisi, 
                                   Camden_polisi, City_polisi, Croydon_polisi, Ealing_polisi, Enfield_polisi, 
                                   Greenwich_polisi, Hackney_polisi, Hammersmith_polisi, Haringey_polisi,
                                   Harrow_polisi, Havering_polisi, Hillingdon_polisi, Hounslow_polisi,
                                   Islington_polisi, Kensington_polisi, Kingston_polisi, 
                                   Lambeth_polisi, Lewisham_polisi, Merton_polisi, Newham_polisi,
                                   Redbridge_polisi, Richmond_polisi, Southwark_polisi, Sutton_polisi, 
                                   Tower_polisi, Waltham_polisi, Wandsworth_polisi, Westminster_polisi])


# %%
df_kantor_polisi=pd.DataFrame({'Daerah': daerah, 'Jumlah Kantor': len_polisi, 'Angka Kejahatan': df_kej_daerah['Total']})
df_kantor_polisi.set_index('Daerah', inplace=True)


# %%
df_kantor_polisi.head()

# %% [markdown]
# ## infografis

# %%
color2= [cmap(i) for i in np.linspace(0, 1, 34)]
fig, ax1 = plt.subplots(figsize=(20, 10))
df_kantor_polisi['Jumlah Kantor'].plot(kind='line', marker='d', secondary_y=True, ls='--', color='y', ax=ax1)
ax= df_kantor_polisi['Angka Kejahatan'].plot(kind='bar', color=color2)
ax.set_ylabel('Angka Kejahatan', fontsize=20)
ax.set_xlabel('Daerah', fontsize=20)
plt.ylabel('Jumlah Kantor Polisi', size=20)
plt.title('Hubungan Angka Kejahatan dan Jumlah Kantor Polisi', size=25)
plt.show()

# %% [markdown]
# 
# ### kesimpulan
# - berdasarkan gambar diatas dapat disimpulkan bahwa jumlah kantor polisi atau kode area sangat berhubungan dengan angka kejahatan
# - di City of London memiliki angka kejahatan yang tinggi karena jumlah kantor polisi yang sedikit
# - hal ini menimbulkan beberapa pertanyaan:
#     - bagaimana kejahatan yang berlangsung di City of London?
# %% [markdown]
# # daerah di London
# %% [markdown]
# ## persiapan

# %%
df_kantor_polisi.head()


# %%
angka_kejahatan=df_kantor_polisi['Angka Kejahatan'].sum()


# %%
max_words = 100
word_string = ''
for Daerah in df_kantor_polisi.index.values:
    if len(Daerah.split(' ')) == 1:
        repeat_num_times = int(df_kantor_polisi.loc[Daerah, 'Angka Kejahatan']/float(angka_kejahatan)*max_words)
        word_string = word_string + ((Daerah + ' ') * repeat_num_times)

word_string


# %%
wordcloud = WordCloud(background_color='white').generate(word_string)


# %%
fig = plt.figure()
fig.set_figwidth(14)
fig.set_figheight(18)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# %% [markdown]
# # kejahatan di City of London
# %% [markdown]
# ## preparasi

# %%
df_14.reset_index(inplace=True)
df_14.set_index('borough', inplace=True)
df_city_14=df_14.loc['City of London']
tiap_bulan_14=df_city_14.groupby('month').sum()
tiap_bulan_14.drop(['year'], axis=1, inplace=True)
tiap_bulan_14.reset_index(inplace=True)
tiap_bulan_14


# %%
df_15.reset_index(inplace=True)
df_15.set_index('borough', inplace=True)
df_city_15=df_15.loc['City of London']
tiap_bulan_15=df_city_15.groupby('month').sum()
tiap_bulan_15.drop(['year'], axis=1, inplace=True)
tiap_bulan_15.reset_index(inplace=True)
tiap_bulan_15


# %%
df_16.reset_index(inplace=True)
df_16.set_index('borough', inplace=True)
df_city_16=df_16.loc['City of London']
tiap_bulan_16=df_city_16.groupby('month').sum()
tiap_bulan_16.drop(['year'], axis=1, inplace=True)
tiap_bulan_16.reset_index(inplace=True)
tiap_bulan_16


# %%
df_city_14_16=pd.DataFrame({'month':tiap_bulan_14['month'],
                                                    '2014':tiap_bulan_14['value'], 
                                                    '2015':tiap_bulan_15['value'], 
                                                    '2016':tiap_bulan_16['value']})
df_city_14_16.set_index('month', inplace=True)
df_city_14_16


# %%
df_city_14_16['total']=df_city_14_16.sum(axis=1)
df_city_14_16.reset_index(inplace=True)

# %% [markdown]
# ## infografis

# %%
plt.figure(figsize=(15, 10))
ax = sns.regplot(x='month', y='total', data=df_city_14_16, color='g', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='month', ylabel='angka kejahatan')
ax.set_title('angka Kejahatan di city of London tiap bualnnya pada tahun 2014-2016')


# %%
df_city_14_16[{'2014','2015','2016'}].plot(kind='box', figsize=(8, 6))

plt.title('Box plot kejahatan di City of London')
plt.ylabel('angka kejahatan')

# %% [markdown]
# ### kesimpulan
# - tingkat kejahatan pada sepanjang tahun 2014-2016 terus mengalami peningkatan setiap bulannya
# - pada tahun 2016 merupakan puncak kejahatan yang terjadi di city of London

