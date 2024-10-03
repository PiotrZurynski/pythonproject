#Project: Borderless Tourist
#List of destinations
destinations=["Paris, France","Shanghai, China","Los Angeles, USA","Sao Paulo, Brazil","Cairo, Egypt"]


#variable to test
test_traveler=['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#function to get destination index
def get_destination_index(destination):
    destination_index=destinations.index(destination)
    return destination_index

#Testing
#print(get_destination_index("Los Angeles, USA"))
#print(get_destination_index("Paris, France"))
#print(get_destination_index("Hyderabad, India"))

#function to get traveler location
def get_traveler_location(traveler):
    traveler_destination=test_traveler[1]
    traveler_destination_index=get_destination_index(traveler_destination)
    return traveler_destination_index

#variable for testing function 
test_destination_index=get_traveler_location(test_traveler)
print(test_destination_index)


#defining a list of attractions xd
attractions=[[] for destination in destinations]

#function to add_attractions
def add_attractions(destination,attraction):
    if destination in destinations:
        destination_index=get_destination_index(destination)
        attractions[destination_index].append(attraction)
    else:
        print("Destination not found")
#Added some attractions
add_attractions('Los Angeles, USA',['Venice Beach','beach'])
add_attractions("Paris, France", ["the Louvre", ["art", "museum"]])
add_attractions("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attractions("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attractions("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attractions("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attractions("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attractions("Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attractions("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attractions("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attractions("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#print(attractions)


#Function for finding interesting places
def find_attractions(destination,interests):
    destination_index=get_destination_index(destination)
    attractions_in_city=attractions[destination_index]
    attractions_with_interest=[]
    for attraction in attractions_in_city:
        possible_attraction=attraction
        attraction_tags=attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
                break

    return attractions_with_interest
    
        
        
#testing
print(get_destination_index('Los Angeles, USA'))
#variable for tests
la_arts=find_attractions('Los Angeles, USA',['art'])
print(la_arts)

#defining function to get attractions for traveler
def get_attractions_for_traveler(traveler):
    traveler_destination=traveler[1]
    traveler_interests=traveler[2]
    traveler_attractions=find_attractions(traveler_destination,traveler_interests)
    interests_string="Hi "+traveler[0]+", we think you'll like these places around \n"
    for attract in traveler_attractions:
        interests_string+=attract
    return interests_string

smills_france=get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)

    



