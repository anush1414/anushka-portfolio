"""
Aggregate Planning Optimization Tool
Linear programming for inventory and workforce planning
"""

import pandas as pd

def optimize_production(demand, holding_cost, overtime_cost):
    """
    Simple optimization calculation
    demand: list of weekly demand
    holding_cost: cost per unit held
    overtime_cost: cost per overtime hour
    """
    
    total_demand = sum(demand)
    avg_demand = total_demand / len(demand)
    
    # Basic heuristic: produce at average demand
    production_plan = [avg_demand] * len(demand)
    
    # Calculate inventory holding
    inventory = 0
    total_holding_cost = 0
    
    for i in range(len(demand)):
        inventory += production_plan[i] - demand[i]
        if inventory < 0:
            inventory = 0  # can't have negative inventory
        total_holding_cost += inventory * holding_cost
    
    results = {
        "total_demand": total_demand,
        "avg_weekly_demand": avg_demand,
        "production_plan": production_plan,
        "total_holding_cost": total_holding_cost
    }
    
    return results

# Sample run
if __name__ == "__main__":
    sample_demand = [100, 120, 110, 130, 125, 115]
    result = optimize_production(sample_demand, holding_cost=2, overtime_cost=50)
    
    print("=" * 40)
    print("OPTIMIZATION RESULTS")
    print("=" * 40)
    print(f"Total Demand: {result['total_demand']}")
    print(f"Avg Weekly Demand: {result['avg_weekly_demand']:.1f}")
    print(f"Total Holding Cost: ${result['total_holding_cost']}")
    print("=" * 40)
