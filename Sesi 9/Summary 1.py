# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Pendahuluan
# %% [markdown]
# ## Statistik deskriptif
# - meringkas dan mengatur data sehingga dapat dengan mudah dipahami
# - berbeda dengan statistik inferensial (karena mendeskripsikan data, tanpa membuat kesimpulan dari sampel untuk ke seluruh populasi)
# - mendeskripsikan data secara umum, dan tidak dikembangkan berdasarkan teori probabilitas
# - berfungsi untuk memahami data dan bagian penting dari Machine Learning
# - Machine Learning membuat prediksi
# - Sehingga descriptive statistics membantu kita lebih memahami apa yang diceritakan oleh data kita, yang akan menghasilkan model dan pemahaman machine learning yang lebih baik secara keseluruhan
# %% [markdown]
# ## Tipe dari Statistika Deskriptif
# - 1. Measure of central tendency
# - 2. Measure of variability (spread/ penyebaran)
# %% [markdown]
# ## Populasi dan Sampel
# -  Populasi
#     - sekumpulan dari semua elemen yang kita amati
#     - sangat banyak, sehingga tidak sesuai untuk collecting dan analyzing data
#     - beberapa kesimpulan dari populasi dibuat dengan memilih dan memeriksa subkumpulan populasi (sampel) dari populasi
# - Sampel
#     - subset/sekumpulan populasi
#     - sampel harus mempertahankan fitur statistik esensial dari populasi sehingga diperoleh hasil yang mewakili dengan sangat benar
#     - dari sampel dapat menarik kesimpulan dari populasi
# %% [markdown]
# ## Outliers atau Pencilan
# - titik data yang berada secara signifikan dari sebagian besar data yang diambil dari sampel atau populasi
# - beberapa penyebab pencilan yang dapat membantu kita yaitu :
#     - nvariasi alami dalam data
#     - perubahan perilaku sistem yang diamati
#     - kesalahan dalam pengumpulan data (penyebab utama yang bisa disebabkan oleh salah perhitungan, kontaminasi data, kesalahan manusia)
# - tisak ada definisi matematis, jadi mengandalkan pengalaman, pengetahuan dan common sense
# %% [markdown]
# ## Measure of Central Tendency
# - ada satu bilangan yang paling baik untuk meringkas seluruh rangkaian pengukuran
# - ada sebuah bilangan merupakan central dari himpunan tersebut
# - menentukan kecenderungan nilai data kita untuk mengelompokan menjadi mean, mode, atau median
# %% [markdown]
# ### Mean atau Rata - rata
# - central tendency dari data diantara angka yang tersebar
# - memperkirakan nilai seluruh kumpulan data
# - sangat dipengaruhi oleh outliers
# - dianggap ukuran tendensi sentral yang paling andal untuk membuat asumsi tentang suatu populasi dari satu sampel
# - rata - rata = jumlah semua nilai dibagi banyaknya nilai
# %% [markdown]
# ### Median  atau P2
# - nilai yang membagi data dalam jumlah yang sama diantara sisi kanan dan kirinya saat data ditata secara berurutan
# - median tidak banyak dipengaruhi oleh outliers dan skewed
# - median hanya menampilkan nilai tengah dan tidak dipengaruhi oleh semua titik data
# - sehingga lebih cocok untuk melaporkan data
#     - nilai tengah (jika jumlah dara ganjil)
#     - rata2 dari 2 nilai tengah (jika jumlah data genap)
# - kadang median ada juga yang merupakan mean
# %% [markdown]
# ### Mode
# - nilai yang sering muncul dari kumpulan data
# - frekuensinya tinggi
# - data tidak memiliki mode jika tidak ada data yang diulang
# - satu-satunya tendensi sentral yang digunakan untuk variabel kategori karena data tidak dapat dihitung
# - variabel kategori ditampilkan sebagai angka dan presentasi
# - polimodal = jika terdapat beberapa nilai muncul pada waktu yang sama lebih dari nilai lainnya
# %% [markdown]
# ## Measure of Spread / Dispersion
# - mengukur seberapa bagus mean dalam mempresentasikan sebuah kumpulan data (How far away from the center)
# %% [markdown]
# ### Standar Deviasi
# - pengukuran jarak antara setiap nilai dan rata-ratanya
# - menunjukan bagaimana dat disebarkan/ seberapa tersebar data dari mean.
# - SD yang rendah menunjukan bahwa data cemderimh mendekati rata - rata
# - SD yang tinggi bahwa data tersebar di nilai yang luas
# - SD populasi dan sampel berbeda dimana kita harus memilihnya
# 
# %% [markdown]
# ### Mean Absolute Deviation
# - rata-rata perbedaan absolut antara setiap nilai dalam satu set nilai dan rata-rata semua nilai dari set itu
# %% [markdown]
# ### Variasi
# - kuadrat SD
# - mencari selisih antara setiap titik data dan mean, mengkuadrat, menjumlahkan dan mengambil rata-rata dari angka itu
# %% [markdown]
# ### Range
# - perbedaan antara nilai terendah dan tertinggi
# %% [markdown]
# ### Presentil
# - me-representasikan posisi suatu nilai dalam kumpulan data
# - dihitung dengan nilai yang paling kecil dan menaik
# - Jika k merupakan presentil ke-n karena n% dari total suku kurang dari k
# %% [markdown]
# ### Kuartil
# - nilai yang membagi data menjadi beberapa kuarter dengan data yang diurutkan dalam urutan ascending/ menaik
# - ada tiga kuartil
#     - Q1 = 25%P
#     - Q2 = 50%P
#     - Q3 = 75%P
#     - Q3-Q1 = range interquartile
# %% [markdown]
# ###  Skewness
# %% [markdown]
# - ukuran asimetri distribusi probabilikas dari real-valued random variabel tentang meannya
# - bisa positif (distribusinya positvely skewed), negatif (distribusinya negatively skewed), dan undefined (tidak ada kemiringan atau nol)
# - menghitung:
#     - Mode skewness ((Mean-Mode)/SD)
#     - Median skewness ((Mean-Median)/SD)
# - koefisien (membandingkan distribusi samoel dengan distribusi nor,al. Semakin besar maka akan semakin besar perbedaan distribusi dan distribusi normal)
# %% [markdown]
# ### Kurtosis
# - ukuran apakah data bersifat heavy-tailed (banyak outlier) atau tidak (light outlier) terhadap distribusi normal
# - ada 3 tipe:
#     - mesokurtik = distribusi normal = 0
#     - leptokurtik = lebih besar dari mesokurtik (ekornya tebal dan berat) / lebih memuncak
#     - platykurtik = lebih rendah dari mesokurtik (ekornya tipis)/ kurang memuncak
# %% [markdown]
# ### Korelasi
# - menunjukan seberapa kuat variabel terkait
# - nilainya -1 sampai +1, semakin mendekati +-1 maka hubungan kedua variabel kuat
# - jika mendekati 0 maka tidak ada hubungan antar variabel
# - negatif (semakin besar variabel maka nilainya makin kecil)
# - positif (makin besar variabel, nilainya makin besar)
# %% [markdown]
# ## Python Statistic Libraries
# - Python's statistik:
#     - untuk deskriptif statistik
#     - dataset tidak besar
#     - jika tidak bisa mengimpor data lain
# - NumPy:
#     - untuk komputasi numerikal
#     - optimal untuk bekerja dengan single-muli dimensional array
#     - libraries memiliki banyak yang biasa untuk analisis statistika
# - SciPy:
#      - untuk komputasi numerikal
#      - berdasarkan NumPy
#      - untuk statistika analisis
# - Pandas:
#     - untuk komputasi numerikal
#     - berdasarkan NumPy
#     - mengendel label excel dengan 1D series dan object di 2D data dengan objek DataFrame
# Matplotlib :
#     - data visualisasi
#     - kombinasi yang baik dengan NumPy, SciPy, dan Pandas
# %% [markdown]
# # Python
# %% [markdown]
# ## persiapan

