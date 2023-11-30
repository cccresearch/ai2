import lib
import ai

response = ai.chat("請問 32179 加上 13426 是多少? 兩者相乘又是多少？")
print('===============================================')
print(response)
print('===============================================')
print(lib.replace_code(response))
