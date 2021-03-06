# Insert operands + and - in 1...9 to form an expresion equals to a target
# +1+2+3-4+5+6+78+9  == 100
def get_ops(num, acc=""):
    if not num:
    	if eval(acc) == 100:
    	    print acc
     
    for i in range(1, len(num)+1):
    	get_ops(num[i:], acc + "+" + num[:i])
    	get_ops(num[i:], acc + "-" + num[:i])
    	
get_ops("123456789")



"""
+1+2+3-4+5+6+78+9
+1+2+34-5+67-8+9
+1+23-4+5+6+78-9
+1+23-4+56+7+8+9
-1+2-3+4+5+6+78+9
+12+3+4+5-6-7+89
+12+3-4+5+67+8+9
+12-3-4+5-6+7+89
+123+4-5+67-89
+123-4-5-6-7+8-9
+123+45-67+8-9
+123-45-67+89

"""
