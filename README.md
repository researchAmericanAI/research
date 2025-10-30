# researchAmericanAI

/endpoint → type in the endpoint where Ollama is running on you computer with /generate at the end. for example, my local host is http://localhost:11434/. in the window, i type, http://localhost:11434/generate. if you're unsure what to do, search ' help me find my local ollama endpoint' using any chatbot. they will explain.

/model → type in the name of the model that you are currently wanting to use exactly as it appears in the Ollama library (https://ollama.com/library) you can use a model from the Ollama window by selecting it from the drop down menu, typing to Ollama once to trigger the download for the model, and then navigating back to the research window. if it is not available from the drop down, you will instead have to run it from a terminal window. open a new terminal window and run the model's execution line from the ollama website's library e.g. 'ollama run gpt-oss:20b'. keep the terminal open while you use it, and close it before you change to another one.

/release → this exports the current conversation to your browser downloads; you can drag and drop them into the research window as references from previous conversations, just make sure to give the model some context when you do. sometimes, if a conversation is too long or the material is too dense, it's better to condense your thoughts and formulate a new idea as a starting point

/recover → this deletes the last dropped file or the last response from the model, whichever came last, it's just a way to undo what happened last - 0: yes, 1: no

/polarity → 0: when you have it in 0 mode, it will try to answer with the full 55 problem-solving tools; 1: when you have it in 1 mode, it will try to answer with yes, no, or give a direct answer

*prerequisites: python 3.6+. Ollama* 
*if you do not have python, the .command will automatically install it for you on Mac*

*************
installation:
*************

Mac:

press command + spacebar and type terminal 

use enter on the keyboard or select the icon

enter the following:

cd ~/Downloads/research-main *(the location where you downloaded the repository may differ)*

chmod +x start.command *(allows the start.command on your Mac)*

./start.command *(opens index.html, the UI. clicking index in the folder will reopen the UI if you lose it.)*

*leave the terminal running...*

*after the first time you run the chmod +x start.command, the server can simply be ran by executing the start.command from the root folder in an empty terminal window*

run! 

PC: 

start.bat included

i couldn't test

if 'one clicking' start.bat fails

files may run separately 

i'm awaiting feedback

i hope it works and doesn't cause any trouble

enjoy!

*support re:search https://ko-fi.com/researchkofi*
