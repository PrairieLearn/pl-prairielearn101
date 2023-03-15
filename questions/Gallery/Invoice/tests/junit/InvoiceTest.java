import org.junit.jupiter.api.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
public class InvoiceTest {

    private Invoice invoice;

    @BeforeEach
    void createInvoice() {
        invoice = new Invoice();
    }

    @ParameterizedTest(name = "Invoice: One regular product, quantity {0}")
    @Order(1)
    @ValueSource(ints = {1, 5})
    void testOneRegularProduct(int quantity) {
        invoice.addItem(new Product(1, "", 50), quantity);
        assertEquals(50 * quantity, invoice.getTotal());
    }

    @ParameterizedTest(name = "Invoice: One promotional product, quantity {0} (below promotion)")
    @Order(2)
    @ValueSource(ints = {1, 5})
    void testOnePromotionProduct(int quantity) {
        invoice.addItem(new PromotionalProduct(1, "", 50, 10, 40), quantity);
        assertEquals(50 * quantity, invoice.getTotal());
    }

    @ParameterizedTest(name = "Invoice: One promotional product, quantity {0} (with promotion)")
    @Order(3)
    @ValueSource(ints = {10, 20})
    void testOnePromotionProductAtPromotion(int quantity) {
        invoice.addItem(new PromotionalProduct(1, "", 50, 10, 40), quantity);
        assertEquals(40 * quantity, invoice.getTotal());
    }

    @Test
    @Order(4)
    @DisplayName("Invoice: Multiple products with different types")
    void testMultipleProducts() {
        invoice.addItem(new Product(1, "", 20), 10); // 200
        invoice.addItem(new Product(2, "", 30), 20); // 600
        invoice.addItem(new PromotionalProduct(3, "", 50, 10, 40), 5); // 250
        invoice.addItem(new PromotionalProduct(4, "", 100, 3, 80), 2); // 200
        invoice.addItem(new PromotionalProduct(5, "", 150, 10, 100), 10); // 1000
        invoice.addItem(new PromotionalProduct(6, "", 200, 2, 150), 3); // 450
        assertEquals(200 + 600 + 250 + 200 + 1000 + 450, invoice.getTotal());
    }

    @Test
    @Order(5)
    @DisplayName("Invoice: Check call to getTotalPrice")
    void testOtherClasses() {
        invoice.addItem(new Product(1, "", 20) {
            @Override
            public int getTotalPrice(int quantity) {
                return 75;
            }
        }, 10);
        invoice.addItem(new PromotionalProduct(1, "", 20, 5, 15) {
            @Override
            public int getTotalPrice(int quantity) {
                return 50;
            }
        }, 10);
        assertEquals(125, invoice.getTotal());
    }
}
