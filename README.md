# House Price Prediction

A tiny NumPy example that estimates a house price from a few known homes. Each example has an area and bedroom count; the program finds the two examples closest to a chosen home and averages their prices.

## Requirements

- Python 3
- NumPy

## Run it

```bash
python -m pip install numpy
python main.py
```

On Windows, use `py` instead of `python` if that is how Python is installed:

```powershell
py -m pip install numpy
py main.py
```

With the sample data and input in `main.py`, the program prints:

```text
205.0
```

## Change the example

Edit `houses` and `prices` in `main.py` to add or change training examples. Each row in `houses` is `[area, bedrooms]`, and the corresponding value at the same index in `prices` is that home's price. Then change `new_house_area` and `bedrooms` to the home you want to estimate.

The script calculates the Euclidean distance from the input to every example, rounds the distances, selects the two smallest, and returns the average of their prices. The sample prices use arbitrary units; the program does not assign a currency.

## Limitations

This is a compact learning demo, not a market-ready valuation model. Area and bedroom count are compared as raw numbers, so area has much more influence on distance than bedroom count. The data is also hard-coded, and the estimate uses only the two nearest examples.
