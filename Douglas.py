# -----------------------------------------
# CALCULATION FUNCTIONS
# -----------------------------------------

# add_totals(orders, order_row_numbers):
# Calculates the total for each order by multiplying Price by Quantity.
# Skips rows with invalid data and records the reason why each row was skipped.

# calculate_summary(shown):
# Calculates and returns the total sales, number of orders,
# and average order value from the displayed orders.

# add_up_by(shown, group_column, amount_column):
# Groups the data using a dictionary and adds up the values
# for each group.
# Used to calculate sales by item, identify best sellers,
# and prepare data for the daily sales chart.

# find_best_seller(shown):
# Finds and returns the item with the highest total quantity sold.

# count_orders_per_range(shown):
# Counts the number of orders within each J$500 price range.
# Used to create the order value histogram.
