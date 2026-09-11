import math


def processar_agua(peso: float, ingerida: float = 0.0) -> dict:
    """Calcula a meta de água, quantidade restante e copos de 250mL faltantes.

    - Peso: em kg (entre 2kg e 500kg)
    - Ingerida: em mL (entre 0mL e 20.000mL)
    """
    # Validações de limites biológicos e de entrada
    if not (2 <= peso <= 500):
        raise ValueError(
            "Peso fora dos limites plausíveis (2.0 kg a 500.0 kg)."
        )

    if not (0 <= ingerida <= 20000):
        raise ValueError(
            "Quantidade de água ingerida inválida (0 mL a 20.000 mL)."
        )

    # Regra de Negócio: 35 mL por kg | Copo padrão: 250 mL
    meta_total = peso * 35.0
    restante = meta_total - ingerida
    percentual = min(max((ingerida / meta_total) * 100, 0.0), 100.0)

    if restante <= 0:
        status = "Meta Atingida! 🎉"
        restante_ml = 0.0
        copos_faltantes = 0
    else:
        status = "Em Progresso"
        restante_ml = restante
        copos_faltantes = math.ceil(restante / 250)

    return {
        "peso_kg": peso,
        "ingerida_ml": ingerida,
        "meta_total_ml": round(meta_total, 2),
        "restante_ml": round(restante_ml, 2),
        "percentual_concluido": round(percentual, 1),
        "copos_faltantes_250ml": copos_faltantes,
        "status": status,
    }


# --- EXEMPLO DE USO / TESTE ---
if __name__ == "__main__":
    try:
        # Exemplo: Pessoa com 68kg que já bebeu 1000mL
        resultado = processar_agua(peso=68.0, ingerida=1000.0)

        print("\n--- RELATÓRIO DE INGESTÃO HÍDRICA ---")
        print(f"Status: {resultado['status']}")
        print(f"Meta Recomendada: {resultado['meta_total_ml']} mL")
        print(f"Progresso: {resultado['percentual_concluido']}%")
        print(f"Faltam: {resultado['restante_ml']} mL")
        print(f"Copos Faltantes (250ml): {resultado['copos_faltantes_250ml']}")

    except ValueError as erro:
        print(f"Erro de validação: {erro}")