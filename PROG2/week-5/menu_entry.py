# -*- coding: utf-8 -*-
"""
@author: rots
"""

# --- class ---
class MenuEntry:
    def __init__(self, title, hotkey, function, next_menu = None):
        '''
        setup menu entry
        - title:    title of menu entry
        - hotkey:   hotkey of menu entry
        - function: function to be called if user selects this menu entry
        - menu:     menu to return to after function call
        '''
        self._title     = title
        self._hotkey    = hotkey
        self._function  = function
        self._next_menu = next_menu



    def get_title(self):
        '''
        return title of menu entry
        '''
        return self._title
    


    def get_hotkey(self):
        '''
        return hotkey of menu entry
        '''
        return self._hotkey
    


    def call(self):
        '''
        - call function of menu entry
        - afterwards call menu to return to if available
        '''
        if self._function:
            self._function()
            if self._next_menu:
                self._next_menu.choose()



if __name__ == "__main__":
    # example usage of MenuEntry
    def test_function(text = ""):
        print(f"test_function({text}) called")

    menu_entry = MenuEntry("test menu entry", "t", test_function)
    hotkey = menu_entry.get_hotkey()
    title  = menu_entry.get_title()
    print(f"{hotkey:>3}  {title}")
    menu_entry.call()
