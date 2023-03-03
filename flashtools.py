'''

made by @host008



NOTE: i suck at programming
'''


import PySimpleGUI as sg
import shutil, os
html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <script src="https://unpkg.com/@ruffle-rs/ruffle"></script>
    <script>
        window.onload = function() {
            var game = document.getElementById("game");
            var width = window.innerWidth;
            var height = window.innerHeight;
            game.style.width = width + "px";
            game.style.height = height + "px";
        }
    </script>
    <style>
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
    </style>
</head>
<body>
    <embed src="game.swf" type="application/x-shockwave-flash" id="game">
</body>
</html>
'''

gui = [
    [sg.Text('Flash Game Creator')],
    [sg.Text('Flash Game Name:'), sg.InputText(key = 'game_name')],
    [sg.Text('Flash Game Location:'), sg.InputText(), sg.FileBrowse(key = 'game_location')],
    [sg.Text('Directory to save to:'), sg.InputText(), sg.FolderBrowse(key = 'save_location')],
    [sg.Text('Folder Name:'), sg.InputText(key = 'folder_name')],
    [sg.Text('Splash/Logo Image: '), sg.InputText(), sg.FileBrowse(key = 'splash_image')],
    [sg.Checkbox('Generate a JSON Template', key = 'json')],
    [sg.Button('Create'), sg.Button('Exit')],
    [sg.Text('JSON Template Output:')],
    [sg.Output(size = (50, 10), key = 'output')],
    [sg.Text('Made by @host008')]
]
flashtools = sg.Window('Flash Game Creator', gui)
while True:
    events, values = flashtools.read()
    if events == sg.WIN_CLOSED or events == 'Exit':
        break
    if events == 'Create':
        if values['game_location'] == '' or values['save_location'] == '' or values['folder_name'] == '' or values['splash_image'] == '':
            sg.popup('Please fill in all fields.')
        else:
            os.mkdir(values['save_location'] + '/' + values['folder_name'])
            with open(values['save_location'] + '/' + values['folder_name'] + '/index.html', 'w') as f:
                f.write(html)
            shutil.copy(values['game_location'], values['save_location'] + '/' + values['folder_name'] + '/game.swf')
            shutil.copy(values['splash_image'], values['save_location'] + '/' + values['folder_name'] + '/splash.png')
            if values['json']:
                flashtools.find_element('output').Update('''
    {
        "name": "%s",
        "root": "%s",
        "file": "index.html",
        "img": "splash.png"
    },''' % (values['game_name'], values['folder_name']))    
            sg.popup('Done!')