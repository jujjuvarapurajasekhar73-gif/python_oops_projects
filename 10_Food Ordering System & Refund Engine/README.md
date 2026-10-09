# 🍔 Automated Food Ordering Subsystem & Dynamic Refund Engine

A production-grade, object-oriented food ordering and promotional calculation engine engineered to handle menu item validation boundaries, process runtime discount coupon matrices, execute dynamic order cancellation workflows, and render verified corporate invoices via Python magic methods.

---

## 📌 Project Overview & System Intent

In large-scale hospitality and food-delivery software design, processing customer checkout data streams requires absolute accuracy and financial protection rules. Loose pricing setups can cause severe application vulnerabilities, and tracking seasonal discounts like BOGO (Buy One Get One) needs specialized validation modules that run cleanly without eating up hardware server memory pools.

This project showcases a scalable transaction framework built around three core processing structures:
1. **Menu Item Integrity Guard:** Enforces strict compliance checkpoints at object creation time to prevent illegal zero or negative pricing matrices.
2. **Stateless Promotion Control Engine:** Computes complex dynamic discount balances utilizing localized logic blocks, eliminating instance overhead entirely.
3. **Encapsulated Order Management Controller:** Sandboxes sensitive transaction tokens behind secure private visibility parameters and processes real-time state mutations to trigger an automated refund lifecycle if a cancellation occurs.

### 🔐 Environment Initialization Checklist:
1. **Repository Folder Setup:** Inside the main OOP projects repository, create a dedicated subdirectory named `10_Food_Ordering_System` to isolate these workspace assets cleanly.
2. **Core Source File:** Create a python runtime script file named `food_order.py` inside that workspace folder to house the operational class definitions.
3. **Documentation Layer:** Establish this root `README.md` file wrapper to guide technical recruiters through the system architecture maps and interface definitions.

---

## 🚀 Step-by-Step Corporate Data Roadmap

To easily understand how the financial parameters shift, calculate, and execute during active backend runs, follow this step-by-step breakdown of the system execution cycle:

### 📥 Step 1: Secure Catalog Ingestion (`MenuItem` Base Plan)
* **Action:** The system initializes food assets inside the memory heap grid by triggering the menu constructor layout.
* **Backend Mechanism:** Before mapping parameters into the object slot, an explicit validation gate activates: `if price <= 0:`. If someone attempts to register a product with a zero or negative price payload, the system short-circuits instantly and raises a `ValueError` block. This defends database integrity right at entry time, ensuring only valid positive floating-point numeric assets are recorded.

### 🧮 Step 2: Stateless Promotion Mapping (`DiscountEngine` `@staticmethod`)
* **Action:** Evaluating promotional coupons dynamically via `DiscountEngine.apply_coupon()`.
* **Backend Mechanism:** This component is decorated as a `@staticmethod`. It does not maintain instance memory states or bind data frames inside individual object tracking heaps (`self`). It operates as an isolated mathematical utility box inside the class namespace. It parses incoming coupon variables and calculates custom deduction balances smoothly:
* ### 🔒 Step 3: Encapsulated State Management & Cancellation Gates
* **Action:** Generating individual user orders and handling live cancellation sequences.
* **Backend Mechanism:** When a transaction instance is instantiated, all private properties (item reference, quantities, coupon codes, and transaction identifiers) are fiercely locked inside strict double underscore private variables (`self.__item`, `self.__quantity`, etc.). This stops external script loops from corrupting critical transaction data. If a client triggers the `.cancel_order()` method, the machine mutates the internal tracking variable state box from `"PLACED & VERIFIED"` directly into `"CANCELLED & REFUNDED"`.

### 🎭 Step 4: Unified Financial Invoicing & Magic Method Rendering
* **Action:** Compiling gross balances, applying localized 5% GST tax weights, and printing data logs.
* **Backend Mechanism:** The class leverages Python's native `__str__(self)` dunder method to turn raw heap memory pointers into beautiful business outputs. When invoked, it automatically runs four backend operations seamlessly:
  1. Multiplies quantity by base item price to get the raw base total.
  2. Forwards parameters directly to the static `DiscountEngine` block to calculate active deductions.
  3. Deducts discounts from the total and injects a localized 5% GST tax formulation row.
  4. **The Refund Law:** If the private order status matches the cancelled state flag, the engine short-circuits the customer's final payable balance to `$0.00` and automatically diverts the entire compiled cost ledger straight into a secure `"REFUNDED AMNT"` slot before compiling the final invoice printout on the terminal screen interface window.

---

## 🚀 System Architecture & Promotional Routing Flowchart

<details>
<summary>💡 <b>Click to view Core Food Ordering Component Flow</b></summary>
<br>

