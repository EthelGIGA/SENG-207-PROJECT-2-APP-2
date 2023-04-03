import qrcode
import PySimpleGUI as sg
from PIL import ImageTk, Image

def generate_qr_code(text):
    qr_code = qrcode.QRCode(version=1, box_size= userSize, border=2,  error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr_code.add_data(text)
    qr_code.make(fit=True)

    qr_code_image = qr_code.make_image(fill_color= userColor, back_color="white")
    return ImageTk.PhotoImage(qr_code_image)

sg.theme('DarkGrey10') 


layout = [
    [sg.Text('Enter text to encode as QR code:',background_color='#022b61')],
    [sg.InputText(key='-INPUT-',background_color='white',text_color='black')],
    [sg.Text('QR CODE Color:',background_color='#022b61',), sg.Combo(values=['blue','green','red','orange','purple' ], default_value='black',key='color',background_color='white',text_color='black'), ],
    [sg.Text('Size:',background_color='#022b61'), sg.Slider(range=(1, 20), default_value=10, orientation='h', key='size')],
    [sg.Button('Create', key='-CREATE-',button_color='#cf7c08')],
    [sg.Image(key='-IMAGE-')]
]


window = sg.Window('Realmz QR Code Generator', layout, background_color='#022b61')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-CREATE-':
        text = values['-INPUT-']
        userColor = values['color']
        userSize = values['size']
        if text.strip() == "":
            sg.popup_error('Input text cannot be empty.')
            continue

        try:
            qr_code_image = generate_qr_code(text)
        except:
            sg.popup_error('Invalid text input. Please try again.')
            continue


        window['-IMAGE-'].update(data=qr_code_image)
        


window.close()