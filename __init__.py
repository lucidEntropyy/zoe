from jesse.strategies import Strategy
import jesse.indicators as ta
from jesse import utils
from jesse.helpers import get_candle_source, slice_candles

class Zoe(Strategy):
    @property
    def vwap(self):
        # VWAP + Standard Dev's
        return ta.vwap(self.candles)

    def pva(self):
        # Prior Value Area
        candles = slice_candles(candles)
        src = get_candle_source(candles)
        ## TODO CALCULATE

    def filter_trend(self):
        # Only opens a long position when close is above ichimoku cloud
        return self.close > self.ichimoku.span_a and self.close > self.ichimoku.span_b

    def filters(self):
        return [self.filter_trend]

    def should_long(self) -> bool:
        # Go long if candle closes above upperband
        return self.close > self.bb[0]

    def should_short(self) -> bool:
        return False

    def should_cancel_entry(self) -> bool:
        return True

    def go_long(self):
        # Open long position using entire balance
        qty = utils.size_to_qty(self.balance, self.price, fee_rate=self.fee_rate)
        self.buy = qty, self.price

    def go_short(self):
        pass

    def update_position(self):
        # Close the position when candle closes below middleband
        if self.close < self.bb[1]:
            self.liquidate()