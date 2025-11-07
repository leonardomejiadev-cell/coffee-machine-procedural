# ☕ Coffee Machine - Procedural Version

A coffee machine simulator built with Python using procedural programming. This project demonstrates fundamental programming concepts including functions, dictionaries, control flow, and resource management.

## 🎯 Project Overview

This is a command-line coffee machine simulator that manages inventory, processes payments, and dispenses three types of coffee drinks. Built entirely with procedural programming using functions and dictionaries.

## ✨ Features

- **Three Coffee Options**: Espresso, Latte, and Cappuccino
- **Resource Management**: Tracks water, milk, and coffee inventory
- **Payment Processing**: Accepts coins (quarters, dimes, nickels, pennies) and calculates change
- **Resource Validation**: Checks ingredient availability before making drinks
- **Financial Tracking**: Monitors machine profits
- **Maintenance Commands**: Secret commands for staff (`off`, `report`)
- **Input Validation**: Handles invalid user selections

## 🛠️ Technologies Used

- Python 3.x
- Procedural Programming
- Dictionary data structures
- Functions with clear separation of concerns

## 📂 Project Structure

```
coffee-machine-procedural/
├── main.py       # Complete program in a single file
└── README.md     # Project documentation
```

## 🚀 How to Run

1. Ensure you have Python 3.x installed
2. Download or clone this repository
3. Navigate to the project directory
4. Run the program:
```bash
python main.py
```

## 💡 Usage Example

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.5 in change.
Here is your latte ☕️. Enjoy!
```

### Commands:
- `espresso` - Order an espresso ($1.50)
- `latte` - Order a latte ($2.50)
- `cappuccino` - Order a cappuccino ($3.00)
- `report` - Display current resources and money (maintenance)
- `off` - Turn off the machine (maintenance)

## 🏗️ Code Architecture

### Data Structures

**MENU Dictionary:**
- Stores all available drinks with their ingredients and costs
- Nested dictionary structure for easy access

**resources Dictionary:**
- Tracks current inventory levels
- Updated after each successful order

### Functions

| Function | Purpose |
|----------|---------|
| `run_coffee_machine()` | Main program loop and user input handler |
| `turn_off_machine()` | Gracefully shuts down the machine |
| `print_report()` | Displays resource levels and profit |
| `process_order()` | Orchestrates the order workflow |
| `check_resources()` | Validates ingredient availability |
| `process_coins()` | Handles coin insertion and calculates total |
| `is_transaction_successful()` | Verifies payment and processes transaction |
| `make_coffee()` | Deducts resources and dispenses drink |

## 📊 Recipe Details

| Drink | Water | Milk | Coffee | Cost |
|-------|-------|------|--------|------|
| Espresso | 50ml | 0ml | 18g | $1.50 |
| Latte | 200ml | 150ml | 24g | $2.50 |
| Cappuccino | 250ml | 100ml | 24g | $3.00 |

## 📚 What I Learned

- **Procedural Programming**: Organizing code with functions for specific tasks
- **Data Structures**: Using dictionaries to represent complex data
- **Control Flow**: Implementing loops and conditionals for program logic
- **Input Validation**: Handling user input and edge cases
- **Resource Management**: Tracking and updating inventory programmatically
- **Function Design**: Creating reusable functions with clear purposes
- **Python Best Practices**: Using docstrings and the `if __name__ == "__main__"` pattern

## 💪 Programming Concepts Demonstrated

- ✅ Functions with clear single responsibilities
- ✅ Global and local variable scope management
- ✅ Dictionary manipulation and nested data structures
- ✅ While loops for continuous program execution
- ✅ Conditional logic with if/elif/else
- ✅ String formatting and user interaction
- ✅ Mathematical calculations (payment processing)
- ✅ Boolean logic for validation

## 🔄 Evolution

This project was later refactored using Object-Oriented Programming (OOP) principles. Check out the OOP version to see how the same functionality can be implemented with classes and objects:

**[Coffee Machine - OOP Version](https://github.com/leonardomejiadev-cell/coffee-machine-oop)**

The OOP version demonstrates improved code organization, better maintainability, and enhanced scalability.

## 🎓 Learning Context

This project is part of my journey through Angela Yu's "100 Days of Code: The Complete Python Pro Bootcamp" - specifically Day 15, focusing on building a solid foundation in procedural programming before advancing to OOP concepts.

## 👤 Author

**Leonardo Mejia**
- GitHub: [@leonardomejiadev-cell](https://github.com/leonardomejiadev-cell)
- Learning Journey: 100 Days of Code - Python

## 📝 Notes

- This is a learning project demonstrating fundamental programming concepts
- The code prioritizes clarity and understanding over optimization
- All functions include docstrings for documentation
- Ingit --versionput validation ensures a smooth user experience

## 🙏 Acknowledgments

- Project requirements from Angela Yu's Python Course
- Built as part of Day 15 - Intermediate Python module
