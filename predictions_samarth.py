# -*- coding: utf-8 -*-
"""predictions_Samarth.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12Nw411OKxTsVPgTWLx6o0PVoP2usvj13
"""

import pandas as pd
import numpy as np
from itertools import cycle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import plotly.graph_objects as go
import math

import matplotlib.pyplot as plt

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

"""# **ETHEREUM DATASET**"""

Ethereum = pd.read_csv("/content/ETHNEW.csv")
Ethereum

"""# **ARBITRUM DATASET**"""

Arbitrum = pd.read_csv("/content/ARBNEW.csv")
Arbitrum

"""# **CHAINLINK DATASET**"""

Chainlink = pd.read_csv("/content/LINKNEW.csv")
Chainlink

"""#**Creation of a variable for predicting '10' days out into the future for Ethereum**

"""

#Creation of a variable for predicting '10' days out into the future
projection_Ethereum = 10
#creation of a new column with a name prediction
Ethereum['Prediction'] = Ethereum[['Close']].shift(-projection_Ethereum)
Ethereum

"""## **Creation of a variable for predicting '10' days out into the future for Arbitrum**"""

#Creation of a variable for predicting '5' days out into the future
projection_Arbitrum = 10
#creation of a new column with a name prediction
Arbitrum['Prediction'] = Arbitrum[['Close']].shift(-projection_Arbitrum)
Arbitrum

"""# **Creation of a variable for predicting '10' days out into the future for Chainlink**"""

#Creation of a variable for predicting '5' days out into the future
projection_Chainlink = 10
#creation of a new column with a name prediction
Chainlink['Prediction'] = Chainlink[['Close']].shift(-projection_Chainlink)
Chainlink

"""## **DATA VISUALIZATION FOR ETH**"""

visualize_Ethereum = cycle(['Open','Close','High','Low','Prediction'])

fig1 = px.line(Ethereum, x=Ethereum.Date, y=[Ethereum['Open'], Ethereum['Close'],
                                          Ethereum['High'], Ethereum['Low'],Ethereum['Prediction']],
             labels={'Date': 'Date','value':'Price'})
fig1.update_layout(title_text='Ethereum', font_size=15, font_color='black',legend_title_text='Parameters')
fig1.for_each_trace(lambda t:  t.update(name = next(visualize_Ethereum)))
fig1.update_xaxes(showgrid=False)
fig1.update_yaxes(showgrid=False)

fig1.show()

"""## **DATA VISUALIZATION FOR ARB**"""

visualize_Arbitrum = cycle(['Open','Close','High','Low','Prediction'])

fig1 = px.line(Arbitrum, x=Arbitrum.Date, y=[Arbitrum['Open'], Arbitrum['Close'],
                                          Arbitrum['High'], Arbitrum['Low'],Arbitrum['Prediction']],
             labels={'Date': 'Date','value':'Price'})
fig1.update_layout(title_text='Arbitrum', font_size=15, font_color='black',legend_title_text='Parameters')
fig1.for_each_trace(lambda t:  t.update(name = next(visualize_Arbitrum)))
fig1.update_xaxes(showgrid=False)
fig1.update_yaxes(showgrid=False)

fig1.show()

"""# **DATA VISUALIZATION FOR LINK**"""

visualize_Chainlink = cycle(['Open','Close','High','Low','Prediction'])

fig1 = px.line(Chainlink, x=Chainlink.Date, y=[Chainlink['Open'], Chainlink['Close'],
                                          Chainlink['High'], Chainlink['Low'],Chainlink['Prediction']],
             labels={'Date': 'Date','value':'Price'})
fig1.update_layout(title_text='Chainlink', font_size=15, font_color='black',legend_title_text='Parameters')
fig1.for_each_trace(lambda t:  t.update(name = next(visualize_Chainlink)))
fig1.update_xaxes(showgrid=False)
fig1.update_yaxes(showgrid=False)

fig1.show()

"""# **CREATION OF THE INDEPENDENT DATA SET(X) & DEPENDENT DATA SET(y) for ETHEREUM**"""

