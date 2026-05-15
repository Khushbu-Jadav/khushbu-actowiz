import json
import jmespath
import re
from datetime import datetime
from rich import print
from pydantic import BaseModel
from typing import List,Optional

flight_code = {
        "6E": "IndiGo",
        "AI": "Air India",
        "QP": "AkasaAir",
        "SG": "SpiceJet",
        "IX": "Air India Express"
    }
class FlightDetails(BaseModel):
    flight_id: str
    flight_name: str
    airline_class: str
    departure_date: str
    departure_from: str
    arrival_to: str
    departure_time: str
    arrival_time: str
    time_duration: str
    total_duration: List[str]
    snfa_price: int
    stfa_price: int
    stops: List[str]
    departure_terminal: str
    arrival_terminal: str


class NextFlightDetails(BaseModel):
    next_flight_id: Optional[str] = None
    next_flight_name: Optional[str] = None
    next_airline_class: Optional[str] = None
    next_departure_from: Optional[str] = None
    next_arrival_to: Optional[str] = None
    next_departure_time: Optional[str] = None
    next_arrival_time: Optional[str] = None
    next_time_duration: Optional[str] = None
    next_departure_terminal: Optional[str] = None
    next_arrival_terminal: Optional[str] = None

class FlightInformation(BaseModel):
    total_base_far: int
    tax: int
    total: int

class Flight(BaseModel):
    flight_details: FlightDetails
    next_flight_details: Optional[NextFlightDetails] = None
    flight_information: FlightInformation

