class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called calss_method of {cls}")

    @staticmethod
    def static_method():
        print("Called Static_method")


test = ClassTest()

# instance methods
# test.instance_method()
# ClassTest.instance_method(test)


ClassTest.static_method()
