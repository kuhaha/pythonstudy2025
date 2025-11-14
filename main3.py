"""
パッケージに関するテスト
"""
# パッケージから一括importするだけ
# モジュール(foo, bar)をいちいちimportしなくて済む
from pkg import * 

a, b = 20, 30
print(f"a={a}, b={b}")
print(f"add(a,b)={add(a, b)}")

"""
出力：
-----
a=20, b=30
add(a,b)=50
"""

# print(f"mul(a,b)={mul(a, b)}")
# NameError: name 'mul' is not defined
# 原因：`mul`は`pkg/__init__.py`の`__all__に含まれていないかえら`