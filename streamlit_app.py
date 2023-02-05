import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patheffects
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.express as px
from PIL import Image
from streamlit_option_menu import option_menu
df = pd.read_csv('2023 QS World University Rankings.csv')
rank = df.head()



#Page Config
im = Image.open("img/icon/chart.png")
st.set_page_config(
    page_title="Data Visualization",
    page_icon=im,
    layout="wide",
)

#Navigasi Sidebar
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"
with st.sidebar :
    selected = option_menu ('List Data',['Source Data','Top 5 Universitas Di Dunia','Jumlah Universitas Terbaik Di Dunia','Data Universitas Di Indonesia Serta Perbandingannya','Data Perbandingan Universitas Terbaik Di Indonesia dan Dunia','Perbandingan Jumlah Universitas Terbaik di ASEAN','GIS','test'], default_index=0)

    
#Halaman Menu
if(selected == 'Source Data'):
    st.title(":bar_chart: Visualisasi Data")
    st.markdown("##")
    df


#Halaman Data 1
if (selected == 'Top 5 Universitas Di Dunia'):
    st.title(":bar_chart: Visualisasi Data 1")
    st.markdown("##")
    st.subheader('Untuk visualisasi yang pertama kami mengambil informasi dari data 2023 QS World University Rankings data yang kita ambil adalah 5 nilai score scaled tertinggi yang ada di dunia , disini kami menggunakan diagram batang (bar plot)')
    st.markdown("##")
    with st.empty():

        #Tabel Rank Top 5
        print("5 Universitas Tertinggi")
        top_5_RankUniv = df.nsmallest(5, 'Rank',keep='first')
        tabel = top_5_RankUniv.loc[:, ['Rank','institution','location','score scaled']]
        st.table(tabel)

        #Chart Bar Rank Top 5
        Name_Univ = rank['institution']
        dribble =[100,98.8,98.5,98.4,97.6]
        fig, ax = plt.subplots(figsize =(16, 9))
        ax.barh(Name_Univ, dribble)

        for s in ['top', 'bottom', 'left', 'right']:
            ax.spines[s].set_visible(False)

        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')

        ax.xaxis.set_tick_params(pad = 5)
        ax.yaxis.set_tick_params(pad = 10)

        ax.invert_yaxis()

        for i in ax.patches:
            plt.text(i.get_width()+0.2, i.get_y()+0.5,
                str(round((i.get_width()), 2)),
                fontsize = 12, fontweight ='bold',
                color ='grey')

        ax.set_title('Skor Universitas Tertinggi di Dunia',
                loc ='left',
                fontsize = 15,
                fontweight ='bold')

    st.pyplot(fig)
    st.write('')


#Halaman Data 2
if (selected == 'Jumlah Universitas Terbaik Di Dunia'):
    st.title(":bar_chart: Visualisasi Data 2")
    st.markdown("##")
    val_count  = df['location'].value_counts()
    plt.style.use('ggplot')
    fig = plt.figure(figsize=(20,20))
    plt.title("Jumlah Universitas Top di Berbagai Negara")

    country_count_plot = sns.countplot(data=df,y="location")
    country_count_plot.set_xlabel("")
    country_count_plot.set_ylabel("")

    st.pyplot(fig)


#Halamad Data 3
if (selected == 'Data Universitas Di Indonesia Serta Perbandingannya'):
    st.title(":bar_chart: Visualisasi Data 3")
    st.markdown("##")

    #Tabel Universitas Di Indonesia
    univ_indo = pd.DataFrame()
    df.loc[df['location']=='Indonesia']

    #Chart Bar
    labels = ['Academic Reputation ', 'Employer Reputation ', 'Faculty Student', 'Citations per faculty','International Faculty','International Students ','International Research Network','Employment Outcome','score scaled']
    Universitas_Indonesia  = [47.5,62.4,44.9,1.9,72.7,4.7,40.3,35.8,38.7]
    Bogor_Agricultural_University = [19.6,28.5,60.7,1.7,54.6,3.3,21.6,11.6,26.2]
    Gadjah_Mada_University = [49.1,55.1,62.3,1.6,39.2,2,28.8,36.2,40.2]

    x = np.arange(len(labels))  
    width = 0.15  

    fig, ax = plt.subplots(figsize=(19, 19))
    rects1 = ax.bar(x - 3*width/2, Universitas_Indonesia, width, label='Universitas Indonesia')
    rects2 = ax.bar(x - width/2, Bogor_Agricultural_University, width, label='Bogor Agricultural University')
    rects3 = ax.bar(x + width/2, Gadjah_Mada_University, width, label='Gadjah Mada University')


    ax.set_ylabel('SCORE')
    ax.set_title('Data Perbandingan Masing-Masing Score dari 3 Universitas di Indonesia')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)

    fig.tight_layout()

    st.pyplot(fig)


