import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from crop_dataset import crop_data


if __name__ == "__main__":
    # Load into DataFrame
    df = pd.DataFrame(crop_data)

    # Features and labels
    X = df[['pH', 'N', 'P', 'K']]
    y = df['name']

    # Train Decision Tree Classifier
    clf = DecisionTreeClassifier()
    clf.fit(X, y)



    # Predict example
    sample = pd.DataFrame([{'pH': 6.5, 'N': 90, 'P': 40, 'K': 60}])
    probs = clf.predict_proba(sample)
    for label, prob in zip(clf.classes_, probs[0]):
        print(f"{label}: {prob:.3f}")

    # Optional: most probable crop
    prediction = clf.predict(sample)
    print("\nMost probable crop:", prediction[0])