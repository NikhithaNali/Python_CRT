# #constructor
# class mobile:
#     def __init__(self):
#       print("mobile constructor called")
# relame=mobile()

############
class mobile:
   #constructor without parameter
        def __init__(self):
             self.model = 'realme x'
        def show_model(self):
             print("model:",self.model)
realme=mobile()
realme.show_model()