#Halamad Data 4
if (selected == 'Data Perbandingan Universitas Terbaik Di Indonesia dan Dunia'):
    st.title(":bar_chart: Visualisasi Data 4")
    st.markdown("##")

    #Grafik MIT
    categories = ['Academic Reputation','Employer Reputation','Faculty Student Ratio','Citations per faculty','International Faculty','International Student','International Research Network','Employement Outcome']
    values = [100,100,100,100,100,90,96.1,100]
    
        
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Product A'
    ))    

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True
        )),
        title=go.layout.Title(text='Massachusetts Institute of Technology (MIT) ',x=0.5),
    showlegend=False
    )

    st.plotly_chart(fig)

    #Grafik UGM
    categories = ['Academic Reputation','Employer Reputation','Faculty Student Ratio','Citations per faculty','International Faculty','International Student','International Research Network','Employement Outcome']
    values = [49.1,55.1,62.3,1.6,39.2, 2,28.8,36.2]
    
        
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Product A'
    ))    

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True
        )),
        title=go.layout.Title(text='Gadjah Mada University',x=0.5),
    showlegend=False
    )

    st.plotly_chart(fig)


#Halamad Data 5
if (selected == 'Perbandingan Jumlah Universitas Terbaik di ASEAN'):
    st.title(":bar_chart: Visualisasi Data 5")
    st.markdown("##")

    #Bar Chart
    countries = ["Indonesia", "Malaysia", "Thailand", "Singapore","Philippines","Vietnam",]
    ASEAN = df[df["location"].isin(countries)]

    ASEAN["location"].value_counts()


    plt.style.use('Solarize_Light2')
    fig = plt.figure(figsize=(10,10))
    plt.title("Top-Ranked ASEAN Universities counted by Country.")
    south_asain_plot = sns.countplot(data=ASEAN,x="location")
    south_asain_plot.set_xlabel("Country Name",)
    south_asain_plot.set_ylabel("Number of Universities")
    st.pyplot(fig)


#Halaman Data GIS
if (selected == 'GIS'):
    st.title('Geographic Information Systems')

    #DataFrame
    univ = pd.DataFrame()
    univ['Count'] = df.groupby('location')['location'].count().sort_values(ascending=False)
    univ = univ.reset_index()
    univ['location code'] = df['location code']

    #GIS
    fig = px.choropleth(univ, locations='location',locationmode="country names",scope="world",color="Count",color_continuous_scale="mint")
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0),height=800,coloraxis_colorbar=dict(
        title="Jumlah Top Universitas di Setiap Negara",
        ticks="outside",
        tickvals=[20,50,80,110,140,170,200],
        dtick=7
    ))
    st.plotly_chart(fig,use_container_width=True)

#Halaman Kelompok
if (selected == 'test'):

    #Header
    st.markdown("<h1 style='text-align: center; color: black;'>LAPORAN TUGAS BESAR PEMROGRAMAN DASAR SAINS DATA LIBRARY PANDAS</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>IF-1</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Dosen : Fakhrian Fadlia Adiwijaya M.kom</h2>", unsafe_allow_html=True)
    st.markdown("##")


    #Logo
    logo = Image.open('img/etc/unikom2.jpg')
    col1, col2, col3 = st.columns([3,6,3])

    with col1:
        st.write(' ')

    with col2:
        st.image(logo)

    with col3:
        st.write(' ')

    #Footer
    st.markdown("<h3 style='text-align: center; color: black;'>Disusun oleh:</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black;'>M Fakhmy Nugraha-10121002</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black;'>Gilang Setiawan Putra-10121003</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black;'>Eric Rizal Rizkyan-10121008</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black;'>Ravi Azzura Putra-10121015</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black;'>Berlian Angga Kusuma-10121016</h3>", unsafe_allow_html=True)
    st.markdown("##")
    st.markdown("<h2 style='text-align: center; color: black;'>JURUSAN TEKNIK INFORMATIKA</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>FAKULTAS TEKNIK DAN ILMU KOMPUTER</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>UNIVERSITAS KOMPUTER INDONESIA</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>2022</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='height:2px;border-width:0;color:gray;background-color:black'>", unsafe_allow_html=True)

    #Kontribusi
    st.markdown("<h2 style='text-align: left; color: black;'>Anggota dan Kontribusinya</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='width: 40%; height: 2px; border-width: 0;color: black; background-color: gray'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left; color: black;'>M Fakhmy Nugraha-10121002</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left; color: black;'>Gilang Setiawan Putra-10121003</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left; color: black;'>Eric Rizal Rizkyan-10121008</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left; color: black;'>Ravi Azzura Putra-10121015</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left; color: black;'>Berlian Angga Kusuma-10121016</h3>", unsafe_allow_html=True)
    st.markdown("##")

    #Foto Dokumentasi
    st.markdown("<h2 style='text-align: left; color: black;'>Foto Dokumentasi</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='width: 30%; height: 2px; border-width: 0;color: black; background-color: gray'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([3,3,4])

    with col1:
        st.image("img/aktivitas/hari1.jpeg")

    with col2:
        st.image("img/aktivitas/hari2.jpeg")

    with col3:
        st.image("img/aktivitas/hari3.jpeg")
    st.markdown("##")
    col4, col5, col6 = st.columns([4,4,5])

    with col4:
        st.image("img/aktivitas/hari4.jpeg")

    with col5:
        st.image("img/aktivitas/hari5.jpeg")

    with col6:
        st.image("img/aktivitas/hari6.jpeg")