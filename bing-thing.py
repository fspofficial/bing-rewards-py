# Script Made by True Syanic /ioinf PrathviKushwaha / Prathviraj Kushwaha / fspofficial <3
import pyautogui
import random
import time

# List of keywords related to Python
keywords = ['python', 'programming', 'data', 'science', 'machine', 'learning', 'neural', 'networks', 'artificial', 
            'intelligence', 'algorithm', 'logic', 'loop', 'list', 'tuple', 'dictionary', 'set', 'function', 
            'module', 'package', 'class', 'object', 'inheritance', 'polymorphism', 'encapsulation', 'abstraction', 
            'exception', 'handling', 'debugging', 'testing', 'automation', 'web', 'development', 'backend', 'frontend', 
            'database', 'sql', 'nosql', 'django', 'flask', 'pyramid', 'fastapi', 'numpy', 'pandas', 'matplotlib', 
            'seaborn', 'scipy', 'scikit-learn', 'tensorflow', 'keras', 'pytorch', 'opencv', 'pygame', 'pygtk', 
            'wxpython', 'pytest', 'unittest', 'selenium', 'beautifulsoup', 'requests', 'asyncio', 'multithreading', 
            'concurrency', 'sockets', 'network', 'security', 'encryption', 'hashing', 'logging', 'pickle', 'json', 
            'yaml', 'xml', 'html', 'css', 'javascript', 'jquery', 'react', 'angular', 'vue', 'node', 'express']

# Loop indefinitely
while True:
    # Choose a random keyword
    keyword = random.choice(keywords)

    # Type the keyword
    pyautogui.typewrite(keyword)

    # Double-click the mouse
    pyautogui.doubleClick()

    # Press the Enter key
    pyautogui.press('enter')

    # Pause for 4 seconds
    time.sleep(4)

    # Scroll down 3 times
    pyautogui.press('pagedown')
    pyautogui.press('pagedown')
    pyautogui.press('pagedown')

    # Pause for 1 second
    time.sleep(1)

    # Scroll up 3 times
    pyautogui.press('pageup')
    pyautogui.press('pageup')
    pyautogui.press('pageup')

    # Pause for 1 second
    time.sleep(1)