# %%
# import libraries
import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd


# %%
# data untuk dikerjakan
# data hampir sama dengan salah satu data ada yang berisi nilai nan
# nan = not a number
x = [8.0, 1, 2.5, 4, 28.0]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]
print(x)
print(x_with_nan)


# %%
# membuat objek np.ndarray dan pd.Series
y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)
print(y)
print(z)
print(y_with_nan)
print(z_with_nan)

# %% [markdown]
# ## Measures of Central Tendency 
# - menunjukan nilai tengah atau pusat dari kumpulan data
# %% [markdown]
# ### Mean
# - sample mean = sample aritmatika mean = average = rata - rata aritmatika dari semua item dalam kumpullan data
# - secara metematis adalah adalah jumlah dari semua elemen dibagi banyaknya elemen

# %%
# pure python
men_ = sum(x)/len(x)
print(men_)


# %%
# statistics built-in
men_ = statistics.mean(x)
print(men_)
men_ = statistics.mean(x_with_nan)
print(men_)


# %%
# dengan numpy dalam sebuah fungsi
men_=np.mean(y)
print(men_)
#  metode lain
men_= y.mean()
print(men_)


# %%
# jika ada nilai nan
print(np.mean(y_with_nan))
print(y_with_nan.mean())


# %%
# mengabaikan nilai nan dengan np.nanmean
np.nanmean(y_with_nan)


