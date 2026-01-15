# Code repository for Data Management I course 

This repo contains some code discussed during the "Data Management I" course of the MSc programme Applied Informatics of the Department of Informatics and Telematics

## Budibase API examples

The repo contains the following files related to the Budibase API:
- `budiapi.py` : a first encounter with the Budibase API.
- `budilib.py` : the "proper" way of writing a small library module for handling requests using the Budibase API.
- `read_budi_table.py` : example of how to use `budilib.py` to read data from a budibase table.

You need to obtain your budibase API key as discussed in the classroom: on the bottom left corner click on your user email or icon and choose ``View API key''

<img width="686" height="349" alt="image" src="https://github.com/user-attachments/assets/22373ab8-2d57-4734-a96a-a9cce9a09776" />

## Examples using the Gmail API

The repo contains the following files to test the Gmail API:
- `gmaillib.py` : a Python module for sending an e-mail with Gmail API
- `test_gmail.py` : an example for using `gmaillib.py`

### Obtain your Gmail credentials file
To work with these files you need to obtain your credentials at [Google Cloud](https://cloud.google.com). Follow the previous link and click on "Console". You will be directed to the Google Cloud console where you will need to create a new project. There may be a new project already created for you named "My First Project" or something similar. Click on it to access other projects:

<img width="850" height="478" alt="image" src="https://github.com/user-attachments/assets/82156f83-04b0-4f49-b787-7ae82973d2d8" />
<br />  
<br />  
Then click on "New Project" and enter a cool name for your project and click "Create"
<br />
<br />

<img width="955" height="519" alt="image" src="https://github.com/user-attachments/assets/b9676c04-52de-4d3a-ba24-f3f5d4ae6dba" />
<br />  
<br />  
Select your project and on the search bar on the right of your project name search for "Gmail API". Click on the Gmail API on the search results and then click "Enable" to enable it.
<br />  
<br /> 
<img width="956" height="350" alt="image" src="https://github.com/user-attachments/assets/5b1a89e2-eeee-4a58-84f8-115a1c7db67d" />
<br />  
<br />  
After you enable it you will be directed in the API/Service Details screen. To use the API you will need to first configure a consent screen. Go to "Credentials" on the menu to your left and then click "Configure consent screen"
<br />  
<br />  
<img width="936" height="645" alt="image" src="https://github.com/user-attachments/assets/34d99bcb-33cf-41d6-a9ad-6a7c74adeee5" />
<br />  
<br />  
Then click "Get Started" and create your App Information. Give a cool name to your app and enter your email as "User support email", then click "Next"
<br />  
<br />  
<img width="916" height="434" alt="image" src="https://github.com/user-attachments/assets/edc208cc-94c1-43fd-a993-07ad316a35fd" />
<br />  
<br /> 
Then choose "Internal" as Audience and click "Next" then enter your email information again on the "Contact Information" and click "Next". Finally agree to the user data policy and click "Continue" and then "Create". Once the Auth screen has been configured, you need to create a client for your Python scripts. So from the menu to your right go to "Clients" and click on "+Create client"
<br />  
<br />  
<img width="960" height="365" alt="image" src="https://github.com/user-attachments/assets/72d70683-2118-48e6-b426-a8fc680d1176" />
<br />  
<br />  
Choose "Desktop App" give another cool name to your client and click "Create"
<br />  
<br />  
<img width="961" height="519" alt="image" src="https://github.com/user-attachments/assets/26321dda-a3d2-43b0-9262-60a39ae132ba" />
<br />  
<br />  
After the client has been created you can download the credentials file by clicking "Download JSON"
<br />  
<br />  
<img width="787" height="245" alt="image" src="https://github.com/user-attachments/assets/0169e783-de74-4107-9b3c-d04b9a32c3b0" />
<br />  
<br />  

### Credentials file
Do not loose this file, and do not share it with anyone else!!!
After you have downloaded it, rename it to 
```
creds.json
```
and copy it to the location where the Python files are stored. The first time you use the `gmaillib.py` module you will be asked to provide consent using a Web browser.













