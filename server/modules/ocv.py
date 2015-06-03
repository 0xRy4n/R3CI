from os.path import exists
import cv2
import base64

CLASSIFIER_DIR = "classifiers/"

classifiers = {}

def init(sender, classifierName):
	if exists(CLASSIFIER_DIR + classifierName + ".xml"):
		classifiers[sender] = cv2.CascadeClassifier(CLASSIFIER_DIR + classifierName + ".xml")
		return True
	else:
		return False

def detect(sender, img):
	#TODO: Actually implement this.
	pass

"""
''' Handles requests from the server
'''
''' {
'''     "img": "<b64 encoded image>"
''' }
"""

def handle(sender, req, database, logger):
	rv = {}
	if "img" in req:
		img = base64.decode(req["img"])
		rv = detect(sender, img)

	return {}
