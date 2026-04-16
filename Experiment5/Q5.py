import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load dataset (change filename if needed)
df = pd.read_csv("data.csv")

# Keep only numeric columns
df = df.select_dtypes(include=['number'])

# Fill missing values with mean
df.fillna(df.mean(), inplace=True)

# Feature Scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Apply PCA (reduce to 2 components)
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)

# Create DataFrame for PCA result
pca_df = pd.DataFrame(pca_data, columns=['PC1', 'PC2'])

# Print output
print("PCA Result:\n", pca_df.head())

# Explained variance
print("\nExplained Variance Ratio:", pca.explained_variance_ratio_)

# Plot graph
plt.scatter(pca_df['PC1'], pca_df['PC2'])
plt.title("PCA Visualization")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()