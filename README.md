# Encrypt and Decrypt - Python Project

This repository contains Python implementations for encryption and decryption algorithms. It aims to demonstrate basic techniques for securing data through encryption and recovering the original data with decryption. The repository includes implementations that handle encryption and decryption using random keys.

## Repository Structure

```plaintext
Encrypt_Decrypt/
├── 28.txt                           # Sample text file used for encryption/decryption demonstration
├── Algo.ipynb                       # Jupyter notebook demonstrating encryption and decryption methods
├── Encrypt_Decrypt_Random.py        # Python script for random encryption and decryption
```

## Description of Files

- **28.txt**: This text file serves as a sample input for encryption and decryption. It contains data that is used to demonstrate how the encryption and decryption scripts work.

- **Algo.ipynb**: This Jupyter notebook provides a more interactive way to experiment with encryption and decryption algorithms. It explains the theory behind the algorithms and shows how to use them.

- **Encrypt_Decrypt_Random.py**: This Python script implements a basic random encryption and decryption algorithm. It generates a random key for the encryption process, and the same key is used for decryption to recover the original message.

## How to Use

1. **Clone the Repository**: 
   Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/senani-derradji/Encrypt_Decrypt.git
   ```

2. **Run the Scripts**:
   You can run the `Encrypt_Decrypt_Random.py` script to perform encryption and decryption operations. To execute the script:
   - Open a terminal or command prompt.
   - Navigate to the directory where the scripts are located.
   - Execute the script using:
     ```bash
     python Encrypt_Decrypt_Random.py
     ```

3. **Work with the Jupyter Notebook**:
   If you want to use the Jupyter notebook, make sure you have Jupyter installed. Then open `Algo.ipynb` in Jupyter and run the cells to learn about and execute the encryption/decryption methods.

4. **Modify and Experiment**:
   You can modify the text in `28.txt` to test different inputs, and experiment with the random encryption method by editing the Python script.

## Requirements

- Python 3.x
- Jupyter (for the notebook)
- No external libraries are required, but you may use libraries like `cryptography` for more advanced encryption methods.
