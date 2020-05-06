## 91social Backend Assignment

To run this program in the command line, simply write <br>
<code>python loan.py {principal_amt} {num_of_emi} {interest_rate_per_anum}</code>

There are 3 essential arguments to this line. (Even though the assignment asks for 2. The assignment assumes a fixed interest rate, but here I have given the option to change interest rate as well)<br>
The first one is <b>principal_amt</b> which refers to the loam amount taken from the bank.<br>
The second is <b>num_of_emi</b> which refers to the number of EMIs that the customer has opted for. For eg., if the customer wants to take a loan for 6 months, then he has to pay 6 months of EMI. If a customer wants to take a loan for 1.5 years, then he has to pay 18 months of EMI.<br>
The third one is <b>interest_rate_per_anum</b> which simply is the annual interest rate of the loan.

### Optional Paramters

If you want to create a json file for the output, you can add the paramter: <code>-o "<output_file_path>"</code> after giving the 3 essential parameters.
A sample command will be:<br>
<p><code>python .\loan.py 1000 12 12 -o "sample.json"</code></p>