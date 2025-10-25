# re:search 

endpoint: *default = local Ollama endpoint*

model: *default = qwen3:4b* 

/endpoint → endpoint entry screen

/model → model name entry screen

/release → export current interaction 

/select →  drag and drop previous interaction

/recover → undo - 0: yes, 1: no

/polarity → 0: exploration; 1: direct answers

/route → back

*support re:search https://ko-fi.com/researchkofi*

*default model qwen3:4b was chosen at random*

*prerequisites: python 3.6+* 

*re:search made possible by Ollama*

*note: re:search does not maintain state persistence*

*resetting context each response keeps tokens precise*

*refine and re:search*

*************
installation:
*************

download the repository

Mac:

press command + spacebar and type terminal 

press enter or select the terminal icon

navigate to the location where you downloaded the repository

example:

type 

cd ~/Downloads/research-main 

*the location where you downloaded the repository; that may differ from the location above*

press enter

type

chmod +x start.command

*allows the start.command on your Mac*

press enter

type

./start.command

*leave the terminal running...*

done

*double clicking the index.html will reopen the re:search terminal*

*after the first run, the server can easily be ran by dragging and dropping the start.command into an empty terminal*

PC: 

start.bat included

yet to test 

if 'one clicking' start.bat fails

files may run separately 

TBD
