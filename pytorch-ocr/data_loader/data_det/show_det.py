import cv2

with open('./test.txt', 'r') as f:
    data = f.readlines()
    for d in data:
        d = d.strip()
        path = d.split('\t')[0]
        rec = d.split('\t')[1]
        print(path)
        print(rec)

        img = cv2.imread(path)

        for i in eval(rec):
            # print(i)
            p = i['points']
            # print(p)

            left_top = p[0]
            right_top = p[1]
            left_bottom = p[3]
            right_bottom = p[2]

            # print(left_top, right_bottom)
            cv2.rectangle(img, (left_top), (right_bottom), (0, 0, 255), 2)


        """
        [
        {"points": [[132, 121], [130, 194], [439, 198], [439, 128]], "transcription": "detection"}, 
        {"points": [[295, 215], [294, 229], [507, 231], [507, 217]], "transcription": "detection"}, 
        {"points": [[349, 234], [349, 247], [507, 248], [507, 235]], "transcription": "detection"}, 
        {"points": [[213, 266], [209, 283], [382, 284], [378, 268]], "transcription": "detection"}, 
        {"points": [[207, 298], [209, 317], [364, 318], [361, 302]], "transcription": "detection"}, 
        {"points": [[211, 333], [210, 351], [435, 352], [435, 335]], "transcription": "detection"}, 
        {"points": [[330, 326], [333, 338], [355, 332], [351, 320]], "transcription": "detection"}, 
        {"points": [[88, 364], [88, 384], [199, 384], [199, 364]], "transcription": "detection"}, 
        {"points": [[209, 367], [207, 384], [253, 384], [253, 368]], "transcription": "detection"}, 
        {"points": [[212, 400], [208, 417], [357, 418], [357, 401]], "transcription": "detection"}, 
        {"points": [[87, 430], [87, 449], [195, 451], [195, 431]], "transcription": "detection"}, 
        {"points": [[207, 467], [203, 481], [456, 485], [455, 468]], "transcription": "detection"}, 
        {"points": [[86, 496], [86, 516], [192, 516], [192, 496]], "transcription": "detection"}, 
        {"points": [[206, 499], [205, 511], [479, 513], [479, 501]], "transcription": "detection"}, 
        {"points": [[204, 513], [205, 525], [485, 526], [487, 516]], "transcription": "detection"}, 
        {"points": [[205, 526], [205, 538], [486, 539], [486, 527]], "transcription": "detection"}, 
        {"points": [[205, 539], [205, 551], [487, 553], [486, 540]], "transcription": "detection"}, 
        {"points": [[204, 551], [204, 564], [371, 564], [367, 553]], "transcription": "detection"}, 
        {"points": [[207, 564], [207, 578], [480, 578], [480, 566]], "transcription": "detection"}, 
        {"points": [[287, 666], [286, 684], [383, 685], [383, 667]], "transcription": "detection"}, 
        {"points": [[26, 759], [26, 770], [218, 771], [215, 761]], "transcription": "detection"}, 
        {"points": [[337, 757], [337, 771], [524, 771], [524, 757]], "transcription": "detection"}, 
        {"points": [[92, 262], [92, 286], [110, 286], [110, 262]], "transcription": "detection"}, 
        {"points": [[175, 266], [175, 285], [196, 285], [196, 266]], "transcription": "detection"}, 
        {"points": [[89, 296], [89, 319], [110, 319], [110, 296]], "transcription": "detection"}, 
        {"points": [[175, 299], [175, 319], [197, 319], [197, 299]], "transcription": "detection"}, 
        {"points": [[89, 330], [89, 351], [110, 351], [110, 330]], "transcription": "detection"}, 
        {"points": [[175, 330], [175, 353], [195, 353], [195, 330]], "transcription": "detection"}, 
        {"points": [[87, 396], [87, 420], [194, 420], [194, 396]], "transcription": "detection"}, 
        {"points": [[207, 433], [207, 449], [316, 449], [316, 433]], "transcription": "detection"}, 
        {"points": [[87, 462], [87, 484], [193, 484], [193, 462]], "transcription": "detection"}, 
        {"points": [[364, 696], [364, 716], [409, 716], [409, 696]], "transcription": "detection"}, 
        {"points": [[416, 696], [416, 710], [431, 710], [431, 696]], "transcription": "detection"}, 
        {"points": [[433, 698], [433, 717], [447, 717], [447, 698]], "transcription": "detection"}, 
        {"points": [[449, 698], [449, 712], [465, 712], [465, 698]], "transcription": "detection"}, 
        {"points": [[473, 700], [473, 714], [485, 714], [485, 700]], "transcription": "detection"}]
        """

        cv2.imshow(rec, img)

        cv2.waitKey()