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
    SYMBOLS = [
        SymbolData(["dot", "bullet", "point"], "•", "Bullter"),
        SymbolData(["arrow", "right"], "→", "Arrow right"),
        SymbolData(["arrow", "left"], "←", "Arrow left"),
        SymbolData(["arrow", "up"], "↑", "Arrow up"),
        SymbolData(["arrow", "down"], "↓", "Arrow down"),
        SymbolData(["check", "tick"], "✓", "Tick"),
        SymbolData(["cross", "x"], "✗", "Cross"),
        SymbolData(["star"], "★", "Star"),
        SymbolData(["heart"], "♥", "Heart"),
        SymbolData(["copyright"], "©", "Copyright"),
        SymbolData(["trademark", "tm"], "™", "Trademark"),
        SymbolData(["registered", "r"], "®", "Registered"),
        SymbolData(["degree"], "°", "Degree"),
        SymbolData(["euro"], "€", "Euro"),
        SymbolData(["pound"], "£", "Pound"),
        SymbolData(["yen"], "¥", "Yen"),
        SymbolData(["infinity"], "∞", "Infinity"),
        SymbolData(["pi"], "π", "Pi"),
        SymbolData(["sum"], "∑", "Sum"),
        SymbolData(["delta"], "Δ", "Delta"),
        SymbolData(["alpha"], "α", "Alpha"),
        SymbolData(["beta"], "β", "Beta"),
        SymbolData(["gamma"], "γ", "Gamma"),
        SymbolData(["omega"], "ω", "Omega"),
        SymbolData(["ellipsis", "dots"], "…", "Dots"),
        SymbolData(["dash", "mdash"], "—", "Dash"),
        SymbolData(["section"], "§", "Section"),
        SymbolData(["not", "equal"], "≠", "Not equals"),
        SymbolData(["approximately", "approx"], "≈", "Approx"),
        SymbolData(["less", "equal"], "≤", "Less equal"),
        SymbolData(["greater", "equal"], "≥", "Greater equal"),
        SymbolData(["plus", "minus"], "±", "PLus or minus"),
        SymbolData(["multiply"], "×", "Multiply"),
        SymbolData(["divide"], "÷", "Divide"),
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