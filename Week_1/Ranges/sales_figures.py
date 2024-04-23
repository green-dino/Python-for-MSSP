sales_figures = [1200, 1500, 1800, 1300, 1600, 1700, 1400, 1900, 2000, 2200]
print("Sales Report:")
for i in range(len(sales_figures)):
    if sales_figures[i] % 2 == 0:
        print(f"Day {i+1}: ${sales_figures[i]} (Even)")
    else:
        print(f"Day {i+1}: ${sales_figures[i]} (Odd)")
