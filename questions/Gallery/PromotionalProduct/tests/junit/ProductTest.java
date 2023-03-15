import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ProductTest {

    private PromotionalProduct product;

    @BeforeEach
    void createProduct() {
        product = new PromotionalProduct(1, "", 50, 10, 40);
    }

    @ParameterizedTest(name = "Below promotion (quantity {0})")
    @ValueSource(ints = {1, 2, 9})
    void testBelowPromotion(int quantity) {
        assertEquals(quantity * 50, product.getTotalPrice(quantity));
    }

    @ParameterizedTest(name = "With promotion (quantity {0})")
    @ValueSource(ints = {10, 50})
    void testWithPromotion(int quantity) {
        assertEquals(quantity * 40, product.getTotalPrice(quantity));
    }
}
