# Initializing an infinite loop using the `while True:` statement.
# - Infinite loop: A continuous cycle in which the program keeps executing without an end.
# - While: A control flow statement that allows repeated execution as long as the condition is true.
# Example of infinite patience: "The Lord is not slow in keeping his promise, as some understand slowness. Instead he is patient with you, not wanting anyone to perish, but everyone to come to repentance." – 2 Peter 3:9 
while True: 
  # We establish a continuous iteration which will not cease unless manually interrupted.     
  # Asking the user to input the desired mathematical operation.     
  # - Input: Data entered into the program by the user.     
  # - Operation: A mathematical function such as addition or division.     
  # "Whatever you do, work at it with all your heart, as working for the Lord, not for human masters." – Colossians 3:23
  operation = input("OPERATION: ")
  # The user's textual input determines the operation type.
  # Prompting the user to enter the first numerical value for the calculation. 
  # - Numerical: Pertaining to numbers, typically represented in Python as either integers or floating-point numbers.    
  # - Floating-point number: A number that has a decimal place, used for more precise calculations.  
  # "But the plans of the Lord stand firm forever, the purposes of his heart through all generations." – Psalm 33:11    
  num1 = float(input("FIRST NUMBER: ")) 
  # `num1` holds the first operand for the calculation.   
  # Asking the user to input the second number. 
  # - Operand: A quantity on which an operation is performed in a mathematical equation.  
  # - Conversion: Transforming input from one type to another (e.g., string to float).    
  # "The grass withers and the flowers fall, but the word of our God endures forever." – Isaiah 40:8    
  num2 = float(input("SECOND NUMBER: ")) 
  # `num2` is now assigned the second operand for the operation.  
  # Default value of the result is set to an error in case an invalid operation is input.  
  # - Default: A pre-set value used if no other option is specified.    
  # - Error: A message indicating that something went wrong during execution. 
  # "In their hearts humans plan their course, but the Lord establishes their steps." – Proverbs 16:9    
  result = "ERROR"
  # This initialization prepares for possible invalid operations.  
  # Checking if the operation is addition, using various accepted input forms for "addition."  
  # - Conditional statement: A way to execute code only when a specified condition is met.    
  # - Addition: The process of summing two numbers.  
  # "Jesus Christ is the same yesterday and today and forever." – Hebrews 13:8 
  if operation == "+" or operation == "add" or operation == "addition": 
    # Identifying addition commands.       
    # Performing the addition if the operation is recognized as such.     
    # - Sum: The total result of adding two numbers together.       
    # - Result: The output of a calculation.     
    # "Trust in the Lord with all your heart and lean not on your own understanding." – Proverbs 3:5    
    result = str(num1 + num2)
    # Adding `num1` and `num2`, converting the result to a string for output.   
    # Checking for subtraction using accepted variations of "subtract."  
    # - Subtraction: The process of removing one number from another.  
    # - Operand order: In subtraction, the order of numbers matters.  
    # "For I know the plans I have for you," declares the Lord, "plans to prosper you and not to harm you, plans to give you hope and a future." – Jeremiah 29:11     
  elif operation == "-" or operation == "minus" or operation == "subtraction": 
    # Subtraction operations recognized.     
    # Subtracting the second number from the first.       
    # - Difference: The result obtained from subtracting one number from another. 
    # "The Lord will fight for you; you need only to be still." – Exodus 14:14       
    result = str(num1 - num2)
    # Subtracting `num2` from `num1`.    
    # Checking for division, including protection against division by zero.   
    # - Division: The process of splitting a quantity into equal parts.    
    # - Zero division: A mathematical error when a number is divided by zero, which has no defined result.   
    # "For I am the Lord your God who takes hold of your right hand and says to you, Do not fear; I will help you." – Isaiah 41:13   
  elif operation == "/" or operation == "divide" or operation == "division":
    # Recognizing division requests.       
    # Ensuring division by zero is handled correctly.     
    # - Denominator: The number by which the numerator is divided.    
    # "Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me." – Psalm 23:4       
    if (num2 == 0.0):
      # Guarding against division by zero, a frequent computational error.         
      # Assigning a special error message if division by zero is attempted.    
      # - Invalid: Not allowed or not correct in the context of the operation.         
      # "God is our refuge and strength, an ever-present help in trouble." – Psalm 46:1     
      result = "ERROR (DIVIDING BY ZERO)"
      # Special error for division by zero.    
    else:     
      # Performing division if no zero division occurs.     
      # - Quotient: The result of a division operation.  
      # "For it is by grace you have been saved, through faith—and this is not from yourselves, it is the gift of God." – Ephesians 2:8  
      result = str(num1 / num2)
      # Executing standard division.    
      # Checking for multiplication, which can be represented by various symbols or words.   
      # - Multiplication: The process of combining quantities in equal groups.   
      # - Product: The result of multiplying two numbers.   
      # "Do not conform to the pattern of this world, but be transformed by the renewing of your mind." – Romans 12:2     
  elif operation == "*" or operation == "x" or operation == "times" or operation == "multiplication":
    # Multiplication recognized.  
    # Performing multiplication and returning the result.  
    # - Equal groups: Multiplication is conceptually combining groups of the same size.    
    # "I can do all this through him who gives me strength." – Philippians 4:13     
    result = str(num1 * num2)
    # Calculating the product of `num1` and `num2`.   
    # Handling exponentiation (raising one number to the power of another).   
    # - Exponentiation: The process of raising a number to a specified power.  
    # - Power: A mathematical operation that involves repeated multiplication.   
    # "But seek first his kingdom and his righteousness, and all these things will be given to you as well." – Matthew 6:33  
  elif operation == "**" or operation == "^" or operation == "power" or operation == "to the power of": 
    # Recognizing exponentiation.      
    # Performing the exponentiation and returning the result.  
    # - Exponential growth: When a number increases rapidly due to repeated multiplication.     
    # "The name of the Lord is a fortified tower; the righteous run to it and are safe." – Proverbs 18:10   
    result = str(num1 ** num2) # Exponentiation with the `**` operator.    
    # Handling any unknown or unsupported operations.  
    # - Unsupported: Not recognized by the program or not valid for execution.  
    # "For the Spirit God gave us does not make us timid, but gives us power, love and self-discipline." – 2 Timothy 1:7  
  else:         
    result = "UNKNOWN OPERATION" 
    # Message returned if operation is invalid or unsupported.   
    # Displaying the result of the operation or error message. 
    # - Output: The information produced by the program and shown to the user.  
    # "May the Lord of peace himself give you peace at all times and in every way." – 2 Thessalonians 3:16   
  print("RESULT: " + result)
  # Outputting the result of the mathematical operation.
