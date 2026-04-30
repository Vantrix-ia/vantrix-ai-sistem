class VantrixDecisionExpert:

    def calculate_v_score(self, product):

        margin = product.margin
        trend = getattr(product, "trend_score", 0)
        saturation = getattr(product, "saturation_score", 0)
        branding = getattr(product, "branding_score", 0)

        return (
            margin * 0.4 +
            trend * 0.3 +
            (1 - saturation) * 0.2 +
            branding * 0.1
        )

    def make_decision(self, product):

        product.v_score = self.calculate_v_score(product)

        if product.v_score >= 0.7:
            product.decision = "BUY"
        elif product.v_score >= 0.5:
            product.decision = "TEST"
        else:
            product.decision = "SKIP"

        return product