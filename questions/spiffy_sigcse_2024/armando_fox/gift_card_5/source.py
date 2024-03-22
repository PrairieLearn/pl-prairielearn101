"""For our last step we will test the code's sad path and factor out common
lines of test code to keep things DRY. We will use the same double, but
this time we instruct it to
always return a falsy value so we can test the other code path in
<code>#pay</code>.  Since setting up the double (and the <code>Customer</code> instance) are
common to both test cases, we move them into a <code>before</code> block as we
did with <code>GiftCard</code>, and group the related examples and their
before-block in a <code>describe</code>.<br /><br />

System Under Test:
<pl-code language="ruby">
class Customer
  attr_accessor :name, :gift_card
  def initialize(name, gift_card=nil)
    @gift_card = gift_card
    @name = name
  end
  def pay(amount)
    if gift_card.withdraw(amount)
      self.notify("payment successful")
    else
      self.notify("purchase cannot be completed")
    end
  end
end
</pl-code>
"""


{"pre": "describe Customer do\n  describe 'trying to buy' do\n", "lines": "before(:?each?) do #0given\n  @loaded_gift_card = ?double?('gift_card')\n  @customer = Customer.new('Student', @loaded_gift_card)\nend\nit 'succeeds if balance covers payment' do\n  allow(@?loaded_gift_card?).to receive(:withdraw).and_return(?true?)\n  expect(@customer).to receive(:notify).with(\"payment successful\")\n  @customer.?pay?(10)\nend\nit 'fails if balance does not cover payment' do\n  allow(@?loaded_gift_card?).to receive(:?withdraw?).and_return(?nil?)\n  expect(@customer).to receive(:?notify?).with(\"purchase cannot be completed\")\n  @customer.?pay?(10)\nend\n", "post": "  end\nend\n"}


