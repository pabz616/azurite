# azurite
```
Welcome! This is where my PYTEST works will go.
```
setup
```
Set up environment in PyCharm IDE (Professional / Community)
https://www.jetbrains.com/pycharm/download/
```

install packages
```
pip Install behave (if this is the agreed-to solution, otherwise skip)
pip install pytest (https://pypi.org/project/pytest/)
```

install assertions (options incl.)
```
pip install PyHamcrest (latest version)
pip nose
```

Basic Assertions to use
```
Assert.assertEquals(actual, expected)
assert.element.is_displayed() .. (a section of the page)
assert some text in self.driver.page_source (the entire page)
```

install screenshot library (if not using driver default)
```
pip install pyautogui (for screenshots, 
.. naming convention - use pyautogui.screenshot(path_to_folder+name_of_test+timestamp.png)

Might need to install:
- pip3 install pyobjc-core
- pip3 install pyobjc
- pip3 install pyautogui
```
