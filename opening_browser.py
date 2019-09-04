#!/usr/bin/env python3

import webbrowser

a_website = "https://www.google.com"

# Open url in a new window of the default browser, if possible
webbrowser.open_new(a_website)

# Open url in a new page (“tab”) of the default browser, if possible
webbrowser.open_new_tab(a_website)

webbrowser.open(a_website, 1) # Equivalent to: webbrowser.open_new(a_website)
webbrowser.open(a_website, 2) # Equivalent to: webbrowser.open_new_tab(a_website)
