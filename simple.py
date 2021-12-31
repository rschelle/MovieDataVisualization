import streamlit as st
import re
import pandas as pd
import plotly.express as px

### Average_Gross_by_Distributors
def Average_Gross_by_Distributors():
    """Wide format: Average Gross Revenue of Distributor. This visual shows Walt Disney generates the highest average gross revenue compared to its peers, while Miramax generates the lowest average gross revenue."""
    stockdata = pd.read_csv("Data/TopDistributors.csv")
    gross_num = []
    for Total_gross in stockdata["AVERAGE GROSS"]:
        string2 = re.sub("\$","",Total_gross)
        string3 = re.sub("\,","",string2)
        gross_num.append( int(string3) )

    stockdata["GROSS AVERAGE"] = gross_num

    return px.bar(stockdata, x = 'DISTRIBUTORS' , labels = {"DISTRIBUTORS": "Distributors", "GROSS AVERAGE": "Average Gross"}, y= 'GROSS AVERAGE', title = "Average Gross of Distrubutors")

#### Genre and  Money
def Genre_and_Money():
    """Wide format:The visual describes the amount of money made by each film genre. Something that the visual clearly tells me is that adventure films disporportionatly make more money than other genres of film."""
    moviedata = pd.read_csv("Data/TopGenres.csv")
    gross_num = []
    for Total_gross in moviedata["TOTAL GROSS"]:
        string2 = re.sub("\$","",Total_gross)
        string3 = re.sub("\,","",string2)
        gross_num.append( int(string3) )

    moviedata["TOTAL GROSS NUM"] = gross_num
    moviedata2 = moviedata[["GENRES","TOTAL GROSS"]]
    import plotly.express as px

    moviedata_df = px.bar()
    return px.bar(moviedata, x="GENRES", y="TOTAL GROSS NUM", labels = {"GENRES":"Genres", "TOTAL GROSS NUM":"Total profits"},title="Genre and Money")

### Bar chart for Market share of media distributors 
def Market_Share_of_distrubutors():
    """Wide format: The second visual describes the market share of disributors such as Walt Disney. The graph shows that the market relating to media is quite diverse desipite diseny's reputation as a monopoly"""
    stockdata = pd.read_csv("Data/TopDistributors.csv")
    MARKET_SHARES = []
    for MARKET_SHARE in stockdata["MARKET SHARE"]:
        string2 = re.sub("\%","", MARKET_SHARE) 
        MARKET_SHARES.append( float(string2) ) 

    stockdata["MARKET_SHARE"] = MARKET_SHARES
    return px.bar(stockdata, x='DISTRIBUTORS', labels = {"DISTRIBUTORS": "Distributors", "MARKET_SHARE": "Market Share"} , y= 'MARKET_SHARE', title = "Market Share of Distrubutors")



#### Bar Chart of Directors From the Past 40 Years and The Total Box Office Income Their Movies Produced
def ReadData():
#### Reads the 'movies.csv' file into a pandas DataFrame
    movieData = pd.read_csv("Data/movies.csv")
    return movieData

def GroupData():
    ungroupedData = ReadData()
#### Groups the data by director and the sum of there movie sales
    groupedData = pd.DataFrame(ungroupedData.groupby(["director"])["gross"].sum())
    return groupedData

def FixDataFrame():
#### Fixes the Data Frame by adding the "Directors" column
    brokenDataFrame = GroupData()
    brokenDataFrame["Directors"] = brokenDataFrame.index
#### Redundant but added for clarity
    fixedDataFrame = brokenDataFrame
    return fixedDataFrame

def CleanDataFrame():
#### Cleans DataFrame of directors with a gross of 0 or None
    df = FixDataFrame()
    df1 = df.dropna()
#### Sort df1 by the gross column in descending order
    df2 = df1.sort_values(by="gross", ascending = False)
#### Returns top 20
    return df2.head(20)



