class GiftCard
  attr_reader :balance, :error
  def initialize(balance)
    if balance < 0
      raise ArgumentError.new("New gift card cannot have negative balance")
    end
    @balance = balance
    @error = 'not nil'
  end
  def withdraw(amount)
    if @balance >= amount
      @balance -= amount
    else
      @error = "Insufficient balance"
      return nil
    end
  end
end
