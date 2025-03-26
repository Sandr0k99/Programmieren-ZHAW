# -*- coding: utf-8 -*-
"""
@author: rots
"""

# --- imports ---
from menu_entry import MenuEntry



# -- class ---
class Menu:
    # --- methods ---
    def __init__(
        self,
        new_heading = "",
        new_prompt  = "Please enter selection: ",
        new_wrong_selection_message = "Selection not valid."
    ):
        '''
        setup menu
        - heading:                  title of menu
        - prompt:                   ask user to select an entry
        - wrong_selection_message:  error message if user's selection is invalid
        '''
        self._heading = new_heading
        self._prompt  = new_prompt
        self._wrong_selection_message = new_wrong_selection_message

        self._entries_by_hotkey = {}  # menu entries accessible by hotkey

    
    
    
    def _show(self):
        '''
        show menu with heading (if present) and all its menu entries
        '''

        # show underlined heading if present
        if self._heading != "":
            print(self._heading)
            print("~" * len(self._heading))
        
        # show each menu entry
        for hotkey, entry in self._entries_by_hotkey.items():
            title  = entry.get_title()
            print(f"{hotkey:>3}  {title}")
    
    
    
    def _show_error_selection_not_valid(self):
        '''
        show error message if user's selection is not valid
        '''
        print()
        print("ERROR:", self._wrong_selection_message)
        print()
    

    
    def add_entry(self, new_entry):
        '''
        add new menu entry
        - do nothing if hotkey already exists
        '''
        hotkey = new_entry.get_hotkey()
        if hotkey not in self._entries_by_hotkey:
            self._entries_by_hotkey[hotkey] = new_entry
    
    
    
    def choose(self):
        '''
        let user choose a menu entry and call its function
        '''
        called = False

        while not called:
            self._show()
            
            selection = input(self._prompt)
            entry     = self._entries_by_hotkey.get(selection)

            if entry:
                entry.call()
                called = True
            else:
                self._show_error_selection_not_valid()



# --- main ---
if __name__ == "__main__":
    # example usage of menu with submenu

    # main menu functions
    def first():
        print("first()")
    
    def second():
        print("second()")
    
    # sub menu functions
    def alpha():
        print("alpha()")
    
    def beta():
        print("beta()")
    
    # prepare menus
    main_menu = Menu(
        "Main Menu",
        "Make your choice! ",
        "Wrong choice, try again ..."
    )
    
    sub_menu = Menu(
        "Sub Menu"
    )

    # add menu entries
    main_menu.add_entry(MenuEntry("first" , "1", first , sub_menu ))
    main_menu.add_entry(MenuEntry("second", "2", second           ))
    
    sub_menu.add_entry( MenuEntry("alpha" , "a", alpha , main_menu))
    sub_menu.add_entry( MenuEntry("beta"  , "b", beta  , main_menu))
    
    # start with main_menu
    main_menu.choose()
