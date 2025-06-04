Sure! Here's the English version of the `README.md`, polished and developer-friendly:

---

````markdown
# 🧬 CellSlighter 0.7

> Slightly worse results than CellSighter, but just slightly more chaotic codebase.

---

## 📦 Requirements

1. Install all dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
````

---

## How to Run

### Training

To train the model, run:

```bash
python cellslighter/train.py
```

#### Training Data

* Unzip and place your training data in the following directory:

  ```
  train/
  ```

#### Checkpoints

* The **top 3 checkpoints** (based on validation metrics) are saved to:

  ```
  cellslighter/checkpoints/
  ```
* Their filenames are also listed in:

  ```
  cellslighter/checkpoints_path.txt
  ```

---

### Evaluation

To evaluate on data structured similarly to training data, run:

```bash
python cellslighter/test.py
```

#### Evaluation Data

* Unzip and place your test data here:

  ```
  test/
  ```

#### Loading Checkpoints

* The script reads checkpoint paths from:

  ```
  cellslighter/checkpoints_path.txt
  ```
* All required checkpoint files must exist in:

  ```
  cellslighter/checkpoints/
  ```

---

## Pretrained Weights

To validate using pretrained weights:

1. Download the checkpoint archive from:

   ```
   https://mega.nz/file/oWtkjZKB#ZEzWKBLw61Ac3QmVh3GR1Nhul9HGBkP0Mn3-1VQ7nHc
   ```
2. Extract and place the `.ckpt` files into:

   ```
   cellslighter/checkpoints/
   ```

---

## Quickstart

```bash
# Run training
python train.py
```

Let me know if you want a badge header (`build passing`, `license`, etc.), GitHub Actions CI integration, or an example output image/plot in the README.
```
