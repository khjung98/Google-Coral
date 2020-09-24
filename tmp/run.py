import os
import time

for i in range (1,18):
    print('#testVGG16-' + str(i) + 'is running')
    os.system('python3 classify_image2.py --model ../model/testVGG16-' + str(i) + '.tflite --labels ../models/inat_bird_labels.txt --input ../images/parrot.jpg')
    print('Done')
    time.sleep(1)