#Creation of the independent data set (X)
X_Ethereum = np.array(Ethereum[['Close']])
X_Ethereum = X_Ethereum[:-projection_Ethereum]
print(X_Ethereum)

#creation of the dependent data set (y)
y_Ethereum = Ethereum['Prediction'].values
y_Ethereum = y_Ethereum[:-projection_Ethereum]
print(y_Ethereum)

"""# **CREATION OF THE INDEPENDENT DATA SET(X) & DEPENDENT DATA SET(y) for ARBITRUM**"""

#Creation of the independent data set (X)
X_Arbitrum = np.array(Arbitrum[['Close']])
X_Arbitrum = X_Arbitrum[:-projection_Arbitrum]
print(X_Arbitrum[:30])

# Or print the shape of X_Arbitrum
print(X_Arbitrum.shape)
#print(X_Arbitrum)

#creation of the dependent data set (y)
y_Arbitrum = Arbitrum['Prediction'].values
y_Arbitrum = y_Arbitrum[:-projection_Arbitrum]
print(y_Arbitrum)

"""## **CREATION OF THE INDEPENDENT DATA SET(X) & DEPENDENT DATA SET(y) for CHAINLINK**"""

#Creation of the independent data set (X)
X_Chainlink = np.array(Chainlink[['Close']])
X_Chainlink = X_Chainlink[:-projection_Chainlink]
print(X_Chainlink)

#creation of the dependent data set (y)
y_Chainlink = Chainlink['Prediction'].values
y_Chainlink = y_Chainlink[:-projection_Chainlink]
print(y_Chainlink)

"""# **SPLIT THE DATA INTO 85% TRAINING & 15% TESTING DATA SETS**


"""

x_train_Ethereum, x_test_Ethereum, y_train_Ethereum, y_test_Ethereum = train_test_split(X_Ethereum,y_Ethereum,test_size=0.15)

x_train_Arbitrum, x_test_Arbitrum, y_train_Arbitrum, y_test_Arbitrum = train_test_split(X_Arbitrum,y_Arbitrum,test_size=0.15)

x_train_Chainlink, x_test_Chainlink, y_train_Chainlink, y_test_Chainlink = train_test_split(X_Chainlink,y_Chainlink,test_size=0.15)

"""# **CREATE & TRAIN THE MODEL**"""

linReg_Ethereum = LinearRegression()
linReg_Ethereum.fit(x_train_Ethereum,y_train_Ethereum)

linReg_Arbitrum = LinearRegression()
linReg_Arbitrum.fit(x_train_Arbitrum,y_train_Arbitrum)

linReg_Chainlink = LinearRegression()
linReg_Chainlink.fit(x_train_Chainlink,y_train_Chainlink)

"""## **EVALUATION**

1. Test the model using score which returns the coefficient of determination "R squared" of the prediction.

2. R squared coefficient of determination is a statistical measure of how well the regression predictions approximate the real data points.

3. In statistics, the coefficient of determination, denoted R2 or r2 and pronounced "R squared", is the proportion of the variation in the dependent variable that is predictable from the independent variable(s).
"""

linReg_confidence_Ethereum = linReg_Ethereum.score(x_test_Ethereum,y_test_Ethereum)
print("Linear Regression Confidence for Ethereum: ",linReg_confidence_Ethereum)
print(linReg_confidence_Ethereum*100,'%')

linReg_confidence_Arbitrum = linReg_Arbitrum.score(x_test_Arbitrum,y_test_Arbitrum)
print("Linear Regression Confidence for Arbitrum: ",linReg_confidence_Arbitrum)
print(linReg_confidence_Arbitrum*100,'%')

linReg_confidence_Chainlink = linReg_Chainlink.score(x_test_Chainlink,y_test_Chainlink)
print("Linear Regression Confidence for Chainlink: ",linReg_confidence_Chainlink)
print(linReg_confidence_Chainlink*100,'%')

"""# **PREDICTION FOR THE NEXT 'N' DAYS**

1. Creation of a variable called x_projection_coin & set it equal to the last 10 rows of data from the original dataset.

2. Print the linear regression models predictions for the next 10 days(here, N=10)

**ETHEREUM**
"""

