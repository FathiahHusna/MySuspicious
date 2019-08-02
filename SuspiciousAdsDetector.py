import base64
import datetime
import io

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table 

from dash.dependencies import Input, Output, State

import textwrap
import os
import pandas as pd
import numpy as np

import plotly.graph_objs as go
#from plotly.offline import iplot, init_notebook_mode, download_plotlyjs, plot 


import requests as req
#import bs4
#calling package URL lib
import urllib
from urllib.request import urlopen as uReq
#pase HTML text
from bs4 import BeautifulSoup as soup

from sklearn.cluster import KMeans 

# The layout is composed of a tree of "components" like html.Div and dcc.Graph.

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

image_filename1 = 'highway car1_trademark_scamtrust.png' # replace with your own image
encoded_image1 = base64.b64encode(open(image_filename1, 'rb').read())
#car_img = html.Img(src='data:image/png;base64,{}'.format(encoded_image1.decode()))

car_img = html.Div([
        html.Img(
            src='data:image/png;base64,{}'.format(encoded_image1.decode()),
            style={
                'height': '30%',
                'width': '100%'
            })
], style={'textAlign': 'center'})

image_filename2 = 'Suspicous Ads.png' # replace with your own image
encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())
title_img = html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()))

#title_img = html.Div([
       # html.Img(
           # src='data:image/png;base64,{}'.format(encoded_image2.decode()))], style={'textAlign': 'center'})

image_filename3 = 'mudah.png' # replace with your own image
encoded_image3 = base64.b64encode(open(image_filename3, 'rb').read())

mudah_img = html.A([
            html.Img(
                src='data:image/png;base64,{}'.format(encoded_image3.decode())
            )
    ], href='https://www.mudah.my/')

#mudah_img =
 #   html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode()))

#mudah_img = html.Div([
 #       html.Img(
  #          src='data:image/png;base64,{}'.format(encoded_image3.decode()),
   #         style={
    #            'height': '5%',
     #           'width': '10%'
      #      })
#])#, style={'textAlign': 'left'})

colors = {
    'text': '#d90404'
}

title = html.H1(children='Suspicious Ads Detector', style = {
    'textAlign': 'center',
    'color': colors['text']
})

trademark = html.Div(children='Beware of SCAMMER, Buy from the Trusted ONE', style= {
    'textAlign': 'center',
    'color': colors['text']
})

markdown_text = ''' 
__NAME__ : FATHIAH HUSNA BINTI FIRDAUS || __SUPERVISOR__ : DR. ALI SEMAN || July 2019 ||  [Video Tutorial](https://www.youtube.com/watch?v=zS2Xq7Mhyh8&feature=youtu.be)
'''

about_text = html.Div([dcc.Markdown(children=markdown_text, style = {
                                    'width': '1400px',
                                    'fontSize' : '12px',
                                    'textAlign' : 'left'
                                    ,'padding-left' : '0px'
                                    ,'display': 'grid'
                                                                    })])

#TAB 1 
markdown_description = ''' 
## Welcome to Suspicious Ads Detector
##### __Suspicious Ads Detector__ aims to detect the suspicious advertisement(s) that appear to be outlier(s) in PCA and cluster analysis. Scope to mudah.my e-commerce of car advertisements.
***
__Step by Step How to Use__
- In order to detect the suspicious ads, you need to have a dataset. Feel free to choose any car, location and number of pages to be scraped from mudah.my!! --> _Go to first tab (Extraction Data)_
- Upload the scraped dataset to perform next methods. You can view the dataset in interactive table! --> _Go to second tab (Upload & View)_
- Just click the buttons to apply data mining and statistical method! Then, you can view the suspicious ads which appear as outliers. No more worries!! --> _Go to third tab (Analysis_)
'''

description_text = html.Div([dcc.Markdown(children=markdown_description, style = {
                                    'width': '97%',
                                    'fontSize' : '20px',
                                    'fontFamily' : 'Bebas Nueue',
                                    'textAlign' : 'left',
                                    'padding-left' : '20px',
                                    'padding-right' : '20px'
                                    ,'display': 'grid',
                                    'background': 'cornsilk'
                                                                    })])
car_options = ['Perodua Myvi', 'Perodua Kancil', 'Honda Accord', 'Honda Civic', 'Toyota Vios']
car_dropdown = dcc.Dropdown(
    options=[     
        {'label':car_options[i], 'value': car_options[i]} for i in range(len(car_options))
    ],
    value=car_options[0], id = 'car', style={'background': 'PowderBlue'}
) 

type_car = html.P([
                    html.Label("Choose a car"),
                    car_dropdown
                        ], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'inline-grid'})

location_options = ['Selangor', 'Kuala Lumpur']

location_dropdown = dcc.Dropdown(
    options=[
        {'label':location_options[i], 'value': location_options[i]} for i in range(len(location_options))
    ],
    value=location_options[0], id = 'location', style={'background': 'PowderBlue'}
) 

type_location = html.P([
                    html.Label("Choose a location"),
                    location_dropdown
                        ], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'inline-grid'})

