"""Your app manages online gift cards for a soon-to-be-major e-tailer.
Customers can use the app to place orders using their card
balance. <br /><br />

We have classes that model the GiftCard and the Customer.  First you
will write tests for the GiftCard class, to verify that: <br /><br />

* a GiftCard when first created has a non-negative cash balance <br />
* a withdrawal when there is enough cash returns success, and changes 
the card balance <br />
* a withdrawal when there is not enough cash returns failure, provides 
an error message explaining the failure, and does not change the card balance. <br />
"""


{"pre": "describe GiftCard do\n", "lines": "it 'fails with negative balance' do\n  expect { GiftCard.new(-1) }.to raise_error(?ArgumentError?)\nend\nit 'succeeds with positive balance' do\n  gift_card = GiftCard.new(20)\n  ?expect?(gift_card.balance).to ?eq?(20)\nend\n", "post": "end\n"}


