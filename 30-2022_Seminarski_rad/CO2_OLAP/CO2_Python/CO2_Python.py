import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv(r'C:\Users\Aleksa\Desktop\30-2022_Seminarski_rad\CO2 emission by countries.csv', encoding='latin1')
df.columns = ['Country','Code','CallingCode','Year','CumEmission','Population','Area','PctWorld','Density']
df['PctWorld'] = df['PctWorld'].astype(str).str.replace('%','').str.replace(',','').astype(float)
df['Density'] = df['Density'].astype(str).str.replace('/km²','').str.replace(',','').astype(float)
df = df.sort_values(['Country','Year'])
df['AnnualEmission'] = df.groupby('Country')['CumEmission'].diff()

clean = df.dropna(subset=['AnnualEmission','Population','Area','Density']).copy()
clean['LogEmission'] = np.log1p(clean['AnnualEmission'])

features = ['Year','Population','Area','Density']
X = clean[features]
y = clean['LogEmission']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lin_model = LinearRegression()
rf_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
lin_model.fit(X_train, y_train)
rf_model.fit(X_train, y_train)
lin_pred = lin_model.predict(X_test)
rf_pred = rf_model.predict(X_test)

# Slika 14 - Feature importance
importances = pd.Series(rf_model.feature_importances_, index=features).sort_values(ascending=True)
print(importances)

plt.figure(figsize=(7,4))
importances.plot(kind='barh', color='darkgreen')
plt.xlabel('Važnost atributa')
plt.title('Važnost atributa u Random Forest modelu')
plt.tight_layout()
plt.savefig('slika14_feature_importance.png', dpi=150)
plt.show()

# Slika 15 - Predicted vs Actual, oba modela jedan pored drugog
fig, axes = plt.subplots(1, 2, figsize=(13,6))

axes[0].scatter(y_test, lin_pred, alpha=0.3, s=10, color='indianred')
axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', linewidth=2)
axes[0].set_xlabel('Stvarna vrednost (log skala)')
axes[0].set_ylabel('Predviđena vrednost (log skala)')
axes[0].set_title('Linear Regression')

axes[1].scatter(y_test, rf_pred, alpha=0.3, s=10, color='steelblue')
axes[1].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', linewidth=2)
axes[1].set_xlabel('Stvarna vrednost (log skala)')
axes[1].set_ylabel('Predviđena vrednost (log skala)')
axes[1].set_title('Random Forest')

plt.suptitle('Stvarne vs. Predviđene vrednosti — poređenje modela')
plt.tight_layout()
plt.savefig('slika15_predicted_vs_actual_oba.png', dpi=150)
plt.show()