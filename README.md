# Liquid Lithium-Water Fluid Dynamic Equivalency Calculator

This application provides a graphical interface for calculating the fluid dynamic equivalency between liquid lithium and water. The properties of lithium used in the calculations are referenced from Jeppson, D W, et al. “Lithium Literature Review: Lithium's Properties and Interactions.” Lithium Literature Review: Lithium's Properties and Interactions (Technical Report) | OSTI.GOV, 1 Apr. 1978.



## How to Run
Ensure you have Python and the required libraries installed (Tkinter, math, matplotlib, numpy). Download the Python script and run it with:
```sh
python tpi.py
```

## Functionality

The program asks the user to enter the following data:

1. Temperature of liquid lithium (°C)
2. Velocity of flow (m/s)
3. Hydraulic diameter of orifice (in m)
4. Diameter of water nozzle (in m)

By clicking the "Enter Requested Data" button, the program performs a series of calculations and generates a plot of the nozzle diameter as a function of water temperature. The resulting physical parameters are then displayed in the application's GUI.

The physical parameters included are:

- Dynamic viscosity of Lithium at given temperature (°C)
- Surface tension of Lithium at given temperature (°C)
- Density of water
- Dynamic viscosity of water at calculated temperature (°C)
- Surface tension of water at calculated temperature (°C)
- Reynolds number
- Weber number
- Calculated velocity (m/s)
- Water temperature (°C)
- Flow rate (GPM)

The calculations are based on fluid dynamic principles and consider various physical properties such as density, viscosity, surface tension, Reynolds number, and Weber number.

## Dependencies

This application requires the following Python libraries:

- `Tkinter`: For the GUI.
- `math`: For mathematical functions and constants.
- `matplotlib`: For plotting the results.
- `numpy`: For handling arrays and numerical calculations.

To install these dependencies, use the following command:

```sh
pip install matplotlib numpy
```
Note: Tkinter and math are part of the standard Python library and do not require separate installation.


