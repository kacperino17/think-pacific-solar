# think-pacific-solar
Air Quality Index Prediction

---

This is an Action Project for Solar Fiji, through the Think Pacific Charity. The project involves forecasting pollution levels based on environmental data and using ai analytical prediction. 


### Environmental Data used ###

Weather conditions - cloud coverage, extreme weather events etc
Traffic data - Specifically regarding air quality.


## General theory and approach

Pollutants table: 6 hour intervals: 06:00, 12:00 etc per day. Fields containing pollutants such as CO, NO2, O3 and SO3 
- Additional fields containing weather modifiers: average wind speed, humidity, temperature inversions(pressure) and rainfall. 
->
Standard AQI Formula taking into account concentration ranges from the pollutants table
->
Weather modifiers will be applied, i.e. stronger winds promote lower AQI due to faster dispersion of pollutants i.e. increasing solar energy output.
->
AQI table: Containing fields of AQI excl. weather ; AQI incl. weather and FINAL AQI. (The two former are required to understand whether data is stable and isn't being modified significantly by errors)


### SOURCES FOR INFORMATION ###

https://www.pranaair.com/en-gb/blog/what-is-air-quality-index-aqi-and-its-calculation/

https://www.iqair.com/support/knowledge-base/KA-04801-INTL

https://www.epa.gov/outdoor-air-quality-data/how-aqi-calculated

https://metone.com/how-to-calculate-aqi-and-nowcast-indices/

