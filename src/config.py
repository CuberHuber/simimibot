import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')
VERSION = os.environ.get('VERSION')
AUTODELETE = int(os.environ.get('AUTODELETE'))
AUTODELETECOMMAND = int(os.environ.get('AUTODELETECOMMAND'))
INTERVAL = int(os.environ.get("INTERVAL"))
CHAT = int(os.environ.get('CHAT'))
TOPLIMIT = int(os.environ.get('TOPLIMIT'))
WORD_FOR_TRUE_MESSAGE = int(os.environ.get('WORD_FOR_TRUE_MESSAGE'))

dev = True if VERSION.lower() == "dev" else False
