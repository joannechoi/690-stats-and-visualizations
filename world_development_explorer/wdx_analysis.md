<img src="https://github.com/joannechoi/DATA-690-WANG/blob/main/world_development_explorer/Visualizations/header.jpg"
     alt="Header Photo"
     style="float: left; margin-right: 10px;" />
     
# Importance of Education in World Development 

## **Introduction**

Education is often seen as the marker of success in society today. Individually, we can expand our knowledge and find opportunities for intellectual and career growth through education. As a society, education will help us build healthier communities, stable economy, and greater equality.

In the "Quality of Education" analysis, various methods of measuring outcome of education was analyzed (Roser et al, 2013). These methods include evaluating test scores from tests such as *Program for International Student Assessment* (PISA) and *Progress in International Reading Literacy Study* (PIRLS) assessments along with many other educational surveys and tests. This research combined the results of multiple assessment and compared them to the GDP per capita of each country. Roser et al concluded that richer countries tended to have higher scores on various educational assessments.

Literacy rate is the most widely available metric for education outcome. Therefore, this analysis will be compare literacy rate to other world development indicators to determine how impactful education is in economic growth of a nation. 

### **Literacy Rate**

One of the most critical indicators for education is literacy rate. Literacy rate is defined as percentage of population of a given age group that can read and write. The age groups are divided into three categories: youth, adult, and elderly. 
- Youth group includes ages between 15 to 24
- Adult group includes ages 15 and older 
- Elderly group includes ages 65 and older. 

Youth literacy rate is particularly important because of the compounding effects of lack of education has on a society. If a child is not able to learn to read at an early age, it will negatively impact their education and eventually lower opportunities for career and limit ability to contribute to the society. 

### **Current Predictions**
Literacy rate will directly impact the country's economy. If society has lower literacy rate, this will impact the overall economy at a macro scale. Inversely, countries with high literacy rate will have more thriving and stable economy. 

#### **Questions**
1. Does youth literacy rate correlate with adult literacy rate?
2. How much impact does literacy rate have in the country's economy?

### **Indicators**
There are many indicators that can measure the society's education level and the economy. For the purposes of the analysis, following world development indicators will be used:

*Literacy rate, youth total (% of people ages 15-24)*
> Percentage of people ages 15-24 who can both read and write with understanding a short simple statement about their everyday life. 

*Literacy rate, adult total (% of people ages 15 and above)*

> Percentage of people ages 15 and above who can both read and write with understanding a short simple statement about their everyday life. 

*GDP per capita, PPP (current international $)*

> Gross income product expressed in current international dollars converted by purchasing power parity conversion factor. 

