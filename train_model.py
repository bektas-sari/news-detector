import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Veriyi yükleyelim
df = pd.read_csv("final_news.csv")

# Boş değerleri temizle
df.dropna(subset=["cleaned_text"], inplace=True)  # NaN olan satırları sil
df["cleaned_text"] = df["cleaned_text"].astype(str)  # Tüm değerleri string olarak ayarla

# Özellikleri (X) ve etiketleri (y) ayıralım
X = df["cleaned_text"]
y = df["label"]

# Veriyi eğitim (%80) ve test (%20) olarak ayıralım
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF vektörleştirme (Metni sayısal verilere çevirme)
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Modeli oluştur ve eğit
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Modeli test et
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)

# Sonuçları yazdır
print(f"✅ Model Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred))

# Modeli kaydet
with open("fake_news_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

# TF-IDF vektörizeri de kaydet
with open("tfidf_vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("✅ Model and vectorizer saved successfully!")
