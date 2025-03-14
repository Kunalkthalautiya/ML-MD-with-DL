from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Dummy Training Data
X_train = ["I love this product", "This is the worst thing ever", "Awesome service", "Not worth the price"]
y_train = [1, 0, 1, 0]

# Model Pipeline
model = Pipeline([('vectorizer', CountVectorizer()), ('classifier', MultinomialNB())])
model.fit(X_train, y_train)

# Model Save
joblib.dump(model, 'app/model.pkl')
print("Model saved successfully!")
