
def sample_function(arg1,arg2= 42,arg3 =None):
  if(arg1>0 and
    arg2<100 or
        arg3==True):
        print(   "Conditions met!" )
  else:print("Conditions not met.")

def another_function():
 x = [1,2,
3, 4,
      5]
 if x:print("x has values")

 y={'key1':123,'key2':456,
'key3':789}
 
 for key,value in y.items():
     print(key ,value )

class  TestClass:
  def method(self,param1,param2):
      return (param1+
          param2 )