pages_text = dcc.Input(
    placeholder='',
    type='number',
    min = 1,
    max= 10,
    value= 1, 
    id = 'page',
    style={'background': 'PowderBlue'}
)

type_pages = html.P([
                    html.Label("Choose num of page(s)"),
                    pages_text
                        ], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'inline-grid'})

#folder_path = dcc.Input(
#    placeholder='Enter Folder Path',
#    type='text',
#    value='', 
#    id = 'fpath',
#    style={'background': 'AliceBlue'}
#)

#folder_name = dcc.Input(
#    placeholder='Enter CSV name (without .csv, up to 6 char)',
#    type='text',
#    value='', 
#    id = 'fname', 
#    maxLength=6,
#    style={'background': 'AliceBlue'}
#)

single_folder = dcc.Input(
    placeholder='Enter folder path and plus "\\" with CSV name (without .csv)',
    type='text',
    value='', 
    id = 'fsingle', 
    style={'background': 'AliceBlue'},
    n_submit=0,
    n_blur=0
)
    
save_btn = html.Button('Scrap & Save', id='scrap', n_clicks=0,  
                       style={'background': 'DodgerBlue', 'font-weight': 'bold', 'color': 'WhiteSmoke', 'fontSize' : '15px'}
                      )
                                        

type_save = html.P([single_folder,
                    save_btn
                        ], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid'})

download_btn = html.A(
    'Download Scraped Data',
        id='download-link',
        download="scraped_dataset.csv",
        href="",
        target="_blank",
        style = {'padding-left' : '20px'}
)

test_output_car = html.Div(id='car-div')

output_car = html.P([test_output_car], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid'})

test_output_location = html.Div(id='location-div')

output_location = html.P([test_output_location], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid'})

test_output_page = html.Div(id='page-div')

output_page = html.P([test_output_page], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid'})

test_output_savefile = html.Div(id='savefile-div')

output_savefile = html.P([test_output_savefile], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid'})

str_scrap = dcc.Markdown(id='markdown_scrap', style = {'width': '97%',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid',
                                    'background': 'AliceBlue'                   
                                                         })

#TAB 2
markdown_upload = ''' 
Browse a csv/excel file from your folder.

__Please make sure:__
- The file must be a dataset scraped from the first tab (Extraction Data)
- Do not change any name of the columns
- Perform cleaning task to the dataset before upload. 
- Below tasks is applied to columns 'Price', 'Manufactured Year' and 'NewMil' which include:
    - Remove rows if have missing values
    - Remove rows if contain mixed numeric and string values
'''

upload_text = html.Div([dcc.Markdown(children=markdown_upload, style = {
                                    'width': '98.5%',
                                    'fontSize' : '15px',
                                    'textAlign' : 'left'
                                    ,'padding-left' : '20px'
                                    ,'display': 'grid',
                                    'background': 'AliceBlue'
                                                                    })])

upload_btn = dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files', style={'color': 'black'})
        ]),
        style={
            'width': '30%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '0px', 
            'background': 'DodgerBlue', 'font-weight': 'bold', 'color': 'WhiteSmoke'
        },
        # Allow multiple files to be uploaded
        multiple=False
    )

 
output_upload = html.Div(id='output-data-upload')   

#type_upload = html.P([
                    #html.Label("Choose a cleaned csv/excel file"),
                    #upload_btn
                    #    ], style = {'width': '400px',
                    #                'fontSize' : '15px',
                    #                'padding-left' : '20px',
                    #                'display': 'grid'})


view_options = ['Top', 'Random', 'Bottom']
view_dropdown = dcc.Dropdown(
    options=[
        {'label':view_options[i], 'value': view_options[i]} for i in range(len(view_options))
    ],
    value=view_options[0]
)

type_view = html.P([
                    html.Label("View data by"),
                    view_dropdown
                        ], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'inline-grid'})


view_btn = html.P([html.Button('View')], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid'})


view_text = dcc.Input(
    placeholder='Enter num of rows',
    type='number',
    min = 5,
    max= 10,
    value= 5, id='rows'
)

type_rows = html.P([
                    html.Label("Choose num of rows"),
                    view_text
                        ], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'inline-grid'})



#TAB 3
pca_btn = html.Button('Apply PCA', id='pca', n_clicks=0, style={'background': 'LimeGreen', 'font-weight': 'bold', 'color': 'GhostWhite', 'fontSize' : '15px'})

type_pca = html.P([html.Label("Apply Data Mining Method!"),pca_btn], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid'})

pca_graph = dcc.Graph(id='mypca_graph')

str_pca = dcc.Markdown(id='markdown_pca', style = {'width': '97%',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid',
                                    'background': 'Azure'                   
                                                         })

elbow_btn = html.Button('Elbow Method', id='elbow', n_clicks=0, style={'background': 'LimeGreen', 'font-weight': 'bold', 'color': 'GhostWhite', 'fontSize' : '15px'})

type_elbow = html.P([html.Label("Cluster Analysis (K-Means Clustering): Test k cluster(s)"),elbow_btn], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid'})

elbow_graph = dcc.Graph(id='myelbow_graph')

str_elbow = dcc.Markdown(id='markdown_elbow', style = {'width': '97%',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid',
                                    'background': 'Azure'                   
                                                         })

clustering_graph = dcc.Graph(id='mycluster_graph')

cluster_text = dcc.Input(
    placeholder='Enter num of clusters',
    type='number',
    min = 0,
    max= 14,
    value= 0,
    id = 'num_k',
    style={'background': 'LightGreen'}
)

type_cluster = html.P([html.Label("Cluster Analysis (K-Means Clustering): Choose k Num of Clusters"), cluster_text], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid'})

str_cluster = dcc.Markdown(id='markdown_cluster', style = {'width': '97%',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid',
                                    'background': 'Azure'                   
                                                         })

boxplot_btn = html.Button('Boxplot', id='bplot', n_clicks=0, style={'background': 'LimeGreen', 'font-weight': 'bold', 'color': 'GhostWhite', 'fontSize' : '15px'})

boxplot_graph = dcc.Graph(id='myboxplot_graph')

type_boxplot = html.P([html.Label("Statistical Analysis (Box Plot): Choose to Compare by Attributes"), boxplot_btn], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid'})

str_boxplot = dcc.Markdown(id='markdown_boxplot', style = {'width': '97%',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid',
                                    'background': 'Azure'                   
                                                         })

scam_text = dcc.Input(
    placeholder='',
    type='number',
    min = -1,
    value= -1,
    id = 'myads-id', 
    style={'background': 'LightGreen'}
)

type_scam = html.P([html.Label("Key in Ads ID which appear as outlier(s)"), scam_text], style = {'width': '400px',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid'})


str_id = dcc.Markdown(id='markdown_id', style = {'width': '97%',
                                    'fontSize' : '15px',
                                    'padding-left' : '20px',
                                    'display': 'grid',
                                    'background': 'Azure'                   
                                                         })

#header_img = html.P([mudah_img, title_img, html.Hr()], style={'display' : 'inline-grid'})
#header_img = html.P([mudah_img, title_img], style={'display' : 'inline'})


header_img = html.P([ mudah_img, title_img], style={'display' : 'inline'} )

tab_style = {
    #'borderBottom': '1px solid #d6d6d6',
    'fontWeight': 'bold'
}
app.layout = html.Div([header_img,  about_text, car_img, description_text,
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Extraction Data', children=[
            html.Div([
                type_car, type_location, type_pages, #type_save, 
                output_car, output_location, output_page, str_scrap, download_btn
            ])
        ], style=tab_style),
        dcc.Tab(label='Upload & View', children=[
            html.Div([
                #type_upload, type_view, type_rows, view_btn, output_upload
                upload_text, upload_btn, output_upload
            ])
        ], style=tab_style),
        dcc.Tab(label='Analysis', children=[
                type_pca, str_pca, pca_graph, type_elbow, str_elbow, elbow_graph, type_cluster, str_cluster, clustering_graph, type_boxplot, str_boxplot, boxplot_graph, type_scam, str_id 
        ], style=tab_style),
    ], colors={
        "border": "white",
        "primary": "gold",
        "background": "cornsilk"})
])

str_graph_error = '''__Problems detected with data. Please clean the data and reupload the csv/excel file to proceed.__ 
_Problems may be caused by: edited column name by user, missing values or mixed datatypes for column(s) \[Price, Year, NewMil\]_'''

str_nt_upload_error = '''__Please upload csv/excel file to proceed__'''

def car_format(input_value):
    car_param = input_value
    car_param = car_param.replace(" ", "/")+ "?"
    return (car_param.lower())

def location_format(input_value):
    location_param = input_value
    if ' ' in location_param:
        location_param = location_param.replace(" ", "-") + "/"
        #print('y')
    else:
        location_param = location_param + "/"
        #print('n')
    return(location_param.lower())

def concate_file(filepath):
    d = filepath.split('\\')
    filename = ''
    for f in range(len(d)):
        filename = os.path.join(filename, d[f])
    return filename

def concate_filepath(filepath, csvfile):
    file = csvfile + '.csv'
    filepath = concate_file(filepath)
    fullpath = os.path.join(filepath, file)
    #fullpath = '\\'.join(os.path.dirname(fullpath).split("/"))
    return fullpath


#def scrap(mycar, mylocation, mypage, filepath):
    #filename = filepath #two textboxes
    #filename = filepath + '.csv' #single textbox
def scrap(mycar, mylocation, mypage):
    def subs (Mileage):
        if Mileage == "0 - 4 999":
            return Mileage.replace("0 - 4 999", "2500", 1)
        elif Mileage == "5 000 - 9 999":
            return Mileage.replace("5 000 - 9 999", "52500", 1)
        elif Mileage == "10 000 - 14 999":
            return Mileage.replace("10 000 - 14 999", "12500", 1)
        elif Mileage == "15 000 - 19 999":
            return Mileage.replace("15 000 - 19 999", "17500", 1)
        elif Mileage == "20 000 - 24 999":
            return Mileage.replace("20 000 - 24 999", "22500", 1)
        elif Mileage == "25 000 - 29 999":
            return Mileage.replace("25 000 - 29 999", "27500", 1)
        elif Mileage == "30 000 - 34 999":
            return Mileage.replace("30 000 - 34 999", "32500", 1)
        elif Mileage == "35 000 - 39 999":
            return Mileage.replace("35 000 - 39 999", "37500", 1)
        elif Mileage == "40 000 - 44 999":
            return Mileage.replace("40 000 - 44 999", "42500", 1)
        elif Mileage == "45 000 - 49 999":
            return Mileage.replace("45 000 - 49 999", "47500", 1)
        elif Mileage == "50 000 - 54 999":
            return Mileage.replace("50 000 - 54 999", "52500", 1)
        elif Mileage == "55 000 - 59 999":
            return Mileage.replace("55 000 - 59 999", "57500", 1)
        elif Mileage == "60 000 - 64 999":
            return Mileage.replace("60 000 - 64 999", "62500", 1)
        elif Mileage == "65 000 - 69 999":
            return Mileage.replace("65 000 - 69 999", "67500", 1)
        elif Mileage == "70 000 - 74 999":
            return Mileage.replace("70 000 - 74 999", "72500", 1)
        elif Mileage == "75 000 - 79 999":
            return Mileage.replace("75 000 - 79 999", "77500", 1)
        elif Mileage == "80 000 - 84 999":
            return Mileage.replace("80 000 - 84 999", "82500", 1)
        elif Mileage == "85 000 - 89 999":
            return Mileage.replace("85 000 - 89 999", "87500", 1)
        elif Mileage == "90 000 - 94 999":
            return Mileage.replace("90 000 - 94 999", "92500", 1)
        elif Mileage == "95 000 - 99 999":
            return Mileage.replace("95 000 - 99 999", "97500", 1)
        elif Mileage == "100 000 - 109 999":
            return Mileage.replace("100 000 - 109 999", "105000", 1)
        elif Mileage == "110 000 - 119 999":
            return Mileage.replace("110 000 - 119 999", "115000", 1)
        elif Mileage == "120 000 - 129 999":
            return Mileage.replace("120 000 - 129 999", "125000", 1)
        elif Mileage == "130 000 - 139 999":
            return Mileage.replace("130 000 - 139 999", "135000", 1)
        elif Mileage == "140 000 - 149 999":
            return Mileage.replace("140 000 - 149 999", "145000", 1)
        elif Mileage == "150 000 - 159 999":
            return Mileage.replace("150 000 - 159 999", "155000", 1)
        elif Mileage == "160 000 - 169 999":
            return Mileage.replace("160 000 - 169 999", "165000", 1)
        elif Mileage == "170 000 - 179 999":
            return Mileage.replace("170 000 - 179 999", "175000", 1)
        elif Mileage == "180 000 - 189 999":
            return Mileage.replace("180 000 - 189 999", "185000", 1)
        elif Mileage == "190 000 - 199 999":
            return Mileage.replace("190 000 - 199 999", "195000", 1)
        elif Mileage == "200 000 - 249 999":
            return Mileage.replace("200 000 - 249 999", "225000", 1)
        elif Mileage == "250 000 - 299 999":
            return Mileage.replace("250 000 - 299 999", "275000", 1)
        elif Mileage == "300 000 - 349 999":
            return Mileage.replace("300 000 - 349 999", "325000", 1)
        elif Mileage == "350 000 - 399 999":
            return Mileage.replace("350 000 - 399 999", "375000", 1)
        elif Mileage == "400 000 - 449 999":
            return Mileage.replace("400 000 - 449 999", "425000", 1)
        elif Mileage == "450 000 - 499 999":
            return Mileage.replace("450 000 - 499 999", "475000", 1)
        else:
            return Mileage

        
    def dprice (a):
        if (' ' in a) == True:
            return ''.join(a.split())
        else:
            return a
    container = []
    pages = []
    
    #Parameter1: LOCATION
    #param1 = location(mylocation)
    param1 = location_format(mylocation)
    car_sale = 'cars-for-sale' + '/'
    #Parameter2: TYPE OF CAR
    #param2 = car(mycar)
    param2 = car_format(mycar)
    #Parameter3: pages
    n = int(mypage)
    user_seller = '&f=p'
    
    front_link = 'https://www.mudah.my/' + param1 + car_sale + param2 + 'o='
    end_link = '&q' + '&so=1' + user_seller + '&th=1'
    
    test_link = front_link + '1' + end_link
    
    #uClient = uReq(test_link)
    #page_html = uClient.read()
    #uClient.close()
    #num_page_soup = soup(page_html, "html.parser")
    page_html = req.get(test_link)
    num_page_soup = soup(page_html.text, "html.parser")
    num_containers = num_page_soup.findAll("div", {"class":"listing_title"})
    str_pg = num_containers[0].h1.text
    split_str_pg = str_pg.split(' ')
    max_pg = int(split_str_pg[-1])
    #print('Max pg:' , max_pg, 'Chosen pages:', n)
    
    if (n <= max_pg):
        #print('if', n, max_pg)
        for i in range(1, n+1 ,1):
            #my_url = 'https://www.mudah.my/kuala-lumpur/cars-for-sale/toyota/vios?o=' + str(i) + '&q=&so=1&f=p&th=1'
            #print('first for loop')
            my_url = front_link + str(i) + end_link
            #print('My_url:' + my_url)
            pages.append(my_url)


        for item in pages:
            page = req.get(item)
            page_soup = soup(page.text, "html.parser")
            containers = page_soup.findAll("div", {"class":"listing_params_container"})


            for fathiah in containers:

                clink = fathiah.div.div.a["href"]
                name = fathiah.div.div.a["title"].strip()
                price = fathiah.findAll("div", {"class":"ads_price"})
                Price = price[0].text.strip()
                year = fathiah.findAll("font", {"class":"icon_label"})
                Year = year[1].text.strip()
                Mileage = year[2].text.strip()
                CC = year[3].text.strip()
                Condition = year[0].text.strip()

                newMil = subs(Mileage).strip()
                Price1 = Price.replace("RM", "", 1)
                nPrice = dprice(Price1)
                container.append((name, nPrice, Year, Mileage, newMil, CC, Condition, clink))



        df = pd.DataFrame(container, columns = ['Name', 'Price', 'Manufactured Year', 'Mileage', 'NewMil', 'CC', 'Condition', 'Link'])
        return df, textwrap.dedent('''''')
        #df.to_csv(filename, index=False, encoding='utf-8')
        #hide semua try and exception utk download button 
        #try:
            #new_filepath = filepath.rsplit('\\', 1)[0]
            #os.chdir(new_filepath)
            #df.to_csv(filename, index=False, encoding='utf-8')
            #print('Saving to dataframe')
        #except IOError as e:
        #except Exception as e:
            #print ("Error in saving", filename)
            #print (e)
            #return "Error in saving " , filename , e
            ##err_str1 = "Error in saving " + filename + "\n" + str(e)
            #err_str1 = '''__Error in saving__ ''' + filename + '\n' + str(e)
            #return err_str1
            #df = pd.DataFrame()
        #else:
            #print("Done scrap " + filename)
            #return "Done scrap " + filename
        
        
    else:
        print('Unable to scrap, the chosen number of pages (', n,  ') exceeded the maximum page(s) available which is' , max_pg)
        str_max_pg = '''__Unable to scrap, the chosen number of pages (__ ''' + '''__''' + str(n) + '''__''' + ''' __) exceeded the maximum page(s) available which is__ ''' + '''__''' + str(max_pg) + '''__'''
        #return 'Unable to scrap, the chosen number of pages (' + str(n) +  ') exceeded the maximum page(s) available which is ' + str(max_pg)
        #return textwrap.dedent(str_max_pg)
        df = pd.DataFrame()
        return df, textwrap.dedent(str_max_pg)
        pass



@app.callback(
    Output(component_id='car-div', component_property = 'children'),
    [Input(component_id = 'car', component_property = 'value')]
)

def test_output_div1(input_value):
    #input_value = car_format(input_value)
    return 'My Car Type: {}'.format(car_format(input_value))

@app.callback(
    Output(component_id='location-div', component_property = 'children'),
    [Input(component_id = 'location', component_property = 'value')]
)

def test_output_div2(input_value):
    #input_value = car_format(input_value)
    return 'My Location Type: {}'.format(location_format(input_value))

@app.callback(
    Output(component_id='page-div', component_property = 'children'),
    [Input(component_id = 'page', component_property = 'value')]
)

def test_output_div3(input_value):
    #input_value = car_format(input_value)
    return 'My Page Numbers: {}'.format(input_value)

#@app.callback(
#    Output(component_id='markdown_scrap', component_property = 'children'),
#    [Input(component_id = 'car', component_property = 'value'), Input(component_id = 'location', component_property = 'value'), Input(component_id = 'page', component_property = 'value'), Input(component_id = 'fpath', component_property = 'value'), Input(component_id = 'fname', component_property = 'value'), 
 #    Input(component_id = 'scrap', component_property = 'n_clicks')]
#)

#def test_output_div4(car, location, page, fpath, fname, n_clicks):
#    if n_clicks==0:
#        return textwrap.dedent('''Click the button to scrap''')
#    elif n_clicks>0:
#        if len(fpath)==0 or len(fname)==0:
#            return textwrap.dedent('''Please fill in folder path and csv file name''')
#        elif len(fname)<6:
#            return textwrap.dedent('''Please fill in csv file name to 6 char''')
#        else:
#            return '''{}'''.format(scrap(car, location, page, concate_filepath(fpath,fname)))
            #return 'Location File: {}'.format(concate_filepath(fpath, fname)) + ' len fpath:' , len(fpath) , ' len fname:' , len(fname)

#@app.callback(
 #   Output(component_id='markdown_scrap', component_property = 'children'),
  #  [Input(component_id = 'car', component_property = 'value'), Input(component_id = 'location', component_property = 'value'), Input(component_id = 'page', component_property = 'value'), Input(component_id = 'fsingle', component_property = 'value'),
   #  Input(component_id = 'fsingle', component_property = 'n_submit'),
    # Input(component_id = 'fsingle', component_property = 'n_blur'),
     #Input(component_id = 'scrap', component_property = 'n_clicks')])

#def test_output_div4(car, location, page, fsingle, n_submit, n_clicks):
 #   if n_clicks==0:
  #      return textwrap.dedent('''Click the button to scrap''')
   # elif n_clicks==1:
    #    if len(fsingle)==0:
     #       return textwrap.dedent('''__Please fill in folder path and csv file name__''')
      #  elif n_submit==1:
       #     return '''{}'''.format(scrap(car, location, page, fsingle))
    #else:
        #return '''__Please refresh the page to proceed the next scraping__'''

@app.callback(
   [Output('download-link', 'href'), Output(component_id='markdown_scrap', component_property = 'children')],
    [Input(component_id = 'car', component_property = 'value'), Input(component_id = 'location', component_property = 'value'), Input(component_id = 'page', component_property = 'value')])

def update_download_link(car, location, page):
    dff, scrap_str = scrap(car, location, page)
    csv_string = dff.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
    return csv_string, scrap_str


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns], fixed_rows={ 'headers': True, 'data': 0 },
    style_cell={'width': '100px', 'textAlign': 'left'}, style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'MintCream'#'LightCyan'#'rgb(248, 248, 248)'
        }], style_header={
        'backgroundColor': 'LightCyan', #'rgb(230, 230, 230)',
        'fontWeight': 'bold'
    }, style_as_list_view=True),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200], style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])


