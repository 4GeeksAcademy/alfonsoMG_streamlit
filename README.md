Sure, I can help you with that. Here's the corrected markdown:


# Diabetes Prediction Web App with Streamlit

This repository contains a simple web application for predicting diabetes using a pre-trained decision tree model. The app is built with Streamlit and allows users to input various health-related parameters through sliders, obtaining a prediction based on the trained model.

## Getting Started

### Prerequisites

- Python 3.6 or later
- pip (package installer for Python)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

### Usage

Run the Streamlit app locally:

   ```bash
   streamlit run streamlit.py
   ```

Visit http://localhost:8501 in your web browser to interact with the application.

### Input Features

The following health parameters can be adjusted using sliders:

- Number of Pregnancies
- Level of Glucose
- Level of Blood Pressure
- Skin Thickness
- Level of Insulin
- BMI (Body Mass Index)
- Diabetes Pedigree
- Age

After adjusting the sliders, click the "Predict" button to obtain a prediction on whether the user is likely to suffer from diabetes or not. The result will be displayed on the web page.

### Model Details

The prediction is made using a decision tree model trained on a dataset related to diabetes. The pre-trained model is loaded from the file models/decision_tree_optimized_model.pk.
The data information is taken form the X_train.csv contained in the data/processed directory.

### Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and contributions are highly appreciated.


```
   (\,/)
   ( . .)
   (")_(")
```
Happy coding :) !

