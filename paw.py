import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

with st.sidebar:
    tipe=st.radio('pilih tipe', ['Distribusi Diskrit', 'Distribusi Kontinyu'])


if tipe == 'Distribusi Diskrit':
      
        def calculate_binomial_distribution(n, p, k):
            x = np.arange(0, n+1)
            y = np.zeros(n+1)

            for i in range(k+1):
                y[i] = (np.math.factorial(n) / (np.math.factorial(i) * np.math.factorial(n-i))) * (p**i) * ((1-p)**(n-i))
            return x, y
        
        def main():
            st.title("Distribusi Binomial")   

            n = st.number_input("Masukkan jumlah percobaan (n):", min_value=1, value=10, step=1)
            p = st.number_input("Masukkan probabilitas sukses (p):", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
            k = st.number_input("Masukkan jumlah sukses (k):", min_value=0, value=5, step=1)

            if st.button("Hitung dan Tampilkan Distribusi"):
                x, y = calculate_binomial_distribution(n, p, k)

                fig, ax = plt.subplots()
                ax.bar(x, y)
                ax.set_xlabel('Jumlah Sukses (k)')
                ax.set_ylabel('Probabilitas')
                ax.set_title('Distribusi Binomial')
                st.pyplot(fig)

        if __name__ == "__main__":
            main()

        def calculate_poisson_distribution(lambd, k):
            x = np.arange(0, k+1)
            y = np.zeros(k+1)

            for i in range(k+1):
                y[i] = (np.exp(-lambd) * (lambd**i)) / np.math.factorial(i)

            return x, y
        
        def main():
            st.title("Distribusi Poisson")

            lambd = st.number_input("Masukkan parameter lambda:", min_value=0.01, value=1.0, step=0.01)
            k = st.number_input("Masukkan jumlah kejadian(k):", min_value=0, value=10, step=1)
            if st.button("Tampilkan Distribusi"):
                x, y = calculate_poisson_distribution(lambd, k)

                fig, ax = plt.subplots()
                ax.bar(x, y)
                ax.set_xlabel('Jumlah Kejadian (k)')
                ax.set_ylabel('Probabilitas')
                ax.set_title('Distribusi Poisson')
                st.pyplot(fig)
        if __name__ == "__main__":
            main()

elif tipe == 'Distribusi Kontinyu':

    def calculate_exponential_distribution(lambd, x):
        y = lambd * np.exp(-lambd * x)
        return y
    def main():
        st.title("Distribusi Eksponensial")

        lambd = st.number_input("Masukkan parameter lambda:", min_value=0.01, value=1.0, step=0.01)
        x = np.linspace(0, 10, 100)

        if st.button("Hitung dan Tampilkan Distribusi"):
            y = calculate_exponential_distribution(lambd, x)
        
            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.fill_between(x, 0, y, alpha=0.3)
            ax.set_xlabel('Nilai')
            ax.set_ylabel('Distribusi Eksponensial')
            ax.set_title('Distribusi Eksponensial')
            st.pyplot(fig)
    if __name__ == "__main__":
        main()
    
    
    def main():
        st.title('Aplikasi Distribusi Normal')
        mean = st.number_input('Mean', value=0.0)
        std = st.number_input('Standard Deviasi', value=1.0)
        x = st.number_input('Nilai x', value=0.0)

        # Menghitung nilai distribusi normal
        p = norm.pdf(x, mean, std)
        cdf = norm.cdf(x, mean, std)

        # Menampilkan hasil
        st.write('Nilai PDF:', p)
        st.write('Nilai CDF:', cdf)

    if __name__ == '__main__':
        main()



