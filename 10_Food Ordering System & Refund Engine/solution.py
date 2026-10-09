# =====================================================================
# 1. CORE MENU COMPONENT INTERFACE (WITH PRICE INTEGRITY GUARD RAILS)
# =====================================================================

class MenuItem:
    def __init__(self, item_name: str, price: float) -> None:
        """
        Initializes a secure food menu item component with string descriptor 
        and strict non-zero base price boundary validation.
        """
        if price <= 0:
            raise ValueError("Menu item price must be a positive non-zero value.")
            
        self.item_name = item_name
        self.price = price


# =====================================================================
# 2. STATIC DISCOUNT EVALUATION ROUTER (PROMOTION CONTROL ENGINE)
# =====================================================================

class DiscountEngine:
    @staticmethod
    def apply_coupon(coupon_code: str, item_price: float, quantity: int) -> float:
        """
        Static Component: Evaluates corporate markdown templates dynamically 
        and extracts calculated deduction balances without maintaining instance memory.
        """
        if coupon_code == "BOGO":
            free_items = quantity // 2
            return free_items * item_price
            
        elif coupon_code == "STEAL40":
            return (item_price * quantity) * 0.40
            
        else:
            return 0.0


# =====================================================================
# 3. ENTERPRISE FOOD ORDER CONTROLLER (WITH DYNAMIC REFUND SYSTEM)
# =====================================================================

class FoodOrder:
    def __init__(self, item: MenuItem, quantity: int, transaction_id: str, coupon_code: str = "") -> None:
        """
        Initializes an enterprise food order controller wrapping parameter tokens 
        and gateway transactional metadata behind secure private visibility layers.
        """
        self.__item = item
        self.__quantity = quantity
        self.__coupon_code = coupon_code
        self.__transaction_id = transaction_id
        self.__order_status: str = "PLACED & VERIFIED"

    def cancel_order(self) -> None:
        """
        Action Method: Mutates the internal order state to execute a cancellation workflow.
        """
        self.__order_status = "CANCELLED & REFUNDED"

    def __str__(self) -> str:
        """
        Magic Method: Unifies baseline calculations, processes static markdown routes, 
        injects localized 5% GST tax weights, and returns a verified text report.
        """
        base_total = self.__item.price * self.__quantity

        discount_money = DiscountEngine.apply_coupon(
            self.__coupon_code, self.__item.price, self.__quantity
        )

        subtotal = base_total - discount_money
        final_bill = subtotal + (subtotal * 0.05)
        refund_money = 0.0

        if self.__order_status == "CANCELLED & REFUNDED":
            refund_money = final_bill
            final_bill = 0.0

        return f"""
        ====================================================
                     ZOMATO ENTERPRISE INVOICE              
        ====================================================
        ITEM NAME    : {self.__item.item_name}
        QUANTITY     : {self.__quantity}
        BASE TOTAL   : ${base_total:.2f}
        COUPON CODE  : '{self.__coupon_code}'
        DISCOUNTED   : -${discount_money:.2f}
        TAX (5% GST) : ${subtotal * 0.05:.2f}
        ----------------------------------------------------
        TXN ID REF   : {self.__transaction_id}
        FINAL PAYABLE: ${final_bill:.2f}
        REFUNDED AMNT: ${refund_money:.2f}
        STATUS       : {self.__order_status}
        ====================================================
        """


# =====================================================================
# 4. AUTOMATED INTEGRATION TESTING SUITE WITH FAULT ISOLATION
# =====================================================================

def run_restaurant_system_tests() -> None:
    """
    Executes automated test cases simulating multiple product options, 
    flat volume markdowns, BOGO math flows, and dynamic cancellation pipelines.
    """
    print("INITIALIZING PRODUCTION FOOD ORDERING CORE RUNTIME\n")
    
    try:
        biryani = MenuItem("Chicken Biryani", 300.0)
    except ValueError as error:
        print(f"Menu Initialization Failed: {error}")
        return

    # Test Case 1: Raja's BOGO evaluation before and after cancellation execution
    try:
        order_raja = FoodOrder(biryani, 5, "TXN_998877A", "BOGO")
        print("TEST CASE 1: BOGO PROMOTION (BEFORE CANCELLATION)")
        print(order_raja)
        
        order_raja.cancel_order()
        print("\nTEST CASE 1: BOGO PROMOTION (AFTER LIVE CANCELLATION)")
        print(order_raja)
    except Exception as error:
        print(f"Error Processing Order 1: {error}")

    # Test Case 2: Surya's volume purchase tracking flat STEAL40 discount matrix
    try:
        order_surya = FoodOrder(biryani, 2, "TXN_112233B", "STEAL40")
        print("\nTEST CASE 2: FLAT 40% DISCOUNT (ACTIVE USER)")
        print(order_surya)
    except Exception as error:
        print(f"Error Processing Order 2: {error}")

    # Test Case 3: Venkat's standard transaction profile without any active promotion codes
    try:
        order_venkat = FoodOrder(biryani, 3, "TXN_445566C", "")
        print("\nTEST CASE 3: STANDARD CHECKOUT (NO COUPON CODE APP)")
        print(order_venkat)
    except Exception as error:
        print(f"Error Processing Order 3: {error}")


# =====================================================================
# 5. SYSTEM RUNTIME ENTRY POINT
# =====================================================================

if __name__ == "__main__":
    run_restaurant_system_tests()
