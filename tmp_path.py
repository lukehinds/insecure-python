import os
import tempfile


filename = 'evil-file.vbs'
tmp = os.path.join(tempfile.gettempdir(), filename)
if not os.path.exists(tmp):
    with open(tmp, "w") as file:
        file.write("defaults")
