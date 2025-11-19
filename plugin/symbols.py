# -*- coding: utf-8 -*-
from flowlauncher import FlowLauncher
import pyperclip


class SymbolData:
    def __init__(self, keywords: list, symbol: str, description: str) -> None:
        self.keywords = keywords
        self.symbol = symbol
        self.description = description


class Main(FlowLauncher):
    # Dictionnaire de symboles avec leurs mots-clés
    SYMBOLS = [
        SymbolData(["dot", "bullet", "point"], "•", "Puce"),
        SymbolData(["arrow", "right"], "→", "Flèche droite"),
        SymbolData(["arrow", "left"], "←", "Flèche gauche"),
        SymbolData(["arrow", "up"], "↑", "Flèche haut"),
        SymbolData(["arrow", "down"], "↓", "Flèche bas"),
        SymbolData(["check", "tick"], "✓", "Coche"),
        SymbolData(["cross", "x"], "✗", "Croix"),
        SymbolData(["star"], "★", "Étoile"),
        SymbolData(["heart"], "♥", "Coeur"),
        SymbolData(["copyright"], "©", "Copyright"),
        SymbolData(["trademark", "tm"], "™", "Trademark"),
        SymbolData(["registered", "r"], "®", "Registered"),
        SymbolData(["degree"], "°", "Degré"),
        SymbolData(["euro"], "€", "Euro"),
        SymbolData(["pound"], "£", "Livre sterling"),
        SymbolData(["yen"], "¥", "Yen"),
        SymbolData(["infinity"], "∞", "Infini"),
        SymbolData(["pi"], "π", "Pi"),
        SymbolData(["sum"], "∑", "Somme"),
        SymbolData(["delta"], "Δ", "Delta"),
        SymbolData(["alpha"], "α", "Alpha"),
        SymbolData(["beta"], "β", "Beta"),
        SymbolData(["gamma"], "γ", "Gamma"),
        SymbolData(["omega"], "ω", "Omega"),
        SymbolData(["ellipsis", "dots"], "…", "Points de suspension"),
        SymbolData(["dash", "mdash"], "—", "Tiret cadratin"),
        SymbolData(["ndash"], "–", "Tiret demi-cadratin"),
        SymbolData(["section"], "§", "Paragraphe"),
        SymbolData(["not", "equal"], "≠", "Différent de"),
        SymbolData(["approximately", "approx"], "≈", "Approximativement"),
        SymbolData(["less", "equal"], "≤", "Inférieur ou égal"),
        SymbolData(["greater", "equal"], "≥", "Supérieur ou égal"),
        SymbolData(["plus", "minus"], "±", "Plus ou moins"),
        SymbolData(["multiply"], "×", "Multiplier"),
        SymbolData(["divide"], "÷", "Diviser"),
    ]

    def searchSymbols(self, query: str) -> list:
        query = query.lower().strip()
        results = []
        
        if not query:
            # Si pas de requête, afficher tous les symboles
            for symbol_data in self.SYMBOLS:
                results.append({
                    "Title": f"{symbol_data.symbol}  —  {symbol_data.description}",
                    "SubTitle": f"Mots-clés: {', '.join(symbol_data.keywords)}",
                    "IcoPath": "assets/app.png",
                    "JsonRPCAction": {
                        "method": "copy_symbol",
                        "parameters": [symbol_data.symbol],
                    }
                })
        else:
            # Rechercher les symboles correspondants
            for symbol_data in self.SYMBOLS:
                # Vérifier si la requête correspond à un des mots-clés
                if any(query in keyword for keyword in symbol_data.keywords):
                    results.append({
                        "Title": f"{symbol_data.symbol}  —  {symbol_data.description}",
                        "SubTitle": f"Appuyez sur Entrée pour copier '{symbol_data.symbol}'",
                        "IcoPath": "assets/app.png",
                        "JsonRPCAction": {
                            "method": "copy_symbol",
                            "parameters": [symbol_data.symbol],
                        }
                    })
        
        if not results and query:
            results.append({
                "Title": "Aucun symbole trouvé",
                "SubTitle": f"Aucun résultat pour '{query}'",
                "IcoPath": "assets/app.png",
            })
        
        return results

    def query(self, arguments: str) -> list:
        return self.searchSymbols(arguments)

    def copy_symbol(self, symbol: str):
        """Copie le symbole dans le presse-papiers"""
        try:
            pyperclip.copy(symbol)
            return {
                "result": {
                    "Title": f"Symbole '{symbol}' copié !",
                    "SubTitle": "Le symbole a été copié dans le presse-papiers",
                    "IcoPath": "assets/app.png",
                }
            }
        except Exception as e:
            return {
                "result": {
                    "Title": "Erreur lors de la copie",
                    "SubTitle": str(e),
                    "IcoPath": "assets/app.png",
                }
            }