#Project: Borderless Tourist
#List of destinations
list=["Paris, France","Shanghai, China","Los Angeles, USA","Sao Paulo, Brazil","Cairo, Egypt"]


#variable to test
test_traveler=['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#function to get destination index
def get_destination_index(destination):
    destination_index=list.index(destination)
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



