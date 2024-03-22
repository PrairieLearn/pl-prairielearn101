class Customer
  attr_accessor :name, :gift_card
  def initialize(name, gift_card=nil)
    @gift_card = gift_card
    @name = name
  end
  def pay(amount)
    if gift_card.withdraw(amount)
      nil
    else
      self.notify("purchase cannot be completed")
    end
  end
end
