"""Your app manages online gift cards for a soon-to-be-major e-tailer.
Customers can use the app to place orders using their card
balance. <br /><br />

We have classes that model the GiftCard and the Customer.  First you
will write tests for the GiftCard class, to verify that: <br /><br />

* a GiftCard when first created has a non-negative cash balance <br />
* a withdrawal when there is enough cash returns success, and changes
the card balance <br />
* a withdrawal when there is not enough cash returns failure, provides 
an error message explaining the failure, and does not change the card balance. <br /><br />

The provided code before the submission box is semantically equivalent to the 
code you wrote previously, but take note that we have chosen to separate it 
logically by putting it into a `describe` block.
"""


{"pre": "describe GiftCard do\n  describe 'creating' do\n    it 'fails with negative balance' do\n      expect { GiftCard.new(-1) }.to raise_error(ArgumentError)\n    end\n    it 'succeeds with positive balance' do\n      gift_card = GiftCard.new(20)\n      expect(gift_card.balance).to eq(20)\n    end\n  end\n  describe 'withdrawing with sufficient balance' do\n", "lines": "it 'returns truthy value' do\n  @gift_card = GiftCard.new(20)\n  @result = @gift_card.?withdraw?(15)\n  ?expect?(@result).to be_truthy\nend\nit 'changes the balance' do\n  @gift_card = GiftCard.new(20)\n  @result = @gift_card.withdraw(15)\n  expect(@gift_card.balance).to ?eq?(5)\nend\nit 'does not result in error message' do\n  @gift_card = GiftCard.new(20)\n  @result = @gift_card.withdraw(15)\n  expect(@gift_card.?error?).to be_empty\nend\n", "post": "  end\nend\n"}


