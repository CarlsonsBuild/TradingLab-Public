"""Public educational candle validator. No TradingLab runtime dependencies."""
import math
from datetime import datetime

def timestamp(value):
    t = datetime.fromisoformat(value)
    if t.tzinfo is None or t.utcoffset() is None:
        raise ValueError('Timezone required')
    return t

def validate(rows, now=None, max_age_seconds=60):
    errors = set()
    if not rows:
        return ['empty_data']
    seen, previous, times = set(), None, []
    for r in rows:
        try:
            t = timestamp(r.get('timestamp'))
            if t in seen: errors.add('duplicate_timestamp')
            if previous is not None and t < previous: errors.add('out_of_order')
            seen.add(t); previous=t; times.append(t)
        except (ValueError, TypeError):
            errors.add('invalid_timestamp')
        values=[r.get(k) for k in ('open','high','low','close')]
        if not all(type(v) in (int,float) and math.isfinite(v) for v in values):
            errors.add('invalid_number')
        else:
            o,h,l,c=values
            if not (0 < l <= min(o,c) <= max(o,c) <= h): errors.add('invalid_ohlc')
        v=r.get('volume')
        if type(v) not in (int,float) or not math.isfinite(v) or v < 0:
            errors.add('invalid_volume')
    if now is not None and times:
        clock=timestamp(now)
        if (clock-max(times)).total_seconds() > max_age_seconds: errors.add('stale_data')
        if max(times)>clock: errors.add('future_timestamp')
    return sorted(errors)