#ETHEREUM
x_projection_Ethereum = np.array(Ethereum[['Close']])[-projection_Ethereum:]
linReg_prediction_Ethereum = linReg_Ethereum.predict(x_projection_Ethereum)
print(x_projection_Ethereum)



"""**ARBITRUM**"""

x_projection_Arbitrum = np.array(Arbitrum[['Close']])[-projection_Arbitrum:]
linReg_prediction_Arbitrum = linReg_Arbitrum.predict(x_projection_Arbitrum)
print(x_projection_Arbitrum)

"""**CHAINLINK**"""

x_projection_Chainlink = np.array(Chainlink[['Close']])[-projection_Chainlink:]
linReg_prediction_Chainlink = linReg_Chainlink.predict(x_projection_Chainlink)
print(x_projection_Chainlink)

last_date = pd.to_datetime(Ethereum['Date'].iloc[-1])
future_dates = [last_date + pd.DateOffset(days=x) for x in range(1, projection_Ethereum + 1)]
future_df = pd.DataFrame(data={'Date': future_dates, 'Prediction': linReg_prediction_Ethereum})
future_df['Date'] = pd.to_datetime(future_df['Date'])

last_date = pd.to_datetime(Arbitrum['Date'].iloc[-1])
future_dates = [last_date + pd.DateOffset(days=x) for x in range(1, projection_Arbitrum + 1)]
future_df = pd.DataFrame(data={'Date': future_dates, 'Prediction': linReg_prediction_Arbitrum})
future_df['Date'] = pd.to_datetime(future_df['Date'])

last_date = pd.to_datetime(Chainlink['Date'].iloc[-1])
future_dates = [last_date + pd.DateOffset(days=x) for x in range(1, projection_Chainlink + 1)]
future_df = pd.DataFrame(data={'Date': future_dates, 'Prediction': linReg_prediction_Chainlink})
future_df['Date'] = pd.to_datetime(future_df['Date'])

complete_df = pd.concat([Ethereum, future_df], ignore_index=True)

complete_df = pd.concat([Arbitrum, future_df], ignore_index=True)

complete_df = pd.concat([Chainlink, future_df], ignore_index=True)

# Obtain predicted value data for specific dates
specific_dates = ['2024-04-17', '2024-04-18', '2024-04-19','2024-04-20','2024-04-21','2024-04-22','2024-04-23','2024-04-24','2024-04-25']  # Example dates
predicted_values_specific_dates = complete_df[complete_df['Date'].isin(specific_dates)]
print(predicted_values_specific_dates[['Date', 'Prediction']])

"""## **Predicting values for Ethereum**"""

linReg_prediction_Ethereum = linReg_Ethereum.predict(x_projection_Ethereum)
# linReg_prediction_Ethereum = (np.floor(linReg_prediction_Ethereum / 25)) * 25
print(linReg_prediction_Ethereum)

"""## **Predicting values for Arbitrum**"""

linReg_prediction_Arbitrum = linReg_Arbitrum.predict(x_projection_Arbitrum)
print(linReg_prediction_Arbitrum)

"""## **Predicting values for Chainlink**"""

linReg_prediction_Chainlink = linReg_Chainlink.predict(x_projection_Chainlink)
print(linReg_prediction_Chainlink)



"""## **ETHEREUM Predicted Price for 17TH FEB-25TH FEB**"""

import pandas as pd
import numpy as np
import plotly.graph_objects as go


# Assuming you have x_projection_Ethereum containing close prices,
# linReg_prediction_Ethereum containing predicted values,
# and projection_dates containing corresponding dates.

# Example: Generating sample projection dates
projection_dates = pd.date_range(start='2024-04-17', periods=len(x_projection_Ethereum), freq='D')


# Create a DataFrame for easier manipulation
projection_data = pd.DataFrame({
    'Date': projection_dates,
        'Predicted Value': linReg_prediction_Ethereum
        })
