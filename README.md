DISCLAIMER: prompts are sent to a private render server. it wraps them in a problem-solving framework. these are then returned to your local ollama model. the specific structure isn't disclosed. your data is not stored or logged. if you need fully local operation with no external calls, this is not for you.

researchAmericanAI uses problem-solving analysis with Ollama models 

/endpoint → type in the endpoint where Ollama is running on your computer with /api/generate added at the end. for example, if your local host is http://localhost:11434/. in the window, type, http://localhost:11434/api/generate. if you're unsure what to do, search 'help me find my local ollama endpoint'.

/model → type in the name of the model you plan to use, exactly as it appears at https://ollama.com/library. select your model from the Ollama window, type and enter anything in the window to trigger the download. if the model you plan to use is not available in the Ollama window, you will instead have to run it from a terminal window. open a new terminal window and run the model's execution line e.g. 'ollama run gpt-oss:20b'. keep the terminal open. Then, navigate to the research window. You are ready to go! Always close the running terminal before changing to another model. 

/release → this exports the current conversation to your browser downloads; you can drag and drop them into the research window as references from previous conversations, just make sure to give the model some context when you do. sometimes, if a conversation is too long or the material is too dense, it's better to condense your thoughts and formulate a new idea as a starting point

/recover → this deletes the last dropped file or the last response from the model, whichever came last, it's just a way to undo what happened last - 0: yes, 1: no

/polarity → 0: when you have it in 0 mode, it will use the full problem-solving toolset; 1: when you have it in 1 mode, it will try to answer with yes, no, or give a direct answer

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

PC: 

start.bat included

*support re:search https://ko-fi.com/researchkofi*