@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])

def update_output(list_of_contents, list_of_names, list_of_dates):
    c = list_of_contents
    n = list_of_names
    d = list_of_dates
    if list_of_contents is not None:
        #children = [
            #parse_contents(c, n, d) for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)
        #]
        return parse_contents(c,n,d)
    
def read_mycsv(contents, filename):

    content_type, content_string = contents.split(',')
    #content_type, content_string = [content.split(',') for content in contents]

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))

    except Exception as e:
        print(e)
        return dash.no_update

    return df

#1.FORMING MATRIX D(RowDataAdjust)
def step1 (r, c, x):
    avgs = []
    for i in range(len(x.columns)):
        avg = x.iloc[:, i].mean()
        avgs.append(avg)
    
    MeanAdjustedData = np.zeros((r,c))
    
    minus = 0.0
    for j in range(c): #column
        for i in range(r): #row
            minus = x.iloc[i, j] - avgs[j] 
            MeanAdjustedData[i][j] = minus
            #print(j, i, df1.iloc[i, j], avgs[j], minus, MeanAdjustedData[i][j])
        minus = 0.0
    
    return MeanAdjustedData

#2. FORMING COVARIANCE MATRIX
def step2(r, matrix):
    mymat = np.dot((1/(r-1)), matrix.T)
    mycov = np.dot(mymat, matrix)
    return mycov

