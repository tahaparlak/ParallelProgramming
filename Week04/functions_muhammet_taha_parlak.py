# Week04/functions_muhammet_taha_parlak.py

# 1. Lambda fonksiyonu: custom_power
# x positional-only (/ işareti ile sağlanır), e positional-or-keyword
custom_power = lambda x=0, e=1, /: x ** e

# 2. Normal fonksiyon: custom_equation
def custom_equation(x=0, y=0, /, a=1, b=1, *, c=1) -> float:
    """
    Calculates (x**a + y**b) / c
    """
    return float((x ** a + y ** b) / c)

# 3. Sayaçlı fonksiyon: fn_w_counter
def fn_w_counter() -> tuple[int, dict]:
    """
    Counts the number of calls with caller information.

    :return: A tuple containing total calls and a dictionary of callers.
    :rtype: tuple[int, dict]
    """
    # Fonksiyonun kendisine öznitelik (attribute)
    if not hasattr(fn_w_counter, "calls"):
        fn_w_counter.calls = 0
        fn_w_counter.callers = {}

    fn_w_counter.calls += 1
    
    # Çağıran modülün adını al (__main__ gibi)
    import inspect
    caller_name = inspect.currentframe().f_back.f_globals.get('__name__', 'unknown')
    
    fn_w_counter.callers[caller_name] = fn_w_counter.callers.get(caller_name, 0) + 1
    
    return fn_w_counter.calls, fn_w_counter.callers
