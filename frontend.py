import streamlit as st
from app.app import Calculator

# Initialize calculator
calc = Calculator()

# App title
st.title("🧮 Simple Calculator App")
st.write("A small Streamlit frontend for Calculator.")

# Select operation
operation = st.selectbox(
    "Choose an operation",
    ("Add", "Subtract", "Multiply", "Divide", "Square Root")
)

# Input fields
try:
    if operation == "Square Root":
        a = st.number_input("Enter a number", value=0.0)

        if st.button("Compute"):
            result = calc.sqrt(a)
            st.success(f"Result: {result}")

    else:
        a = st.number_input("Enter first number", value=0.0)
        b = st.number_input("Enter second number", value=0.0)

        if st.button("Compute"):
            if operation == "Add":
                result = calc.add(a, b)
            elif operation == "Subtract":
                result = calc.subtract(a, b)
            elif operation == "Multiply":
                result = calc.multiply(a, b)
            elif operation == "Divide":
                result = calc.divide(a, b)

            st.success(f"Result: {result}")

except ValueError as e:
    st.error(str(e))
