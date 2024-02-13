#size
APP_SIZE=(400,700)
MAIN_ROWS = 7
MAIN_COLUMNS=4


#size login window 
LOGIN_WINDOW_SIZE = (600,400)

#text
FONT='Montserrat'
OUTPUT_FONT_SIZE=70
LOGIN_TITLE_FONT_SIZE=25
BUTTON_FONT_SIZE=12

STYLING = {
    'gap':0.5,
    'button-corner-radius':12
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

COLORS ={
    'blue-sky':{'fg':'#00A0FF','hover':'#197EBA','text':'white',},
    
    'dark-gray':{'fg':('#D4D4D2','#505050'),'hover':('#efefed','#686868'),'text':('black','white')},
    
    'orange':{'fg':'#FF9500','hover':'#ffb143','text':('black','white')},
 
    'orange-highlight':{'fg':'white','hover':'white','text':('black','#FF9500')},    
}

TITLE_BAR_HEX_COLORS = {
    'dark': 0x00000000,
    'light':0x00EEEEEE
}
BLACK='#000000',
WHITE='#EEEEEE'