# %%
# pada pd.Series
z.mean()


# %%
#pandas mengabaikan nilai nan secara default
z_with_nan.mean()

# %% [markdown]
# ### Weighted mean
# - weighted aritmatika mean = weighted average = generalisasi dari rata - rata aritmatika yang memungkinkan kita untuk menentuka kontribusi relatif dari setiap titik data ke hasil
# - bobot Wi untuk setiap untuk setiap data Xi dari dataset X adalah jumlah item di X.  Maka kita mengalikan setiap titik data dengan bobot yang sesuai, menjumlahkannya, dan membagi semua data yang diperoleh
# - Weighted mean berguna saat kita membutuhkan rata - rata kumpulan data yang berisi item yang muncul dengan frekuensi relatif tertentu, atau kita dapat menghitung rata - rata dari setiap set

# %%
# weighted mean dalam python pure dengan menggabungkan sum() dengan range() atau zip()
x= [8.0, 1, 2.5, 4, 28.0]
w=[0.1, 0.2, 0.3, 0.25, 0.15]
wmean= sum(w[i]* x[i] for i in range(len(x)))/sum(w)
print(wmean)

wmean=sum(x_* w_ for (x_, w_) in zip(x,w))/sum(w)
print(wmean)


# %%
# kumpulan data yang besar dapt menggunakan NumPy
y, z, w = np.array(x), pd.Series(x),np.array(w)
wmean = np.average(y, weights=w)
print(wmean)
wmean = np.average(x, weights=w)
print(wmean)


# %%
y


# %%
z


# %%
w


# %%
# element-wise product w*y dengan np.sum() atau .sum():
(w*y).sum()/w.sum()

# %% [markdown]
# ### Harmonic mean
# - reciprocal (1/value) dari mean dari semua item dalam data set
# - matematis ditulis = n/jumlah (1/Xi)
# - contoh :
#     - kita berpergian sejauh 10 km pada kecepatan 60 km/jam. lainnya 10 km pada 20 km/jam. Berapa kecepatan rata - rata kita?
#     - 2/(1/60+1/20)= 2/(4/60)=2*60/4=30 km/h
# 

# %%
x


# %%
# dengan pure python
hmean= len(x)/sum(1/item for item in x)
hmean
#hasilnya sangat berbeda dengan mean aritmatika


# %%
# metode lain
hmean=statistics.harmonic_mean(x)
hmean


# %%
scipy.stats.hmean(y)


# %%
scipy.stats.hmean(z)

