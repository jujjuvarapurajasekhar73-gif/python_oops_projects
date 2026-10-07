# =====================================================================
# 1. CORE ENTERPRISE EMPLOYEE TEMPLATE INTERFACE (PARENT CLASS)
# =====================================================================

class Employee:
    def __init__(self, emp_id: int, name: str, basic_salary: float, leaves_taken: int = 0) -> None:
        """
        Initializes the base employee profile with identification and basic salary configuration.
        """
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        self.leaves_taken = leaves_taken

    @staticmethod
    def calculate_pf(basic_salary: float) -> float:
        """
        Static Component: Computes the standard 12% Provident Fund deduction from base salary.
        """
        return basic_salary * 0.12

    def salary_increment(self, percentage: float) -> None:
        """
        Applies a percentage-based increment to update the employee's basic salary.
        """
        self.basic_salary += self.basic_salary * percentage

    def __str__(self) -> str:
        """
        Magic Method: Automatically renders a professional corporate salary slip format.
        """
        return f"""
        ====================================================
                    ENTERPRISE CORPORATE SALARY SLIP        
        ====================================================
        EMPLOYEE ID : {self.emp_id}
        NAME        : {self.name}
        NET PAYOUT  : ${self.calculate_net_salary():.2f}
        STATUS      : PROCESSED & VERIFIED
        ====================================================
        """


# =====================================================================
# 2. SUBCLASS IMPLEMENTATION: FIXED FULL-TIME PERSONNEL PROTOCOLS
# =====================================================================

class FullTimeEmployee(Employee):
    def __init__(self, emp_id: int, name: str, basic_salary: float, leaves_taken: int = 0, bonus: float = 0.0) -> None:
        """
        Initializes a full-time employee with a base salary, leaves, and monthly bonus configurations.
        """
        super().__init__(emp_id, name, basic_salary, leaves_taken)
        self.bonus = bonus

    def calculate_net_salary(self) -> float:
        """
        Enforces corporate payroll logic including HRA allowances, LOP leave cuts, PF tracking, and tax deductions.
        """
        hra = self.basic_salary * 0.20
        
        # Loss of Pay logic assessing standard leave allowances
        if self.leaves_taken > 2:
            lop_cut = (self.basic_salary / 30) * (self.leaves_taken - 2)
        else:
            lop_cut = 0.0

        gross_salary = self.basic_salary + hra + self.bonus - lop_cut
        
        # Invoking static parent operations alongside flat localized tax calculations
        pf_deduction = Employee.calculate_pf(self.basic_salary)
        tax_deduction = gross_salary * 0.10
        
        return gross_salary - pf_deduction - tax_deduction


# =====================================================================
# 3. SUBCLASS IMPLEMENTATION: VARIABLE HOURLY CONTRACTOR PROTOCOLS
# =====================================================================

class ContractorEmployee(Employee):
    def __init__(self, emp_id: int, name: str, hours_worked: int, hourly_rate: float) -> None:
        """
        Initializes a contractor employee with hourly wage and time tracking metrics.
        """
        super().__init__(emp_id, name, basic_salary=0.0)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_net_salary(self) -> float:
        """
        Computes the hourly payroll logic and applies a flat 10% tax deduction on total earnings.
        """
        gross_earnings = self.hours_worked * self.hourly_rate
        tax_deduction = gross_earnings * 0.10
        return gross_earnings - tax_deduction


# =====================================================================
# 4. AUTOMATED payroll WORKFLOW INTEGRATION SUITE
# =====================================================================

def run_corporate_payroll_tests() -> None:
    """
    Executes automation test cases to verify the production pipeline execution.
    """
    print("--- Starting Production Payroll Processing Engine ---")

    # Case 1: Ingesting a Full-Time instance profile with custom parameter sets
    emp1 = FullTimeEmployee(101, "Raja", 50000.0, leaves_taken=5, bonus=5000.0)
    emp1.salary_increment(0.10)
    print(emp1)

    # Case 2: Ingesting a Contractor instance tracking pure dynamic hourly assets
    emp2 = ContractorEmployee(102, "Surya", hours_worked=160, hourly_rate=50.0)
    print(emp2)


# =====================================================================
# 5. SYSTEM RUNTIME ENTRY POINT
# =====================================================================

if __name__ == "__main__":
    run_corporate_payroll_tests()
