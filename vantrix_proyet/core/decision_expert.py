class VantrixDecisionExpert:

    def make_decision(self, product):
        v_score = (
            product.profit * 0.4 +
            product.trend_score * 0.3 +
            (1 - product.saturation_score) * 0.2 +
            product.branding_score * 0.1
        )

        product.v_score = round(v_score, 2)

        if product.v_score > 50:
            product.decision = "GANADOR"
        else:
            product.decision = "DESCARTAR"

        return product