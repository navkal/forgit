

import pandas as pd

df = pd.read_csv('ZN-T-Results-1.csv' )
df = df.rename( columns={ 'Unnamed: 0': 'timestamp' } )
df = df[ df['timestamp'] < '2018-01-08 02:30:00' ]

print( 'bf', df.shape )
df = df[['116','345','Gymm']]
print( 'af', df.shape )

print( df )

print( 'bf dropna', df.shape )
df = df.dropna( axis=0, how='all' )
print( 'af dropna', df.shape )
print( df )

print( 'bf dropna any', df.shape )
df = df.dropna( axis=0, how='any' )
print( 'af dropna any', df.shape )
print( df )

# submit this to created_in_pycharm branch