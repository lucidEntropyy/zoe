from jesse.strategies import Strategy
import jesse.indicators as ta
from jesse import utils
from jesse.helpers import get_candle_source, slice_candles
from datetime import *

class Zoe(Strategy):

    @property
    def vwap(self):
        return ta.vwap(self.candles, source_type="hl2", anchor='D')

    @property
    def slow_sma(self):
        return ta.sma(self.candles, 200)

    def should_long(self) -> bool:
        # Go long if candle close > vwap
        if self.vwap is None:
            return

        return self.close > self.vwap and self.close > self.slow_sma

    #def should_short(self) -> bool:
    #    return False

    def timeOfDay(self):
        timestamp = self.current_candle[0]/1000
        time = datetime.fromtimestamp(timestamp)
        return time.hour > 4 and time.hour < 23

    def filters(self):
        return [
            self.timeOfDay
        ]

    def should_cancel_entry(self) -> bool:
        return True

    def go_long(self):
        # Open long position using entire balance
        qty = utils.size_to_qty(self.balance, self.price, fee_rate=self.fee_rate)
        self.buy = qty, self.price

    def go_short(self):
        pass

    def update_position(self):
        timestamp = self.current_candle[0]/1000
        time = datetime.fromtimestamp(timestamp)

        if self.vwap is None:
            return

        if self.close < self.vwap and self.close < self.slow_sma:
            self.liquidate()

        if time.hour == 23:
            self.liquidate()