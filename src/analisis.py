"""Complete las dos funciones antes de ejecutar el estudio."""
import numpy as np

def desplazamiento_referencia(x, L, E, A, P, q):
    """u(0)=0, EA*u'(L)=P, q uniforme. Devuelva un array en mm."""
    x = np.asarray(x, dtype=float)

    u = ((P + q*L)*x - (q*x**2)/2) / (E*A)

    return u

def error_puntos_medios(resultado, L, E, A, P, q):
    """Devuelva el maximo error absoluto de u_h frente a u_ref en puntos medios.
    No basta comparar los nodos: interpole u_h linealmente en cada elemento.
    """
    x = resultado.x
    u = resultado.u

    # Puntos medios de cada elemento
    x_medio = (x[:-1] + x[1:]) / 2

    # Interpolacion lineal de u_h en los puntos medios
    u_h_medio = (u[:-1] + u[1:]) / 2

    # Solucion de referencia en los mismos puntos
    u_ref_medio = desplazamiento_referencia(x_medio, L, E, A, P, q)

    # Error absoluto
    error = np.abs(u_h_medio - u_ref_medio)

    return np.max(error)
