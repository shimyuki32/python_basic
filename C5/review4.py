from itertools import product


letter = """Dear {salutation} {name}
Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never 
be used in a {room}, especially near any {animals}.

Send us you rreceipt and {amount} for shipping and handling.
We will send you another {product} that, in ourt tests,
is {percent}% less likely to have {verbed}.
Thank you for your support.

Sincerely,
{spokesman}
{job_title}
"""

print(letter)
print(letter.format(salutation = 'Mr',
                    name = 'Haru', 
                    product = 'oven',
                    verbed = 'broken', 
                    room= 'apartment', 
                    animals = 'cat', 
                    amount = '30 dollars',
                    percent = '20', 
                    spokesman = 'shimizu', 
                    job_title = 'CEO'))
