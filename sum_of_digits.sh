echo "Enter a number:"
read number

# Initialize sum to 0
sum=0

# Loop through each digit
while [ $number -gt 0 ]; do
  # Extract the last digit
  digit=$((number % 10))
  # Add the digit to the sum
  sum=$((sum + digit))
  # Remove the last digit
  number=$((number / 10))
done

# Display the result
echo "The sum of the digits is: $sum"
