# working with sets
from pyscript import display

all_students = {'Atasha', 'Mergal', 'Ainah', 'Alonso', 'Tessa', 'Seth'}
club1 = {'Atasha', 'Mergal', 'Ainah', 'Alonso'}
club2 = {'Tessa', 'Seth', 'Mergal', 'Ainah'}

display(club1, target='output')
display(club2, target='output')

all_students = club1 | club2
display(all_students, target='output')

both_clubs = club1 & club2
display(both_clubs, target='output')

only_club1 = club1 - club2
display(only_club1, target='output')

only_club2 = club2 - club1
display(only_club2, target='output')

exactly_one_club = club1 ^ club2
display(exactly_one_club, target='output')
