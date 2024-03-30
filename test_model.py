import yfinance as yf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import load_model

def test_lstm_model():
    # Load the trained model
    model = load_model('predictor.h5')

    # Load and preprocess the test data
    stock_symbol = "BTC-USD"
    start_date = "2024-01-01"
    end_date = "2024-02-01"
    data = yf.download(stock_symbol, start=start_date, end=end_date)

    def preprocess_data(data):
        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(data[['Close']].values)
        return scaled_data, scaler

    scaled_data, data_scaler = preprocess_data(data)

    sequence_length = 20

    # Sequence-to-Sequence Transformation
    def create_sequences(data, sequence_length):

        X, y = [], []
        for i in range(len(data) - sequence_length):
            X.append(data[i:i+sequence_length])
            y.append(data[i+sequence_length])
        return np.array(X), np.array(y)


    X_test, y_test = create_sequences(scaled_data, sequence_length)

    # Predict
    y_pred = model.predict(X_test)
    y_pred = data_scaler.inverse_transform(y_pred)

    # Calculate Mean Squared Error
    actual_prices = data_scaler.inverse_transform(y_test)
    mse = mean_squared_error(actual_prices, y_pred)

    # Assert the Mean Squared Error is less than a threshold
    assert mse < 10000, "Mean Squared Error is too high"

    # Additional tests can be added here if needed

