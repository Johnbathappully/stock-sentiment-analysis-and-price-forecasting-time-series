# stock-sentiment-analysis-and-price-forecasting
 Performed sentiment analysis on real-time stock simulations. Modeled with methods namely ets, arima, varma,  ML-DL iterations including n-beats and multivariate models .Also adopted aws forecast, fb prophet &amp; garchh

# use textblob package/bert model and own  trained nueral network for live sentiment analysis
![sentiment analysis](https://user-images.githubusercontent.com/114779060/216783292-17ab1354-e56b-4afb-aba2-cd9ed04b093f.jpg)

# web scrapped from reddit/twitter and news headlines
![reddit twitter news scrape](https://user-images.githubusercontent.com/114779060/216783373-65587c33-f287-4624-ba73-aace8f523300.jpg)

# sqrt/log/box cox transformations on btc dataset
![1transformations](https://user-images.githubusercontent.com/114779060/216783532-b875969a-df31-4309-86e1-adabe402efa6.jpg)

# correlation b/w open and closing price  feature along with  simple moving average
![correl and sma](https://user-images.githubusercontent.com/114779060/216783741-6418288c-a29e-43cd-b3be-14c29a255487.jpg)

# smoothening using ewma/ simpleexpontentialsmoothing/ holt linear/holt winter (seasonality and trend) .found best settings with walk forward validation tuning
![holt](https://user-images.githubusercontent.com/114779060/216784646-04ff4ebe-f46a-4eeb-920c-70c702c0fb66.jpg)

# testing ar(1) ,ma(1),arima(1,1,1),arima(12,1,12)
![arima](https://user-images.githubusercontent.com/114779060/216784812-154e6f2d-df77-4f73-b84f-4eb7b25f5bd4.jpg)

# stationarity check with Augmented Dickey–Fuller test and finding manually ar and ma values by  pacf,acf  plot
![stationarity check  coupled pacf_acf test manual](https://user-images.githubusercontent.com/114779060/216786384-baa1d9bf-f7a0-4df8-ba9a-47e82ad4e876.jpg)

# auto sarima gives  better result than auto arima
![auto arima sarima model best](https://user-images.githubusercontent.com/114779060/216786663-6b557192-9019-4e21-b1e0-c1f68aa311a7.jpg)

# varima models(accounting more variables) clearly helped improving accuracy than arima
![varma beeter than arima](https://user-images.githubusercontent.com/114779060/216786854-5247eb71-6176-4f25-8681-6556693b6615.jpg)

#  single-step/multi-step and multi-output forecasting with help of  machine learning(linear regression,random forest,support vector regression) with and  w/o differencing
![machine learning](https://user-images.githubusercontent.com/114779060/216787014-4bcf78cb-bfba-4bc6-83b1-496a4998ef78.jpg)


# modelled volatility with garch/arch model on normal and t distribution.The volatily component in stocks is clearly distingushable from random walks
![summary garch arch t](https://user-images.githubusercontent.com/114779060/216787224-2f2d3765-c4de-4d5d-8643-5a709e417476.jpg)

# experimentation of deep learning model summary on cnn/lstm/multivariate/n-beats/ensemble techinque
![deep learning models](https://user-images.githubusercontent.com/114779060/216787355-f75ecb66-e84c-4467-8136-5d0636ad8c65.jpg)

# many deep learning models were able to better predict than naive forecast
![deep learning  model results](https://user-images.githubusercontent.com/114779060/216787512-579301f0-a3b9-42b8-9081-bf910aa43d61.jpg)

# applied prebuiltdeepar+ algorithm on Aws forecast 
![aws](https://user-images.githubusercontent.com/114779060/216787722-49b9e2fe-285a-436d-8799-0da73bc0c201.jpg)

#  bot utilizes Zerodha Kite Trade API and help of technical indicators like rsi/supertrend /bollinger bands/moviing averages .keeps a check of other similar stock
![proof](https://user-images.githubusercontent.com/114779060/216787949-c3954d01-557a-451b-85fb-ef42bafb90ff.jpg)