def DisplayBoxChart():
    """Narrow Format""" #Description: This box chart displays the top 20 directors alongside the sales of the movies they directed.
    movieData = CleanDataFrame()
    #### Creates a plotly express bar chart
    return px.bar(movieData, x = "Directors", y = "gross", title = "Directors From the Past 40 Years and The Total Box Office Income Their Movies Produced",
                labels = {"gross":"Total Movie Sales", "Directors":"Director"}, width = 2*400)


#### Scatter plot of total amount of movies in the past 40 years grouped by their rating

def MovieData():
#### Reads CSV file into a pandas DataFrame
    data = pd.read_csv("./Data/movies.csv")
    return data

def GroupData1():
#### Groups the data by the amount of ratings by year
    data = MovieData()
    groupedData = pd.DataFrame(data.groupby(["year", "rating"])["name"].count())
    return groupedData

def FixDataFrame1():
#### For loop shenanigans to split the "broken DataFrame" into lists
    brokenDataFrame = GroupData1()
    yearList = []
    ratingList = []
    for i in range(len(brokenDataFrame)):
        tempTuple = brokenDataFrame.index[i]
        yearList.append(tempTuple[0])
        ratingList.append(tempTuple[1])
    return yearList, ratingList

def MovieDataFrame():
#### Brings the 3 lists together into one pandas DataFrame
    yearList, ratingList = FixDataFrame1()
    moviesDataFrame = pd.DataFrame(list(zip(yearList, ratingList, GroupData1()["name"].tolist()
)), columns = ['Year', 'Rating', 'Movies'])
    return moviesDataFrame

def DisplayScatterPlot():
    """Wide Format""" #Description: This graph shows the total amount of movies in the past 40 years grouped by their rating. Something to note is how "R" rated movies seem to dominate the market compared to the other ratings.
#### Takes the newly constructed pandas DataFrame, and displays a scatter plot using plotly
    df = MovieDataFrame()
    fig = px.scatter(df, x = "Year", y = "Movies", color = "Rating", title = "Total Number of Movies Grouped by Rating Over The Past 40 years")
    return fig


### histogram
genHisto = pd.read_csv("Data/HighestGrossers.csv")
tickets_solD = []
for tickets_sold in genHisto["TICKETS SOLD"]:
    string2 = re.sub("\,","",tickets_sold)
    tickets_solD.append( int(string2) )

genHisto["Number of Movie Tickets Sold"] = tickets_solD
#def GenHisto():
    #return px.histogram(data_frame = genHisto, x = "Number of Movie Tickets Sold",
                  #nbins = 14,title = "Number of Movies in each Range of Tickets Sold(1995-2021)", color = "MPAA RATING")
def GenHistoRobert():
    """Narrow Format""" #description: This is a Histogram that shows how many years a range of tickets were sold along with the genres of those top movies in each year. Most of the time, 50-60 million tickets were sold every year.
    return px.histogram(data_frame = genHisto, x = "Number of Movie Tickets Sold",
                  nbins = 14, color = "MPAA RATING", width = 2*200, height = 2*150) ##Updated to include height and width
#GenHistoRobert()



### bubble chart
genBubChrt = pd.read_csv("Data/TopGenres.csv")



gross_num = []
for Total_gross in genBubChrt["TOTAL GROSS"]:
    string2 = re.sub("\$","",Total_gross)
    string3 = re.sub("\,","",string2)
    gross_num.append( int(string3) )
genBubChrt["TOTAL GROSS2"] = gross_num

market_share = []
for Market_share in genBubChrt["MARKET SHARE"]:
    strinG = re.sub("\%","",Market_share)
    market_share.append( float(strinG)/100 )
genBubChrt["MARKET SHARE2"] = market_share

moviE = []
for mOvie in genBubChrt["MOVIES"]:
    striNg= re.sub("\,","",mOvie)
    moviE.append( int(striNg) )
genBubChrt["MOVIES2"] = moviE

def genBubChrtF():
    """Wide Format""" #discription: This is a bubble chart that shows the amount of money a genre of movies made as well as the number of movies made in that particular genre with the market share percentage of each genre. It is interesting that the more movies in a genre released in the years 1995-2021 doesn't mean that the genre made more money.
    #Done - Robert S
    return px.scatter(data_frame = genBubChrt, x="GENRES", y="TOTAL GROSS2",
        size="MOVIES2", color="MARKET SHARE2", hover_name="RANK", title = "Movie Gross and their Genres", labels={'TOTAL GROSS2':'Movie Gross','MARKET SHARE2':'Market Share'})
