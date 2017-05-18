import os
totalMonths = 5;
currentDirectory = os.getcwd()
for complaint_idx, complaint_element in enumerate(list_names):
    #directory naming
    createNewDirectory = currentDirectory + '/' + str(complaint_element)
    if not os.path.exists(createNewDirectory):
        os.makedirs(createNewDirectory)
        os.chdir(createNewDirectory)
    for month_idx in range(0,totalMonths):       
        imageTitle = str(complaint_element) + '_' + str(month_idx) + '.png'
        #just saving the plot without transparency
        img = ndimage.gaussian_filter(a[complaint_idx][month_idx], sigma=(1,1), order=0)
        plt.figure(figsize=(12,12))
        plt.imshow(img, interpolation='nearest')
        plt.axis('off')
        plt.savefig(imageTitle, bbox_inches='tight', transparent=True)
        plt.close()
        
        #removing the white in the png
        img = Image.open(imageTitle)
        img = img.convert("RGBA")
        datas = img.getdata()
        
        newData = []
        setWhite = 211; #the lowest white rgb
        for item in datas:
            if 251 <= item[0] <= 255 and 251 <= item[1] <= 255 and setWhite <= item[2] <= 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        img.save(imageTitle, "PNG")
    os.chdir(currentDirectory)