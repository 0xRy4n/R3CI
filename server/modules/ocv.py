from os.path import exists
import cv2
import base64

CLASSIFIER_DIR = "classifiers/"

classifiers = {}

def init(server, logger, sender, req):
	if req["classifier"]:
		if exists(CLASSIFIER_DIR + req["classifier"] + ".xml"):
			classifiers[sender] = cv2.CascadeClassifier(
				CLASSIFIER_DIR + req["classifier"] + ".xml")

			logger.info("Added classifier ({}) for user {}".format(
				(CLASSIFIER_DIR + req["classifier"] + ".xml"), sender))
		else:
			logger.info("Could not add classifier ({}) for user {}".format(
				(CLASSIFIER_DIR + req["classifier"] + ".xml"), sender))

	return {}

def delete(server, logger, sender):
	if sender in classifiers:
		del classifiers[sender]


def detect(sender, img):
	#TODO: Actually implement this.
	pass

"""
''' Identifies classified robots in image
'''
''' Client sends a base64 encoded image:
''' {
'''     "img": "<b64 encoded image>"
''' }
'''
''' Returns:
''' {
'''     "<uid>": "name",
'''     ... for however many robots are in image
''' }
"""

def handle(sender, req, database, logger):
	rv = {}
	if "img" in req:
		img = base64.decode(req["img"])
		rv = detect(sender, img)

	return {}
