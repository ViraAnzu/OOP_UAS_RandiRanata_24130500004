import datetime
from abc import ABC, abstractmethod

class Club:
    def __init__(self, club_id: str, name: str, founding_date: datetime.date, tagline: str):
        self.__club_id = club_id
        self.__name = name
        self.__founding_date = founding_date
        self.__tagline = tagline
        self.__sponsors = []  
        self.__teams = []    
        self.__staff = []     

    def add_sponsor(self, sponsor):
        self.__sponsors.append(sponsor)

    def add_team(self, team):
        self.__teams.append(team)

    def add_staff(self, staff_member):
        self.__staff.append(staff_member)

    def get_club_info(self):
        return f"Club ID: {self.__club_id}, Name: {self.__name}, Founded: {self.__founding_date}, Tagline: {self.__tagline}"

class Sponsor:
    def __init__(self, sponsor_id: str, name: str, phone: str, email: str, contact_name: str, contract_start_date: datetime.date, contract_end_date: datetime.date):
        self.__sponsor_id = sponsor_id
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__contact_name = contact_name
        self.__contract_start_date = contract_start_date
        self.__contract_end_date = contract_end_date

    def renew_contract(self, new_end_date: datetime.date):
        self.__contract_end_date = new_end_date

class Team:
    def __init__(self, team_id: str, name: str, division: str, founding_date: datetime.date, team_type: str):
        self.__team_id = team_id
        self.__name = name
        self.__division = division
        self.__founding_date = founding_date
        self.__team_type = team_type  
        self.__players = []           
        self.__coaches = []           
        self.__training_sessions = [] 

    def add_player(self, player):
        self.__players.append(player)

    def add_coach(self, coach):
        self.__coaches.append(coach)

    def add_training_session(self, session):
        self.__training_sessions.append(session)

    def get_team_info(self):
        return f"Team ID: {self.__team_id}, Name: {self.__name}, Division: {self.__division}, Type: {self.__team_type}"

class TrainingSession:
    def __init__(self, session_id: str, session_date: datetime.date, start_time: str, end_time: str, location: str, team_id: str):
        self.__session_id = session_id
        self.__session_date = session_date
        self.__start_time = start_time
        self.__end_time = end_time
        self.__location = location
        self.__team_id = team_id  
        self.__coaches = []       
        self.__players = []      

    def add_coach_participant(self, coach):
        self.__coaches.append(coach)

    def add_player_participant(self, player):
        self.__players.append(player)

    def record_attendance(self, player, present: bool):
        pass

class Match:
    def __init__(self, match_id: str, match_date: datetime.date, match_time: str, location: str, home_team_score: int, away_team_score: int, home_team_id: str, away_team_id: str, season_id: str):
        self.__match_id = match_id
        self.__match_date = match_date
        self.__match_time = match_time
        self.__location = location
        self.__home_team_score = home_team_score
        self.__away_team_score = away_team_score
        self.__home_team_id = home_team_id  
        self.__away_team_id = away_team_id  
        self.__season_id = season_id      

    def record_score(self, home_score: int, away_score: int):
        self.__home_team_score = home_score
        self.__away_team_score = away_score

    def generate_report(self):
        pass

class Season:
    def __init__(self, season_id: str, year: int, start_date: datetime.date, end_date: datetime.date, league_name: str):
        self.__season_id = season_id
        self.__year = year
        self.__start_date = start_date
        self.__end_date = end_date
        self.__league_name = league_name
        self.__matches = []  

    def add_match(self, match):
        self.__matches.append(match)

    def get_standings(self):
        pass

class Stadium:
    def __init__(self, stadium_id: str, name: str, location: str, capacity: int):
        self.__stadium_id = stadium_id
        self.__name = name
        self.__location = location
        self.__capacity = capacity

    def check_availability(self, date: datetime.date, time: str):
        pass

    def rent_stadium(self, date: datetime.date, time: str):
        pass

class Contract:
    def __init__(self, contract_id: str, start_date: datetime.date, end_date: datetime.date, salary: float, position: str, class_name: str, person_id: str):
        self.__contract_id = contract_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__salary = salary
        self.__position = position
        self.__class_name = class_name  
        self.__person_id = person_id    

    def renew_contract(self, new_end_date: datetime.date, new_salary: float):
        self.__end_date = new_end_date
        self.__salary = new_salary

    def terminate_contract(self):
        pass


