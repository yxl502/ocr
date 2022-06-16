import os
import cv2

# img_lists = os.listdir('./train')
#
# for i in img_lists:
#     img = cv2.imread('./train/' + i)
#     cv2.imshow(str(i), img)
#
#     cv2.waitKey()
#     cv2.destroyAllWindows()


with open('./train.txt', 'r') as f:
    data = f.readlines()
    for d in data:
        d = d.strip()
        path = d.split('\t')[0]
        label = d.split('\t')[1]
        print(path)
        print(label)

        img = cv2.imread(path)
        cv2.imshow(label, img)

        cv2.waitKey()