## 311 Data Visualization Project ##

Download Normalized and UnNormalized images from Dropbox 
https://www.dropbox.com/s/nqeqcv55ueq2f6h/kdelayer.zip?dl=


After download this zip, put the entire unzipped "kdelayer" folder inside /template/data311/


Import your .csv 311 data file to MongoDB (for locally stored db)
https://www.dropbox.com/s/rpm4a8p49hirnh5/311_Data.csv?dl=0
https://www.dropbox.com/s/lf58ixbwci9lpl0/population.csv?dl=0


```
#!bash
mongoimport -d visualization311 -c complaints --type csv --file 311_Data.csv --headerline
mongoimport -d visualization311 -c population --type csv --file population.csv --headerline

```

To run the server on local instance, run
```

#!python
python data_311.py

```

Be sure to use virtualenv when working with libraries from this project. Sync your pip with
```

#!python
pip install -r requirements.txt

```