class Person(ABC): 
    def __init__(self, person_id: str, first_name: str, last_name: str, date_of_birth: datetime.date, nationality: str):
        self._person_id = person_id 
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._nationality = nationality
        self.__contracts = []  

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

    def add_contract(self, contract):
        self.__contracts.append(contract)

    @abstractmethod
    def get_role_details(self):
        """Abstract method to get role-specific details."""
        pass

class Player(Person):
    def __init__(self, person_id: str, first_name: str, last_name: str, date_of_birth: datetime.date, nationality: str, player_id: str, position: str, status: str, jersey_number: int):
        super().__init__(person_id, first_name, last_name, date_of_birth, nationality)
        self.__player_id = player_id
        self.__position = position  
        self.__status = status      
        self.__jersey_number = jersey_number

    def play_match(self):
        print(f"{self.get_full_name()} is playing a match.")

    def get_role_details(self):
        return f"Player ID: {self.__player_id}, Position: {self.__position}, Jersey: {self.__jersey_number}, Status: {self.__status}"

class Coach(Person):
    def __init__(self, person_id: str, first_name: str, last_name: str, date_of_birth: datetime.date, nationality: str, coach_id: str, coach_type: str):
        super().__init__(person_id, first_name, last_name, date_of_birth, nationality)
        self.__coach_id = coach_id
        self.__coach_type = coach_type  

    def conduct_training(self):
        print(f"{self.get_full_name()} ({self.__coach_type}) is conducting training.")

    def get_role_details(self):
        return f"Coach ID: {self.__coach_id}, Type: {self.__coach_type}"

class Staff(Person):
    def __init__(self, person_id: str, first_name: str, last_name: str, date_of_birth: datetime.date, nationality: str, staff_id: str, department: str, position: str):
        super().__init__(person_id, first_name, last_name, date_of_birth, nationality)
        self.__staff_id = staff_id
        self.__department = department  
        self.__position = position      

    def perform_duties(self):
        print(f"{self.get_full_name()} ({self.__position} in {self.__department}) is performing duties.")

    def get_role_details(self):
        return f"Staff ID: {self.__staff_id}, Department: {self.__department}, Position: {self.__position}"

class PersonCreator(ABC):
    @abstractmethod
    def create_person(self, person_id: str, first_name: str, last_name: str, date_of_birth: datetime.date, nationality: str, **kwargs) -> Person:
        """
        Abstract method to create a Person object.
        Subclasses will implement this to return specific types of Person.
        kwargs allow passing role-specific attributes.
        """
        pass

class PlayerCreator(PersonCreator):
    def create_person(self, person_id: str, first_name: str, last_name: str, date_of_birth: datetime.date, nationality: str, **kwargs) -> Player:
        player_id = kwargs.get('player_id')
        position = kwargs.get('position')
        status = kwargs.get('status')
        jersey_number = kwargs.get('jersey_number')
        if not all([player_id, position, status, jersey_number is not None]):
            raise ValueError("Missing required arguments for Player creation.")
        return Player(person_id, first_name, last_name, date_of_birth, nationality, player_id, position, status, jersey_number)

class CoachCreator(PersonCreator):
    def create_person(self, person_id: str, first_name: str, last_name: str, date_of_birth: datetime.date, nationality: str, **kwargs) -> Coach:
        coach_id = kwargs.get('coach_id')
        coach_type = kwargs.get('coach_type')
        if not all([coach_id, coach_type]):
            raise ValueError("Missing required arguments for Coach creation.")
        return Coach(person_id, first_name, last_name, date_of_birth, nationality, coach_id, coach_type)

class StaffCreator(PersonCreator):
    def create_person(self, person_id: str, first_name: str, last_name: str, date_of_birth: datetime.date, nationality: str, **kwargs) -> Staff:
        staff_id = kwargs.get('staff_id')
        department = kwargs.get('department')
        position = kwargs.get('position')
        if not all([staff_id, department, position]):
            raise ValueError("Missing required arguments for Staff creation.")
        return Staff(person_id, first_name, last_name, date_of_birth, nationality, staff_id, department, position)


print("--- Scenario Implementation: FC Cakrawala (with Factory Method) ---")

fc_cakrawala = Club(
    club_id="CC001",
    name="FC Cakrawala",
    founding_date=datetime.date(2020, 1, 15),
    tagline="Binaan Universitas Cakrawala"
)
print(f"Created Club: {fc_cakrawala.get_club_info()}")

fc_cakrawala_muda = Team(
    team_id="TCM001",
    name="FC Cakrawala Muda",
    division="U-23",
    founding_date=datetime.date(2021, 3, 1),
    team_type="U-23"
)
fc_cakrawala.add_team(fc_cakrawala_muda)
print(f"Created Team: {fc_cakrawala_muda.get_team_info()}")

