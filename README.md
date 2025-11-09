**DISCLAIMER:** prompts are sent to a private render server. these are then returned to your local ollama model. the specific structure isn't disclosed. your data is not stored or logged.

/endpoint → type in the endpoint where Ollama is running on your computer with /api/generate added at the end. for example, if your local host is http://localhost:11434/. in the window, type, http://localhost:11434/api/generate. if you're unsure what to do, search 'help me find my local ollama endpoint'.

/model → type in the name of the model you plan to use, exactly as it appears at https://ollama.com/library. select your model from the Ollama window drop down menu. then, type in the Ollama chat to trigger the download. if the model you plan to use is not available in the Ollama drop down, run it from a terminal window. open a new terminal window and run the model's execution line e.g. 'ollama run gpt-oss:20b'. keep the terminal open. Then, navigate to the research window. You are ready to go! Always close the running terminal before changing models.

/release → this exports the current conversation to your browser downloads; you can drag and drop these releases into the research window as references from previous conversations, just make sure to give the model some context when you do. sometimes, if a conversation is too long or the material is too dense, it's better to condense your thoughts and formulate a new idea as a starting point

/recover → this deletes the last dropped file or the last response from the model, whichever came last, it's just a way to undo what happened last - 0: yes, 1: no

/intro → add a prompt wrapper prefix

/outro→ add a prompt wrapper postfix

/polarity → 0: when in 0 mode, it will use the full problem-solving toolset; 1: when in 1 mode, it will try to answer with yes, no, or give a direct answer

prerequisites: python 3.6+. Ollama if you do not have python, the .command will automatically install it for you on Mac

installation:

Mac:
1. open terminal (command + space, type "terminal")
2. cd to folder: `cd ~/Downloads/research-main`
3. run: `chmod +x start.command`
4. run: `./start.command` (opens UI; keep terminal open)
5. next time: just run `./start.command` from the folder

PC:
1. open the folder where you downloaded the repository
2. double-click `start.bat` (opens UI; keep window open)
3. next time: double-click `start.bat` again

support re:search https://ko-fi.com/researchkofi
