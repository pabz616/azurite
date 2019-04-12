# azurite
```
Welcome! This is where my PYTEST works will go.
```
Setup
```
Set up environment in PyCharm IDE (Professional / Community)
https://www.jetbrains.com/pycharm/download/
```

Install packages
```
pip Install behave (if this is the agreed-to solution, otherwise skip)
pip install pytest (https://pypi.org/project/pytest/)
```

Install assertions (options incl.)
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

Basic Waits to use
```
...because we will need this for AJAX / LATENT sites

Implicit Wait
...polls the dom for a specified set of time (ms)
example: driver.implicitly_wait(t), where t = time (in ms)

Explicit Wait
...waits for a specified condition to occur
example: 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

example: 
try:
     my_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "x"))
     my_element.click()
except:
     print(some message stating its not present)
src: https://seleniumhq.github.io/selenium/docs/api/java/org/openqa/selenium/support/ui/ExpectedConditions.html
```

Install screenshot library (if not using driver default)
```
pip install pyautogui (for screenshots, 
.. naming convention - use pyautogui.screenshot(path_to_folder+name_of_test+timestamp.png)

Might need to install:
- pip3 install pyobjc-core
- pip3 install pyobjc
- pip3 install pyautogui
```
