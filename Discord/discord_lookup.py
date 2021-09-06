from datetime import datetime

def main():
    user_id = input("Enter your discord id: ")
    print(convert_id_to_date(user_id))
    
def convert_id_to_date(user_id):
    try:
        binary = f"{int(user_id):b}"
        unix_binary = binary[0: len(binary)-22]
        timestamp = (int(unix_binary, 2) + 1420070400000)//1000
        date = datetime.fromtimestamp(timestamp)   
        return f"The creation date of {user_id} is {date}"
    except:
        return "An exception occurred because of invalid input."
    
if __name__ == "__main__":
    main()
