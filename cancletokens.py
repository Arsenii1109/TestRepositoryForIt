from cantok import TimeoutToken
import time

import random

def operation_with_timeout(token):
    try:
        while token:
            print("Performing operation...")
            time.sleep(0.5)
    except Exception as e:
        print(f"Operation interrupted: {e}")
    finally:
        print("Operation finished.")

if __name__ == "__main__":
    token = TimeoutToken()

    token.cancel()
    
    operation_with_timeout(token)
    random.randint(1, 10)