Above indicators were defined by the World Bank: ([Literacy rate, youth total](https://datacatalog.worldbank.org/literacy-rate-youth-total-people-ages-15-24-1), [Literacy rate, adult total](https://datacatalog.worldbank.org/literacy-rate-adult-total-people-ages-15-and-above-6), [GDP per capita, PPP (current international $)](https://datacatalog.worldbank.org/gdp-capita-ppp-current-international-1))

### **Countries**

For analysis, I compared literacy rate for youth total and literacy for adult literacy rate. I downloaded the dataset for all regions for the literacy comparison. I filtered data by different income groups.

World Health Organization (WHO) defined the income groups as following: 

*Low Income*
> GNI per capita \$1,025 or less.  

*Low Middle Income*
> GNI per capita between \$1,026 and $4,045

*Upper Middle Income*
> GNI per capita between \$4,046 and $12,535 

*High Income*
> GNI per capita of $12,536 or more

I selected a country from each of income groups to represent different economic status. 

\* Note: All countries in the low income category did not have 5 years worth of data. I selected a country with at least 3 years worth of data. 

#### **Selected Countries:**
1. Mali - Low Income (Sub-Saharan Africa)
2. Bangladesh - Lower Middle Income (South Asia)
3. Brazil - Upper Middle Income (Latin America & Caribbean)
4. Singapore - High Income (East Asia & Pacific)

### **Years**

Within the selected regions, most abundant data was between 2011 to 2018. Therefore, analysis will be done for data between 2011-2018.

## Analysis and Findings

1. Does youth literacy rate correlate with adult literacy rate?

**General Trend**

<img src="https://github.com/joannechoi/DATA-690-WANG/blob/main/world_development_explorer/Visualizations/1_gen_literacyrate_2018.png"
     alt="General Literacy Rate Trend"
     style="float: left; margin-right: 10px;" />
     
First, I compared the youth literacy rate to adult literacy rate for all regions to gather the overall trend. Based on this analysis, I observed that there is a linear relationship between the two indicators. Regions with higher youth literacy rate had higher adult literacy rate.

**Countries Comparison**

<img src="https://github.com/joannechoi/DATA-690-WANG/blob/main/world_development_explorer/Visualizations/2_literacyrate_2011.png"
     alt="4 Countries Literacy Rate Trend"
     style="float: left; margin-right: 10px;" />
     
As of 2011, Bangladesh, Brazil, Mali, and Singapore followed the same trend as the overall trend. There was a linear relationship with all countries, where countries with higher youth literacy trended to have higher adult literacy. 

<img src="https://github.com/joannechoi/DATA-690-WANG/blob/main/world_development_explorer/Visualizations/3_literacyrate_income_2011.png"
     alt="4 Countries Literacy Rate Trend by income group"
     style="float: left; margin-right: 10px;" />
     
- The literacy rate also corresponds to the income group. Mali, which is in low income category, had the lowest literacy rate for both youth and adult. 
- Singapore, which is in high income category, had the high literacy rate.
- Bangladesh and Brazil, which are in lower middle and upper middle income categories respectively, have literacy rates in between low income and high income countries. 

<img src="https://github.com/joannechoi/DATA-690-WANG/blob/main/world_development_explorer/Visualizations/4_literacyrate_2018.png"
     alt="4 Countries Literacy Rate Trend by income group"
     style="float: left; margin-right: 10px;" />

As of 2018, each countries' literacy rate increased slightly. However, the overall trend of country's literacy rate has not changed. The analysis of 2011 data still applies to 2018 data. 

2. How much impact does literacy rate have in the country's economy?

To explore the literacy rate's impact on the economy, I compared the literacy rate with country's GDP per capita. Since youth literacy rate had linear relationship with adult literacy rate, I used youth literacy rate for further analysis.

**General Trend**

<img src="https://github.com/joannechoi/DATA-690-WANG/blob/main/world_development_explorer/Visualizations/5_gen_lit_GDP_2018.png"
     alt="General literacy rate by GDP per capita"
     style="float: left; margin-right: 10px;" />
     
When comparing all regions, overall trends seem to show correlation between youth literacy rate and GDP per capita. Regions with higher literacy rate seem to have higher GDP per capita. 

However, there is a cluster of countries with high youth literacy rate, that share similar GDP per capita as countries with low youth literacy rate. 

**Countries Comparison**

<img src="https://github.com/joannechoi/DATA-690-WANG/blob/main/world_development_explorer/Visualizations/6_lit_GDP_2011.png"
     alt="4 Countries literacy rate by GDP per capita 2011"
     style="float: left; margin-right: 10px;" />

- In 2011, though youth literacy rate for Mali and Bangladesh vary by more than 30%, their GDP per capita are not very different. 
- In contrast, the youth literacy rate for Brazil and Singapore are very similar, their GDP per capita vary by more than $65,000. 
- Rather, Brazil and Bangladesh had less variance in GDP per capita than Bangladesh and Singapore did. 

<img src="https://github.com/joannechoi/DATA-690-WANG/blob/main/world_development_explorer/Visualizations/7_lit_GDP_2018.png"
     alt="General literacy rate by GDP per capita 2018"
     style="float: left; margin-right: 10px;" />

- As of 2018, Singapore's GPD per capita have increase by $20,000. However, the youth literacy rate remained at 100%. This observation indicates that there is another indicator that may explain the increase in GDP per capita better than youth literacy rate. 
- Brazil's youth literacy rate and GDP per capita remain about the same from 2011 to 2018. Brazil's GDP per capita actually decreased slightly in 2018 compared to 2011 data. 
- Bangladesh's youth literacy rate improved the most between the four countries from 2011 to 2018. However, the country's GDP per capita did not increase as significantly with the improved youth literacy rate. 
- Mali's youth literacy rate increased by at least 10% from 2011 to 2018. However, the GDP per capita did not rise significantly with the youth literacy rate. 
- In 2018, Bangladesh's youth literacy rate has almost caught up to Brazil's youth literacy rate, but there is still remarkable difference in GDP per capita. 

## Further Analysis

I wanted to explore more indicators that may impact literacy rate and indicators that will be impacted by literacy rate. 

Indicators: 
1. Primary school starting age (years) ([World Bank](https://datacatalog.worldbank.org/primary-school-starting-age-years-0))
> Primary school starting age is the age at which students would enter primary education, assuming they had started at the official entrance age for the lowest level of education, had studied full-time throughout and had progressed through the system without repeating or skipping a grade.

I wanted to see if starting age of primary school impacted the youth literacy rate. 

<img src="https://github.com/joannechoi/DATA-690-WANG/blob/main/world_development_explorer/Visualizations/8_school_start.png"
     alt="General School Start Age"
     style="float: left; margin-right: 10px;" />

Most countries start primary school at age of 6, but the literacy rate varies from 30% to 100%. This observation seems to conclude that the starting age does not directly impact the youth literacy rate. 

<img src="https://github.com/joannechoi/DATA-690-WANG/blob/main/world_development_explorer/Visualizations/9_school_start.png"
     alt="4 Countries School Start Age"
     style="float: left; margin-right: 10px;" />

For the four selected countries, countries who started primary school at age 6 had higher literacy rate than the country that started primary school at age 7.
- This is data bias because as shown in the general trend scatterplot, the starting age of the primary school is not an important indicator for youth literacy. 
- According to Education and Economic Growth (, paper published by Standard University, the quality of the education matters more than the duration of schooling that determines the impact of education on the economic growth (Hanushek & Woessmann, 2010)

2. Current health expenditure (% of GDP) ([World Bank](https://datacatalog.worldbank.org/current-health-expenditure-gdp))
> Estimates of current health expenditures include healthcare goods and services consumed during each year. This indicator does not include capital health expenditures such as buildings, machinery, IT and stocks of vaccines for emergency or outbreaks.

Similarly with GDP per capita, I wanted to see how literacy rate will impact the health expenditure. I wanted to analyze whether low literacy rate will decrease the health expenditure due to lack of access or due to low affordability. 

Since low literacy generally correlates with lower GDP per capita, population in lower income won't have as much disposable income to spend on healthcare.  

<img src="https://github.com/joannechoi/DATA-690-WANG/blob/main/world_development_explorer/Visualizations/10_gen_lit_health.png"
     alt="General literacy rate by health expenditure 2018"
     style="float: left; margin-right: 10px;" />
     
The general trend of all regions tends to show high variability  among highly literate regions. Many countries with 90% or higher youth literacy rate spend between 2% to almost 10% of their GDP on health expenditure. 

<img src="https://github.com/joannechoi/DATA-690-WANG/blob/main/world_development_explorer/Visualizations/11_gen_lit_health_afghanistan.png"
     alt="Afghanistan literacy rate by health expenditure 2018"
     style="float: left; margin-right: 10px;" />

Afghanistan had one of the lowest literacy rate, but had relatively high health expenditure. Further research into Afghanistan's economy will help explain why they are an outlier. 

<img src="https://github.com/joannechoi/DATA-690-WANG/blob/main/world_development_explorer/Visualizations/12_lit_health.png"
     alt="4 Countries literacy rate by health expenditure 2018"
     style="float: left; margin-right: 10px;" />

For the selected four countries, the results of the analysis tend to match the general trend. Though Bangladesh, Brazil, and Singapore have similar literacy rate, the health expenditure varied significantly. In 2018, Bangladesh spent 2.3% of their GDP on health expenditure, whereas Brazil spent 9.5% of their GDP on health expenditure. 

Mali has the lowest literacy rate, but spent less of their GDP on health expenditure than Brazil and Singapore did. 

Based on the inconclusiveness of the comparison, literacy rate does not seem to be the best indicator to dictate a country's health expenditure. Health expenditure could depend more on the country's public health education and access for the general population more than the literacy rate. 

## Conclusion

For further analysis of education as the country's economic growth indicator, following improvements are recommended:
- The definition of how literacy rate measured varies from country to country. It is difficult to have standardized method of measuring literacy rate or educational outcome due to cultural, societal, and economic differences between each country. Different indicator should be explored to measure the outcome of education. 
- There are a lot of missing data, mostly from countries in the low-income category. Many countries only had 1 or 2 years worth of data, therefore could not be used for the multi-year analysis. 

## References

Hanushek, E., &amp; Wößmann, L. (2010). Education and economic growth. International Encyclopedia of Education, 245-252. doi:10.1016/b978-0-08-044894-7.01227-6

Roser, M., Nagdy, M., &amp; Ortiz-Ospina, E. (2013, July 17). Quality of education. Retrieved March 27, 2021, from https://ourworldindata.org/quality-of-education
