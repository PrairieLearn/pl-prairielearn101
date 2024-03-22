"""Take a look at the pay method of Customer, which is the
subject of the next set of tests that you will construct.<br /><br />

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

The new challenge in testing
<code>#pay</code> is that it calls an instance method of another class
(<code>GiftCard#withdraw</code>).  In this case we know all about the behavior of
that method, and it's fairly simple.  But if
don't know the details of how it works, or even worse if it's
temporarily broken, we don't want our tests to fail just because
<code>#withdraw</code> is failing.  So we use test doubles to isolate the
<code>Customer</code> tests from the behavior of <code>GiftCard</code>.<br /><br />

If you look at <code>Customer#pay</code>, the only behavior we really care about
regarding <code>#withdraw</code> is whether it returns a truthy or falsy value,
since that determines what happens next.  This challenge guides you through
building a single test case in which we construct a <i>test double</i> for
a gift card.  The <code>double</code> is an object that has no built-in behaviors,
so it must be given just enough behavior to be useful
for this test case: we use allow to say "If the double gets a call
to withdraw, it should just return true".  Similarly, if <code>#pay</code> is
working correctly, the result of a successful withdrawal should be a
call to <code>Customer#notify</code> with a happy message.  Note that in this
case, <code>Customer#notify</code> hasn't even been implemented!  By saying
that we expect to receive a call to it with a particular argument, we
basically "short-circuit" the real method call.  This further isolates
our test case from other methods, even those in <code>Customer</code> itself. <br /><br />
"""


{"pre": "describe Customer do\n  it 'buys the item if balance covers payment' do\n", "lines": "@loaded_gift_card = double('gift_card') #0given\nallow(@loaded_gift_card).to receive(:?withdraw?).and_return(true)\n@customer = ?Customer?.new('Student', @fake_gift_card)\nexpect(?@customer?).to receive(:?notify?).with(\"payment successful\")\n@customer.?pay?(10)\n", "post": "  end\nend\n"}


