import pandas as pd
import glob

def load_all():
  call_codes = pd.read_csv('./raw/call_codes.csv')
  call_codes['combined_call_codes'] = call_codes["type"] + call_codes["pd_code"].astype('str')

  files = glob.glob('./raw/jcpd*.csv')

  data = [ ]
  for fname in files:
    print 'loading: ' + fname
    d = pd.read_csv(fname)
    d.columns = [c.lower() for c in d.columns]
    data.append(d)

  all_calls = pd.concat(data)
  all_calls['callcode'] = all_calls['callcode'].astype('str')
  all_calls['short_call_code'] = all_calls['callcode'].apply(lambda x : x.split('.')[0])
  all_calls = all_calls.merge(call_codes, left_on='short_call_code', right_on='combined_call_codes')
  return all_calls
  
def write_csv_all():
  all_calls = load_all()
  all_calls.to_csv('./jcpd-calls-for-service-all.csv', index=False)
