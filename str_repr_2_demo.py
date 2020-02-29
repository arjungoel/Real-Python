# __str__ vs __repr__
# __str__ is mainly used for giving an easy-to-read representation of your class.
# __str__ is easy to read for human consumption.
# __repr__ is umambiguous and the goal here to be as explicit as possible about what this object is and more meant
# for internal use and something that would make things easier to debug for developer but you wouldn't necessarily
# want to display that to a user.

import datetime
today = datetime.date.today()
print(str(today))
print(repr(today))