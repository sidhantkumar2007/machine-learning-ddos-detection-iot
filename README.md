# UL-ECE-DDoS-H-IoT-Datasets2025

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15305814.svg)](https://doi.org/10.5281/zenodo.15305814)

This repository hosts two datasets for DDoS attack detection in Healthcare IoT (H-IoT) environments:

* **UL-ECE-MQTT-DDoS-H-IoT2025** (simulated using Cooja with MQTT traffic)
* **UL-ECE-UDP-DDoS-H-IoT2025** (simulated using ns-3 with UDP traffic)

Both datasets provide preprocessed CSV files along with their corresponding preprocessing scripts.

---

## Repository Structure

```text
UL-ECE-DDoS-H-IoT-Datasets2025/
├── MQTT/
│   ├── UL-ECE-MQTT-DDoS-H-IoT2025.csv
│   ├── UL-ECE-MQTT-DDoS-H-IoT2025-raw.txt (raw data)
│   └── preprocessing_ddos_mqtt_cooja.py
│
├── UDP/
│   ├── UL-ECE-UDP-DDoS-H-IoT2025.csv
│   └── preprocessing_ddos_udp_ns_3.py
│
├── ddos_detection_project.py   ← Machine Learning Model
└── README.md
```

> **Note:**
> The raw simulation log file for UL-ECE-UDP-DDoS-H-IoT2025 is larger than the platform's upload limit and is available upon request.

---

## Citation

If you use these datasets in your research, please cite:

```bibtex
@article{akhi2025tcn,
  title={TCN-Based DDoS Detection and Mitigation in 5G Healthcare-IoT: A Frequency Monitoring and Dynamic Threshold Approach},
  author={Akhi, Mirza and Eising, Ciarán and Dhirani, Lubna Luxmi},
  journal={IEEE Access},
  year={2025},
  publisher={IEEE}
}
```

---

## Dataset Authors

* Mirza Akhi
* University of Limerick (UL), Ireland

---

# Machine Learning Model for IoT DDoS Detection

## Overview

This project includes a Machine Learning implementation to detect DDoS attacks using the **MQTT dataset**.

The model classifies IoT traffic into:

*  Normal Traffic
*  DDoS Attack

---

## Model Details

* **Algorithm:** Random Forest Classifier
* **Library:** Scikit-learn
* **Type:** Supervised Learning

---

## Workflow

1. Load dataset using Pandas
2. Explore data (head, info, missing values)
3. Auto-detect target column
4. Encode categorical features
5. Split data (80% train / 20% test)
6. Train Random Forest model
7. Evaluate performance

---

## Output

* Accuracy Score
* Classification Report
* Confusion Matrix
* Feature Importance Graph
* Target Distribution Plot

---

## How to Run

```bash
pip install pandas numpy matplotlib seaborn scikit-learn

python ddos_detection_project.py
```

---

## Notes

* Ensure dataset path is correct (`MQTT/UL-ECE-MQTT-DDoS-H-IoT2025.csv`)
* Works on preprocessed data
* Large datasets may require sufficient RAM

---

## Future Improvements

* Deep Learning models (LSTM / CNN)
* Real-time detection system
* API deployment (Flask / FastAPI)
* Hyperparameter tuning

---

# Project Group Members

| Enrollment No. | Name                        |
| -------------- | -----------------           |
| 24BSA10100     | MEDHAVI DHEER SRIVASTAVA    |
| 24BSA10116     |  ADARSH KUMAR               |
| 24BSA10134     | SHATAKSHI AKHILESH THAKUR   |
| 24BSA10148     | HIRAL JAGETIYA              |
| 24BSA10171     | MANAV VIJAY YADAV           |
| 24BSA10172     | SIDHANT KUMAR               |

---

## Acknowledgment

Dataset provided by:

* Mirza Akhi
* University of Limerick (UL), Ireland
