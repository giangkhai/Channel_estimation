import numpy as np
from scipy.linalg import dft
K = 64
def generate_data(num_samples, K, dB, Np):

    sigma_z = 10 ** (-dB / 20)
    Tg = 10e-6
    tau_rms = 2.5e-6
    f0 = 900e6
    T = 128e-6

    X1 = np.zeros((num_samples, K), dtype=float)
    X2 = np.zeros((num_samples, K), dtype=float)
    y1 = np.zeros((num_samples, K), dtype=float)
    y2 = np.zeros((num_samples, K), dtype=float)
    for i in range(num_samples):

        tau_p = np.zeros(Np)
        tau_p[1:] = np.random.uniform(0, Tg, Np - 1)


        sigma_hp_squared = np.exp(-tau_p / tau_rms)
        sigma_hp_squared /= np.sum(sigma_hp_squared)
        real_hp = np.random.normal(0, np.sqrt(sigma_hp_squared / 2), Np)
        imag_hp = np.random.normal(0, np.sqrt(sigma_hp_squared / 2), Np)
        hp = real_hp + 1j * imag_hp

        b = np.zeros(K, dtype=complex)
        for l in range(K):
            sum_hp = 0
            for p in range(Np):
                phase1 = np.exp(-2j * np.pi * f0 * tau_p[p])
                phase2 = np.exp(-1j * np.pi * (K - 1) * (tau_p[p] / T - l / K))

                denom = np.sin(np.pi * (tau_p[p] / T - l / K))
                if np.abs(denom) < 1e-10:
                    sinc_part = K
                else:
                    sinc_part = (np.sin(np.pi * K * (tau_p[p] /T - l / K)) / denom)

                sum_hp += hp[p] * phase1 * phase2 * sinc_part
            b[l] = sum_hp / K


        H = np.fft.fft(b)

        QPSK = np.array([np.exp(1j * np.pi / 4), np.exp(3 * 1j * np.pi / 4), np.exp(5 * 1j * np.pi / 4), np.exp(7 * 1j * np.pi / 4)])
        d_values = np.random.choice(QPSK, size=K)


        z = np.sqrt(sigma_z / 2) * (np.random.randn(K) + 1j * np.random.randn(K))
        D = np.diag(d_values)
        y = D@H + z

        X1[i] = np.real(np.linalg.inv(D)@y)
        X2[i] = np.imag(np.linalg.inv(D)@y)
        y1[i] = np.real(H)
        y2[i] = np.imag(H)
    return X1, X2, y1, y2

X1_train, X2_train, y1_train, y2_train = generate_data(5000, K, 5, 5)
X1_test , X2_test, y1_test, y2_test = generate_data(1000, K, 5, 5)
X_train = np.concatenate((X1_train, X2_train), axis=1)
y_train = np.concatenate((y1_train, y2_train), axis=1)
X_test = np.concatenate((X1_test, X2_test), axis=1)
y_test = np.concatenate((y1_test, y2_test), axis=1)