# %% [markdown]
# ### Geometric mean
# - akar ke-n dari hasil kali semua n elemen xi dalam dataset
# - contoh Geometric mean dari 2 dan 18:
#     - 2x18 = 36, sqrt(36)=6
# - contoh lagi, ada kamera zoom 200 nilai 8, zoom 250 nilai 6:
#     - jika ditambah dan dirata2 biasa maka ulasan yang angkanya sangat kecil dan tidak memberikan efek apapun
#     - jadi kita dapat menggunakan geometric mean

# %%
# pure Python
gmean = 1
for item in x:
    gmean*= item
gmean**=1/len(x)
gmean


# %%
scipy.stats.gmean(y)


# %%
scipy.stats.gmean(z)

# %% [markdown]
# ### Median
# - elemen tengah dari data yang diurutkan
# - tidak dipengaruhi nilai outliers
# - pada elemen ganjil = hanya ada satu nilai tengah dan berperilaku sebagai median
# - pada elemen genap = ada dua nilai tengah:
#     - median_low(): mengembalikan nilai tengah yang lebih rendah
#     - median_high() : mengembalikan nilai tengah yang lebih tinggi

# %%
x


# %%
# pure python
n = len(x)
if n % 2:
    median_ = sorted(x)[round(0.5*(n-1))]
else:
    x_ord, index= sorted(x), round(0.5*n)
    median_ = 0.5* (x_ord[index-1]+ x_ord[index])
median_


# %%
statistics.median(x)


# %%
x[:-1]


# %%
statistics.median_low(x[:-1])


# %%
statistics.median_high(x[:-1])


# %%
# statistics puthon tidak mengembalikan nan ketika ada nilai nan diantara titik data
print(x_with_nan)
print(statistics.median(x_with_nan))
print(statistics.median_high(x_with_nan))
print(statistics.median_low(x_with_nan))


# %%
# median dengan NumPy
print(y)
print(np.median(y))
print(np.median(y[:-1]))

# %% [markdown]
# ### Mode
# - nilai dalam kumpulan data yang paling sering muncul
# - multimodal = tidak ada satu pun nilai yang sama dan memiliki beberapa nilai modal

# %%
u = [2, 3, 2, 8, 12]
v = [12, 15, 12, 15, 21, 15, 12]


# %%
#python pure
print(max((u.count(item), item) for item in set (u))[1])
# statistics
print(statistics.mode(u))
#scipy.stats
print(scipy.stats.mode(u))
print(scipy.stats.mode(v))


# %%
u, v, w = pd.Series(u), pd.Series(v), pd.Series([2,2, math.nan])


# %%
u


# %%
v


# %%
w


# %%
# dengan pandas
print(u.mode())
print(v.mode())
print(w.mode())

# %% [markdown]
# ## Measures of Variability
# - ukuran variabilitas yang mengukur penyebaran titik data
# %% [markdown]
# ### Variasi
# - mengukur penyebaran data
# - menunjukan secara numerik seberapa jauh titik data dari mean
# - suatu data mungkin memiliki median dan mean yang sama tetapi merka memiliki data yang berbeda secara signifikan oleh karena itu meassures of variability dibutuhkan 

# %%
# python pure
n = len(x)
mean_ = sum(x)/n
var_= sum((item- mean_)**2 for item in x)/ (n-1)
var_


# %%
#statistics
print(statistics.variance(x))
#NumPy
print(np.var(y, ddof=1))
print(y.var(ddof=1))
#ddof=1 menyetel degress of freedom ke 1
# berarti banyaknya pengamatan bebas dari total pengamatan n. 

