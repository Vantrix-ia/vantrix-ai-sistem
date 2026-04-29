import requests


class TrendSources:

    @staticmethod
    def amazon_proxy():
        """
        Simula Amazon Best Sellers usando FakeStore + heurística
        """
        response = requests.get("https://fakestoreapi.com/products")
        data = response.json()

        trends = []

        for item in data:
            rating = item.get("rating", {})

            trends.append({
                "name": item.get("title"),
                "price": float(item.get("price", 0)),
                "reviews": rating.get("count", 0),
                "rating": rating.get("rate", 0)
            })

        return trends


    @staticmethod
    def tiktok_proxy():
        """
        Simula tendencia viral (placeholder hasta scraping real)
        """
        keywords = [
            "led light",
            "fitness band",
            "neck massager",
            "portable blender",
            "smart bottle"
        ]

        return keywords