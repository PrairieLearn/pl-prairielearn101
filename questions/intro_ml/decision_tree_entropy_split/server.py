import random, copy
import numpy as np
from scipy.stats import entropy
import pandas as pd
import prairielearn as pl


def generate(data):
  
    col_names = ['name', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 
             'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tail', 'domestic', 'catsize', 'type']
    class_names = np.array(['mammal', 'bird', 'reptile', 'fish', 'amphibian', 'bug', 'invertebrate'])
    df = pd.read_csv("clientFilesQuestion/zoo.data", names=col_names)
    
    # class names are: 1 mammal, 2 bird, 3 reptile, 4 fish, 5 amphibian, 6 bug and 7 invertebrate
    choices = [{'class0': 6, 'name0': 'bug', 'class1': 4, 'name1': 'fish',  'cols': ['hair', 'eggs', 'predator', 'tail', 'domestic']},
                {'class0': 6, 'name0': 'bug', 'class1': 4, 'name1': 'fish',  'cols': ['breathes', 'milk', 'predator', 'venomous', 'domestic']} ,
                {'class0': 6, 'name0': 'bug', 'class1': 1, 'name1': 'mammal', 'cols': ['aquatic', 'eggs', 'venomous', 'airborne', 'hair']},
                {'class0': 2, 'name0': 'bird', 'class1': 1, 'name1': 'mammal', 'cols': ['tail', 'feathers', 'backbone', 'predator', 'aquatic']},
                {'class0': 2, 'name0': 'bird', 'class1': 4, 'name1': 'fish', 'cols': ['predator', 'milk', 'domestic', 'feathers', 'toothed']}  ]
                
    o = random.choice(choices)
    data['params'] = o
    
    df_sub = df[df.type.isin([o['class0'], o['class1']])].groupby('type').sample(n=5)
    df_sub = df_sub.sample(frac=1)
    
    X = df_sub[o['cols']].reset_index(drop=True)
    y = class_names[df_sub['type']-1]
    y_int = df_sub['type'].reset_index(drop=True)
    
    df_disp = pd.DataFrame(df_sub['name'])
    df_disp[o['cols']] = df_sub[o['cols']]
    df_disp = df_disp.assign(category = y)
    df_disp.reset_index(drop=True, inplace=True)
    data['params']['dat'] = pl.to_json(df_disp)
    
    n_total = X.shape[0]
    unique, counts = np.unique(y, return_counts=True)
    e = entropy(counts/n_total, base=2)
    
    feats = []
    for j in range(X.shape[1]):
      # consider negative and positive branch:
      y_neg = y_int[X[X.iloc[:, j]==0].index]
      y_neg_unique, y_neg_counts = np.unique(y_neg, return_counts=True)
      y_neg_counts = np.array( [ np.count_nonzero(y_neg == o['class0']),  np.count_nonzero(y_neg == o['class1']) ] )
      y_neg_total = y_neg.shape[0]
      y_pos = y_int[X[X.iloc[:, j]==1].index]
      y_pos_total = y_pos.shape[0]
      y_pos_counts = np.array( [ np.count_nonzero(y_pos == o['class0']),  np.count_nonzero(y_pos == o['class1']) ] )
      e_neg = entropy(y_neg_counts/y_neg_total, base=2) if y_neg_total else 0
      e_pos = entropy(y_pos_counts/y_pos_total, base=2) if y_pos_total else 0
      cond_e = y_neg_total/(y_neg_total+y_pos_total)*e_neg + y_pos_total/(y_neg_total+y_pos_total)*e_pos
      gain = e-cond_e
      feats.append({'j': j, 'name': X.columns[j], 'n': y_neg_total + y_pos_total, 'n_neg': y_neg_total, 'n_pos': y_pos_total,
                    'count_neg': y_neg_counts.tolist(), 'count_pos': y_pos_counts.tolist(),
                    'e_neg': round(e_neg, 5), 'e_pos': round(e_pos,5), 'cond_e': round(cond_e, 5), 'e_gain': round(gain, 5), 
                    'isZero': bool(np.isclose( gain, 0 )), 'isOne': bool(np.isclose( gain, 1 ))
      })
                    
    data['params']['feats'] = pl.to_json(feats)
    
    gains = [f['e_gain'] for f in feats]
    max_gains = np.argmax(gains)
    max_gain_cols = X.columns[max_gains]
    
    data['params']['split'] = [{'tag': f['name'], 'ans': f['name'] in max_gain_cols} for f in feats]
    
    data['params']['e'] = float(e)