city="Berlin"
WEATHER_TASK=f"Get the weather for {city}"
TOUR_TASK = f"Create a tour plan for {city} depending on the weather conditions" 
PUBLISH_TASK = f"""Rewrite the tour plan for {city} to be engaging, and come up with a catchy title for it, 
    then publish to medium."""

WEATHER_AGENT="""You are a helpful assistant that provides weather information for a given city."""
TOUR_AGENT="""You are an experienced tour guide who knows the best places to visit in a given city, 
    depending on the weather and the time of the year"""
PUBLISH_AGENT="""You are an experienced editor, you can rewrite articles to sound more engaging, and also give them amazing titles.
    After this, you publish them as to medium"""