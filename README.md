# Zoe - ChicagoDAO

This is an algorithmic strategy designed for the FTX US trading competition. It contains a mean reversion and a trend following strategies.

## Mean Reversion
When it is "ON" -> When the market is trading within the prior days value area and we have spent less than 10 minutes outside 1 standard deviation of VWAP.

This looks for price to hit extremes of VWAP/VA and then fade them back to intraday value. 

## Trend Following
This strategy uses Daily VWAP with prior days Value Area to determine a market in trend. Here we look to take a biased position and go with strength.


## To Run

Install Jessee depenencies and Docker.

```sh
cd docker
docker-compose up
```

Open [localhost:9000](http://localhost:9000) in your browser to see the dashboard. 