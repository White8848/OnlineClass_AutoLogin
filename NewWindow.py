#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Yirule

import PySimpleGUI as sg


def new_win():
    # Create some widgets
    text = sg.Text("What's your name?")
    text_entry = sg.InputText()
    ok_btn = sg.Button('OK')
    cancel_btn = sg.Button('Cancel')
    layout = [[text, text_entry],
              [ok_btn, cancel_btn]]

    # Create the Window
    window = sg.Window('Hello PySimpleGUI', layout)

    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            # User closed the Window or hit the Cancel button
            break
        print(f'Event: {event}')
        print(str(values))

    window.close()


if __name__ == "__main__":
    new_win()