#3. CALCULATE EIGENVALUES, EIGENVECTORS
def step3_4(r, matrix):
    import scipy.linalg as la
    A = np.array(matrix)
    results = la.eig(A)
    
    # First column is the first eigenvector
    eigvals, eigvecs = la.eig(A)
    
    #SORTING EIGENVALS WITH CORRESPOND EIGENVECS
    idx = eigvals.argsort()[::-1]   
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:,idx]
    
    #2 COMPONENTS
    feature_vec = np.zeros((r,2))
    
    #copy r rows and c columns from eigvecs
    for j in range(len(feature_vec[0])): #column
        for i in range(len(feature_vec)): #row 
            feature_vec[i][j]=eigvecs[i][j].copy()
            
    return feature_vec

#5 FORM NEW DATA SET
def step5(matrix1, matrix2):
    RowFeatureVecs_ = matrix1.T
    RowDataAdjust = matrix2.T
    FinalData = np.dot(RowFeatureVecs_, RowDataAdjust)
    FinalDataT = FinalData.T
    
    return FinalDataT

def data_label(df):
    prices = []
    inds =[]
    years = []
    mils = []
    for i in range(len(df)):
        price = "Price: " + df['Price'].values[i].astype(str)
        prices.append(price)
        ind = "ID: " + df.index.values[i].astype(str)
        inds.append(ind)
        year = "Year: " + df['Manufactured Year'].values[i].astype(str) #Private
        years.append(year)
        mil = "Mileage: " + df['NewMil'].values[i].astype(str)
        mils.append(mil)

    mytexts = []
    for i in range(len(df)):
        mytext = inds[i] + ", " + prices[i] + ", " + years[i] + ", " + mils[i]
        mytexts.append(mytext)
    
    return mytexts

