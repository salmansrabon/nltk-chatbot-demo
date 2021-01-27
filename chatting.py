from datetime import datetime

from load_model import response

while True:
    try:

        query = input('Me:')
        if "what time" in query:
            current_time=datetime.now()
            print(current_time)
        else:
            response(query)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break