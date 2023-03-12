import random, copy
import matplotlib.pyplot as plt
import numpy as np

def html_color(f):
    Colors = plt.get_cmap('Purples')
    return '#{:02x}{:02x}{:02x}'.format(*(255*np.array(Colors(f))).astype(int)[0:3])

def confusion_matrix_colors(d):
    den = sum(d.values())
    return  {k: html_color(v / den) for k, v in d.items()}

def compute_metrics(d):
    return {
    'accuracy'   : 100*( d['tp'] + d['tn'] )/sum(d.values()),
    'pos_actual' : 100*(d['tp'] + d['fn'])  /sum(d.values()),
    'pos_pred'   : 100*(d['tp'] + d['fp'])  /sum(d.values()),
    'tpr'        : 100*( d['tp'])           /(d['tp'] + d['fn']), 
    'tnr'        : 100*( d['tn'])           /(d['fp'] + d['tn']),
    'ppv'        : 100*( d['tp'])           /(d['tp'] + d['fp']), 
    'npv'        : 100*( d['tn'])           /(d['tn'] + d['fn']),
    'fpr'        : 100*( d['fp'])           /(d['fp'] + d['tn']), 
    'fdr'        : 100*( d['fp'])           /(d['tp'] + d['tp']),
    'fnr'        : 100*( d['fn'])           /(d['fn'] + d['tp']), 
    'for'        : 100*( d['fn'])           /(d['fn'] + d['tn'])
    }

