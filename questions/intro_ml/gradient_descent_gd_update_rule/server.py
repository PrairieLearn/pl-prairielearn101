import random, copy
import sympy
import prairielearn as pl




def generate(data):
    # Declare math symbols
    #x_ij, y_i, yhat_i, l_r, g_w, g_b, w, b, t = sympy.symbols('x_{ij} y_i \hat{y_i} l_r \mathbf{g_w} g_b w b t')

    x_ij, y_i, yhat_i, alpha, w_j = sympy.symbols('x_ij y_i yhat_i alpha w_j')
    
    g1 = 2*(sympy.ln(yhat_i) - sympy.ln(y_i))*(1/yhat_i)*x_ij
    
    #g2 = 2*(sympy.log(yhat_i) - sympy.log(y_i))*(1/yhat_i)
    
    u1 = w_j - alpha * 2*(sympy.ln(yhat_i) - sympy.ln(y_i))*(1/yhat_i)*x_ij
    
    #u2 = b**t - l_r * g_b
   
    
    
    data['correct_answers']['g1'] = pl.to_json(g1)
    #data['correct_answers']['g2'] = pl.to_json(g2)
    
    data['correct_answers']['u1'] = pl.to_json(u1)
    #data['correct_answers']['u2'] = pl.to_json(u2)
    
'''
2*(\log(\hat{y_i}) - \log(y_i))\frac{1}{\hat{y_i}}x_{ij}\\
2*(\log(\hat{y_i}) - \log(y_i))\frac{1}{\hat{y_i}}\\
-2 \left[ \frac{1}{z_i} - y_i\right]\frac{1}{z_i^2}x_{ij}\\
-2 \left[ \frac{1}{z_i} - y_i\right]\frac{1}{z_i^2}\\
\left[ p_i - y_i\right] e^{-{(x_i-b_j)}^2/2}\\
\left[ p_i - y_i\right] a_j (b_j - x_i)e^{-{(x_i-b_j)}^2/2}\\
'''