# %% [markdown]
# contoh ddof 
# - misal ada 10 data dan ada estimasi data yang kita inginkan
# - maka, 9 angka bebas dan 1 angka harus memenuhi nilai estimasi
# - artinya 1 derajat kebebasan itu hilang 
# - maka derajat kehilangannya menjadi n-1 = 10-1 = 9
# %% [markdown]
# var()
# - memiliki ddof, tetapi default = 1, jadi dapat menghilangkannya
# - untuk nilai nan dapat digunakan parameter opsional skipna
# %% [markdown]
# varian populasi
# - (n-1) diganti dengan n (di pure python)
# - statistics.pvariance() untuk statistik
# - parameter ddof=0 untuk NumPy / Pandas. NumPy default ddof=0
# %% [markdown]
# ### Standard Deviation
# - sampel SD untuk mengukur penyebaran data
# - akar dari varians

# %%
# di pure python dapat dihitung dengan mengetahui nilai variasi
std_ = var_**0.5
std_


# %%
# statistics
std_=statistics.stdev(x)
std_


# %%
std_=statistics.stdev(x, mean_)
std_


# %%
# numpy
print(np.std(y, ddof=1))
print(y.std(ddof=1))
print(z.std(ddof=1))
#ddof = 1 dan tidak bisa menghilangkannya
# skipna untuk memperlakukan nilai nan secara berbeda

# %% [markdown]
# ### Skewness
# - mengukur nilai asimetri suatu sampel data
# - negatif = ada ekor dominan di sisi kiri
# - positif = dominan disisi kanan
# - mendekati 0 (+- 0,5) dianggap simetris

# %%
#skewness dengan pure python ditentukan dengan mengetahui ukuran data. mean_, sdt
x = [8.0, 1, 2.5, 4, 28.0]
n = len(x)
mean_ = sum(x)/n
var_ = sum((item-mean_)**2 for item in x)/(n-1)
std_ = var_**0.5
skew_ = (sum((item - mean_)**3 for item in x)*n/ ((n-1)*(n-2)*std_**3))
skew_
# skew positif menunjukan x punya right-side tail


# %%
scipy.stats.skew(x, bias=False)


# %%
scipy.stats.skew(y_with_nan, bias=False)
#nilai nan perlu dikontrol dengan nan_policy ('propagate', 'raise', 'omit')


# %%
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)
print(z.skew())
print(z_with_nan.skew())

# %% [markdown]
# ### Precentiles dan Quantile
# - elemen dalam kumpulan data sehingga p% elemen dalam kumpulan data kurang dari atau sama dengan nilai tersebut
# - (100-p)% elemen lebih besar atau sama dengan nilai tersebut
# - tiap dataset mempunyai quartile, yang merupakan presentil yang membagi dataset menjadi empat bagian:
#     - q1 = p-25 = 25% item terkecil
#     - q2 = p-50 = 25% item diantara q1 dan q2, 25% lainnua diantara q2 dan q3
#     - q3 = p-75 = 25% item terbesaar dari sisa kumpulan data

# %%
x = [-5.0, -1.1, 0.1, 2.0, 8.0, 12.8, 21.0, 25.8, 41.0]
print(statistics.quantiles(x, n=2))
print(statistics.quantiles(x, n=4, method='inclusive'))
# 8.0 = median dari x
# 0.1 dan 21.0 sampel presentil ke-25 dan ke-75
# n = jumlah presentil probabilitas sama yang dihasilkan
# method = cara menghitungnya


# %%
y=np.array(x)
print(np.percentile(y, 5))
print(np.percentile(y, 95))


# %%
#precentile membutuhkan argumen dataset dan nilai presntil
#dataset dapat berupa array NumPy, list, tuplr
# precentile berupa urutan data diantara 0 - 100
print(np.percentile(y, [25, 50, 75]))
print(np.median(y))


# %%
y_with_nan= np.insert(y, 2, np.nan)
print(y_with_nan)


# %%
# untuk menghindari nilai nan dapat menggunakan np.nanpercentile
print(np.nanpercentile(y_with_nan, [25, 50, 75]))


# %%
#quantile dengan nilai 0-1
print(np.quantile(y, 0.05))
print(np.quantile(y, 0.95))


# %%
np.quantile(y, [0.25, 0.5, 0.75])


# %%
print(np.nanquantile(y_with_nan, [0.25, 0.5, 0.75]))


