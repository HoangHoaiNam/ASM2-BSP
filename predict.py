import pandas as pd

# Tạo dữ liệu mẫu
data = {
    'Ad_Spend': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
    'Economic_Index': [5.1, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5],
    'Seasonality': [1, 2, 3, 4, 1, 2, 3, 4, 1, 2],
    'Sales': [150, 220, 330, 440, 560, 670, 780, 890, 1000, 1110]
}

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(data)

# Xác định các đặc trưng đầu vào (X) và biến mục tiêu (y)
X = df[['Ad_Spend', 'Economic_Index', 'Seasonality']]
y = df['Sales']


from sklearn.model_selection import train_test_split

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.linear_model import LinearRegression

# Khởi tạo mô hình hồi quy tuyến tính
model = LinearRegression()

# Huấn luyện mô hình
model.fit(X_train, y_train)


# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá mô hình
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'R-squared: {r2}')


# Dữ liệu mới
future_data = pd.DataFrame({
    'Ad_Spend': [1100, 1200],
    'Economic_Index': [10.0, 10.5],
    'Seasonality': [3, 4]
})

# Dự đoán doanh số tương lai
future_sales = model.predict(future_data)
print(f'Future Sales Predictions: {future_sales}')
