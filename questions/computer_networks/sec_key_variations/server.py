import random, copy

def generate(data):
    
    main1 = """
  sender -> encrypt -> network -> decrypt -> receiver
  {rank = same; sender; encrypt; network; decrypt; receiver;}  
"""

    main2 = """
  encrypt2 [label="Encrypt" fillcolor="2"]
  decrypt2 [label="Decrypt" fillcolor="2"]
  sender -> encrypt -> encrypt2 -> network -> decrypt2 -> decrypt -> receiver
  {rank = same; sender; encrypt; encrypt2; network; decrypt2; decrypt; receiver;}  
"""

    sharedkey = """
  sharedkey [width="3" label="Shared Secret Key &#128477;" fillcolor="9"]

  sharedkey -> encrypt [style="dashed"]
  sharedkey -> decrypt [style="dashed"]
  {rank = min; sharedkey;}  
"""
    rxpubkey = """
  rxpubkey [label="Bob's Public Key &#128477;" fillcolor="4"]
  rxprvkey [label="Bob's Private Key &#128477;" fillcolor="4"]
  rxpubkey -> encrypt [style="dashed"]
  rxprvkey -> decrypt [style="dashed"]
  {rank = min; rxpubkey; rxprvkey;}  
"""

    txprvkey = """
  txpubkey [label="Alice's Public Key &#128477;" fillcolor="8"]
  txprvkey [label="Alice's Private Key &#128477;" fillcolor="8"]
  txpubkey -> decrypt [style="dashed"]
  txprvkey -> encrypt [style="dashed"]
  {rank = min; txpubkey; txprvkey;}  
"""

    bothkey = """
  rxpubkey [label="Bob's Public\n Key &#128477;" fillcolor="4"]
  rxprvkey [label="Bob's Private\n Key &#128477;" fillcolor="4"]
  rxpubkey -> encrypt [style="dashed"]
  rxprvkey -> decrypt [style="dashed"]
  txpubkey [label="Alice's Public\n Key &#128477;" fillcolor="8"]
  txprvkey [label="Alice's Private\n Key &#128477;" fillcolor="8"]
  txpubkey -> decrypt2 [style="dashed"]
  txprvkey -> encrypt2 [style="dashed"]
  {rank = min; rxpubkey; rxprvkey; txpubkey; txprvkey;}  
"""

    data['params'] = random.choice([ 
        {'key': 'The message is encrypted by Alice and decrypted by Bob using a secret key that is known only to Alice, Bob, and their friends Carol and David.', 'graph': sharedkey, 'ans': [True, True, False, False], 'ansx': [True, False, False], 'main': main1, 'asym': False},
        {'key': "The message is encrypted by Alice using Bob's public key (known to everyone), and decrypted by Bob using Bob's private key (known only to Bob).", 'graph': rxpubkey, 'ans': [True, True, False, False], 'ansx': [True, False, False], 'main': main1, 'asym': True},
        {'key': "The message is encrypted by Alice using Alice's private key (known only to Alice), and decrypted by Bob using Alice's public key (known to everyone).", 'graph': txprvkey, 'ans': [True, False, True, False], 'ansx': [False, True, False], 'main': main1, 'asym': True},
        {'key': "The message is encrypted by Alice using Bob's public key (known to everyone) and then again using Alice's private key (known only to Alice). The message is decrypted by Bob using Alice's public key (known to everyone) and then using Bob's private key (known only to Bob).", 'graph': bothkey, 'ans': [True, True, True, False], 'ansx': [False, False, True], 'main': main2, 'asym': True}

    ])