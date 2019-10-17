import os
import subprocess


if(os.path.exists("clientside.py") and os.path.exists("serverside.py")):
  subprocess.run("py clientside.py  & py serverside.py", shell=True)
else:
    print("Clientside.py or serverside.py is not available")
