"""
Spread analysis methods for the trading bot
"""

from typing import Dict, Optional
import logging
from utils.spread_analyzer import SpreadAnalyzer

class SpreadMethods:
    def __init__(self):
        self.logger = logging.getLogger('SpreadMethods')
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
        
        Args:
            symbol: Symbol pair yang akan dianalisa (e.g., 'BNBUSDT')
            
        Returns:
            Dict dengan hasil analisa spread
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
            
    async def analyze_spread_opportunity(self, symbol: str) -> Dict:
        """
        Analisa peluang trading berdasarkan spread
        
        Args:
            symbol: Symbol pair yang akan dianalisa
            
        Returns:
            Dict dengan hasil analisa dan rekomendasi trading
        """
        spread_analysis = await self.check_spread_conditions(symbol)
        
        opportunity = {
            'symbol': symbol,
            'can_trade': spread_analysis['is_tradeable'],
            'spread_score': spread_analysis['spread_score'],
            'spread': spread_analysis['spread'],
            'message': spread_analysis['message']
        }
        
        if spread_analysis['is_tradeable']:
            opportunity.update({
                'status': 'OK',
                'action': 'Proceed with trading analysis'
            })
        else:
            opportunity.update({
                'status': 'HOLD',
                'action': 'Wait for better spread conditions'
            })
            
        return opportunity
            
    async def send_telegram_message(self, message: str):
        """Send message to Telegram (placeholder)"""
        self.logger.info(f"Would send Telegram message: {message}")

def main():
    """
    Main function untuk testing
    """
    print("This module contains spread analysis methods.")
    print("It should be imported and used as part of the main trading bot.")
    print("See the documentation for usage examples.")

if __name__ == "__main__":
    main()
