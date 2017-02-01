import cv2
import os

def FaceDetect(img, img_name_prefix = "", face_img_save_folder = "./"):
	face_cascade_classifier = cv2.CascadeClassifier(r"./haarcascade_frontalface_default.xml")

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade_classifier.detectMultiScale(gray, 1.2, 5)
	if len(faces) == 0:
		return None

	face_img = img
	index = 0
	for (x, y, w, h) in faces:
		cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
		if __name__ != "__main__":
			current_face_img_save_fiepath = os.path.join(face_img_save_folder, "%s_%d.jpg" % (img_name_prefix, index))
			cv2.imwrite(current_face_img_save_fiepath, img[y:y+h, x:x+w])
			index = index + 1

	if __name__ == "__main__":
		cv2.imshow("faces", face_img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	return faces

def test():
	test_img_folder = "./test"
	imgList = os.listdir(test_img_folder)
	print "#img\t%d" % (len(imgList))
	imgList = map(lambda x : os.path.join(test_img_folder, x), imgList)
	for img_path in imgList:
		print img_path
		img = cv2.imread(img_path)
		detect_result = FaceDetect(img)
		 


if __name__ == "__main__":
	test()