half_range = 12.5  # Half of 25 points
projection_data['Lower Bound'] = projection_data['Predicted Value'] - half_range
projection_data['Upper Bound'] = projection_data['Predicted Value'] + half_range
# projection_data['Prediction Range'] = projection_data.apply(lambda row: f"{row['Lower Bound']:.2f} - {row['Upper Bound']:.2f}", axis=1)
projection_data['Prediction Range'] = (projection_data.apply(lambda row: f"{np.floor(row['Lower Bound'] / 25) * 25:.2f} - {np.floor(row['Upper Bound'] / 25) * 25:.2f}", axis=1))


        # Create a Plotly table
table_fig = go.Figure(data=[go.Table(
header=dict(values=["Date", "Predicted Value", "Prediction Range"]),
cells=dict(values=[
  projection_data['Date'].dt.strftime('%Y-%m-%d'),  # Format dates as strings
  projection_data['Predicted Value'].map('{:.2f}'.format),  # Format values to 2 decimal places
  projection_data['Prediction Range']
  ])
  )])

# Update table layout
table_fig.update_layout(title="Projection Values for Ethereum ")
# Show the table
table_fig.show()

"""## **ARBITRUM Predicted Price for 17TH FEB-25TH FEB**"""

import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Example predicted values for Arbitrum

# linReg_prediction_Arbitrum = [1.44, 1.424, 1.47, 1.50, 1.54, 1.46, 1.45, 1.41, 1.19, 0.97]

# Example: Generating sample projection dates
projection_dates = pd.date_range(start='2024-04-17', periods=len(linReg_prediction_Arbitrum), freq='D')

# Define the half range
half_range = 0.125  # Half of 0.25 (25 points)

# Calculate lower and upper bounds
lower_bounds = [value - half_range for value in linReg_prediction_Arbitrum]
upper_bounds = [value + half_range for value in linReg_prediction_Arbitrum]

# Format prediction range
prediction_ranges = [f"{lower:.2f} - {upper:.2f}" for lower, upper in zip(lower_bounds, upper_bounds)]

# Create DataFrame
projection_data = pd.DataFrame({
    'Date': projection_dates,
    'Predicted Value': linReg_prediction_Arbitrum,
    'Prediction Range': prediction_ranges
    })

            # Create a Plotly table
table_fig = go.Figure(data=[go.Table(
                header=dict(values=["Date", "Predicted Value", "Prediction Range"]),
                    cells=dict(values=[
                            projection_data['Date'].dt.strftime('%Y-%m-%d'),  # Format dates as strings
                                    projection_data['Predicted Value'].map('{:.2f}'.format),  # Format values to 2 decimal places
                                            projection_data['Prediction Range']
                                                ])
                                                )])

                                                # Update table layout
table_fig.update_layout(title="Projection Values for Arbitrum")

                                                # Show the table
table_fig.show()

"""## **CHAINLINK Predicted Price for 17TH FEB-25TH FEB**


"""

import pandas as pd
import numpy as np
import plotly.graph_objects as go

projection_dates = pd.date_range(start='2024-04-17', periods=len(linReg_prediction_Chainlink), freq='D')

half_range = 0.125  # Half of 0.25 (25 points)

lower_bounds = [value - half_range for value in linReg_prediction_Chainlink]
upper_bounds = [value + half_range for value in linReg_prediction_Chainlink]

# Format prediction range
prediction_ranges = [f"{lower:.2f} - {upper:.2f}" for lower, upper in zip(lower_bounds, upper_bounds)]

projection_data = pd.DataFrame({
      'Date': projection_dates,
      'Predicted Value': linReg_prediction_Chainlink,
      'Prediction Range': prediction_ranges
                  })

table_fig = go.Figure(data=[go.Table(
header=dict(values=["Date", "Predicted Value", "Prediction Range"]),
cells=dict(values=[
projection_data['Date'].dt.strftime('%Y-%m-%d'),  # Format dates as strings
projection_data['Predicted Value'].map('{:.2f}'.format),  # Format values to 2 decimal places
                                                                                                                                                  projection_data['Prediction Range']
                                                                                                                                                                                                  ])
                                                                                                                                                                                                                                                  )])


table_fig.update_layout(title="Projection Values for Chainlink")

table_fig.show()