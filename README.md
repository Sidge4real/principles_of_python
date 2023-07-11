# Python installation
Hi, I got some issues with installing python. I hear others has it too, so if you visit this resporitory out of intrest, you can find solution to those problems.
- [Install python](https://www.python.org/) on your computer, if u didn't yet
- Make sure if you installed an edtor, example [visual studio code](https://code.visualstudio.com/)
- Make sure you installed recommended/stable versions

At the moment I've Python 3.11.4, with this version I got 2 issues
1. Python not found
2. Python 'pip install' command not found

# Fix issues
I only can explain for windows, might be same resolution for other OS, but not sure!
1. Search on your windows search: advanced system settings
2. click on envirement variables (yellow marked)
<img src="https://github.com/Sidge4real/principles_of_python/blob/master/images/advanced_system_stettings.PNG">
3. Choose 'PATH', to add a path to your system paths.
<img src="https://github.com/Sidge4real/principles_of_python/blob/master/images/add_path_windows.PNG">
4. Click 'new' and fill in the link you gonna search in step 5
<img src="https://github.com/Sidge4real/principles_of_python/blob/master/images/enviremnt_var.PNG">

5. push windows key and 'R' together and fill in the small window '%appdata% , it will bring you to the application data files
   - You gonna search for python or python311 or other named map with 'python' init.
Like these paths:
   > C:\Users\[pc_user_name]\AppData\Local\Programs\Python\Python311\python   [python itself to run]
   > C:\Users\[pc_user_name]\AppData\Local\Programs\Python\Python311\Scripts  [scripts, inclusive 'pip install' command]
6. Copy those paths, check that it's not '/' , but '\' and add them to the screen where you where on location to add paths
7. click 'ok' and restart 'visual studio code'

 It should work fine now.

 # Extentions
With the links you can find extentions for python:
 - https://marketplace.visualstudio.com/items?itemName=ms-python.python
 - https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance

Other:
- https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode
- https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare
- https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client

# Extra's
Thunder client:
- Using thunder client inside visual studio code, you can test api's for response and data.
- https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client
Postman:
- Using postman as app or in browser app, you can do same things as thunder client


