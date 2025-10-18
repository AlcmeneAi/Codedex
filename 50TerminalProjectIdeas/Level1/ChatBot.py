import random 
import datetime

user_name = ""
reminder_list = []
reminders = []

print("Personal Assistant Bot Starting...")
print("="*50)

def main():
    """Main function to run the chatbot."""
    greet_user()
    
    while True:
        user_input = input(f"{user_name}, how can I assist you? (Type 'help' for options or 'quit' to exit): ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print(f"Goodbye, {user_name}! Have a great day! 👋")
            break
        elif user_input.lower() == 'help':
            show_help()
            continue
        elif not user_input:
            print("Please enter a command or type 'help' for options.")
            continue
        
        response = (get_time_response(user_input) or
                    get_quote_response(user_input) or
                    get_math_response(user_input) or
                    get_weather_response(user_input)
                    )
        
        if response:
            print(response)
        else:
            print("I'm sorry, I didn't understand that. Type 'help' to see what I can do.")


            
def greet_user():
    """Welcome the user and get their name."""
    global user_name

    print("Hello! I'm your Personal Assistant Bot! 🤖")
    print("I'm here to help you with:")
    print("• Time and date information")
    print("• Motivational quotes")
    print("• Basic calculations")
    print("• Weather conversations")
    print("• And much more!")
    print()

    user_name = input("Before we get started, what's your name? ")

    if user_name:
        print(f"Nice to meet you, {user_name}! How can I assist you today?")
    else:
        user_name = "Friend"
        print("No worries! I'll just call you 'Friend'. How can I assist you today?")
    print("Type 'help' to see all available commands or 'quit' to exit.")
    print("-"*50)   

def show_help():
    """Display available commands."""
    print("Here are the commands you can use:")
    print("• time - Get the current time")
    print("• date - Get today's date")
    print("• quote - Receive a motivational quote")
    print("• calc - Perform a basic calculation")
    print("• weather - Talk about the weather")
    print("• help - Show this help message")
    print("• quit - Exit the chatbot")
    print("-"*50)

def get_current_time():
     """Return current time information"""
     now = datetime.datetime.now()
     current_time = now.strftime("%I:%M %p")
     current_date = now.strftime("%B %d, %Y")
     current_day = now.strftime("%A")
    
     return f"Current time: {current_time}\nToday's date: {current_date}\nDay: {current_day}"

def get_time_response(user_input):
    """Handle time-related requests"""
    time_keywords = ['time', 'date', 'day', 'today', 'now', 'current']
    
    if any(keyword in user_input.lower() for keyword in time_keywords):
        return get_current_time()
    return None

def get_motivational_quote():
    """Return a random motivational quote"""
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt", 
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "It is during our darkest moments that we must focus to see the light. - Aristotle",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "Innovation distinguishes between a leader and a follower. - Steve Jobs",
        "Life is what happens to you while you're busy making other plans. - John Lennon"
    ]
    
    return random.choice(quotes)

def get_quote_response(user_input):
    """Handle requests for motivational quotes"""
    quote_keywords = ['quote', 'motivation', 'inspire', 'inspiration', 'motivate', 'encourage']
    
    if any(keyword in user_input.lower() for keyword in quote_keywords):
        return f"Here's some inspiration for you, {user_name}:\n\n{get_motivational_quote()}"
    return None

def calculate_expression(user_input):
    """Handle basic math calculations"""
    try:
        # Extract numbers and operations from input
        if "+" in user_input:
            parts = user_input.split("+")
            if len(parts) == 2:
                num1 = int(parts[0].strip())
                num2 = int(parts[1].strip())
                result = num1 + num2
                return f"{num1} + {num2} = {result}"
                
        elif "-" in user_input:
            parts = user_input.split("-")
            if len(parts) == 2:
                num1 = int(parts[0].strip())
                num2 = int(parts[1].strip())
                result = num1 - num2
                return f"{num1} - {num2} = {result}"
                
        elif "*" in user_input or "x" in user_input.lower():
            parts = user_input.replace("x", "*").split("*")
            if len(parts) == 2:
                num1 = int(parts[0].strip())
                num2 = int(parts[1].strip())
                result = num1 * num2
                return f"{num1} × {num2} = {result}"
                
        elif "/" in user_input:
            parts = user_input.split("/")
            if len(parts) == 2:
                num1 = int(parts[0].strip())
                num2 = int(parts[1].strip())
                if num2 != 0:
                    result = num1 / num2
                    return f"{num1} ÷ {num2} = {result}"
                else:
                    return "Sorry, I can't divide by zero!"
                    
    except (ValueError, IndexError):
        return "I couldn't understand that calculation. Try something like '5 + 3' or '10 * 2'"
    
    return None

def get_math_response(user_input):
    """Handle math-related requests"""
    math_keywords = ['calculate', 'math', 'plus', 'minus', 'times', 'divided']
    math_symbols = ['+', '-', '*', '/', 'x']
    
    if any(keyword in user_input.lower() for keyword in math_keywords) or any(symbol in user_input for symbol in math_symbols):
        result = calculate_expression(user_input)
        if result:
            return result
        else:
            return "I can help with basic math! Try: '5 + 3', '10 - 2', '4 * 7', or '15 / 3'"
    return None

def get_weather_response(user_input):
    """Handle weather-related conversations"""
    weather_keywords = ['weather', 'rain', 'sunny', 'cloudy', 'forecast', 'temperature', 'hot', 'cold']
    
    if any(keyword in user_input.lower() for keyword in weather_keywords):
        responses = [
            "The weather is looking great today! Perfect for a walk outside. 🌞",
            "It might be a bit cloudy today, but don't forget your umbrella just in case! ☁️☔",
            "It's a beautiful sunny day! A great time to enjoy the outdoors. 🌤️",
            "Looks like it could rain later, so keep an eye on the sky! 🌧️",
            "It's quite chilly today, make sure to bundle up if you're heading out! 🧥❄️",
            "The forecast says it's going to be warm and sunny all week! 🌞🌡️"
        ]
        return random.choice(responses)
    return None

# Start the chatbot
if __name__ == "__main__":
    main()