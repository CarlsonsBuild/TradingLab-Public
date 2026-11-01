import unittest
from public_demo import validate

def row(t='2026-01-01T12:00:00+00:00', **kw):
    return dict(timestamp=t,open=10,high=12,low=9,close=11,volume=100,**kw)

class ValidatorTests(unittest.TestCase):
    def test_valid(self): self.assertEqual(validate([row()]), [])
    def test_duplicate(self): self.assertIn('duplicate_timestamp',validate([row(),row()]))
    def test_order(self): self.assertIn('out_of_order',validate([row('2026-01-02T12:00:00+00:00'),row()]))
    def test_naive(self): self.assertIn('invalid_timestamp',validate([row('2026-01-01T12:00:00')]))
    def test_bad_timestamp(self): self.assertIn('invalid_timestamp',validate([row('not-a-date')]))
    def test_price_range(self):
        r=row(); r['high']=8
        self.assertIn('invalid_ohlc',validate([r]))
    def test_nan(self):
        r=row(); r['close']=float('nan')
        self.assertIn('invalid_number',validate([r]))
    def test_negative_volume(self):
        r=row(); r['volume']=-1
        self.assertIn('invalid_volume',validate([r]))
    def test_missing(self): self.assertIn('invalid_number',validate([{'timestamp':row()['timestamp']}]))
    def test_stale(self): self.assertIn('stale_data',validate([row()],now='2026-01-01T12:10:00+00:00',max_age_seconds=60))
    def test_future(self): self.assertIn('future_timestamp',validate([row()],now='2026-01-01T11:00:00+00:00',max_age_seconds=60))
    def test_empty(self): self.assertIn('empty_data',validate([]))

if __name__=='__main__': unittest.main()
