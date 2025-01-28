import streamlit as st
import numpy as np

def calculate_lambda_lim(A, B, C, n):
    return 20 * A * B * C / np.sqrt(n)

def main():
    
    st.title("Verifica di Snellezza di un Pilastro in CLS")
    
    st.header("Inserisci i dati di input")
    
    q_eff = st.number_input("Coefficiente di fluage effettivo (φ_eff)", min_value=0.0, step=0.1, value=2.0)
    A = 1 / (1 + 0.2 * q_eff) if q_eff > 0 else 0.7
    st.latex(r"\A = 1 / (1 + 0.2 * q_eff) ")
    omega = st.number_input("Rapporto meccanico di armatura (ω)", min_value=0.0, step=0.1, value=0.02)
    B = np.sqrt(1 + 2 * omega) if omega > 0 else 1.1
    
    M01 = st.number_input("Momento estremo M01 (kNm)", value=50.0)
    M02 = st.number_input("Momento estremo M02 (kNm, con |M02| ≥ |M01|)", value=70.0)
    
    r_m = M01 / M02 if M02 != 0 else 0.7
    C = 1.7 - r_m if r_m > 0 else 0.7
    
    NEd = st.number_input("Forza assiale NEd (kN)", value=500.0)
    Ac_fcd = st.number_input("Ac * fcd (kN)", value=1000.0)
    n = NEd / Ac_fcd if Ac_fcd != 0 else 1.0
    
    lambda_lim = calculate_lambda_lim(A, B, C, n)
    
    st.subheader("Risultati della verifica")
    st.latex(r"\lambda_{lim} = 20 \cdot A \cdot B \cdot C / \sqrt{n}")
    st.write(f"Sostituendo i valori numerici:")
    st.latex(f"\lambda_{{lim}} = 20 \cdot {A:.2f} \cdot {B:.2f} \cdot {C:.2f} / \sqrt{{{n:.2f}}} = {lambda_lim:.2f}")
    
    lambda_input = st.number_input("Inserisci il valore di λ calcolato", value=30.0)
    
    if lambda_input < lambda_lim:
        st.success("Gli effetti del secondo ordine possono essere trascurati (λ < λ_lim).")
    else:
        st.warning("Gli effetti del secondo ordine devono essere considerati (λ ≥ λ_lim).")

if __name__ == "__main__":
    main()
