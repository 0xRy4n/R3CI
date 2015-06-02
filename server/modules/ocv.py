import cv
import base64

"""
''' Handles requests from the server
'''
''' {
'''     "img": "<b64 encoded image>"
''' }
"""

def handle(req, database):
	if "img" in req:
		img = base64.decode(req["img"])

	return {}
