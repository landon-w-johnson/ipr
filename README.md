# Requirements

1. Python with NumPy

# How to Use This

1. Put `calculateIPR.py` in a working directory with all of the `PARCHG` files for which you want to calculate the IPR.

1. Set the variable `electrons_per_orbital` in the script `calculateIPR.py` appropriately. It should be 1 if you include the tag `LNONCOLLINEAR=.TRUE.` in your `INCAR`, or 2 otherwise.

1. Run `calculateIPR.py`.

1. Your IPR values are stored in `ipr.txt`.

# Known Bugs

1. All of the `PARCHG` files in your working directory **must** be from the same system. The script only reads the number of data entries from the first `PARCHG` file it finds, so any mismatches will cause it to crash or give incomplete data.