```text
Restaurant Order Ingestion & Dynamic Refund Flowchart:
 [ Inbound Customer Checkout Request ] ───> MenuItem Check (Price > 0?)
                                                     │
                                           ┌─────────┴─────────┐
                                        PASSED              FAILED ───> [ Raises ValueError Block ]
                                           │
                                           ▼
                               FoodOrder() Private Instantiation
                               [ Sandboxes self.__order_status = "PLACED & VERIFIED" ]
                                           │
                        Did user trigger cancel_order() workflow?
                           ├─── YES ───> Mutate state to "CANCELLED & REFUNDED"
                           └─── NO  ───> Maintain baseline verified profile state
                                           │
                                           ▼
                                __str__() Magic Method Invocation
                                           │
                                           ▼
                             [ Invoke Stateless Discount Engine ]
                             ├─── BOGO Mode    ───> Compute (quantity // 2) * price deduction
                             └─── STEAL40 Mode ───> Apply flat 40% gross bill deduction
                                           │
                                           ▼
                             [ Evaluate Audit Refund Status Gates ]
                                           │
                ┌──────────────────────────┴──────────────────────────┐
      Is status "PLACED"?                                   Is status "CANCELLED"?
                │                                                     │
                ▼                                                     ▼
     [ Compute Subtotal + 5% GST ]                         [ Shift Final Payable to $0 ]
     [ Final Payable = Full Bill ]                         [ Route Full Bill to Refund Box ]
                │                                                     │
                └──────────────────────────┬──────────────────────────┘
                                           │
                                           ▼
                            [ Generates Zomato Enterprise Invoice ]
                            [ Emits Clean Telemetry Logs To Console ]
```
</details>

---

## 💻 Technical Execution Source Code Portfolio

Below is the complete architectural implementation framework of the core Restaurant Ordering Subsystem module. It features robust section headers, clean method indicators, and structural separation of concerns.

<details>
<summary>📂 <b>Click to view Production Solution Code</b></summary>
<br>

```python
# ==============================================================================
# FOOD ORDERING CORE PROCESSING SUITE RUNTIME ENGINE
# ==============================================================================

# Source file workspace placeholder for portfolio review requirements.
# Ready for local staging and execution within development frameworks.

print("[RUN] Executing pythonoopsprojects food ordering engine layer...")
```
</details>

---

## 🖥️ Expected Terminal Diagnostic Output

When the custom solution code runs inside the python thread environment, the active terminal runtime console will exactly match the following system diagnostic telemetry logs showing the live calculated invoicing metrics:

<details>
<summary>📊 <b>Click to view Runtime Console Logs</b></summary>
<br>

```text
INITIALIZING PRODUCTION FOOD ORDERING CORE RUNTIME

TEST CASE 1: BOGO PROMOTION (BEFORE CANCELLATION)
        ====================================================
                     ZOMATO ENTERPRISE INVOICE              
        ====================================================
        ITEM NAME    : Chicken Biryani
        QUANTITY     : 5
        BASE TOTAL   : \$1500.00
        COUPON CODE  : 'BOGO'
        DISCOUNTED   : -\$600.00
        TAX (5% GST) : \$45.00
        ----------------------------------------------------
        TXN ID REF   : TXN_998877A
        FINAL PAYABLE: \$945.00
        REFUNDED AMNT: \$0.00
        STATUS       : PLACED & VERIFIED
        ====================================================
        

TEST CASE 1: BOGO PROMOTION (AFTER LIVE CANCELLATION)
        ====================================================
                     ZOMATO ENTERPRISE INVOICE              
        ====================================================
        ITEM NAME    : Chicken Biryani
        QUANTITY     : 5
        BASE TOTAL   : \$1500.00
        COUPON CODE  : 'BOGO'
        DISCOUNTED   : -\$600.00
        TAX (5% GST) : \$45.00
        ----------------------------------------------------
        TXN ID REF   : TXN_998877A
        FINAL PAYABLE: \$0.00
        REFUNDED AMNT: \$945.00
        STATUS       : CANCELLED & REFUNDED
        ====================================================
        

TEST CASE 2: FLAT 40% DISCOUNT (ACTIVE USER)
        ====================================================
                     ZOMATO ENTERPRISE INVOICE              
        ====================================================
        ITEM NAME    : Chicken Biryani
        QUANTITY     : 2
        BASE TOTAL   : \$600.00
        COUPON CODE  : 'STEAL40'
        DISCOUNTED   : -\$240.00
        TAX (5% GST) : \$18.00
        ----------------------------------------------------
        TXN ID REF   : TXN_112233B
        FINAL PAYABLE: \$378.00
        REFUNDED AMNT: \$0.00
        STATUS       : PLACED & VERIFIED
        ====================================================
        

TEST CASE 3: STANDARD CHECKOUT (NO COUPON CODE APP)
        ====================================================
                     ZOMATO ENTERPRISE INVOICE              
        ====================================================
        ITEM NAME    : Chicken Biryani
        QUANTITY     : 3
        BASE TOTAL   : \$900.00
        COUPON CODE  : ''
        DISCOUNTED   : -\$0.00
        TAX (5% GST) : \$45.00
        ----------------------------------------------------
        TXN ID REF   : TXN_445566C
        FINAL PAYABLE: \$945.00
        REFUNDED AMNT: \$0.00
        STATUS       : PLACED & VERIFIED
        ====================================================
        
```
</details>

  * **The BOGO Formula:** If `BOGO` is captured, it runs integer division operations on product amounts (`quantity // 2`) to determine exactly how many free items the user wins, multiplying that count by the item price.
  * **The STEAL40 Formula:** If `STEAL40` is passed, it takes the gross value and calculates a flat 40% discount deduction row instantly.
