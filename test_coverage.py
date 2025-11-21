name: Python CI 

on:
    push:
        branches: [ main ]

jobs:
    test-coverage:
        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v4

        - name: Set up Python
          uses: actions/setup-python@v5
          with:
              python-version: '3.10'

        - name: Install dependencies
          run: |
              python -m pip install --upgrade pip
              pip install pytest coverage

        - name: run Unit Tests
          run: |
              python -m unittest test_graph.py

