#size
APP_SIZE=(400,700)
MAIN_ROWS = 7
MAIN_COLUMNS=4


#size login window 
LOGIN_WINDOW_SIZE = (600,400)

#text
FONT='Poppins'
OUTPUT_FONT_SIZE=70
LOGIN_TITLE_FONT_SIZE=25
TITLE_FONT_SIZE = 20
BUTTON_FONT_SIZE=14
NORMAL_SIZE=12


STYLING = {
    'gap':0.5,
    'button-corner-radius':15
}

NUM_POSITIONS={
    '.':{'col':2 , 'row':6 , 'span':1},
    0:{'col':0 , 'row':6 , 'span':2},
    1:{'col':0 , 'row':5 , 'span':1},
    2:{'col':1 , 'row':5 , 'span':1},
    3:{'col':2 , 'row':5 , 'span':1},
    4:{'col':0 , 'row':4 , 'span':1},
    5:{'col':1 , 'row':4 , 'span':1},
    6:{'col':2 , 'row':4 , 'span':1},
    7:{'col':0 , 'row':3 , 'span':1},
    8:{'col':1 , 'row':3 , 'span':1},
    9:{'col':2 , 'row':3 , 'span':1},
}


OPERATORS = {
    'clear' : {'col':0 , 'row':2, 'text':'AC', 'image path' :None},
    'invert' : {'col':1 , 'row':2, 'text':'', 'image path':{'light':'images/invert button dark.png ','dark':'images/invert button light.png'}},
    'percent' : {'col':2 , 'row':2, 'text':'%', 'image path':{'light':'images/inverts'}},
}

IMAGE_LINKS={
    'logoLepharma':'D:\\Work\\Projet GEKATON\\Projet LEPHARMA\\codage\\Lepharma Software\\app\\images\\lepharmaLogo.png',
    'userProfile':'D:\\Work\\Projet GEKATON\\Projet LEPHARMA\\codage\\Lepharma Software\\app\\images\\userProfil.png'
}

COLORS ={
    #accent color
    'blue-sky':{'fg':'#00A0FF','hover':'#197EBA','text':'white',},
    
    #for buttons
    'gray':{'fg':'#F1F1F1','hover':'#D9D9D9','text':'black',},
    #dark color
    'primary':{'fg':'#142D63','text':'#4B5563','hover':'#3057AB'},
   
    'orange':{'fg':'#FF9500','hover':'#ffb143','text':('black','white')},
 
    'text-color':{'fg':'#FF9500','title':'#142D63','text':'#4B5563'},
    
    'light':{'fg':'#F1F4F8','title':'#142D63','text':'#4B5563'},
       
}

TITLE_BAR_HEX_COLORS = {
    'dark': 0x00000000,
    'light':0x00EEEEEE
}
BLACK='#000000',
WHITE='#EEEEEE'