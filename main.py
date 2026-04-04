import fastf1

session = fastf1.get_session(2021, 7, 'Q')
session.name
print(session.date)