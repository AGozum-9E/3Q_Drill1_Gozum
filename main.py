# Collecting and Displaying Data
from pyscript import display, document

def collecting_data(e):
    document.getElementById('Output').innerHTML = ""
    first= document.getElementById("First").value
    last = document.getElementById("Last").value
    sci = float(document.getElementById("Science").value)
    eng= float(document.getElementById("English").value)
    fil = float(document.getElementById("Filipino").value)
    math = float(document.getElementById("Math").value)
    ict = float(document.getElementById("Computer").value)
    pe = float(document.getElementById("PhysHealth").value)


    display(f'NAME: {first} {last}')
    display(f'SCIENCE:{sci}') 
    display(f'ENGLISH:{eng}') 
    display(f'FILIPINO:{fil}') 
    display(f'MATH:{math}') 
    display(f'ICT:{ict}') 
    display(f'PE:{pe}') 

    display(f'Your General Weighted Average is: {(sci + eng + fil + math + ict + pe) / 6}') 


    result = int(document.getElementById('result').value)
    if result > 74:
        display(f'You passed', target='Output')
    else:
        display(f'You failed', target='Output')