#genBubChrtF()

### bar chart
acmoviesDf = pd.read_csv("Data/movies.csv")
number_of_times = acmoviesDf.groupby("star")["name"].count()
number_of_timesdf = pd.DataFrame(number_of_times)
number_of_timesdf["star"] = number_of_timesdf.index
top9df = number_of_timesdf.loc[ number_of_timesdf["name"] > 30]
Opacity=0.0
def amBarChart(Opacity):
    """Narrow Format""" #description: This visual(bar chart)clearly depicts the number of movies in which each of the nine movie celebrities has starred, the color-coding makes this chart even more engrossing and easy to analyze. It is interesting to see that Nicolas Cage has starred in most movies, Robert De Niro and Tom Hanks have starred in surprisingly the same number of movies from 1980 to 2020.
    ###Done - Robert S 
    if(Opacity == 0.2):
        return px.bar(data_frame = top9df, x = "star", y = "name",title = "Number of Movies Actors Starred In",opacity = 0.2, labels={'name':'Number of Movies','star':'Movie Stars'},width = 200*2)
    elif(Opacity == 0.4):
        return px.bar(data_frame = top9df, x = "star", y = "name",title = "Number of Movies Actors Starred In",opacity = 0.4, labels={'name':'Number of Movies','star':'Movie Stars'},width = 200*2)
    elif(Opacity == 0.6):
        return px.bar(data_frame = top9df, x = "star", y = "name",title = "Number of Movies Actors Starred In",opacity = 0.6, labels={'name':'Number of Movies','star':'Movie Stars'},width = 200*2)
    else:
        return px.bar(data_frame = top9df, x = "star", y = "name",title = "Number of Movies Actors Starred In",opacity = 1.0, labels={'name':'Number of Movies','star':'Movie Stars'},width = 200*2)
# amBarChart(0.6)


#-------------------------------------------------------<3---------------------------------------------------------------------#

st.image("Imagine Dragons Logo.jpg") ####TODO: Update this with Austin's banner image

row0_spacer1, row0_1, row0_spacer2 = st.columns((0.1, 3, 0.1))

row0_1.title("Analyzing The Relationship Between Movies and The Gross Number")

row0_1.subheader("Streamlit web page by [AI-Camp](http://www.ai-camp.org):\"Imagine Dragons\" Team")

row1_spacer1, row1_1, row1_spacer2 = st.columns((0.1, 2, 0.1))

with row1_1:
    st.markdown("Hi! Welcome to the project made by Imagine Dragons Team from the AI Camp, and we take a deep look of the relationship between movies and the gorss number. In our research, we focus on different aspects of the movie industry and analyze how they connect to the final gross number. To accompish these tasks we made use of two different datasets: [dataset 1](https://www.kaggle.com/danielgrijalvas/movies), [dataset 2](https://www.kaggle.com/johnharshith/hollywood-theatrical-market-synopsis-1995-to-2021).")

row2_spacer1, row2_1, row2_spacer2,row2_2, row2_spacer3 = st.columns((0.1, 2.5, 0.1, 1.5, 0.1))

with row2_1:
    st.write("Number of Movies in each Range of Tickets Sold(1995-2021)")
    st.plotly_chart(GenHistoRobert())
    
with row2_2:
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.write("This is a Histogram that shows how many years a range of tickets were sold along with the genres of those top movies in each year. Most of the time, 50-60 million tickets were sold every year.") #Copied from Rose on discord
    st.text(" ")
    st.write("From [Dataset 2](https://www.kaggle.com/johnharshith/hollywood-theatrical-market-synopsis-1995-to-2021)")
    
row3_spacer1, row3_1, row3_spacer2,row3_2, row3_spacer3 = st.columns((0.1, 1.5, 0.1, 2.5, 0.1))

