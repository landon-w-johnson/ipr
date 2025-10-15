# Requirements

1. Python with NumPy

# How to Use This

1. Put `calculateIPR.py` in a working directory with all of the `PARCHG` files for which you want to calculate the IPR.

1. Set the variable `electrons_per_orbital` in the script `calculateIPR.py` appropriately. It should be 1 if you include the tag `LNONCOLLINEAR=.TRUE.` in your `INCAR`, or 2 otherwise.

1. Run `calculateIPR.py`.

1. Your IPR values are stored in `ipr.txt`.

# Known Bugs

1. This is not using the scaling factor, so any scaling factor other than 1 will cause problems.

1. This will not work for spin-polarized or noncollinear spin calculations. It reads the entire length of the `PARCHG` files, not just to the end of the spin up + spin down block.