def pca_plot(FinalData, mytexts):
    return{
        'data': 
        [go.Scatter(x=FinalData[:,0], y=FinalData[:,1], mode="markers", marker = {
            'size':10, 'color':"pink", 'line' : {'width':1, 'color':"black"}
        }, text= mytexts)],
        'layout': go.Layout(
            title='2 Component PCA', 
            xaxis= {'title':'component 1'}, yaxis={'title':'component 2'}, hovermode = 'closest', autosize=True
        )
    }

def myPCA(df):
    #df = read_mycsv(contents, filename)
    strcol = ['Name', 'Mileage', 'CC', 'Condition', 'Link']
    datacol = ['Price', 'Manufactured Year', 'NewMil']
    x = df[datacol]
    y = df[strcol]
    MeanAdjustedData = step1(len(df), len(x.columns), x)
    mycov = step2(len(df), MeanAdjustedData)
    feature_vec = step3_4(len(x.columns), mycov)
    FinalData = step5(feature_vec, MeanAdjustedData)
    return FinalData

def myPCA_plot(df): 
    try:
        #df = read_mycsv(contents, filename)
        FinalData = myPCA(df)
        mytexts = data_label(df)
        
        return textwrap.dedent('''Here is the PCA result:'''), pca_plot(FinalData, mytexts)
    #except IOError as e:
    except Exception as e:
        print (e)
        return textwrap.dedent(str_graph_error), dash.no_update

