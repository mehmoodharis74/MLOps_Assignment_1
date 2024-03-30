import yfinance as yf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split

# Defining the stock values and downloading data from yahoo finance
stock_symbol = "ETH-USD"
start_date = "2023-01-01"
end_date = "2024-01-01"
data = yf.download(stock_symbol, start=start_date, end=end_date)

print(data)


# Data Preprocessing using MinMaxScaler
def preprocess_data(data):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data[['Close']].values)

    return scaled_data, scaler


scaled_data, data_scaler = preprocess_data(data)


# Sequence-to-Sequence Transformation
def create_sequences(data, sequence_length):

    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[i:i+sequence_length])
        y.append(data[i+sequence_length])
    return np.array(X), np.array(y)


sequence_length = 20
X, y = create_sequences(scaled_data, sequence_length)

# Split the Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False)


model = Sequential()
model.add(LSTM(units=128, activation='tanh', input_shape=(sequence_length, 1)))
model.add(Dense(32, activation='linear'))
model.add(Dense(16, activation='linear'))
model.add(Dense(1, activation='relu'))
model.compile(optimizer='adam', loss='mean_squared_error')

# Model Training
epochs = 50
batch_size = 32
history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

model.save('predictor.h5')

# Model Evaluation
y_pred = model.predict(X_test)
y_pred = data_scaler.inverse_transform(y_pred)
y_test = data_scaler.inverse_transform(y_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error on Test Data: {mse}")

