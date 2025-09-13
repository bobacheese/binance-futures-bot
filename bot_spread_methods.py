"""
Bot methods for spread analysis and trading decisions
"""

from typing import Dict, Optional
import logging
from utils.spread_analyzer import SpreadAnalyzer

class BotSpreadMethods:
    def __init__(self):
        self.logger = logging.getLogger('BotSpreadMethods')
        self.config = {}
        self.exchange = None
        self.spread_analyzer = None
        
    def setup_spread_analyzer(self):
        """Setup spread analyzer"""
        try:
            spread_config = self.config.get('spread_config', {
                'max_spread': 0.0003,
                'spread_window': 10,
                'min_spread_score': 70
            })
            self.spread_analyzer = SpreadAnalyzer(spread_config)
            self.logger.info("Spread analyzer initialized successfully")
        except Exception as e:
            self.logger.error(f"Error initializing spread analyzer: {e}")
            raise
            
    async def check_spread_conditions(self, symbol: str) -> Dict:
        """
        Mengecek kondisi spread sebelum trading
        """
        try:
            # Ambil orderbook
            orderbook = await self.exchange.fetch_order_book(symbol)
            
            # Analisa spread
            spread_analysis = self.spread_analyzer.analyze_spread(orderbook)
            
            # Log hasil analisa
            self.logger.info(f"Spread analysis for {symbol}: {spread_analysis['message']}")
            
            # Update spread info ke Telegram jika spread terlalu tinggi
            if not spread_analysis['is_tradeable'] and self.config['notifikasi']['telegram']:
                await self.send_telegram_message(
                    f"⚠️ {symbol} Spread Warning:\n"
                    f"{spread_analysis['message']}\n"
                    f"Score: {spread_analysis['spread_score']}/100"
                )
                
            return spread_analysis
            
        except Exception as e:
            self.logger.error(f"Error checking spread conditions: {e}")
            return {
                'is_tradeable': False,
                'spread': float('inf'),
                'spread_score': 0,
                'message': f'Error: {str(e)}'
            }
            
    async def generate_trading_signal(self, symbol: str) -> Optional[Dict]:
        """
        Generate trading signal (placeholder method)
        In real implementation, this would do technical analysis and ML prediction
        """
        return {
            'symbol': symbol,
            'direction': 'BUY',
            'confidence': 0.85,
            'price': 100.0
        }
            
    async def analyze_trading_opportunity(self, symbol: str) -> Dict:
        """
        Analisa peluang trading dengan mempertimbangkan spread
        """
        # Cek kondisi spread terlebih dahulu
        spread_analysis = await self.check_spread_conditions(symbol)
        if not spread_analysis['is_tradeable']:
            return {
                'should_trade': False,
                'reason': spread_analysis['message'],
                'signal': None
            }
            
        # Jika spread OK, lanjutkan dengan analisa teknikal dan ML
        signal = await self.generate_trading_signal(symbol)
        
        # Combine spread score dengan confidence ML
        if signal and signal.get('confidence', 0) > self.config.get('ml_config', {}).get('confidence_threshold', 0.8):
            return {
                'should_trade': True,
                'reason': f"Spread OK ({spread_analysis['spread_score']}/100) & Strong Signal",
                'signal': signal
            }
            
        return {
            'should_trade': False,
            'reason': 'No strong trading signal',
            'signal': signal
        }
            
    async def send_telegram_message(self, message: str):
        """
        Placeholder for sending Telegram messages
        In real implementation, this would use python-telegram-bot
        """
        self.logger.info(f"Would send Telegram message: {message}")

if __name__ == "__main__":
    print("This module contains bot methods and should be imported, not run directly.")