@app.callback([Output('markdown_pca', 'children'), Output('mypca_graph', 'figure')], [Input('pca', 'n_clicks'), Input('upload-data', 'contents')], [State('upload-data', 'filename')])

def mypca_output(n_clicks, contents, filename):
    if contents is not None:
        df = read_mycsv(contents, filename)
        if n_clicks==0:
            return textwrap.dedent('''Click the button to view PCA result'''), {}
        elif n_clicks>0:     
            return myPCA_plot(df)
    else:
        return textwrap.dedent(str_nt_upload_error), {}

def elbow_label():
    elbow_text = []
    for i in range(15):
        myelbow = 'Cluster, k=' + str(i) 
        elbow_text.append(myelbow)
    return elbow_text

def plot_elbow(Sum_of_squared_distances, elbow_text):    
    return{
        'data': 
        [go.Scatter(x=np.arange(15), y=Sum_of_squared_distances, text = elbow_text)],
        'layout': 
        go.Layout(title='Elbow Method for Optimal k', xaxis=dict(title='k'), yaxis=dict(title='Sum_of_Squared_Distances'), hovermode = 'closest', autosize=True)
        
    }
    
    
def test_k(df):  
    try:
        #df = import_df(lpath.value, lname.value+'.csv')
        FinalData = myPCA(df)
        Sum_of_squared_distances = []
        K = range(1,15)
        for k in K:
            km = KMeans(n_clusters=k)
            km = km.fit(FinalData)
            Sum_of_squared_distances.append(km.inertia_)
        elbow_text = elbow_label()
        return textwrap.dedent('''Here is the elbow result:'''), plot_elbow(Sum_of_squared_distances, elbow_text)
    except Exception as e:
        print (e)
        return textwrap.dedent(str_graph_error), dash.no_update
    
