import xml.etree.ElementTree as ET
from os import listdir, remove, rename

#IMAGE_DIR = "Dataset/train/images"
#ANNOT_DIR = "Dataset/train/annotations"
IMAGE_DIR = "Database_2/Medical mask/Medical mask/Medical Mask/images"
ANNOT_DIR = "Database_2/Medical mask/Medical mask/Medical Mask/annot_xml"


cnt_mask = 0
cnt_no_mask = 0
cnt_inc_mask = 0
for filename in listdir(ANNOT_DIR):
    tree = ET.parse(ANNOT_DIR + "/" + filename)
    root = tree.getroot()

    objs = root.findall('.//object')
    for obj in objs:
        label = obj.find("name").text
        if label == "without_mask":
            cnt_no_mask += 1
        elif label == "with_mask":
            cnt_mask += 1
        elif label == "mask_weared_incorrect":
            cnt_inc_mask += 1

print("Bounding boxes:\n\tWith Mask: {}\n\tNo Mask: {}\n\tIncorrect Mask: {}\n".format(cnt_mask, cnt_no_mask, cnt_inc_mask))
'''
num_test_mask = cnt_mask//100*5
num_test_no_mask = cnt_no_mask//100*5
num_test_inc_mask = cnt_inc_mask//100*5

print("Test bounding boxes:\n\tWith Mask: {}\n\tNo Mask: {}\n\tIncorrect Mask: {}\n".format(num_test_mask, num_test_no_mask, num_test_inc_mask))

cnt_mask = 0
cnt_no_mask = 0
cnt_inc_mask = 0
for filename in listdir(ANNOT_DIR):
    tree = ET.parse(ANNOT_DIR + "/" + filename)
    root = tree.getroot()
    imagename = root.find("filename")

    labels = root.findall('.//name')
    #if len(labels) == 1:
        # se c'è solo una persona con mascherina incorretta.. salto alla prossima, cerco immagini di test con più di una persona
        #continue
    okay = False
    for label in labels:
        if label.text == "mask_weared_incorrect":
            okay = True
            break
    if okay and cnt_inc_mask < num_test_inc_mask:
        for label in labels:
            if label.text == "without_mask":
                cnt_no_mask += 1
            elif label.text == "with_mask":
                cnt_mask += 1
            elif label.text == "mask_weared_incorrect":
                cnt_inc_mask += 1

        rename(ANNOT_DIR + "/" + filename, "Dataset_7/Dataset_No_Augmentation_tt" + "/test/annotations/" + filename)
        rename(IMAGE_DIR + "/" + str(imagename.text), "Dataset_7/Dataset_No_Augmentation_tt" + "/test/images/" + str(imagename.text))

for filename in listdir(ANNOT_DIR):
    tree = ET.parse(ANNOT_DIR + "/" + filename)
    root = tree.getroot()
    imagename = root.find("filename")

    labels = root.findall('.//name')
    okay = False
    for label in labels:
        if label.text == "mask_weared_incorrect":
            okay = False
            break
        if label.text == "without_mask":
            okay = True

    if okay and cnt_no_mask < num_test_no_mask:
        for label in labels:
            if label.text == "without_mask":
                cnt_no_mask += 1
            elif label.text == "with_mask":
                cnt_mask += 1

        rename(ANNOT_DIR + "/" + filename, "Dataset_7/Dataset_No_Augmentation_tt" + "/test/annotations/" + filename)
        rename(IMAGE_DIR + "/" + str(imagename.text), "Dataset_7/Dataset_No_Augmentation_tt" + "/test/images/" + str(imagename.text))


for filename in listdir(ANNOT_DIR):
    tree = ET.parse(ANNOT_DIR + "/" + filename)
    root = tree.getroot()
    imagename = root.find("filename")

    labels = root.findall('.//name')
    okay = False
    for label in labels:
        if label.text == "mask_weared_incorrect":
            okay = False
            break
        if label.text == "without_mask":
            okay = False
            break
        if label.text == "with_mask":
            okay = True

    if okay and cnt_mask < num_test_mask:
        for label in labels:
            cnt_mask += 1

        rename(ANNOT_DIR + "/" + filename, "Dataset_7/Dataset_No_Augmentation_tt" + "/test/annotations/" + filename)
        rename(IMAGE_DIR + "/" + str(imagename.text), "Dataset_7/Dataset_No_Augmentation_tt" + "/test/images/" + str(imagename.text))

print("AFTER TEST\nBounding boxes:\n\tWith Mask: {}\n\tNo Mask: {}\n\tIncorrect Mask: {}\n".format(cnt_mask, cnt_no_mask, cnt_inc_mask))'''