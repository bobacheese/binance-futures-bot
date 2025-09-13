"""
Program Bot Trading Binance Futures
Dibuat dengan 💖 oleh Copilot
"""

import ccxt
import pandas as pd
import numpy as np
import ta
import time
from datetime import datetime
import logging
import json
import yaml
from models.model_ml import ModelPrediksi
import telegram
from rich.console import Console
from rich.table import Table
from rich import box
import threading
import os
from typing import Dict
from utils.trading_utils import *
from utils.spread_analyzer import SpreadAnalyzer

class BinanceFuturesBot:
    def __init__(self, config_file='config.yaml'):
        """
        Inisialisasi Bot Trading
        
        Args:
            config_file: Nama file konfigurasi yang akan digunakan (default: config.yaml)
                        Bisa menggunakan 'config_scalping.yaml' atau 'config_modal_kecil.yaml'
        """
        # Setup logger terlebih dahulu
        self.logger = logging.getLogger('BinanceFuturesBot')
        self.config_file = config_file
        self.setup_bot()
        self.setup_logging()
        self.load_models()
        self.setup_spread_analyzer()
        
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
                await self.telegram_bot.send_message(
                    chat_id=self.chat_id,
                    text=f"⚠️ {symbol} Spread Warning:\n"
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
        if signal and signal['confidence'] > self.config['ml_config']['confidence_threshold']:
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
        
    def setup_bot(self):
        """Setup konfigurasi awal bot"""
        try:
            # Baca konfigurasi
            config_path = os.path.join(os.path.dirname(__file__), 'config', self.config_file)
            
            # Cek apakah file config ada
            if not os.path.exists(config_path):
                raise FileNotFoundError(f"File konfigurasi {self.config_file} tidak ditemukan")
                
            with open(config_path, 'r', encoding='utf-8') as file:
                self.config = yaml.safe_load(file)['bot_config']
                self.logger.info(f"Berhasil memuat konfigurasi dari {self.config_file}")
            
            # Validasi config
            validasi_config(self.config)
            
            # Setup exchange
            self.exchange = ccxt.binance({
                'apiKey': self.config['api_key'],
                'secret': self.config['api_secret'],
                'enableRateLimit': True,
                'options': {'defaultType': 'future'}
            })
            
            # Setup notifikasi
            if self.config['notifikasi']['telegram']:
                self.telegram_bot = telegram.Bot(token=self.config['telegram_token'])
                self.chat_id = self.config['telegram_chat_id']
            
            # Setup tampilan
            self.console = Console()
            
            # Inisialisasi statistik
            self.statistik = muat_statistik(
                os.path.join(os.path.dirname(__file__), 'logs', 'statistik_trading.json')
            )
            
        except Exception as e:
            raise Exception(f"Error dalam setup bot: {e}")
    
    def setup_logging(self):
        """Setup sistem logging"""
        log_path = os.path.join(os.path.dirname(__file__), 'logs', 'bot_trading.log')
        logging.basicConfig(
            level=logging.INFO if self.config['mode']['debug'] else logging.WARNING,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_path),
                logging.StreamHandler()
            ]
        )
    
    def load_models(self):
        """Load model machine learning"""
        try:
            model_path = os.path.join(os.path.dirname(__file__), 'models', 'model_trading.joblib')
            self.model = ModelPrediksi()
            self.model.muat_model(model_path)
            logging.info("Model ML berhasil dimuat")
        except:
            logging.warning("Model ML belum ada, akan dibuat saat training pertama")