with row3_1:
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.write(".\n.\n.\n This visual(bar chart)clearly depicts the number of movies in which each of the nine movie celebrities has starred, the color-coding makes this chart even more engrossing and easy to analyze. It is interesting to see that Nicolas Cage has starred in most movies, Robert De Niro and Tom Hanks have starred in surprisingly the same number of movies from 1980 to 2020.") ###Add in description after choosing plot    
    st.text(" ")
    st.write("From [Dataset 1](https://www.kaggle.com/danielgrijalvas/movies)")

#row3_2.title("Example title for amBarChart")
with row3_2:
    st.plotly_chart(amBarChart(1)) 

row4_spacer1, row4_1, row4_spacer2 = st.columns((0.1, 4, 0.1))

with row4_1:
    st.plotly_chart(DisplayBoxChart())
    st.text(" ")
    st.text(" ")
    st.write("This box chart displays the top 20 gross total movie sales with there respective directors.") ##Update Description to match the box chart
    st.text(" ")
    st.write("From [Dataset 1](https://www.kaggle.com/danielgrijalvas/movies)")
    
row5_spacer1, row5_1, row5_spacer2 = st.columns((0.1, 4, 0.1))

with row5_1:
    st.plotly_chart(DisplayScatterPlot())
    st.text(" ")
    st.text(" ")
    st.write(
        "This graph shows the total amount of movies in the past 40 years grouped by their rating. Something to note is how "R" rated movies seem to dominate the market compared to the other ratings.")
    st.text(" ")
    st.write("From [Dataset 1](https://www.kaggle.com/danielgrijalvas/movies)")

with row5_1:
    ####Scatter plot goes here
    st.plotly_chart(Market_Share_of_distrubutors())
    st.write("This visual describes the market share of disributors such as Disney. What I notice from the graph is that despite Disney's large market share, it only really controls 17% of the entire market.")
    st.text(" ")
    st.write("From [Dataset 2](https://www.kaggle.com/johnharshith/hollywood-theatrical-market-synopsis-1995-to-2021)")
    
    
row7_spacer1, row7_1, row7_spacer2 = st.columns((0.1, 4, 0.1))

with row7_1:
    st.plotly_chart(genBubChrtF())
    st.write("This is a bubble chart that shows the amount of money a genre of movies made as well as the number of movies made in that particular genre with the market share percentage of each genre. It is interesting that the more movies in a genre released in the years 1995-2021 doesn't mean that the genre made more money.")
    st.text(" ")
    st.write("From [Dataset 2](https://www.kaggle.com/johnharshith/hollywood-theatrical-market-synopsis-1995-to-2021)")
    
row8_spacer1, row8_1, row8_spacer2 = st.columns((0.1, 4, 0.1))

with row8_1:
    st.plotly_chart(Genre_and_Money())
    st.write("The visual describes the amount of money made by each film genre. Something that the visual clearly tells me is that adventure films disporportionatly make more money than other genres of film.")
    st.text(" ")
    st.write("From [Dataset 2](https://www.kaggle.com/johnharshith/hollywood-theatrical-market-synopsis-1995-to-2021)")
    
row9_spacer1, row9_1, row9_spacer2 = st.columns((0.1, 4, 0.1))

    
    
with row9_1:
    st.plotly_chart(Market_Share_of_distrubutors())
    st.write("The second visual describes the market share of disributors such as Walt Disney. The graph shows that the market relating to media is quite diverse desipite diseny's reputation as a monopoly.")
    st.text(" ")
    st.write("From [Dataset 2](https://www.kaggle.com/johnharshith/hollywood-theatrical-market-synopsis-1995-to-2021)")
    
row10_spacer1, row10_1, row10_spacer2 = st.columns((0.1, 4, 0.1))

with row10_1:
    st.plotly_chart(Average_Gross_by_Distributors())
    st.write(" Average Gross Revenue of Distributor. This visual shows Walt Disney generates the highest average gross revenue compared to its peers, while Miramax generates the lowest average gross revenue.")
    st.text(" ")
    st.write("From [Dataset 2](https://www.kaggle.com/johnharshith/hollywood-theatrical-market-synopsis-1995-to-2021)")

