import time

# Global variable to hold the connection
_conn = None
_vessel = None

def ksp_conectar(nome_nave):
    global _conn, _vessel
    print(f"Tentando conectar à nave '{nome_nave}'...")
    try:
        import krpc
        _conn = krpc.connect(name=nome_nave)
        _vessel = _conn.space_center.active_vessel
        print(f"Conectado com sucesso à nave: {_vessel.name}")
    except Exception as e:
        print(f"[MODO SIMULAÇÃO] Não foi possível conectar ao kRPC: {e}")
        print("[MODO SIMULAÇÃO] Rodando em modo de simulação.")
        _conn = None
        _vessel = None

def ksp_obter_altitude():
    if _vessel:
        return _vessel.flight().mean_altitude
    else:
        # Mock simulation: altitude increases over time if "accelerating"
        import random
        return random.uniform(0, 15000)

def ksp_obter_velocidade():
    if _vessel:
        return _vessel.flight(_vessel.orbit.body.reference_frame).speed
    else:
         # Mock value
        return 100.0

def ksp_apoastro():
    if _vessel:
        return _vessel.orbit.apoapsis_altitude
    else:
         # Mock value
        return 50000.0

def ksp_ativar_estagio():
    if _vessel:
        _vessel.control.activate_next_stage()
        print("Estágio ativado no kRPC.")
    else:
        print("[MODO SIMULAÇÃO] ksp_ativar_estagio() executado.")

def ksp_travar_sas():
    if _vessel:
        _vessel.control.sas = True
        print("SAS ativado.")
    else:
        print("[MODO SIMULAÇÃO] ksp_travar_sas() executado.")

def ksp_acelerar(valor):
    """
    Define a aceleração (throttle) de 0.0 a 1.0.
    """
    if _vessel:
        _vessel.control.throttle = float(valor)
        print(f"Aceleração definida para {valor}")
    else:
        print(f"[MODO SIMULAÇÃO] ksp_acelerar({valor}) executado.")
