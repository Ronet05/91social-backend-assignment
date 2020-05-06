from loan import tojsonfile, loan_management

class TestCases:

    def checkcase_normal(self, input):        
        case = loan_management(input[0], input[1], input[2])
        print(case.calc_for_duration())


    def checkcase_json(self, input, path):
        case = loan_management(input[0], input[1], input[2])
        response = case.calc_for_duration()
        tojsonfile(response, path)


if __name__ == "__main__":
    inputs = [[25000, 12, 8],[500000, 72, 11.48], [100, 3, 14], [10000000, 1200, 9.67], [12, 2, 3.75]]
    obj = TestCases()
    count=0
    for i in inputs:
        path = 'test'+str(count)+'.json'
        count+=1
        obj.checkcase_normal(i)
        obj.checkcase_json(i,path)
        