#Navigate to C:\Users\HOSTNAME\AppData\Local\Programs\Python\Python37\Scripts>
#use the syntax "pip install MODULE" for import
#The following modules need to be imported:
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

#Defines the threshold of the image and determines if each pixel is above or below the mean
#Assigns black or white depending on pixel threshold to the mean
def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    from statistics import mean
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)
    balance = mean(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr

#Program starts
startTime = time.time()

#Opens image, creates immage array, determines threshold values and plots pixels for image visualization
i = Image.open('capture.PNG')
iar = np.array(i)
iar = threshold(iar)
fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax1.imshow(iar)

#Program will write into the shell how long the image analysis process took
endTime = time.time()
print('The image analysis took %s seconds to process.' % (endTime - startTime))

#Displays the analyzed image
plt.show()
