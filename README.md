# QPSK OFDM Simulation Project

## Overview
This project simulates a QPSK modulation system combined with OFDM channel coding. The implementation consists of two main files: `DnCNN_LS.py` and `data_gen.py`.
## References:
  - [1](https://repository.library.northeastern.edu/files/neu:cj82pr619/fulltext.pdf) Amir Tadayon, Channel Estimation For OFDM Systems.
  - [2](https://www.diva-portal.org/smash/get/diva2:996957/FULLTEXT01.pdf). Ov Edfors et Al, An introduction to orthogonal frequency-division multiplexing.

## Features
- QPSK modulation and demodulation
- OFDM channel coding with block-type pilots
- Assume that the length of one frame is shorter than the coherent time
- Dataset generation through the `data_gen.py` script
- The DnCNN_LS models were trained with SNR values at 0, 5, 10, 15, 20, and 25 dB, located in the results folder as `.keras` file, with 150 epochs

