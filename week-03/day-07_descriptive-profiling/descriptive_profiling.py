import pandas as pd
import matplotlib.pyplot as plt

sales = pd.DataFrame({
    "customer": ["Alice", "Bob", "Alice", "Carol", "Bob", "David", "Carol", "Alice"],
    "category": ["Racket", "Shoes", "Shoes", "Racket", "Racket", "Shoes", "Shoes", "Racket"],
    "amount": [180, 120, 95, 210, 160, 130, 110, 220],
    "rating": [5, 4, 4, 5, 3, 4, 5, 5]
})

# histogram
def plot_sales_histogram(sales):
    sales['amount'].plot(kind='hist', bins=10, color='blue', edgecolor='black', alpha=0.7)
    plt.title('Sales Amount Distribution')
    plt.xlabel('Amount')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig("week-03/day-07_descriptive-profiling/amount_histogram.png")
    plt.close()

plot_sales_histogram(sales)

def plot_sales_bar_chart(sales):
    category_sales = sales.groupby("category")["amount"].sum()
    category_sales.plot(kind='bar', color='green', edgecolor='black', alpha=0.7)
    plt.title('Total Sales by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Sales Amount')
    plt.tight_layout()
    plt.savefig("week-03/day-07_descriptive-profiling/category_sales.png")
    plt.close()

plot_sales_bar_chart(sales)

def scatter_plot_sales(sales):
    plt.scatter(sales['amount'], sales['rating'], color='red', alpha=0.7)
    plt.title('Sales Amount vs Rating')
    plt.xlabel('Amount')
    plt.ylabel('Rating')
    plt.tight_layout()
    plt.savefig("week-03/day-07_descriptive-profiling/amount_vs_rating.png")
    plt.close()

scatter_plot_sales(sales)
