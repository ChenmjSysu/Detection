import os
import datetime
import time
import VideoCapture
import FaceDetection

def run(capture, captured_img_save_folder, face_img_save_folder):
	print datetime.datetime.now(),
	captured_img_filepath, img = VideoCapture.WriteImage(capture, captured_img_save_folder)
	face_detect_result = FaceDetection.FaceDetect(img, os.path.basename(captured_img_filepath.split(".jpg")[0]), face_img_save_folder)
	if face_detect_result is None:
		print "OK"
		return

	print "%d faces detected" % len(face_detect_result)

def CheckIsExist(folder):
	if not os.path.isdir(folder):
		os.mkdir(folder)

if __name__ == "__main__":
	captured_img_save_folder = "./CapturedImg"
	face_img_save_folder = "./FaceImg"
	CheckIsExist(captured_img_save_folder)
	CheckIsExist(face_img_save_folder)

	capture = VideoCapture.TurnOnCam()
	while True:
		run(capture, captured_img_save_folder, face_img_save_folder)
		time.sleep(1)