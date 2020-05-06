import json
import numpy as np
from datetime import datetime, date, timedelta
import calendar
import sys

def tojsonfile(inp, out_file_path):
    out = open(out_file_path,'w')
    json.dump(inp, out)
    out.close()

class loan_management:
    # since we are talking about emi, 
    # no. of emi will automatically mean number of months
    def __init__(self, p, time, r):
        self.principal = p
        self.duration = time
        self.rate_anum = r
        self.payable_amt = p+(p*r*(time/12))/100
        self.created_date = date.today()


    def emi_calc(self):
        rate_month = self.rate_anum/(12*100)
        #interest is monthly_rate*principal_amount*1 (i.e.1 month)
        emi_interest = round(rate_month*self.principal,2)
        emi_principal = round(self.principal/self.duration,2)
        total_emi = emi_interest+emi_principal
        return emi_principal, emi_interest, total_emi

    def calc_for_duration(self):
        #constant for every month
        response = {}
        emi_principal, emi_interest, total_emi = self.emi_calc()
        start_principal = self.payable_amt
        deadline_date = self.created_date
        array_emis = []
    
        for i in range(self.duration):            
            temp = {}
            start_principal = round(start_principal - total_emi, 2)
            if start_principal<10 and start_principal>-10:
                start_principal=0

            days_in_month = calendar.monthrange(deadline_date.year, deadline_date.month)[1]
            deadline_date += timedelta(days = days_in_month)
            deadline_date_str = deadline_date.strftime("%dth %b %Y")
            temp['EMI No.']=i+1
            temp['Principal EMI']=emi_principal
            temp['Interest EMI']=emi_interest
            temp['Total EMI']=total_emi
            temp['EMI Date']=deadline_date_str
            temp['Principal Remaining']=start_principal
            array_emis.append(temp)
        
        response["Loan Creation Date"] = self.created_date.strftime("%dth %b %Y")
        response["Principal Amount"] = self.principal
        response["No Of EMI's"] = self.duration
        response["Total payable amount"] = self.payable_amt
        response["EMI Details"]=array_emis

        return response

    

if __name__ == "__main__":
    arg= sys.argv
    emi_object = loan_management(float(arg[1]), int(arg[2]), float(arg[3]))
    try:
        if(arg[4]=="-o"):
            output_file_path = arg[5]
            tojsonfile(emi_object.calc_for_duration(), output_file_path)
    except:
        pass
    print(emi_object.calc_for_duration())
    
