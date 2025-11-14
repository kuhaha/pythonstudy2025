"""
モジュールごとの読み込みに関するテスト
"""

import foo
grade = 89    
print(f"grade={grade},calc(grage)={foo.calc(grade)}")
print(f"PI={foo.PI}")

"""
出力：
-----
grade=89,calc(grage)=A
PI=3.14159
"""