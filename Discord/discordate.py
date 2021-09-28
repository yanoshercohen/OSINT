from datetime import datetime

def main():
    user_id = input("Enter your Discord ID: ")
    if user_id.isdecimal():
        try:
            print(convert_id_to_date(user_id))
        except ValueError as e:
            print(e)
    else:
        print(f"Discord ID \"{user_id}\" is not valid.")
   
def convert_id_to_date(user_id):
    timestamp = ((int(user_id) >> 22) + 1420070400000)//1000
    if not 0 <= timestamp <= 32536799999:
        raise ValueError(f'Discord ID "{user_id}" is not valid.')
    return f'The creation date of "{user_id}" is {datetime.fromtimestamp(timestamp)}'
    
if __name__ == "__main__":
    main()
