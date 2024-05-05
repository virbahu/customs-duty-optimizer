import numpy as np
def calculate_customs_duty(hs_code, origin, value, fta_eligible=False, duty_rate=0.05, fta_rate=0.0):
    effective_rate = fta_rate if fta_eligible else duty_rate
    duty = value * effective_rate
    savings = value * (duty_rate - effective_rate) if fta_eligible else 0
    mpf = min(max(value * 0.003464, 31.67), 614.35)
    total = duty + mpf
    return {"duty": round(duty, 2), "mpf": round(mpf, 2), "total_landed": round(total, 2), "fta_savings": round(savings, 2), "effective_rate_pct": round(effective_rate*100, 2)}
if __name__=="__main__":
    print(calculate_customs_duty("8471.30", "MX", 50000, True, 0.05, 0.0))
    print(calculate_customs_duty("8471.30", "CN", 50000, False, 0.25))
