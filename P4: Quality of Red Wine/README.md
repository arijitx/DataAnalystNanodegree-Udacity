Red Wine Quality by Arijit Mukherjee
========================================================

```{r echo=FALSE, message=FALSE, warning=FALSE, packages}


library(ggplot2)
library(knitr)
library(GGally)
library(gridExtra)
```

## Data Description 

```{r echo=FALSE, Load_the_Data}
# Load the Data
#directory - /home/zed/DataAnalystNanodegree-Udacity/P4: Quality of Red Wine/
red_wine=read.csv('wineQualityReds.csv')
summary(red_wine)
str(red_wine)

```

# Univariate Plots Section

Our Dataset has 12 varriables with 1599 obserbvation of different red wines

```{r echo=FALSE , warning=FALSE , message=FALSE}
ggplot(aes(x=fixed.acidity),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of Fixed.Acidity ')

ggplot(aes(x=volatile.acidity),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of Volatile.Acidity ')
```

Fixed Acidity and Volatile Acidity looks normally distributed

```{r echo=FALSE , warning=FALSE , message=FALSE}
ggplot(aes(x=citric.acid),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of Citric.Acid ')

ggplot(aes(x=citric.acid),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of Citric.Acid ')+
  scale_x_log10()

```

Citric Acidity looks skewed . . adding a log10 transformation wont change much .

```{r echo=FALSE , warning=FALSE ,message=FALSE}

ggplot(aes(x=residual.sugar),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of Residual Sugar')

ggplot(aes(x=residual.sugar),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of Residual Sugar')+
  scale_x_log10()

ggplot(aes(x=chlorides),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of Chlorides')

ggplot(aes(x=chlorides),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of Chlorides')+
  scale_x_log10()
```

Residual Sugar looks Skewed adding a log10() transform wont change much 
on the other hand Cholrides distribution looks skewed but adding a log10 transform makes it normal distributed with a right tail

```{r echo=FALSE , warning=FALSE ,message=FALSE}
ggplot(aes(x=free.sulfur.dioxide),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of free.sulfur.dioxide')

ggplot(aes(x=total.sulfur.dioxide),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of total.sulfur.dioxide')

ggplot(aes(x=total.sulfur.dioxide),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of total.sulfur.dioxide')+
  scale_x_log10()

```

Adding log10() transformation on X axis makes the distribution Normal for Total.sulfur.dioxide

```{r echo=FALSE , warning=FALSE , message=FALSE}
ggplot(aes(x=density),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of Density')

ggplot(aes(x=pH),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of pH')

```

pH and Density is normally distrbuted

```{r echo=FALSE , warning=FALSE , message=FALSE}
ggplot(aes(x=sulphates),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of sulphates')

ggplot(aes(x=sulphates),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of sulphates')+
  scale_x_log10()

ggplot(aes(x=alcohol),data = red_wine)+
  geom_histogram()+
  ggtitle('Frequency of Alcohol')

```

Frequency of Sulphate looks normally distributed after adding log10() transformation


```{r echo=FALSE , warning=FALSE , message=FALSE}
ggplot(aes(x=quality),data = red_wine)+
  geom_bar()+
  ggtitle('Frequency of Quality ')
```


# Univariate Analysis

