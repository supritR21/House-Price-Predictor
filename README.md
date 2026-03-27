# House Price Predictor

End-to-end machine learning project for house price prediction using the Ames Housing dataset, built with ZenML pipelines and MLflow model deployment.

## Overview

This repository contains a production-style ML system under:

- `prices-predictor-system/`

The pipeline performs:

1. Data ingestion from compressed dataset
2. Missing value handling
3. Feature engineering
4. Outlier removal
5. Train/test split
6. Model training and evaluation
7. Continuous deployment with MLflow serving
8. Inference from deployed model service

## Tech Stack

- Python 3.12
- ZenML
- MLflow
- scikit-learn
- pandas / numpy
- matplotlib / seaborn / statsmodels

## Project Structure

```text
House-Price-Predictor/
	prices-predictor-system/
		analysis/
		data/
		extracted_data/
			AmesHousing.csv
		pipelines/
			training_pipeline.py
			deployment_pipeline.py
		src/
		steps/
		requirements.txt
		config.yaml
		run_pipeline.py
		run_deployment.py
		sample_predict.py
```

## Setup

### 1. Navigate into the main ML project

```bash
cd prices-predictor-system
```

### 2. Create virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize ZenML (first time only)

```bash
zenml init
```

## Run Training Pipeline

Primary pipeline file:

- `pipelines/training_pipeline.py`

Run:

```bash
python pipelines/training_pipeline.py
```

This executes:

- `data_ingestion_step`
- `handle_missing_values_step`
- `feature_engineering_step`
- `outlier_detection_step`
- `data_splitter_step`
- `model_building_step`
- `model_evaluator_step`

## Run Deployment + Inference Pipelines

Deployment script:

- `run_deployment.py`

Run:

```bash
python run_deployment.py
```

This triggers:

- `continuous_deployment_pipeline()`
- `inference_pipeline()`

Stop active deployed prediction service:

```bash
python run_deployment.py --stop-service
```

## MLflow UI

After running pipelines, open MLflow UI:

```bash
mlflow ui
```

Then visit:

- `http://127.0.0.1:5000`

## Prediction Flow

The deployed model inference step uses:

- `steps/dynamic_importer.py` for sample batch data
- `steps/prediction_service_loader.py` to locate MLflow deployment service
- `steps/predictor.py` to run predictions

## Data

Dataset used:

- Ames Housing (`extracted_data/AmesHousing.csv`)

Training pipeline also references:

- `data/archive.zip`

Ensure expected data files exist before training.

## Configuration

Model metadata and ZenML settings are defined in:

- `config.yaml`

Includes:

- model name: `prices_predictor`
- tags: regression / housing / price prediction
- Docker integration requirement for MLflow

## Known Issues (Current Codebase)

There are a few typos/bugs in current scripts:

- `run_pipeline.py` assigns `run = ml_pipeline` but does not call it.
- `run_deployment.py` has a pipeline name typo with extra spacing/character mismatch in service lookup.
- `steps/prediction_service_loader.py` returns `existing_services` list while annotation says single service.
- `sample_predict.py` uses `requests.posts` instead of `requests.post` and references `response.txt` instead of `response.text`.

These can affect deployment and manual prediction testing.

## Useful Commands

```bash
# Training
python pipelines/training_pipeline.py

# Deployment + inference
python run_deployment.py

# Stop model service
python run_deployment.py --stop-service

# MLflow UI
mlflow ui
```

## Author

Suprit Raj
