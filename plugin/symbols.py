# -*- coding: utf-8 -*-
from flowlauncher import FlowLauncher
import pyperclip


class SymbolData:
    def __init__(self, keywords: list, symbol: str, description: str) -> None:
        self.keywords = keywords
        self.symbol = symbol
        self.description = description


class Main(FlowLauncher):
    # Dictionnary
    symbols = [
        # Arrows
        SymbolData(["arrow", "right"], "→", "Arrow right"),
        SymbolData(["arrow", "left"], "←", "Arrow left"),
        SymbolData(["arrow", "up"], "↑", "Arrow up"),
        SymbolData(["arrow", "down"], "↓", "Arrow down"),
        SymbolData(["double", "arrow", "right"], "⇒", "Double arrow right"),
        SymbolData(["double", "arrow", "left"], "⇐", "Double arrow left"),
        SymbolData(["double", "arrow", "up"], "⇑", "Double arrow up"),
        SymbolData(["double", "arrow", "down"], "⇓", "Double arrow down"),
        SymbolData(["arrow", "up", "right"], "↗", "Arrow up right"),
        SymbolData(["arrow", "up", "left"], "↖", "Arrow up left"),
        SymbolData(["arrow", "down", "right"], "↘", "Arrow down right"),
        SymbolData(["arrow", "down", "left"], "↙", "Arrow down left"),

        # Maths
        SymbolData(["plus"], "+", "Plus"),
        SymbolData(["minus"], "−", "Minus"),
        SymbolData(["plus", "minus"], "±", "Plus or minus"),
        SymbolData(["multiply"], "×", "Multiply"),
        SymbolData(["divide"], "÷", "Divide"),
        SymbolData(["equal"], "=", "Equal"),
        SymbolData(["not", "equal"], "≠", "Not equal"),
        SymbolData(["less", "equal"], "≤", "Less or equal"),
        SymbolData(["greater", "equal"], "≥", "Greater or equal"),
        SymbolData(["approximately", "approx"], "≈", "Approximately equal"),
        SymbolData(["infinity"], "∞", "Infinity"),
        SymbolData(["pi"], "π", "Pi"),
        SymbolData(["sum"], "∑", "Sum"),
        SymbolData(["product"], "∏", "Product"),
        SymbolData(["square", "root"], "√", "Square root"),
        SymbolData(["integral"], "∫", "Integral"),
        SymbolData(["partial"], "∂", "Partial"),
        SymbolData(["nabla"], "∇", "Nabla"),
        SymbolData(["theta"], "θ", "Theta"),
        SymbolData(["lambda"], "λ", "Lambda"),
        SymbolData(["sigma"], "σ", "Sigma"),
        SymbolData(["phi"], "φ", "Phi"),
        SymbolData(["delta"], "Δ", "Delta"),
        SymbolData(["omega"], "ω", "Omega"),
        SymbolData(["alpha"], "α", "Alpha"),
        SymbolData(["beta"], "β", "Beta"),
        SymbolData(["gamma"], "γ", "Gamma"),

        # Currencies
        SymbolData(["euro"], "€", "Euro"),
        SymbolData(["pound"], "£", "Pound"),
        SymbolData(["yen"], "¥", "Yen"),
        SymbolData(["dollar"], "$", "Dollar"),
        SymbolData(["cent"], "¢", "Cent"),

        # Typographical symbols
        SymbolData(["bullet", "dot", "point"], "•", "Bullet"),
        SymbolData(["middle", "dot"], "·", "Middle dot"),
        SymbolData(["ellipsis", "dots"], "…", "Ellipsis"),
        SymbolData(["dash", "mdash"], "—", "Dash"),
        SymbolData(["ndash"], "–", "En dash"),
        SymbolData(["section"], "§", "Section"),
        SymbolData(["paragraph"], "¶", "Paragraph"),
        SymbolData(["copyright"], "©", "Copyright"),
        SymbolData(["trademark", "tm"], "™", "Trademark"),
        SymbolData(["registered", "r"], "®", "Registered"),
        SymbolData(["degree"], "°", "Degree"),
        SymbolData(["degree", "celsius"], "℃", "Degree Celsius"),
        SymbolData(["degree", "fahrenheit"], "℉", "Degree Fahrenheit"),
        SymbolData(["micro"], "µ", "Micro"),
        SymbolData(["ohm"], "Ω", "Ohm"),

        # Shapes
        SymbolData(["square"], "■", "Square"),
        SymbolData(["circle"], "●", "Circle"),
        SymbolData(["diamond"], "◆", "Diamond"),
        SymbolData(["star"], "★", "Star"),
        SymbolData(["heart"], "♥", "Heart"),
        SymbolData(["triangle", "up"], "▲", "Triangle up"),
        SymbolData(["triangle", "down"], "▼", "Triangle down"),
        SymbolData(["triangle", "left"], "◀", "Triangle left"),
        SymbolData(["triangle", "right"], "▶", "Triangle right"),
        SymbolData(["circle", "hollow"], "○", "Hollow circle"),
        SymbolData(["square", "hollow"], "□", "Hollow square"),

        # Others
        SymbolData(["check", "tick"], "✓", "Tick"),
        SymbolData(["cross", "x"], "✗", "Cross"),
        SymbolData(["up", "caret"], "‸", "Caret up"),
        SymbolData(["down", "caret"], "⌄", "Caret down"),
        SymbolData(["section"], "§", "Section"),
    ]


    def searchSymbols(self, query: str) -> list:
        query = query.lower().strip()
        results = []
        
        if not query:
            # No request -> all symbols
            for symbol_data in self.SYMBOLS:
                results.append({
                    "Title": f"{symbol_data.symbol}  —  {symbol_data.description}",
                    "SubTitle": f"Keywords: {', '.join(symbol_data.keywords)}",
                    "IcoPath": "assets/app.png",
                    "JsonRPCAction": {
                        "method": "copy_symbol",
                        "parameters": [symbol_data.symbol],
                    }
                })
        else:
            # Search symbols
            for symbol_data in self.SYMBOLS:
                # Check query
                if any(query in keyword for keyword in symbol_data.keywords):
                    results.append({
                        "Title": f"{symbol_data.symbol}  —  {symbol_data.description}",
                        "SubTitle": f"Press Enter to copy '{symbol_data.symbol}'",
                        "IcoPath": "assets/app.png",
                        "JsonRPCAction": {
                            "method": "copy_symbol",
                            "parameters": [symbol_data.symbol],
                        }
                    })
        
        if not results and query:
            results.append({
                "Title": "No symbol found",
                "SubTitle": f"No result for '{query}'",
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
                    "Title": f"Symbol '{symbol}' copied !",
                    "SubTitle": "Symbol copied into clipboard",
                    "IcoPath": "assets/app.png",
                }
            }
        except Exception as e:
            return {
                "result": {
                    "Title": "Error",
                    "SubTitle": str(e),
                    "IcoPath": "assets/app.png",
                }
            }