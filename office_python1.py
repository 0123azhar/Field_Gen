import random
import datetime
import pandas as pd
from luhn import append


class Gen:
    def __init__(self, no_of_recs, seed):
        self.n = no_of_recs
        random.seed(seed)
    
    def acct_nbr(self):
        '''outputs account numbers as a list'''
        acct_nbr_list = []
        while len(acct_nbr_list)<self.n:
            rnd = (random.randint(100000000000000000,999999999999999999))
            rnd = append(str(rnd))
            #duplicate check
            if rnd in acct_nbr_list:
               continue
            else:
                acct_nbr_list += [rnd]
        return acct_nbr_list 
    
    def exp_dt(self):
        '''outputs expiry date as a list'''
        exp_dt_list = []
        curr_yr = datetime.date.today().year
        while len(exp_dt_list)<self.n:
            rnd1 = (random.randint(1,12))
            dgt = rnd1 // 10
            if dgt == 0:
                rnd1 =  str(str('0') + str(rnd1))
            #expiry date: 2019 to 2025
            rnd2 = random.randint(0,5)
            exp_yr = curr_yr + rnd2
            exp_dt = str(str(rnd1)+str(exp_yr))
            exp_dt_list += [exp_dt]
        return exp_dt_list
    
    def cvv(self):
        '''outputs cvv as a list'''
        cvv_list = []
        while len(cvv_list)<self.n:
            rnd = (random.randint(100,999))
            #duplicate check
            if rnd in cvv_list:
                continue
            else:
                cvv_list += [rnd]
        return cvv_list
    
    def block_code(self):
        '''outputs block codes as a list'''
        block_code_list = []
        for _ in range(self.n):  
            block_code = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
            block_code_list += [block_code]
        return block_code_list
    
    def status(self):
        ''' outputs account status as a list'''
        status_list = []
        for _ in range(self.n):
            status = random.choice('ADIMNQJ')
            status_list += [status]  
        return status_list
    
    def open_date(self):
        open_date_list = []
        for _ in range(self.n):
            current_year = datetime.date.today().year
            current_month = datetime.date.today().month
            #making 2 digit
            dgt = current_month // 10
            if dgt == 0:
                current_month =  str(str('0') + str(current_month))
            open_date = str(str(current_month) + str(current_year))
            open_date_list += [open_date] 
        return open_date_list
    
    def amt(self):
        '''outputs credit limit and current balence as a list'''
        credit_limit_list = []
        curr_bal_list = []
        for _ in range(self.n):
            random_real_nbr1 = round(random.uniform(0,999999999999999),2)
            credit_limit_list += [random_real_nbr1]
            random_real_nbr2 = round(random.uniform(0,999999999999999),2)
            while random_real_nbr2 < random_real_nbr1:
              random_real_nbr2 = round(random.uniform(0,999999999999999),2)
            curr_bal_list += [random_real_nbr2]
        return [credit_limit_list, curr_bal_list] 
    
    def Export(self):
        '''creates a dataframe and exportsa it in csv formate'''
        df = pd.DataFrame( list( zip( self.acct_nbr(), self.exp_dt(), self.cvv(), self.block_code(), self.status(), self.open_date(), self.amt()[0], self.amt()[1] )), 
                   columns =['acct_nbr', 'expiry_dt', 'cvv', 'block_code', 'status', 'open_date', 'credit_limit', 'curr_bal'])

        df.to_csv(r'C:\Users\azhar\Documents\Python_Projects\office_project\export_dataframe.csv', index = None, header=True)
        print('export_dataframe.csv created')  

if __name__== '__main__':
    print('run generator.py')
