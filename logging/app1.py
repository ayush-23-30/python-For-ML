import logging 

## Logging  Setting 

logging.basicConfig(
  level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
);

logger =logging.getLogger("Arthmethic_App");

def add (a,b):
  result = a+b;
  logger.debug(f'Adding {a} and {b}'); 
  return result

def subtract (a,b):
  result = a-b;
  logger.debug(f'Subtracts {a} and {b}'); 
  return result

def multiply (a,b):
  result = a*b;
  logger.debug(f'Multiplying {a} and {b}'); 
  return result

def Divide (a,b):
  try:
    result = a // b;
    logger.debug(f'Divide {a} and {b}'); 
    return result
  except ZeroDivisionError:
    logger.error('Division By Zero Error'); 
    return None
    




print(add(1,4))
print(subtract(45,534))
print(multiply(3,5))
print(Divide(23,5))