@app.callback([Output('markdown_elbow', 'children'), Output('myelbow_graph', 'figure')], [Input('elbow', 'n_clicks'), Input('upload-data', 'contents')], [State('upload-data', 'filename')])

def elbow_output(n_clicks, contents, filename):
    if contents is not None:
        df = read_mycsv(contents, filename)
        if n_clicks==0:
            return textwrap.dedent('''Click the button to view elbow result'''), {}
        elif n_clicks>0:     
            return test_k(df)
    else:
        return textwrap.dedent(str_nt_upload_error), {} 

def myClustering_k(n, df):
    #df = import_df(lpath.value, lname.value+'.csv')
    mytexts = data_label(df)
    FinalData = myPCA(df)
    kmean = KMeans(n_clusters=n)
    kmean.fit(FinalData)
    ReducedCentroid = kmean.cluster_centers_   
    ReducedLabels = kmean.labels_
    return ReducedCentroid, ReducedLabels, FinalData, mytexts

def myClustering_All(n, df):
    #df = import_df(lpath.value, lname.value+'.csv')
    strcol = ['Name', 'Mileage', 'CC', 'Condition', 'Link']
    datacol = ['Price', 'Manufactured Year', 'NewMil']
    x = df[datacol]
    y = df[strcol]
    kmeanAll = KMeans(n_clusters=n)
    kmeanAll.fit(x)
    AllCentroid = kmeanAll.cluster_centers_
    return AllCentroid

def clustering_plot(matrix, centroid, myktexts, NewCents, ReducedLabels):
    return{
        'data': 
        [
            go.Scatter(x=matrix[:,0], y=matrix[:,1], showlegend=True, name="Points", mode="markers", marker = {
            'size':10, 'line' : {'width':1}, 'color':ReducedLabels}, text= myktexts), 
            go.Scatter(x=centroid[:,0], y=centroid[:,1], showlegend=True, name="Centroids", mode='markers', marker= {'symbol':"x-dot", 'size':12, 'color':'black'}, text= NewCents)
        ],
        'layout': 
        go.Layout(
            title='2 Component PCA (Applied K-Means Clustering)', 
            xaxis= {'title':'component 1'}, yaxis={'title':'component 2'}, hovermode = 'closest', autosize=True
        )
    }
    
