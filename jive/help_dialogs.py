from PyQt5.QtWidgets import QMessageBox

from jive import config as cfg


def open_about(parent):
    text = f"""
<strong>Jabba's Image Viewer {cfg.VERSION}</strong>

<a href="https://github.com/jabbalaci/JiVE-Image-Viewer">https://github.com/jabbalaci/JiVE-Image-Viewer</a>

Laszlo Szathmary (Jabba Laci), 2018
jabba.laci@gmail.com
""".strip().replace("\n", "<br>")
    QMessageBox.about(parent, "About", text)