import cv2
import os
import datetime

def FormatedDatetime():
	return datetime.datetime.now().strftime('%b_%d_%y_%H_%M_%S');

def TurnOnCam():
	capture = cv2.VideoCapture(0)
	size = (int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
		int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
	video = cv2.VideoWriter("video.avi", cv2.cv.CV_FOURCC("I", "4", "2", "0"), 30, size)

	print "Camera ready: ", capture.isOpened()

	return capture

def WriteImage(capture, img_save_folder = "./"):
	ret, img = capture.read()
	if __name__ == "__main__":
		cv2.imshow("img", img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	save_filepath = os.path.join(img_save_folder, FormatedDatetime() + ".jpg")
	cv2.imwrite(save_filepath, img)
	return save_filepath, img

def test():
	capture = TurnOnCam()
	WriteImage(capture)

if __name__ == "__main__":
	test()