#!/usr/bin/env sed -f

# 1. 寻找 `.SendNewMetric(` 这种模式, 且不是注释行 `//`
# 2. 直到找到 `})` 这种模式
# 3. 这两个之间的内容, 换行都给删除掉

/^\s\+[a-zA-Z_].*\.SendNewMetric(/{
    :a
    N
    /})/!ba
    s/\n//g
}


/^\s\+[a-zA-Z_].*\.SendMetric(/{
    :a
    N
    /})/!ba
    s/\n//g
}