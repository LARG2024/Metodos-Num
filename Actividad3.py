
def f(x):
    """Función no lineal."""
    return x**3 - x - 1

def df(x):
    """Derivada de la función no lineal."""
    return 3*x**2 - 1

def newton_raphson(x0, tol, max_iter):
    """Método de Newton-Raphson."""
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            print("Derivada cero. El método falla.")
            return None
        x_new = x - fx/dfx
        if abs(x_new - x) < tol:
            return x_new, i
        x = x_new
    print("Máximo de iteraciones alcanzado.")
    return x, max_iter

def secant(x0, x1, tol, max_iter):
    """Método de la secante."""
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            print("División por cero. El método falla.")
            return None
        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if abs(x_new - x1) < tol:
            return x_new, i
        x0, x1 = x1, x_new
    print("Máximo de iteraciones alcanzado.")
    return x1, max_iter

# Parámetros de prueba
tol = 1e-6
max_iter = 100

# Conjunto de condiciones iniciales
Valores_iniciales = [
    (1.5, 1.0, 1.5),  # Caso 1: Aproximaciones alrededor de la raíz
    (0.5, 0.0, 0.5),  # Caso 2: Aproximaciones más alejadas
    (2.0, 1.5, 2.0)   # Caso 3: Aproximaciones al otro lado de la raíz
]

# Ejecución de pruebas para diferentes condiciones iniciales
for x0_newton, x0_sec, x1_sec in Valores_iniciales:
    print(f"Probando con condiciones iniciales:")
    print(f"Newton-Raphson x0 = {x0_newton}")
    print(f"Secante x0 = {x0_sec}, x1 = {x1_sec}")
    
    newton, iter_newton = newton_raphson(x0_newton, tol, max_iter)
    m_secant, iter_secant = secant(x0_sec, x1_sec, tol, max_iter)
    
    print(f"Método de Newton-Raphson: raíz = {newton}, iteraciones = {iter_newton}")
    print(f"Método de la secante: raíz = {m_secant}, iteraciones = {iter_secant}")
    print("-" * 50)