### What is the structure of your dataset?

  Number of Records: 1599<br>
  Number of Attributes:  11 + output attribute<br>
  Attribute information: 
   Input Variable
   1 - fixed acidity (tartaric acid - g / dm^3)
   2 - volatile acidity (acetic acid - g / dm^3)
   3 - citric acid (g / dm^3)
   4 - residual sugar (g / dm^3)
   5 - chlorides (sodium chloride - g / dm^3
   6 - free sulfur dioxide (mg / dm^3)
   7 - total sulfur dioxide (mg / dm^3)
   8 - density (g / cm^3)
   9 - pH
   10 - sulphates (potassium sulphate - g / dm3)
   11 - alcohol (% by volume)
   Output variable (based on sensory data): 
   12 - quality (score between 0 and 10)
  
### What is/are the main feature(s) of interest in your dataset?

Quality is the main feature of interest in this dataset 

### What other features in the dataset do you think will help support your investigation into your feature(s) of interest?

The information provided by the authors that there are correlation between certain features. Thus we look into the feature which effects the quality and as there are much more number of Wines of average quality than very low and very high quality wines it will be a task to dected the outliers to find the excelent and poor quality wines.

### Did you create any new variables from existing variables in the dataset?

No , I didn't created any new variables from existing variables in the dataset.

### Of the features you investigated, were there any unusual distributions? Did you perform any operations on the data to tidy, adjust, or change the form of the data? If so, why did you do this?

Citric Acidity looked unusally distributed but adding log-transform it wont change much. Total.sulfur.dioxide and Frequency of Sulphate looked skewed but adding a log10 transformation changed the form of the data to normally distributed . 


# Bivariate Plots Section

```{r echo=FALSE ,warning=FALSE ,message=FALSE, fig.width=12, fig.height=12, Bivariate_Plots}
pair1 <- data.frame(
        Fixed_Acidity = red_wine$fixed.acidity,
        Volati_leAcidity = red_wine$volatile.acidity,
        Citric_Acid=red_wine$citric.acid,
        Residual_Sugar=red_wine$residual.sugar,
        Chlorides=red_wine$chlorides,
        Free_Sulfur_Dioxide=red_wine$free.sulfur.dioxide,
        Quality = red_wine$quality
)
ggpairs(pair1 ,
        lower = list(continuous = wrap("points", shape = I('.'))), 
        upper = list(combo = wrap("box", outlier.shape = I('.'))))

pair2 <- data.frame(
        Total_Sulfur_Dioxide = red_wine$total.sulfur.dioxide,
        Density = red_wine$density,
        pH=red_wine$pH,
        Sulphates=red_wine$sulphates,
        Alcohol=red_wine$alcohol,
        Quality = red_wine$quality
)
ggpairs(pair2 ,
        lower = list(continuous = wrap("points", shape = I('.'))), 
        upper = list(combo = wrap("box", outlier.shape = I('.'))))
```

We can see that 
```{r echo=FALSE}
cor.test(red_wine$quality,red_wine$alcohol)
cor.test(red_wine$quality,red_wine$volatile.acidity)
cor.test(red_wine$quality,red_wine$sulphates)
cor.test(red_wine$quality,red_wine$citric.acid)
```

<br><br>
**Alcohol (Corr : .476)**<br>
**Volatile.Acidity (Corr : -.391)**<br>
**Sulphates (Corr : .251)**<br>
**Citric.Acid (Corr : .226)**<br>


```{r echo=FALSE}

ggplot(data=red_wine,aes(x=quality,y=alcohol))+
  geom_boxplot(stat='boxplot',aes(group=quality))+
  ggtitle('Box Plot Quality by Alcohol')+
  xlab('Quality')+
  ylab('Alcohol % by Volume')

ggplot(data=red_wine,aes(x=quality,y=volatile.acidity))+
  geom_boxplot(stat='boxplot',aes(group=quality))+
  ggtitle('Box Plot Quality by Volatile Acidity')+
  xlab('Quality')+
  ylab('Volatile Acidity g / dm^3')

ggplot(data=red_wine,aes(x=quality,y=sulphates))+
  geom_boxplot(stat='boxplot',aes(group=quality))+
  ggtitle('Box Plot Quality by Sulphates')+
  xlab('Quality')+
  ylab('Sulphates g / dm^3')

ggplot(data=red_wine,aes(x=quality,y=citric.acid))+
  geom_boxplot(stat='boxplot',aes(group=quality))+
  ggtitle('Box Plot Quality by Citric Acid')+
  xlab('Quality')+
  ylab('Citric Acid g / dm^3')

#between pH and other fixed.acidity and citric.acid
ggplot(data=red_wine,aes(x=pH,y=citric.acid))+
  geom_point()+
  geom_smooth(method='lm')+
  ggtitle('pH Vs Citric Acid')+
  xlab('pH')+
  ylab('Citric Acid g / dm^3')

ggplot(data=red_wine,aes(x=pH,y=fixed.acidity))+
  geom_point()+
  geom_smooth(method='lm')+
  ggtitle('pH Vs Fixed Acidity')+
  xlab('pH')+
  ylab('Fixed Acidity g / dm^3')


```
```{r echo=FALSE}
cor.test(red_wine$pH,red_wine$fixed.acidity)
cor.test(red_wine$pH,red_wine$citric.acid)
```

From the above box plots its clear that The attributes Alcohol and Volatile Acidity contributes the most in Quality while Citric Acid and Sulphates also have some effects on the Quality. One intersting effect is on pH as it measures the level of acidity of a solution we can see pH has high correlation values with Fixed Acidity and Citric Acid.

# Bivariate Analysis

### Talk about some of the relationships you observed in this part of the investigation. How did the feature(s) of interest vary with other features in the dataset?

It looks like For all high quality Red wine the mean of alcohol,sulphates,citric.acid is relatively higher than the low quality Red wine samples .

And For volatile.acidity the level is relatively lower in the high quality products than the lower ones

### Did you observe any interesting relationships between the other features (not the main feature(s) of interest)?

There is high correlation between pH and both citric.acid and fixed.acidity as pH indirectly measures the acidity of a soultion.<br>
**Correlation**
<br><br>
pH ----- Citric.Acid     :   -.542<br>
pH ----- Fixed.Acidity   :   -.683<br>

This means with increase of Citric.Acid and Fixed.Acidity pH levels decreases.



### What was the strongest relationship you found?

Alcohol and Quality <br>
pH and Fixed.Acidity<br>


# Multivariate Plots Section

```{r echo=FALSE, Multivariate_Plots}
red_wine$quality=factor(red_wine$quality)
ggplot(data=red_wine,aes(x=alcohol,y=volatile.acidity,colour=quality))+
  geom_point()+
  ggtitle('Quality By Alcohol and Volatile Acidity')+
  xlab('Alcohol % by Volume')+
  ylab('Volatile Acidity g / dm^3')+
  scale_color_brewer(palette = "Reds") + 
  theme_dark()

ggplot(data=red_wine,aes(x=alcohol,y=citric.acid,colour=quality))+
  geom_point()+
  ggtitle('Quality By Alcohol and Citric Acid')+
  xlab('Alcohol % by Volume')+
  ylab('Citric Acid g / dm^3')+
  scale_color_brewer(palette = "Reds") + 
  theme_dark()

ggplot(data=red_wine,aes(x=volatile.acidity,y=citric.acid,colour=quality))+
  geom_point()+
  ggtitle('Quality By Alcohol and Citric Acid')+
  xlab('Volatile Acidity g / dm^3')+
  ylab('Citric Acid g / dm^3')+
  scale_color_brewer(palette = "Reds") + 
  theme_dark()


```

Now we can see the realtions between Quality and the other variables which effect the quality but due to many obverbvations belonging from the midum quality samples its tough to draw some decision from the above visualizations so lets subset the dataframe without the 5,6 quality wines

```{r echo=FALSE}
red_wine_sub=subset(red_wine,red_wine$quality!=5 &red_wine$quality!=6)
ggplot(data=red_wine_sub,aes(x=alcohol,y=volatile.acidity,colour=quality))+
  geom_point()+
   ggtitle('Wine Samples Quality By Alcohol and Volatile Acidity')+
  xlab('Alcohol % By Volume')+
  ylab('Volatile Acidity g / dm^3')+
  scale_color_brewer(palette = "Reds") + 
  theme_dark()
```

Now from the visualization its clear that the lower-right corner samples are of high quality and the upper-right part samples are of low quality .

```{r echo=FALSE}

ggplot(data=red_wine_sub,aes(x=alcohol,y=citric.acid,colour=quality))+
  geom_point()+
   ggtitle('Wine Samples Quality By Citric Acid And Alcohol ')+
  xlab('Alcohol % By Volume')+
  ylab('Citric Acid g / dm^3')+
  scale_color_brewer(palette = "Reds") + 
  theme_dark()

ggplot(data=red_wine_sub,aes(x=alcohol,y=sulphates,colour=quality))+
  geom_point()+
  ggtitle('Wine Samples Quality By Sulphates And Alcohol ')+
  xlab('Alcohol % By Volume')+
  ylab('Sulphates g / dm^3')+
  scale_color_brewer(palette = "Reds") + 
  theme_dark()

```

Now lets draw two visualization to relate Quality-Citric.Acid-Alcohol-Volatile.Acidity and Quality-Sulphates-Alcohol-Volatile.Acidity

```{r echo=FALSE}

ggplot(data=red_wine_sub,
  aes(x=alcohol,y=citric.acid,colour=quality,size=volatile.acidity))+
  geom_point(alpha=.5)+
  ggtitle('Wine Samples Quality By Citric Acid Alcohol and Volatile Acidity')+
  xlab('Alcohol % By Volume')+
  ylab('Citric Acid g / dm^3')+
  scale_color_brewer(palette = "Reds") + 
  theme_dark()

ggplot(data=red_wine_sub,
  aes(x=alcohol,y=sulphates,colour=quality,size=volatile.acidity))+
  geom_point(alpha=.5)+
  ggtitle('Wine Samples Quality By Sulphates Alcohol and Volatile Acidity')+
  xlab('Alcohol % By Volume')+
  ylab('Sulphates g / dm^3')+
  scale_color_brewer(palette = "Reds") + 
  theme_dark()

```

# Multivariate Analysis

### Talk about some of the relationships you observed in this part of the investigation. Were there features that strengthened each other in terms of looking at your feature(s) of interest?

Most of the High Quality Wines have high level of Alcohol-Citric.Acid-Sulphates and Low level of Volatile.Acidity

### Were there any interesting or surprising interactions between features?

With much high level of Alcohol and low level of Citric.Acid some of the samples were of High Quality .

### OPTIONAL: Did you create any models with your dataset? Discuss the strengths and limitations of your model.

------

# Final Plots and Summary

### Plot One

```{r echo=FALSE, Plot_One}
ggplot(aes(x=quality,fill=quality),data = red_wine)+
  geom_bar()+
  ggtitle('Frequency of Quality ')+
  xlab('Quality')

summary(red_wine$quality,group=quality)
```

### Description One

In the total 1599 samples most of the samples were of medium quality. There were only 10 samples of quality 3 and only 18 samples of quality 8 most of them were in either 5 or 6 

### Plot Two

```{r echo=FALSE, Plot_Two}
p1=ggplot(data=red_wine,aes(x=quality,y=alcohol))+
  geom_boxplot(stat='boxplot',aes(group=quality))+
  ggtitle('Box Plot Quality by Alcohol')+
  xlab('Quality')+
  ylab('Alcohol % by Volume')

p2=ggplot(data=red_wine,aes(x=quality,y=volatile.acidity))+
  geom_boxplot(stat='boxplot',aes(group=quality))+
  ggtitle('Box Plot Quality by Volatile Acidity')+
  xlab('Quality')+
  ylab('Volatile Acidity g / dm^3')


grid.arrange(p1,p2,ncol=1)

```

### Description Two

The above plot shows the 2 main component that have high effects on the quality . The Alchol - Volatile.Acidity determines the quality of the wine . The high Quality Wines have relatively high mean of Alcohol % than the lower quality ones and The low Quality wines have much higher mean of Volatile Acidity than the High Quality Wines .

### Plot Three

```{r echo=FALSE, Plot_Three, fig.width=12}

ggplot(data=red_wine_sub,
  aes(x=alcohol,y=citric.acid,colour=quality,size=volatile.acidity))+
  geom_point(alpha=.5)+
  ggtitle('Wine Samples Quality By Citric Acid Alcohol and Volatile Acidity')+
  xlab('Alcohol % By Volume')+
  ylab('Citric Acid g / dm^3')+
  scale_color_brewer(palette = "Reds") + 
  scale_size_continuous(name="Volatile Acidity % By Volume")+
  theme_dark()
```

### Description Three

In the above we see the difference between the Best and Worst Wines .
Any wine sample with alcohol % greater than 1.1 and citric acid level .25 is graded High Quality and Alcohol % have the strongest effect on the wine quality.


------

# Reflection

In the dataset there were 1599 observation in which we tried to find the effect of chemical factors on the quality of the wine . Alcohol and Volatile.Acidity has the strongest effect on the quality of a wine . While the hihg level of Alchol indicates a high quality wine on the other hand high level of Volatile.Acidity can make the quality of the wine degrade. Quality is proportional to the level of alcohol and The Quality is inversly proportional to the Level of Volatile Acidity . The next dominant factors are the Citric.Acid and Sulphates . Citric.Acid have some effects on the quality of wine but high Volatile.Acidity can degrade the quality of wine even with high level of Citric.Acid . 
Firstly we selected the main dependent Variable The Quality and we tried to find which attributes have most effects to the Quality . Finally we narrowed down to 3 Variables Alcohol,Volatile Acidity and Citric Acid . We used correlation between them to find the effects of these attributes on Quality.
The most challengeing part of the dataset is The Quality is a sensory measurement which can change drastically from human to human as the rating of quality is given by Humans .
In the future we can train a Linear Model to predict the quality of a Wine from various attributes like the Alcohol,Volatile Acidity,Citric Acid and Sulphates.