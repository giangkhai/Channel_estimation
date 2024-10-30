# QPSK OFDM Simulation Project

## Overview
This project simulates a QPSK modulation system combined with OFDM channel coding. The implementation consists of two main files: `DnCNN_LS.py` and `data_gen.py`. The OFDM system simulates a uniformly distributed pilot across K sub-carriers. The OFDM channel is modeled based on the thesis by Amir Tadayon, which can be referenced [here](https://repository.library.northeastern.edu/files/neu:cj82pr619/fulltext.pdf).

## Features
- QPSK modulation and demodulation
- OFDM channel coding with block-type pilots
- Assume that the length of one frame is shorter than the coherent time
- Simulation of the OFDM channel based on Amir Tadayon's work
- Dataset generation through the `data_gen.py` script

