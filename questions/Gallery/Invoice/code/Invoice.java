import java.util.ArrayList;
import java.util.List;

public class Invoice {

    public List<InvoiceLine> items = new ArrayList<>();

    public Invoice() {
    }

    public void addItem(Product product, int quantity) {
        items.add(new InvoiceLine(product, quantity));
    }

    public int getTotal() {
        /* TO BE COMPLETED BY THE STUDENT */
    }

    public class InvoiceLine {
        private Product product;
        private int quantity;

        public InvoiceLine(Product product, int quantity) {
            this.product = product;
            this.quantity = quantity;
        }

        public Product getProduct() {
            return product;
        }

        public int getQuantity() {
            return quantity;
        }
    }
}
