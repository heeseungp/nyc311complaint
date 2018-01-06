# 311 Data Visualization Project

![GIF of the visualization project going over how the website works. First the about page, second is the summary page, third is the demo page, and last is the team member page](https://media.giphy.com/media/l0HU2Ftho1HxjDZZK/giphy.gif)

Since the creation of New York City’s open data law (Local Law 11 of 2012), the growing amount of data that is publicly recorded has burgeoned. While the open data movement has made the data more accessible, interpreting it has not been any easier. 

According to Fast.Co Design, a business media brand, as quoted from this article, “… there wasn’t a tool to generate broad, location-based insights for people at the top”. 

As a result, a new dashboard was created for the Mayor’s Office in January of 2017, however, the dashboard is not available for public use, and it is in this context that we believe we can offer our services to bridge this gap for those interested in exploring this data. 

This data visualization is a dashboard allowing users to filter the 311 complaint types and time to observe and locate complainitive neighborhoods in NYC in 14 different types of complaint. To interact with the map, first choose a complaint type from the complaint type dropdown. The data can be seen in normalized or unnormalized form by selecting the radio buttons. Furthermore, users can use the slider to choose the specific months, giving advantages of focusing on one specific month (from January 2010 to December 2016 ).

## Instruction

Download a zipfile from https://www.dropbox.com/sh/2njaqi04efwl8da/AAABlOxSY7_hQi1fKHXpsA72a?dl=0

After extraction, the nyc311 file includes mapimg and gif files.

Insert mapimg file inside /static/img/

Insert gif file inside /static/


Be sure to use virtualenv when working with libraries from this project. Sync your pip with
```

#!python
pip install -r requirements.txt

```

To run the server on local instance, run
```

#!python
python data_311.py

```