def myClustering_KMeans(n, df):
    #n = int(n)
    try:
        AllCentroid = myClustering_All(n, df)
        ReducedCentroid, ReducedLabels, FinalData, mytexts = myClustering_k(n, df)

        AllCentsPrice = []
        AllCentsYr = []
        AllCentsMil = []
        for i in range(len(AllCentroid)):
            AllPrice = 'Price: ' + str(AllCentroid[i][0])
            AllCentsPrice.append(AllPrice)
            AllYr = 'Year: ' + str(AllCentroid[i][1])
            AllCentsYr.append(AllYr)
            AllMil = 'Mileage: ' + str(AllCentroid[i][2])
            AllCentsMil.append(AllMil)

        AllCents = []
        for i in range(len(AllCentsPrice)):
            AllCent = AllCentsPrice[i] + ", " + AllCentsYr[i] + ", " + AllCentsMil[i]
            AllCents.append(AllCent)

        cents = []
        for i in range(len(ReducedCentroid)):
            cent = "Centroid: " + str(i)
            cents.append(cent)

        NewCents = []
        for i in range(len(ReducedCentroid)):
            NewCent = cents[i] + ", " + AllCents[i]
            NewCents.append(NewCent)

        ktexts = []
        for i in range(len(ReducedLabels)):
            ktext = "Cluster: " + ReducedLabels[i].astype(str)
            ktexts.append(ktext)

        myktexts = []
        for i in range(len(FinalData)):
            myktext = ktexts[i] + ", " + mytexts[i]
            myktexts.append(myktext)

        return textwrap.dedent('''Here is the K-Means Clustering result:'''), clustering_plot(FinalData, ReducedCentroid, myktexts, NewCents, ReducedLabels)
        #return NewCents, ktexts
    except Exception as e:
        print (e)
        return textwrap.dedent(str_graph_error), dash.no_update
        

@app.callback([Output('markdown_cluster', 'children'), Output('mycluster_graph', 'figure')], [Input('num_k', 'value'), Input('upload-data', 'contents')], [State('upload-data', 'filename')])  

def mycluster_output(numk, contents, filename):
    n = int(numk)
    if contents is not None:
        df = read_mycsv(contents, filename) 
        if n==0:
            return textwrap.dedent('''Choose num of clusters to view K-Means Clustering result'''), {}
        elif n>0:
            return myClustering_KMeans(n, df)
    else:
        return textwrap.dedent(str_nt_upload_error), {} 

def myBoxplot(df):    
    try: 
        mytexts = data_label(df)
        strcol = ['Name', 'Mileage', 'CC', 'Condition', 'Link']
        datacol = ['Price', 'Manufactured Year', 'NewMil']
        x = df[datacol]
        y = df[strcol]
        btrace0 = go.Box(y=x.iloc[:,0] , boxpoints = "all", jitter=0.3, pointpos=-1.8, showlegend=True, name=x.columns[0], text= mytexts)
        btrace1 = go.Box(y=x.iloc[:,1] , boxpoints = "all", jitter=0.3, pointpos=-1.8, showlegend=True, name=x.columns[1], text= mytexts)
        btrace2 = go.Box(y=x.iloc[:,2] , boxpoints = "all", jitter=0.3, pointpos=-1.8, showlegend=True, name=x.columns[2], text= mytexts)

        #bdata=[btrace0, btrace1, btrace2]
        blayout = go.Layout(title='Boxplot', hovermode = 'closest')
        return textwrap.dedent('''Here is the boxplot result:'''), {
        'data': [btrace0, btrace1, btrace2],
        'layout': blayout
    }
    except Exception as e:
        print (e)
        return textwrap.dedent(str_graph_error), dash.no_update
    
@app.callback([Output('markdown_boxplot', 'children'), Output('myboxplot_graph', 'figure')], [Input('bplot', 'n_clicks'), Input('upload-data', 'contents')], [State('upload-data', 'filename')])

def bplot_output(n_clicks, contents, filename):
    if contents is not None:
        df = read_mycsv(contents, filename)
        if n_clicks==0:
            return textwrap.dedent('''Click the button to view boxplot result'''), {}
        elif n_clicks>0:     
            return myBoxplot(df)
    else:
        return textwrap.dedent(str_nt_upload_error), {} 
    
@app.callback(Output('markdown_id', 'children'), [Input('myads-id', 'value'), Input('upload-data', 'contents')], [State('upload-data', 'filename')])

def mymarkdown_output(myid, contents, filename):
    n = int(myid) 
    if contents is not None:
        df = read_mycsv(contents, filename) 
        m1 = '''Please key in Advertisement ID between 0 to ''' + str(len(df)-1)
        m2 = '''__ID chosen more than maximum Advertisement ID which is__ __''' + str(len(df)-1) + '''__'''
           
        if n==-1:
            return textwrap.dedent(m1)
        elif n>=len(df):
            return textwrap.dedent(m2)
        else:
            m3 = '''Name: {},'''.format(df['Name'].iloc[n]) + ''' Price: {},'''.format(df['Price'].iloc[n]) + ''' Year: {},'''.format(df['Manufactured Year'].iloc[n]) + ''' Mileage: {},'''.format(df['NewMil'].iloc[n]) + ''' EngCC: {},'''.format(df['CC'].iloc[n]) + ''' Condition: {},'''.format(df['Condition'].iloc[n]) + ''' Link: {}'''.format(df['Link'].iloc[n])
            return textwrap.dedent(m3)
    else:
        return textwrap.dedent(str_nt_upload_error)

if __name__ == '__main__':
    app.run_server(debug=True)