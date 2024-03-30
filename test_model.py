import yfinance as yf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('predictor.h5')

# Load and preprocess the test data
stock_symbol = "BTC-USD"
start_date = "2024-01-01"
end_date = "2024-02-01"
data = yf.download(stock_symbol, start=start_date, end=end_date)

def preprocess_data(data, data_scaler):
    scaled_data = data_scaler.transform(data[['Close']].values)
    return scaled_data

# Assuming you have saved MinMaxScaler during training
data_scaler = MinMaxScaler()
data_scaler.fit_transform(data[['Close']].values)

# Preprocess the test data
scaled_data = preprocess_data(data, data_scaler)

sequence_length = 20

# Create sequences
def create_sequences(data, sequence_length):
    X = []
    for i in range(len(data) - sequence_length):
        X.append(data[i:i+sequence_length])
    return np.array(X)

X_test = create_sequences(scaled_data, sequence_length)

# Predict
y_pred = model.predict(X_test)
y_pred = data_scaler.inverse_transform(y_pred)

# Calculate Mean Squared Error
actual_prices = data['Close'].values[sequence_length:]
mse = mean_squared_error(actual_prices, y_pred)

print(f"Mean Squared Error on Test Data: {mse}")