player_creator = PlayerCreator()
coach_creator = CoachCreator()
staff_creator = StaffCreator() 

head_coach = coach_creator.create_person(
    person_id="PCH001",
    first_name="Budi",
    last_name="Santoso",
    date_of_birth=datetime.date(1980, 5, 20),
    nationality="Indonesian",
    coach_id="CH001",
    coach_type="Head Coach"
)
fc_cakrawala_muda.add_coach(head_coach)
print(f"Added Head Coach: {head_coach.get_full_name()} - {head_coach.get_role_details()}")

assistant_coach = coach_creator.create_person(
    person_id="PCH002",
    first_name="Citra",
    last_name="Dewi",
    date_of_birth=datetime.date(1990, 10, 10),
    nationality="Indonesian",
    coach_id="CH002",
    coach_type="Assistant Coach"
)
fc_cakrawala_muda.add_coach(assistant_coach)
print(f"Added Assistant Coach: {assistant_coach.get_full_name()} - {assistant_coach.get_role_details()}")

players_data = [
    ("PPL001", "Ahmad", "Fauzi", datetime.date(2002, 1, 1), "Indonesian", "PL001", "Forward", "Active", 10),
    ("PPL002", "Bagus", "Setiawan", datetime.date(2003, 2, 2), "Indonesian", "PL002", "Midfielder", "Active", 8),
    ("PPL003", "Cahyo", "Pratama", datetime.date(2002, 3, 3), "Indonesian", "PL003", "Defender", "Active", 4),
    ("PPL004", "Dani", "Saputra", datetime.date(2004, 4, 4), "Indonesian", "PL004", "Goalkeeper", "Active", 1),
    ("PPL005", "Eko", "Wijaya", datetime.date(2003, 5, 5), "Indonesian", "PL005", "Midfielder", "Active", 7),
    ("PPL006", "Fajar", "Ramadhan", datetime.date(2002, 6, 6), "Indonesian", "PL006", "Forward", "Active", 9),
    ("PPL007", "Gerry", "Susanto", datetime.date(2004, 7, 7), "Indonesian", "PL007", "Defender", "Active", 2),
    ("PPL008", "Hadi", "Nugroho", datetime.date(2003, 8, 8), "Indonesian", "PL008", "Midfielder", "Active", 6),
    ("PPL009", "Indra", "Kusuma", datetime.date(2002, 9, 9), "Indonesian", "PL009", "Forward", "Active", 11),
    ("PPL010", "Joko", "Santoso", datetime.date(2004, 10, 10), "Indonesian", "PL010", "Defender", "Active", 5),
    ("PPL011", "Kevin", "Aditya", datetime.date(2003, 11, 11), "Indonesian", "PL011", "Midfielder", "Active", 13),
    ("PPL012", "Lutfi", "Hidayat", datetime.date(2002, 12, 12), "Indonesian", "PL012", "Forward", "Active", 14),
    ("PPL013", "Maman", "Firmansyah", datetime.date(2004, 1, 1), "Indonesian", "PL013", "Defender", "Active", 15),
    ("PPL014", "Nanda", "Putra", datetime.date(2003, 2, 1), "Indonesian", "PL014", "Midfielder", "Active", 16),
    ("PPL015", "Oscar", "Pratama", datetime.date(2002, 3, 1), "Indonesian", "PL015", "Goalkeeper", "Active", 22),
]

for p_data in players_data:
    person_id, first_name, last_name, dob, nationality, player_id, position, status, jersey_number = p_data
    player = player_creator.create_person(
        person_id=person_id,
        first_name=first_name,
        last_name=last_name,
        date_of_birth=dob,
        nationality=nationality,
        player_id=player_id,
        position=position,
        status=status,
        jersey_number=jersey_number
    )
    fc_cakrawala_muda.add_player(player)
    print(f"Added Player: {player.get_full_name()} - {player.get_role_details()}")

print(f"\nFC Cakrawala Muda now has {len(fc_cakrawala_muda._Team__players)} players and {len(fc_cakrawala_muda._Team__coaches)} coaches.")

if fc_cakrawala_muda._Team__players:
    first_player = fc_cakrawala_muda._Team__players[0]
    player_contract = Contract(
        contract_id="CPL001",
        start_date=datetime.date(2024, 7, 1),
        end_date=datetime.date(2025, 6, 30),
        salary=5000000.0, 
        position="Forward",
        class_name="Player",
        person_id=first_player._person_id 
    )
    first_player.add_contract(player_contract)
    print(f"\nContract created for {first_player.get_full_name()}")