## 311 Data Visualization Project ##

Download Normalized and UnNormalized images from DropBox (https://www.dropbox.com/s/nqeqcv55ueq2f6h/kdelayer.zip?dl=0)
After download this zip, put the entire unzipped "kdelayer" folder inside /template/data311/


Import your .csv 311 data file to MongoDB (for locally stored db)
```

#!bash
mongoimport -d visualization311 -c complaints --type csv --file 311_Data.csv --headerline
mongoimport -d visualization311 -c population --type csv --file population.csv --headerline

```

To run the server on local instance, run
```

#!python
python main.py

```

Be sure to use virtualenv when working with libraries from this project. Sync your pip with
```

#!python
pip install -r requirements.txt

```
