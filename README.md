# linkedin_screenshot
A super simple script for screenshotting my linkedin profile daily (i'm running a short experiment to see if posting is useful). 

The code is written in python using selenium to automate account login and uses chrome dev tools to save the screenshot as a mhtml file. Utilises Windows task scheduler to run it at set times daily.

## Installation manual
1. Download the `Linkedin_Snapshot.py` file onto your device
1. Make sure python is installed on your device. Once python is installed, install selenium via this command:
`pip install selenium`
2. Within `Linkedin_Snapshot.py` change your username and password to your linkedin login
3. Afterwards Change the url in `driver.get("https://www.linkedin.com/in/florachan010/")` to your own profile page url
4. Run the program via `python Linkedin_Snapshot.py` and watch the magic happen. The snapshot will be saved to the same path as where the script is running from.

### What is task scheduler?


### What is .MHTML?
MHTML (MIME HTML) is a web page archive format that combines a page's HTML code and its external resources (images, audio, CSS) into a single file with a .mhtml or .mht extension. Used for offline viewing, it ensures a page remains intact, though it is less common today compared to traditional HTML or PDF saves.
