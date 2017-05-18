# OG Use to get the normalized KDE
import os 
denom_img = ndimage.gaussian_filter(w_all, sigma=(1, 1), order=0)
denom_img[denom_img<10**-3]=0
plt.set_cmap('hot_r')
plt.figure(figsize=(12,12))
plt.axis('off')
plt.imshow(denom_img, interpolation='nearest')
plt.savefig('foo.png', bbox_inches='tight', transparent=True)
plt.show()
plt.close()


os.chdir('/home/heeseung5/Documents/visualization/Data/normalized')
currentDirectory = os.getcwd()
totalMonths = 84
for complaint_idx, complaint_element in enumerate(list_names):
    #create a new directory, if it does not exist
    createNewDirectory = currentDirectory + '/' + str(complaint_element)
    if not os.path.exists(createNewDirectory):
        os.makedirs(createNewDirectory)
        os.chdir(createNewDirectory)
        
    noise_normalized = a[complaint_idx]/denom_img #complaints 
    noise_normalized = np.log(noise_normalized)
    noise_normalized[noise_normalized==np.inf]=0
    noise_normalized = np.nan_to_num(noise_normalized)
    for month_idx in range(0,totalMonths):
        imageTitle = str(complaint_element) + '_' + str(month_idx) + '.png'
        img = ndimage.gaussian_filter(noise_normalized[month_idx], sigma=(1, 1), order=0) #months
        img[img<10**-3]=0
        plt.set_cmap('hot_r')
        plt.figure(figsize=(12,12))
        plt.axis("off")
        plt.imshow(img, interpolation='nearest')
        plt.savefig(imageTitle, bbox_inches='tight', transparent=True)
        plt.close()
    
        #convert white to transparency 
        img = Image.open(imageTitle)
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        setWhite = 211 #the lowest white rgb
        for item in datas:
            if 251 <= item[0] <= 255 and 251 <= item[1] <= 255 and setWhite <= item[2] <= 255:
                newData.append((255, 255, 255, 0))

            else:
                newData.append(item)
        img.putdata(newData)
        img.save(imageTitle, "PNG")
        
    os.chdir(currentDirectory)