# %%
# pd.Series juga memiliki method .quantile()
z, z_with_nan = pd.Series(y), pd.Series(y_with_nan)
print(z.quantile(0.05))
print(z.quantile(0.95))


# %%
z.quantile([0.25, 0.5, 0.75])


# %%
z_with_nan.quantile([0.25, 0.5, 0.75])

# %% [markdown]
# ### Ranges
# - perbedaan antara elemen maksimum dan minimum dalam kumpulan data

# %%
print(np.ptp(y))
print(np.ptp(z))
print(np.ptp(y_with_nan))
print(np.ptp(z_with_nan))


# %%
#interquartile range
quantiles = np.quantile(y, [0.25, 0.75])
quantiles[1] - quantiles[0]


# %%
quantiles= z.quantile([0.25, 0.75])
quantiles[0.75]-quantiles[0.25]

# %% [markdown]
# ## Ringkasan dari Deskriptif Statistik
# - fungsi yang mendapatkan deskriptif statistik dengan cepat dengan satu panggilan fungsi atau merhod
# %% [markdown]
# ### deskripsi
# %% [markdown]
# describe(), menampilkan :
# - nobs: jumlah pengamatan atau elemen dalam kumpulan data Anda
# - minmax: tuple dengan nilai minimum dan maksimum dari kumpulan data Anda
# - mean: rata-rata set data Anda
# - varians: varians set data Anda
# - skewness: kemiringan dataset Anda
# - kurtosis: kurtosis dari kumpulan data Anda

# %%
#argumen 1 = dataset (bisa array NumPy, list, tuple, dataframe, dll)
# ddof=1 penting untuk menghitung varians
# bias=False untuk memaksa mengoreksi skewness dan kurtosis untuk statistical bias
result_ = scipy.stats.describe(y, ddof=1, bias=False)
result_


# %%
# dapat dengan dot notation
print(result_.nobs)
print(result_.minmax[0])
print(result_.minmax[1])
print(result_.mean)
print(result_.variance)
print(result_.skewness)
print(result_.kurtosis)

# %% [markdown]
# pandas:
# - count : elemen dalam dataset
# - mean : rata-rata
# - std : standar deviasi
# - min and max: nilai minimum dan maximum
# - 25, 50, 75% : quartile dataset

# %%
#pandas juga memiliki fungsi serupa
z.describe()

# %% [markdown]
# ### Pengukuran dari Korelasi diantara pasangan Data
# - perlu memeriksa hubungan antara elemen yang sesuai dari dua variabel dalam kumpulan data
# - jenis korelasi:
#     - positif : ketika x makin besar maka nilainya makin besar
#     - negatif : ketika x makin besar maka nilainya makin kecil
#     - weak/ tidak ada korelasi : tidak ada hubungan

# %%
x= list(range(-10,11))
y = [0, 2, 2, 2, 2, 3, 3, 6, 7, 4, 7, 6, 6, 9, 4, 5, 5, 10, 11, 12, 14]

x_, y_ =  np.array(x), np.array(y)
x__, y__ = pd.Series(x_), pd.Series(y_)

# %% [markdown]
# ### Kovariasi 
# - ukuran yang mengukur kekuatan dan arah hubungan antara sepasang variabel
# - mengukur kekuatan dan arah hubungan antara sepasang variabel:
#     - positif : Hubungan yang lebih kuat sesuai dengan nilai kovarians yang lebih tinggi hubungan yang kuat 
#     - negatif :Hubungan yang lebih kuat sesuai dengan nilai kovarians yang lebih rendah (atau lebih tinggi)
#     - weak : kovarians mendekati nol
# 

# %%
# Python pure
n = len(x)
mean_x, mean_y = sum(x)/n, sum(y)/n
cov_xy = (sum((x[k]- mean_x)*(y[k]- mean_y) for k in range (n))/(n-1))
cov_xy


# %%
# dengan NumPy
cov_matrix = np.cov(x_, y_)
cov_matrix


