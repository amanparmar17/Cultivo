# Cultivo
Machine learning and ai based crop consultant written in Python(django)

## Overview
In the project, we introduce a scalable, accurate, and inexpensive method to predict crop yield using publicly available datasets and machine learning. The algorithms used include Regression Analysis, K-Fold and Batch Training. Our learning approach can predict crop yield with high spatial resolution several months before harvest, using only globally available covariates. We believe our solution can potentially help making informed planting decisions, setting appropriate food reserve level, identifying low-yield regions and improving risk management of crop-related derivatives.

## Introduction
Cultivo is a machine learning based crop consultant, developed using the high level technology Django, trained extensively over information gained from multiple trusted sources, to provide some valuable insights about the crop that user feels like growing in his region/locality. Along with insights, the consultant also provides numerous crop suggestions, keeping in mind the agricultural history and patterns of the area. A close success rate of the crop is predicted, so as to make the decision making more reliable, accurate and profitable.

## Algorithms Used:  </br>
    * Customized Multiple Linear Regression
    * Customized K Fold Method

## Output Generated:  </br>
    • Current weather details
    • Soil conditions for  the past 10 days
    • Predicted parameters including,
        ◦ Imports
        ◦ Exports
        ◦ Production
        ◦ Production per unit Area
        ◦ Gross Production Value
    • Final calculated success rate
    • Other crop suggestions

## Test Cases  

			| District | Crop | Success Rate |
		        | ------------- | ------------- |
			
		        | Howrah | Wheat | 84.944 % |
		        | Anantapur | Rice | 81.899 % |
			| Chittoor | Groundnut | 88.901 % |
		        | Anantapur | Groundnut | 87.101 % |
			| Visakhapatanam | Millet | 99.267 % |
		        | Gaya | Sugarcane | 95.403 % |


## APIs used:
    • For weather information
        ◦ Weather API by OpenWeatherMap
        ◦ Geocoding API by The Open Cage
    • For soil information
        ◦ Agweather API by WeatherBit

## Final success rate is calculated, keeping in mind 5 important factors i.e, 
	* Imports of the crop in the past 10 years 
	* Exports of the crop in the past 10 years 
	* Production of the crop in the past 10 years 
	* Production per unit area of the crop in the past 10 years, for the concerned area 
	* Gross production value of the crop in the past 10 years
	


