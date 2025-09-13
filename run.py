"""
File utama bot trading
Dibuat dengan 💖 oleh Copilot
"""

import sys
import os

# Tambahkan path ke PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from binance_bot.utils.trading_utils import *
from binance_bot.models.model_ml import ModelPrediksi
from binance_bot.bot import BinanceFuturesBot

if __name__ == "__main__":
    try:
        bot = BinanceFuturesBot()
        bot.run()
    except KeyboardInterrupt:
        print("\nBot dihentikan oleh user")
    except Exception as e:
        print(f"Error fatal: {e}")