with open(r"C:\python practice\day10\easemytrip.json","r",encoding='utf-8') as f:
    data = json.load(f)

    res_data = []

    flight_data = jmespath.search("j[0].s[*]", data)
   
    for index,flights in enumerate(flight_data):

        d = flights["segMatchingKey"]
        flight_index = jmespath.search('b[0].FL[*]', flights)

        date_pattern = re.search(r'(\w{3}-\d{2}\w{7})', d)
        matches = re.search(r'^([A-Z]{3})([A-Z]{3})(\w{3}-\d{2}\w{7})(\d{2}:\d{2})(\d{2}:\d{2})', d)
        departure_from = matches.group(1)
        arrival_to = matches.group(2)
        departure_time = matches.group(4)
        arrival_time = matches.group(5)
        time_duration = str(datetime.strptime(arrival_time, "%H:%M") - datetime.strptime(departure_time, "%H:%M") )
        departure_date = date_pattern.group(1)
        departure_terminal = jmespath.search(f'dctFltDtl."{flight_index[0]}".DTER', data)
        arrival_terminal = jmespath.search(f'dctFltDtl."{flight_index[0]}".ATER', data) 
       
        duration = jmespath.search("b[*].JyTm", flights)
        stops = jmespath.search("b[*].BDT", flights)
        id=jmespath.search("segKeyArr[0]",flights)
        flight_id=id[29:]
        snfa=jmespath.search("lstFr[0].SNFA",flights)
        stfa=jmespath.search("lstFr[0].STFA",flights)
        airline_class=jmespath.search("lstFr[0].CB",flights)
        next_departure_terminal = ""
        next_arrival_terminal = ""
        next_time_duration = None
        if len(flight_index) == 2:
            next_departure_terminal = jmespath.search(f'dctFltDtl."{flight_index[1]}".DTER', data) 
            next_arrival_terminal = jmespath.search(f'dctFltDtl."{flight_index[1]}".ATER', data) 

        id2=jmespath.search("segKeyArr[1]",flights)
        next_airline_class=jmespath.search("lstFr[0].CB",flights)
        flight_id2=id2[29:] if id2 else None
        route=jmespath.search("b[0].CT",flights)
        parts = route.split("-")
        next_from = parts[1] if len(parts) > 1 else None
        next_to = parts[2] if len(parts) > 2 else None
        next_dep_time=id2[19:24] if id2 else None
        next_arr_time=id2[24:29] if id2 else None
        if next_dep_time and next_arr_time:
            next_time_duration = str(datetime.strptime(next_arr_time, "%H:%M") - datetime.strptime(next_dep_time, "%H:%M"))
            
        total_base_far=jmespath.search("AP",flights)
        tax=jmespath.search("APT",flights)
        total=jmespath.search("PT",flights)
        
        # flight_data ={
        #     "flight_details": {
        #     "flight_id": flight_id,
        #     "flight_name": flight_code.get(flight_id[:2]),
        #     "airline_class":airline_class,
        #     "departure_date": departure_date,
        #     "departure_from": departure_from,
        #     "arrival_to": arrival_to,
        #     "departure_time": departure_time,
        #     "arrival_time": arrival_time,
        #     "time_duration":time_duration,
        #     "total_duration": duration,
        #     "snfa_price": snfa,
        #     "stfa_price": stfa,
        #     "stops": stops,
        #     "departure_terminal":"no terminal data given" if departure_terminal == "" else 'Terminal - ' + departure_terminal,
        #     "arrival_teminal":"no terminal data given" if arrival_terminal == "" else 'Terminal - ' + arrival_terminal
        # },
        #     "next_flight_details":
        #     {
        #         "next_flight_id":flight_id2,
        #         "next_flight_name": "no flight" if not flight_id2 else flight_code.get(flight_id2[:2]),
        #         "next_airline_class":next_airline_class,
        #         "next_departure_from":next_from,
        #         "next_arrival_to":next_to,
        #         "next_departure_time":next_dep_time,
        #         "next_arrival_time":next_arr_time,
        #         "next_time_duration":next_time_duration,
        #         "next_departure_terminal":"no terminal data given" if next_departure_terminal == "" else 'Terminal - ' + next_departure_terminal,
        #         "next_arrival_terminal": "no terminal data given" if next_arrival_terminal == "" else 'Terminal - ' + next_arrival_terminal
        #     } if flight_id2 else {},
        #         "flight_information": {
        #         "total_base_far": total_base_far,
        #         "tax": tax,
        #         "total": total
        #         }
            
        # }








        flight_obj =Flight(
            flight_details= FlightDetails(

            flight_id= flight_id,
            flight_name=flight_code.get(flight_id[:2]),
            airline_class=airline_class,
            departure_date= departure_date,
            departure_from=departure_from,
            arrival_to= arrival_to,
            departure_time= departure_time,
            arrival_time= arrival_time,
            time_duration=time_duration,
            total_duration= duration,
            snfa_price= snfa,
            stfa_price= stfa,
            stops=stops,
            departure_terminal=("no terminal data given" if departure_terminal == "" else 'Terminal - ' + departure_terminal),
            arrival_terminal=("no terminal data given" if arrival_terminal == "" else 'Terminal - ' + arrival_terminal)
            ),
        next_flight_details=(
            NextFlightDetails(
                next_flight_id=flight_id2,
                next_flight_name= ("no flight" if not flight_id2 else flight_code.get(flight_id2[:2])),
                next_airline_class=next_airline_class,
                next_departure_from=next_from,
                next_arrival_to=next_to,
                next_departure_time=next_dep_time,
                next_arrival_time=next_arr_time,
                next_time_duration=next_time_duration,
                next_departure_terminal=("no terminal data given" if next_departure_terminal == "" else 'Terminal - ' + next_departure_terminal),
                next_arrival_terminal= ("no terminal data given" if next_arrival_terminal == "" else 'Terminal - ' + next_arrival_terminal)
             ) if flight_id2 else {}),
        flight_information=FlightInformation (
                total_base_far= total_base_far,
                tax= tax,
                total= total
            )
        
        )

        res_data.append(flight_obj.model_dump())

print(res_data)


with open(r"C:\python practice\day10\mynew_easemytrip.json","w",encoding='utf-8') as f:
    json.dump(res_data,f,indent=4)