# %%
print(x_.var(ddof=1))
print(y_.var(ddof=1))

# %% [markdown]
# varians dari x dan y sama dengan cov_matrix[0,0] dan cov_matrix[1,1]

# %%
cov_xy=cov_matrix[0,1]
cov_xy


# %%
cov_xy=cov_matrix[1,0]
cov_xy


# %%
# pandas
cov_xy = x__.cov(y__)
cov_xy


# %%
cov_xy=y__.cov(x__)
cov_xy

# %% [markdown]
# ### Koefisien korelasi
# - disebut juga pearson product-moment correlation coefficient
# - dilambangkan dengan simbol r
# - koefisien adalah ukuran lain dari korelasi antar data
# - r>0 , korelasi positif
# - r<0 , negatif korelasi
# - r = 1, nilai  maksimum yang mungkin dari r, r=1 linear dengan variabel
# - r = -1, nilai minimum yang mungkin dari r, dan merupakan hubungan linear negatif
# - r = 0, hubungan antar variabel rendah

# %%
# pure python
var_x= sum((item - mean_x)**2 for item in x)/(n-1)
var_y= sum((item - mean_y)**2 for item in y)/(n-1)
std_x, std_y = var_x**0.5, var_y**0.5
r=cov_xy/(std_x*std_y)
r


# %%
#scipy.stats
r, p = scipy.stats.pearsonr(x_, y_)
print(r)
print(p)


# %%
# np.correcoef
corr_matrix = np.corrcoef(x_, y_)
corr_matrix 


# %%
print(scipy.stats.linregress(x_, y_))


# %%
print(scipy.stats.linregress(x_, y_).rvalue)

# %% [markdown]
# # 2D Data
# %% [markdown]
# - diperoleh dari:
#     - database tabel
#     - CSV files
#     - excel
#     - calc
#     - google spreadsheets
# %% [markdown]
# ## Axes

# %%
a = np.array([[1, 1, 1],
                        [2, 3, 2],
                        [4, 9, 2],
                        [8, 27, 4], 
                        [16, 1, 1]])
a


# %%
# kumpulan data 2D diolah dalam bentuk data 1D
print(np.mean(a))
print(a.mean())
print(np.median(a))
print(a.var(ddof=1))


# %%
#ingin mengolah dengan bentuk 2D
# axis = None () | mengatakan untuk menghitung statistik di semua data dalam array. 
# Contoh di atas bekerja seperti ini. Perilaku ini sering menjadi default di NumPy.
# axis = 0 | Mengatakan untuk menghitung statistik di semua baris, yaitu, untuk setiap kolom larik.
# Perilaku ini sering menjadi default untuk fungsi statistik SciPy.
# axis = 1 | mengatakan untuk menghitung statistik di semua kolom, yaitu, untuk setiap baris array


# %%
np.mean(a, axis=0)
# pada tiap kolom


# %%
a.mean(axis=0)


# %%
np.mean(a, axis=1)
#pada tiap baris


# %%
a.mean(axis=1)


# %%
# parameter axis juga berlaku untuk fungsi lainnya
np.median(a, axis=0)


# %%
np.median(a, axis=1)


# %%
a.var(axis=0, ddof=1)


# %%
a.var(axis=1, ddof=1)


# %%
#scipy.stats akan default axis=0
scipy.stats.gmean(a)


# %%
scipy.stats.gmean(a, axis=1)


# %%
scipy.stats.gmean(a, axis=None)


# %%
scipy.stats.describe(a, axis=None, ddof=1, bias=False)


# %%
scipy.stats.describe(a, ddof=1, bias=False) #default axis = 1


# %%
scipy.stats.describe(a, ddof=1, axis=0, bias=False) #default axis = 1

# %% [markdown]
# ## DataFrames
# - fundamental Pandas

# %%
row_names = ['first', 'second', 'third', 'fourth', 'fifth']
col_names = ['A', 'B', 'C']
df = pd.DataFrame(a, index=row_names, columns=col_names)
df


