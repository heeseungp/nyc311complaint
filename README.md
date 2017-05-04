## 311 Data Visualization Project ##

Import your .csv 311 data file to MongoDB (for locally stored db)
```

#!bash
mongoimport -d 311 -c complaints --type csv --file 311_Data_15_Complaint_Types.csv --headerline

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