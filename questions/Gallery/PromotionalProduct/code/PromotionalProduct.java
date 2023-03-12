public class PromotionalProduct extends Product {

    private int promotionQuantity;
    private int promotionPrice;

    public PromotionalProduct(int id, String name, int price,
                              int promotionQuantity, int promotionPrice) {
        super(id, name, price);
        this.promotionQuantity = promotionQuantity;
        this.promotionPrice = promotionPrice;
    }

    public int getPromotionQuantity() {
        return promotionQuantity;
    }

    public int getPromotionPrice() {
        return promotionPrice;
    }

    @Override
    public int getTotalPrice(int quantity) {
        /* TO BE COMPLETED BY THE STUDENT */
    }
}