# %%
df.mean()


# %%
df.var()


# %%
df.mean(axis=1)


# %%
df.var(axis=1)


# %%
# mengisolasi stiap kolom
df['A']


# %%
print(df['A'].mean())
print(df['A'].var())


# %%
df.values


# %%
df.to_numpy()


# %%
df.describe()


# %%
# mengakses setiap summary pada setiap item
#[baris],[kolom]
df.describe().at['mean', 'A']

# %% [markdown]
# # Visualisasi Data
# %% [markdown]
# ## Box plot

# %%
np.random.seed(seed=0)
x = np.random.randn(1000)
y = np.random.randn(100)
z = np.random.randn(10)


# %%
import matplotlib.pyplot as plt
plt.style.use('ggplot')


# %%
fig, ax = plt.subplots()
ax.boxplot((x, y, z), vert=False, showmeans=True, meanline=True,
                                labels=('x','y','z'), patch_artist=True, 
                                medianprops={'lw':2, 'color':'purple'},
                                meanprops={'lw':2, 'color':'red'})
plt.show()

# %% [markdown]
# ## Histogram

# %%
hist, bin_edges = np.histogram(x, bins=10)
hist


# %%
bin_edges


# %%
# kumulatif False
fig, ax = plt.subplots()
ax.hist(x, bin_edges, cumulative=False)
ax.set_xlabel('x')
ax.set_ylabel('frequency')
plt.show()


# %%
# kumulatif true
fig, ax = plt.subplots()
ax.hist(x, bin_edges, cumulative=True)
ax.set_xlabel('x')
ax.set_ylabel('frequency')
plt.show()

# %% [markdown]
# ## pie charts

# %%
x, y, z = 128, 256, 1024


# %%
fig, ax = plt.subplots()
ax.pie((x, y, z), labels=('x', 'y', 'z'), autopct='%1.1f%%')
plt.show()

# %% [markdown]
# ## Bar Charts

# %%
x = np.arange(21)
y = np.random.randint(21, size=21)
err = np.random.randn(21)


# %%
x


# %%
y


# %%
err


# %%
fig, ax = plt.subplots()
ax.bar(x, y, yerr=err)
ax.set_ylabel('y')
ax.set_xlabel('x')
plt.show()

# %% [markdown]
# ## Scatter plot

# %%
x = np.arange(21)
y= 5+2*x+2*np.random.randn(21)
slope, intercept, r, *___ = scipy.stats.linregress(x,y)
line= f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'


# %%
fig, ax = plt.subplots()
ax.plot(x, y, lw=0, marker='s', label='Data points')
ax.plot(x, intercept+slope*x, label=line)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(facecolor='white')
plt.show()

# %% [markdown]
# ## Heatmaps

# %%
matrix=np.cov(x,y).round(decimals=2)
fig, ax = plt.subplots()
ax.imshow(matrix)
ax.grid(False)
ax.xaxis.set(ticks=(0,1), ticklabels=('x', 'y'))
ax.yaxis.set(ticks=(0,1), ticklabels= ('x', 'y'))
ax.set_ylim(1.5, -0.5)
for i in range (2):
    for j in range (2):
        ax.text(j, i, matrix[i, j], ha='center', va='center', color='w')
plt.show()


# %%
# yang kuning merupakan nilai yang paling besar
# ungu merupakan nilai yang paling kecil
# biru merupakan nilai antara


# %%
x


# %%
y


# %%
matrix = np.corrcoef(x, y).round(decimals=2)
fig, ax = plt.subplots()
ax.imshow(matrix)
ax.grid(False)
ax.xaxis.set(ticks=(0,1), ticklabels=('x', 'y'))
ax.yaxis.set(ticks=(0,1), ticklabels=('x', 'y'))
ax.set_ylim(1.5, -0.5)
for i in range (2):
    for j in range (2):
        ax.text(j, i, matrix[i, j], ha='center', va='center', color='w')
plt.show()


