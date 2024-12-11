# AI Camera Classifier

This repository contains an AI-based Camera Classifier that detects and classifies objects in images. The model is trained using a custom dataset and employs machine learning techniques to predict the names of objects in real time.

---

## Features

- **Image Classification:** Trained to identify and classify objects in images.
- **Model Training:** Built using a dataset to train the model effectively.
- **Object Detection:** Predicts the object's name from new input images.
- **User-Friendly:** Easy to use with a well-documented setup process.

---

## Technologies Used

- **Programming Language:** Python
- **Libraries:**
  - TensorFlow/Keras for model building and training
  - OpenCV for image processing
  - NumPy for data manipulation
  - Matplotlib for visualization

---

## Project Structure

```
AI--Camera-Classifier/
│
├── dataset/                 # Contains the training and testing datasets
├── models/                  # Saved model files
├── src/                     # Source code for the project
│   ├── train.py             # Script to train the model
│   ├── predict.py           # Script to make predictions
│   └── utils.py             # Utility functions
├── requirements.txt         # Dependencies
└── README.md                # Project documentation (this file)
```

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Likith-Yadav/AI--Camera-Classifier.git
   cd AI--Camera-Classifier
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Train the Model:**
   - Place your training images in the `dataset/train/` directory.
   - Run the training script:
     ```bash
     python src/train.py
     ```

2. **Make Predictions:**
   - Place an image in the `test_images/` folder or use the camera feed.
   - Run the prediction script:
     ```bash
     python src/predict.py --image <path_to_image>
     ```

3. **View Results:**
   - The script will output the predicted object name and display the image.

---

## Example Output

![Example Output]![Screenshot (102)](https://github.com/user-attachments/assets/c5b99f85-e3dd-48fa-8598-43ecf64e5d67)
![Screenshot (103)](https://github.com/user-attachments/assets/289778e0-9570-48da-a7ea-8c1c32a86472)


---

## Future Enhancements

- Add real-time object detection using webcam.
- Improve accuracy by using a larger dataset.
- Deploy the model as a web application.

---

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request with your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Inspiration: AI and ML community.
- Libraries: TensorFlow, OpenCV, NumPy, and others.

---

## Author

**Likith Yadav**  
[GitHub](https://github.com/Likith-Yadav)  
[LinkedIn](https://www.linkedin.com/in/likith-yadav/)