def generate(data):
    
    # set up basic stats
    
    fn_1, fn_2, tp_1, tp_2, fp_1, fp_2, tn_1, tn_2 = np.repeat(-1, 8)
    
    # make sure all values are bigger than zero
    while any(v <= 0 for v in [fn_1, fn_2, tp_1, tp_2, fp_1, fp_2, tn_1, tn_2]):

        n = 1000*np.random.randint(15, 50)
        p_1 = np.round(np.random.uniform(0.4, 0.6), 3)
        p_2 = 1 - p_1
        n_1 = int(n*p_1)
        n_2 = int(n*p_2)
        
        # base rates
        actual_pos_1 = np.round(np.random.uniform(0.65, 0.8), 2)
        actual_pos_2 = np.round(np.random.uniform(0.35, 0.50), 2)
        actual_posn_1 = int(actual_pos_1*n_1)
        actual_negn_1 = n_1 - actual_posn_1
        actual_posn_2 = int(actual_pos_2*n_2)
        actual_negn_2 = n_2 - actual_posn_2
    
        # accuracy
        acc = np.random.uniform(0.65, 0.8)
        acc_1 = np.random.uniform(acc-0.015, acc+0.015)
        acc_2 = np.random.uniform(acc-0.015, acc+0.015)
        correct_n_1 = int(acc_1*n_1)
        correct_n_2 = int(acc_2*n_2)
        wrong_n_1 = n_1 - correct_n_1
        wrong_n_2 = n_2 - correct_n_2
    
        # now, either equalize PPV or equalize FPR
        opt = random.choice([0, 1])
        
        if opt:
            # equal FOR: FN/(FN+TN)
            #fort = 0.1 #np.random.uniform(0.1, 0.3)
            #fort_1 = np.random.uniform(fort-0.015, fort+0.015)
            #fort_2 = np.random.uniform(fort-0.015, fort+0.015)
            
            
            k = np.random.uniform(7/36, 12/36)
            k_1 = k + np.random.uniform(-0.05, +0.05)
            k_2 = k + np.random.uniform(-0.05, +0.05)
            fn_1 = int(k_1*(n_1 - actual_posn_1 - wrong_n_1))
            fn_2 = int(k_2*(n_2 - actual_posn_2 - wrong_n_2))
            
            tp_1 = actual_posn_1 - fn_1
            tp_2 = actual_posn_2 - fn_2
        
            # now fp is set and so is tn
            fp_1 = wrong_n_1 - fn_1
            fp_2 = wrong_n_2 - fn_2
            tn_1 = n_1 - fp_1 - tp_1 - fn_1
            tn_2 = n_2 - fp_2 - tp_2 - fn_2
            
            data['params']['ans'] = {'for': "false", 'fpr': "true"}

        else:
        
            # equal FPR - FP/(FP + TN)
            fpr = np.random.uniform(0.1, 0.3)
            fpr_1 = np.random.uniform(fpr-0.015, fpr+0.015)
            fpr_2 = np.random.uniform(fpr-0.015, fpr+0.015)
            
            # now everything is fixed
            fp_1 = int(actual_negn_1*fpr_1)
            fp_2 = int(actual_negn_2*fpr_2)
            tn_1 = actual_negn_1 - fp_1
            tn_2 = actual_negn_2 - fp_2
        
            tp_1 = correct_n_1 - tn_1
            tp_2 = correct_n_2 - tn_2
            fn_1 = n_1 - fp_1 -tn_1 - tp_1
            fn_2 = n_2 - fp_2 -tn_2 - tp_2
            
            data['params']['ans'] = {'for': "true", 'fpr': "false"}


    data['params']['refs'] = random.choice([ 
        {'overall': "University of Central Westeros", 'g1': "the Crownlands", 'g2': "the Westerlands"},
        {'overall': "University of the Milky Way", 'g1': "Mars", 'g2': "Titan"},
        {'overall': "Starfleet Technical University", 'g1': "Tau Cygna V Colony", 'g2': "Delta Rana IV Colony"},
        {'overall': "University of the Colonies of Kobol", 'g1': 'Scorpia', 'g2': 'Caprica'}

        ])
    #data['params']['g1_cm'] = {'tn': 500, 'fp': 450, 'fn': 350, 'tp': 1100}
    data['params']['g1_cm'] = {'tn': tn_1, 'fp': fp_1, 'fn': fn_1, 'tp': tp_1}
    data['params']['g1_cm_colors'] = confusion_matrix_colors(data['params']['g1_cm'])

    #data['params']['g2_cm'] = {'tn': 1400, 'fp': 500, 'fn': 800, 'tp': 990}
    data['params']['g2_cm'] = {'tn': tn_2, 'fp': fp_2, 'fn': fn_2, 'tp': tp_2}
    data['params']['g2_cm_colors'] = confusion_matrix_colors(data['params']['g2_cm'])

    data['params']['overall_cm'] = {
        'tn': data['params']['g1_cm']['tn'] + data['params']['g2_cm']['tn'],
        'fp': data['params']['g1_cm']['fp'] + data['params']['g2_cm']['fp'],
        'fn': data['params']['g1_cm']['fn'] + data['params']['g2_cm']['fn'],
        'tp': data['params']['g1_cm']['tp'] + data['params']['g2_cm']['tp']
    }

    overall_metrics = compute_metrics(data['params']['overall_cm'])
    g1_metrics      = compute_metrics(data['params']['g1_cm'])
    g2_metrics      = compute_metrics(data['params']['g2_cm'])

    data['correct_answers']['pos-g1-pred'] = g1_metrics['pos_pred']
    data['correct_answers']['pos-g2-pred'] = g2_metrics['pos_pred']
    data['correct_answers']['pos-overall-pred'] = overall_metrics['pos_pred']

    data['correct_answers']['pos-g1-actual'] = g1_metrics['pos_actual']
    data['correct_answers']['pos-g2-actual'] = g2_metrics['pos_actual']
    data['correct_answers']['pos-overall-actual'] = overall_metrics['pos_actual']

    data['correct_answers']['accuracy-g1'] = g1_metrics['accuracy']
    data['correct_answers']['accuracy-g2'] = g2_metrics['accuracy']
    data['correct_answers']['accuracy-overall'] = overall_metrics['accuracy']

    data['correct_answers']['for-g1'] = g1_metrics['for']
    data['correct_answers']['for-g2'] = g2_metrics['for']
    data['correct_answers']['for-overall'] = overall_metrics['for']

    data['correct_answers']['ppv-g1'] = g1_metrics['ppv']
    data['correct_answers']['ppv-g2'] = g2_metrics['ppv']
    data['correct_answers']['ppv-overall'] = overall_metrics['ppv']

    data['correct_answers']['npv-g1'] = g1_metrics['npv']
    data['correct_answers']['npv-g2'] = g2_metrics['npv']
    data['correct_answers']['npv-overall'] = overall_metrics['npv']

    data['correct_answers']['fpr-g1'] = g1_metrics['fpr']
    data['correct_answers']['fpr-g2'] = g2_metrics['fpr']
    data['correct_answers']['fpr-overall'] = overall_metrics['fpr']

    data['correct_answers']['fnr-g1'] = g1_metrics['fnr']
    data['correct_answers']['fnr-g2'] = g2_metrics['fnr']
    data['correct_answers']['fnr-overall'] = overall_metrics['fnr']
