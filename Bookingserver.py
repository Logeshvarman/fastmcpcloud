from fastmcp import FastMCP
from serpapi import google_search
from dotenv import load_dotenv
from os import getenv
from pathlib import Path
load_dotenv()

mcp = FastMCP("Booking_Server")

@mcp.tool
def findFlights(departureAirportCode: str,
                arrivalAirportCode: str,
                departureDate: str,
                ) -> dict:

    """
    departureAirportCode: str -> Must be the valid airport id for the given city
    arrivalAirportCode: str -> Must be the valid airportid for the given city
    departureDate: str -> Format: YYYY-MM-DD

    Example if departing airport is Chennai, code is MAA
    if Hyderabad, code is HYD 

            """
    params = {
    "engine": "google_flights",
    "departure_id": departureAirportCode,
    "arrival_id": arrivalAirportCode,
    "outbound_date": departureDate,
    "currency": "INR",
    "hl": "en",
    "type": "2",
    "api_key": getenv("SERP_API")
    }

    search = google_search.GoogleSearch(params)
    results = search.get_dict()
    return results

@mcp.tool
def bookFlight(flightId:str, date:str) -> dict:
    """
    flightId:str -> FlightID of the flight the user wants to book
    Date:str -> Date on which the user wants to travel
    """

    return {
        "FlightID" : flightId,
        "Confirmation_Status": "Confirmed",
        "Booking_ID": "UV123FD"
    }


@mcp.tool
def find_cabs(pickup_location: str) -> dict:
    """
    Searches for available cab/taxi services near the pickup location.
    
    Args:
        pickup_location: city or exact location (example: 'Chennai Airport', 'London Heathrow')
    """

    params = {
        "engine": "google",
        "q": f"cab taxi service near {pickup_location}",
        "location": pickup_location,
        "hl": "en",
        "api_key": getenv("SERP_API")
    }

    search = google_search.GoogleSearch(params)
    results = search.get_dict()   

    return {
        "pickup_location": pickup_location,
        "cab_results": results
    }


@mcp.tool
def book_cab(pickup_location: str, dropoff_location: str, pickup_time: str) -> dict:
    """
    Books a cab from point A to point B at a specific time.
    """

    booking_id = "CAB-998877"

    return {
        "status": "SUCCESS",
        "message": f"Cab booked from {pickup_location} to {dropoff_location}",
        "driver_name": "Dave",
        "pickup_time": pickup_time,
        "booking_reference": booking_id
    }


@mcp.tool
def findHotels(location:str,
               checkinDate: str,
               checkoutDate:str,
               noOfAdults:int,

               ) -> dict:
    
    """
    Tool which is used to find hotels

    location:str -> City/Town which the user is visiting
    checkinDate: str -> Format: YYYY-MM-DD
    checkoutDate: str -> Format: YYYY-MM-DD
    noOfAdults:int -> No of people traveling
    """
    params = {
        "engine": "google_hotels",
        "q": location,
        "check_in_date": checkinDate,
        "check_out_date": checkoutDate,
        "adults": noOfAdults,
        "currency": "INR",
        "hl": "en",
        "api_key": getenv("SERP_API")
        }
    
    search = google_search.GoogleSearch(params)
    results = search.get_dict()
    return results

@mcp.tool
def bookHotel(
        hotelName:str,
        checkinDate: str,
        checkoutDate:str,
        noOfAdults:int,
) -> dict:
    
    """
    Tool which is used to book hotel
    
    hotelName: str -> Name of the hotel
    checkinDate: str -> Format: YYYY-MM-DD
    checkoutDate: str -> Format: YYYY-MM-DD
    noOfAdults:int -> No of people traveling
    """
    return {
        "hotelName": hotelName,
        "checkinDate": checkinDate,
        "checkoutDate": checkoutDate,
        "noOfAdults": noOfAdults,
        "bookingStatus": "Confirmed",
        "bookingID": "GHN1234"
    }

if __name__ == "__main__":
   mcp.run(transport="streamable-http",host="0.0.0.0", port=8003)
