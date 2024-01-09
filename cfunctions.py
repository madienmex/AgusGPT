import json
import os
#custom python methods for chatbot

#function definition
schema = [
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        },
        #my own
        {
            "name": "get_last_name",
            "description": "Last Name for a person named Agustin exclusively",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The Last Name for a person named Agustin exclusively",},
                },
                "required": ["name"],
            },
        }
    ]

# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)

def get_last_name(name):
    """The Last Name for a person named Agustin"""
    name_info = {
        "name": name,
        "last name": "Gonzalez",
    }
    return json.dumps(name_info)

available_functions = {
            "get_current_weather": get_current_weather,
            "get_last_name": get_last_name,
        }  # available functions

#available_functions = {
#            "get_current_weather": cf.get_current_weather,
#            "get_last_name": cf.get_last_name,
#        }  # available functions

#Function Count
def fun_count():
    return len(schema);