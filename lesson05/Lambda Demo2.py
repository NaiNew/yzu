# 利用Lambda 製作出switch的運行邏輯
sex = 3
{1:lambda : print('男'), 2:lambda : print('女')}.get(sex, lambda :print('錯誤'))()

sex_info = {1:lambda: print('男'), 2:lambda: print('女')}
sex_info.get(2)()

