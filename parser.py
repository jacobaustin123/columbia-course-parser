"""
parser.py

usage: python parser.py <course directory URL>

for example:

python parser.py http://www.columbia.edu/cu/bulletin/uwb/subj/HUMA/_Fall2018.html

"""

from bs4 import BeautifulSoup
import re
import sys

class Section:
    keywords = {'professor' : re.compile('Instructor:'), 'section' : re.compile('Section [0-9]+'), 'date': re.compile('Day/Time:'), 'enrollment' : re.compile('Enrollment: ')}

    gold = ['Ouijdane Absi',
            'Azfar Adil',
            'Sonia Ahsan',
            'Jenna Alden',
            'Elizabeth Amann',
            'Michael Aufrichtig',
            'Gergely Baics',
            'Robert Barnett',
            'Berenice Baudry',
            'Rebecca Bauman',
            'Karin Beck',
            'Felice Beneduce',
            'Amy Benson',
            'Orlando Bentancor',
            'Mark Buchan',
            'Daniel Callahan',
            'Lynn Catterson',
            'Collomia Charles',
            'James Colgrove',
            'Jessamyn Conrad',
            'Mateo Cruz',
            'Nicholas Dames',
            'George Deodatis',
            'Zayd Dohrn',
            'Ann Douglas',
            'Brent Edwards',
            'Nicholas Engel',
            'Tina Fruehauf',
            'Robert Fucci',
            'John Gamber',
            'Bradford Garton',
            'Brian Gibney',
            'Erik Gray',
            'Farah Griffin',
            'Elia Gurna',
            'David Gutkin',
            'Gary Guy',
            'Hendrik Hamer',
            'Saskia Hamilton',
            'Emily Hayman',
            'Karen Hiles',
            'Joseph Howley',
            'Ana Huback',
            'Ivana Hughes',
            'Eleanor Johnson',
            'Katherine Kasdorf',
            'Ira Katznelson',
            'David Kittay',
            'Rina Kreitman',
            'Jenna Lawrence',
            'Shayne Legassie',
            'Jeffrey Lependorf',
            'Isabelle Levy',
            'Reyes Llopis-Garcia',
            'David Madigan',
            'Celine Marange',
            'Severine Martin',
            'Susan Mendelsohn',
            'Cheryl Mendelson',
            'Robert Miller',
            'Liza Monroy',
            'Jill Muller',
            'Kevin Murphy',
            'Ashley Nail',
            'Joshua Navon',
            'Frances Negron-Muntaner',
            'Youssef Nouhi',
            'Juliet Nusbaum',
            "David O'Connell",
            'Kristina Olson',
            'George Padilla',
            'Peter Park',
            'Peter Pazzaglini',
            'Susan Pedersen',
            'Ana Petrovic',
            'Sarah Phillips',
            'Caterina Pizzigoni',
            'Samuel Pluta',
            'Peter Pouncey',
            'Archie Rand',
            'Mariel Rodney',
            'Francisco Rosales-Varo',
            'Luke Rosenau',
            'Carol Rounds',
            'Giovanni Ruffini',
            'JosÃ© Ruiz-Campillo',
            'Karen Russell',
            'Rocco Servedio',
            'Jill Shapiro',
            'Robert Shapiro',
            'Leslie Sharpe',
            'Beau Shaw',
            'Oliver Simons',
            'Molly Smith',
            'Justin Snider',
            'Scott Snyder',
            'Sunhee Song',
            'Gordon Spencer',
            'Robert Stein',
            'Jamy Stillman',
            'Neferti Tadiar',
            'Colleen Thomas',
            'Kenneth Torrey',
            'Caitlin Trainor',
            'Elsa Ubeda',
            'Maria Valencia',
            'David Vallancourt',
            'Matt Vaz',
            'Tomas Vu-Daniel',
            'Xiaodan Wang',
            'Mark Watson',
            'Robert Weston',
            'Jennifer White',
            'Gareth Williams',
            'Jon Williams',
            'Catherine Williams',
            'Loren Wolfe',
            'William Worthen',
            'Amber Youell-Fingleton',
            'James Zetzel',
            'Garrett Ziegler',
            'Saskia Ziolkowski']
    silver = ['Bradley Abrams',
              'Nadia Abu-El-Haj',
              'Bashir Abu-Manneh',
              'James Adams',
              'May Ahmar',
              'Alexander Alberro',
              'Carlos Alonso',
              'Jarod Alper',
              'Alheli Alvarado-Diaz',
              'Tarik Amar',
              'Jannette Amaral',
              'Marissa Ambio',
              'Robert Amdur',
              'Gregory Amenoff',
              'Arjomand, Amir',
              'Benjamin Anastas',
              'Paul Anderer',
              'Eric Anderson',
              'Richard Anderson',
              'Marcellus Andrews',
              'Heidi Applegate',
              'Isaura Arce-Fernandez',
              'Gail Archer',
              'Seyhan Arkonac',
              'Flora Armetta',
              'Charles Armstrong',
              'Isaac-Davy Aronson',
              'Daniel Attinger',
              'Elizabeth Auran',
              'Vincent Aurora',
              'Emily Austin',
              'SÃ©verine Autesserre',
              'Ellis Avery',
              'Andreas Avgousti',
              'Luis Avila',
              'Peter Awn',
              'Gregory Baggett',
              'Zainab Bahrani',
              'Bonnie Baker',
              'Steve Baker',
              'Janaki Bakhle',
              'Anjali Balasingham',
              'Humberto Ballesteros',
              'Randall Balmer',
              'Karen Barkey',
              'Teodolinda Barolini',
              'Kelly Barry',
              'James Basker',
              'Christopher Baswell',
              'David Bayer',
              'Corbett Bazler',
              'Cris Beam',
              'Jordan Bear',
              'Stephanie Beardman',
              'Peter Bearman',
              'Deborah Becher',
              'Priscilla Becker',
              'Katharine Bedford',
              'Kledja Bega',
              'Tarik Belhoussein',
              'Robert Belknap',
              'Macalester Bell',
              'Taoufik Ben-Amor',
              'Tamar Ben-Vered',
              'kathy berenson',
              'Mark Berger',
              'Volker Berghahn',
              'Adam Berlin',
              'Nehama Bersohn',
              'Rym Bettaieb',
              'Carl Bettendorf',
              'Raimondo Betti',
              'Richard Betts',
              'Dwijen Bhattacharjya',
              'Tyler Bickford',
              'Katherine Biers',
              'Albert Bininachvili',
              'Elizabeth Blackmar',
              'Allan Blaer',
              'Paul Blaer',
              'Casey Blake',
              'Marcellus Blount',
              'Martha Blumberg',
              'Jeffrey Blustein',
              'Kristina Boerger',
              'Eleanor Boeschenstein',
              'Lee Bollinger',
              'Alice Boone',
              'Satyajit Bose',
              'Emerson Bowyer',
              'Brian Boyd',
              'Anne Boyman',
              'Marijeta Bozovic',
              'Deborah Bradley-Kramer',
              'Lisbeth Brandt',
              'Emily Breault',
              'Alan Brinkley',
              'Alan Brott',
              'Constance Brown',
              'Christopher Brown',
              'Jeffrey Brown',
              'Chris Buchenholz',
              'Denise Budd',
              'Jason Buhle',
              'Richard Bulliet',
              'Elda Buonanno',
              'Richard Bushman',
              'Paul Cadden-Zimansky',
              'Vangelis Calotychos',
              'Maguette Camara',
              'Cristina Cammarano',
              'Luis Campos',
              'Resit Canbeyli',
              'Adam Cannon',
              'Jeremy Carlo',
              'Taylor Carman',
              'Mark Carnes',
              'Daphne Carr',
              'Denise Carroll',
              'Jon Carter',
              'Alessandra Casella',
              'Paola Castagna',
              'Mauricio Castillo',
              'Patrizio Ceccagnoli',
              'Steven Chaikelson',
              'Damon Chaky',
              'Martin Chalfie',
              'Frances Champagne',
              'Tessa Chandler',
              'Kartik Chandran',
              'Ryan Chaney',
              'Stephane Charitos',
              'Partha Chatterjee',
              'Ajay Chaudhary',
              'Tavius Cheatham',
              'Joanna Cheetham',
              'Rachel Chung',
              'Amanda Claybaugh',
              'Heather Cleary-Wolfgang',
              'Jean-Christophe Cloutier',
              'John Coatsworth',
              'Pamela Cobrin',
              'Mary Cochran',
              'Deborah Coen',
              'Monica Cohen',
              'David Cohen',
              'Uri Cohen',
              'Sarah Cole',
              'Brian Cole',
              'Jonathan Cole',
              'Michael Cole',
              'Charly Coleman',
              'Nancy Collins',
              'Michael Collins',
              'Elaine Combs-Schilling',
              'Michael Como',
              'Maite Conde',
              'Vrinda Condillac',
              'James Connolly',
              'Peter Connor',
              'Janet Conrad',
              'Roderick Cooke',
              'Alexander Cooley',
              'Kevin Costa',
              'Elizabeth Cottrell',
              'Brinton Coxe',
              'Angelina Craig',
              'Angelina Craig-Florez',
              'Caleb Crain',
              'Emma Crandall',
              'James Crapotta',
              'Jonathan Crary',
              'Julie Crawford',
              'Mary Cregan',
              'Pascale Crepon',
              'Nicole Cuenot',
              'John Cunningham',
              'Sebastian Currier',
              'Gerald Curtis',
              'Christine Cynn',
              'Patricia Dailey',
              'Kate Daloz',
              'Dennis Dalton',
              'David Damrosch',
              'Caleb Dance',
              'John DaPrato',
              'Kurt Dasbach',
              'Panagiota Daskalopoulos',
              'Jeremy Dauber',
              'Jenny Davidson',
              'Flora Davidson',
              'Aguilar, de',
              'Angelis, De',
              'Genova, De',
              'Groot, de',
              'la de',
              'Silva, De',
              'Vincent Debaene',
              'Mark Debellis',
              'Vidya Dehejia',
              'Andrew Delbanco',
              'Dawn Delbanco',
              'Anand Deopurkar',
              'Alicia DeSantis',
              'Rosalyn Deutsche',
              'Gangi, Di',
              'Souleymane Diagne',
              'de Diaz',
              'Anne Diebel',
              'David Dinkins',
              'Daniel Dipaolo',
              'Matthew DiPentima',
              'Madeleine Dobie',
              'Jeremy Dodd',
              'Linda Doerrer',
              'Megan Doherty',
              'Ryan Dohoney',
              'Justin Dombrowski',
              'Paloma Duong',
              'Jason Earle',
              'Kathy Eden',
              'Stephen Edwards',
              'Shigeru Eguchi',
              'Aaron Einbond',
              'David Eisenbach',
              'Peter Eisenberger',
              'Mona El-Ghobashy',
              'George El-Hage',
              'Susan Elmes',
              'David Elson',
              'Jennifer Emerson',
              'Karen Emmerich',
              'David Epstein',
              'Etem Erol',
              'Elizabeth Esch',
              'Michael Eskin',
              'Isabel Estrada',
              'Sharon Everson',
              'Gil Eyal',
              'Murat Eyuboglu',
              'Scott Failla',
              'Leon Falk',
              'Reem Faraj',
              'Barbara Farnham',
              'Nathaniel Farrell',
              'Tanisha Fazal',
              'Maksym Fedorchuk',
              'Marlon Feld',
              'Sidney Felder',
              'Yang Feng',
              'Cassie Fennell',
              'Christina Ferando',
              'Robert Ferguson',
              'Julio Fernandez',
              'Kathy Fewster',
              'Dana Fields',
              'William Fifer',
              'Tauqir Fillebeen',
              'William Fisher',
              'Aili Flint',
              'Meredith Fluke',
              'Marcus Folch',
              'Helene Foley',
              'Eric Foner',
              'Alban Forcione',
              'Donlin Foreman',
              'Juliet Forshaw',
              'Virginia Fortna',
              'Severin Fowles',
              'Aaron Fox',
              'Mariana Fraga',
              'Anna Frajlich-Zajac',
              'John Frankfurt',
              'Federica Franze',
              'Paula Franzese',
              'Shelly Fredman',
              'Jason Freeman',
              'Walter Frisch',
              'Timothy Frye',
              'Sharon Fulton',
              'Albert Fung',
              'Rivka Galchen',
              'Jason Galie',
              'Patrick Gallagher',
              'Boris Gasparov',
              'Serge Gavronsky',
              'Liza Gennaro',
              'Mason Gentzler',
              'Abosede George',
              'Giuseppe Gerbino',
              'Irwin Gertzog',
              'Flora Ghezzo',
              'Lindsay Gibson',
              'Chad Gifford',
              'Jonathan Gill',
              'Stuart Gill',
              'Dehn Gilmore',
              'Marianne Giordani',
              'Todd Gitlin',
              'Elise Giuliano',
              'Atle Gjelsvik',
              'Kate Glasner',
              'Patrick Glauthier',
              'Kaiama Glover',
              'Carol Gluck',
              'Lydia Goehr',
              'Leon Gold',
              'Dorian Goldfeld',
              'Sandra Goldmark',
              'Michael Golston',
              'Melissa Gonzalez',
              'Lucy Goodhart',
              'Glenn Gordon',
              'Bidyut Goswami',
              'Stuart Gottlieb',
              'Stathis Gourgouris',
              'Maria Gozzi',
              'Luis Gravano',
              'Ellen Gray',
              'Joshua Green',
              'Brooke Greene',
              'Cordula Grewe',
              'Patricia Grieve',
              'Kevin Griffin',
              'Erk Grimm',
              'Eitan Grinspun',
              'Jonathan Gross',
              'Achsah Guibbory',
              'Vanessa Guida',
              'Sunil Gulati',
              'Aaron Gullickson',
              'Hannah Gurman',
              'Musa Gurnis',
              'Owen Gutfreund',
              'Rebecca Guy',
              'Lianne Habinek',
              'Evan Haefeli',
              'Najam Haider',
              'Ian Halim',
              'Andrew Hall',
              'Wael Hallaq',
              'Sean Hallowell',
              'Ross Hamilton',
              'James Hannaham',
              'Andrew Haringer',
              'Scott Harold',
              'James Harrigan',
              'Teresa Harris',
              'Sharon Harrison',
              'Matthew Hart',
              'Christopher Harwood',
              'John Hawley',
              'Michael Hawn',
              'Claire Hazen',
              'Tony Heinz',
              'David Helfand',
              'Jeffrey Helzner',
              'Farzaneh Hemmasi',
              'Sidney Hemming',
              'Karen Henson',
              'Paul Hertz',
              'Larry Heuer',
              'Derrick Higginbotham',
              'Tory Higgins',
              'Marianne Hirsch',
              'Julia Hirschberg',
              'Kate Ho',
              'Wei Ho',
              'Huckleberry Hodge',
              'Miriam Hoffman',
              'Justin Hoffman',
              'Sharon Hoffmann',
              'Lisa Hollibaugh',
              'Ralph Holloway',
              'Heidi Holst-Knudsen',
              'Jennifer Hom',
              'James Hone',
              'Clement Hongler',
              'Barbel Honisch',
              'Donald Hood',
              'Nicole Horejsi',
              'Maja Horn',
              'Peter Horn',
              'Alexandra Horowitz',
              'Daniel Hsu',
              'Lingjun Hu',
              'Shao-Ying Hua',
              'Pascale Hubert-Leibler',
              'Theodore Hughes',
              'Thomas Humensky',
              'Megan Huston',
              'Andreas Huyssen',
              ', Iglesias',
              'Elizabeth Irwin',
              'Marilyn Ivy',
              'Alain Jachiet',
              'Gerrit Jackson',
              'Susan Jacobs',
              'Janet Jakobsen',
              'Chadwick Jenkins',
              'Juan Jimenez-Caicedo',
              'Wen Jin',
              'Peter Johnson',
              'Amy Johnson',
              'Kathryn Johnston',
              'Matthew Jones',
              'Branden Joseph',
              'Isabelle Jouanneau-Fertig',
              'Grigsby Julia',
              'David Kagan',
              'Jonathon Kahn',
              'Hossein Kamaly',
              'Lara Kammrath',
              'Natalie Kampen',
              'Ezer Kang',
              'Ilia Karatsoreos',
              'Karen Karbiener',
              'Jennie Kassanoff',
              'David Kastan',
              'Harry Kavros',
              'Joel Kaye',
              'Alison Keimowitz',
              'Peter Kelemen',
              'Valerie Keller',
              'Darcy Kelley',
              'John Kender',
              'Gale Kenny',
              'Allegra Kent',
              'Brahim Kerkour',
              'Mark Kesselman',
              'Alice Kessler-Harris',
              'David Keyes',
              'Jameel Khaja',
              'Rashid Khalidi',
              'Shamus Khan',
              'Chad Kia',
              'Young Kim',
              'Nelson Kim',
              'Seth Kimmel',
              'Jessica Kimpell',
              'Robert King',
              'Philip Kitcher',
              'Patricia Kitcher',
              'Holger Klein',
              'Irena Klepfisz',
              'Sarah Klock',
              'Liza Knapp',
              'Susanne Knittel',
              'Chisu Ko',
              'Dorothy Ko',
              'Paul Kockelman',
              'Aladar Kogler',
              'Richard Kopelman',
              'Richard Korb',
              'David Kornhaber',
              'Donna Kornhaber',
              'Adam Kosto',
              'Lindsay Koval',
              'Rosalind Krauss',
              'Igor Krichever',
              'Karl Kroeber',
              'Elizabeth Kujawinski',
              'Akash Kumar',
              'Cagatay Kutluhan',
              'Jeffrey Kysar',
              'Robert LaFosse',
              'Upmanu Lall',
              'Tristan Lambert',
              'Alexander Landfair',
              'Margaret Lange',
              'Jean Laponce',
              'William Latzko',
              'Aaron Lauda',
              'Jonathan Lawhead',
              'Sarah Lazur',
              'Nam Le',
              'Guyader, Le',
              'William Leach',
              'Valentina Lebedev',
              'Johnathan Lee',
              'Risha Lee',
              'Jae Lee',
              'Robert Legvold',
              'James Leighton',
              'Elizabeth Leininger',
              'Colette LeRoux',
              'Christina Leslie',
              'Cheryl Leung',
              'Kate Levin',
              'Janna Levin',
              'Peter Levin',
              'Fabien Levy',
              'George Lewis',
              'Karen Lewis',
              'Ruth Lexton',
              'Feng Li',
              'Sara Lieber',
              'Emma Lieber',
              'Robert Lieberman',
              'Natasha Lightfoot',
              'Mark Lilla',
              'Martin Lindquist',
              'Robert Lipshitz',
              'Samuel Lipsyte',
              'Max Lipyanskiy',
              'Jared Lister',
              'Emilie Littlehales',
              'Vila, Llovet',
              'Kirsten Lodge',
              'Aenon Loo',
              'Sylvere Lotringer',
              'Morgan Luker',
              'Ivan Lupic',
              'David Lurie',
              'Andrew Lynn',
              'Adam, Mac',
              'Alfred MacAdam',
              'Mehammed Mack',
              'David Macklovitch',
              'Alexander Madva',
              'Terryanne Maenza-Gmelch',
              'Brian Mailloux',
              'Matthew Main',
              'Marco Maiuro',
              'Tal Malkin',
              'Mahmood Mamdani',
              'Gregory Mann',
              'Andrew Manson',
              'Sharon Marcus',
              'Kimberly Marten',
              'Darragh Martin',
              'Deborah Martinsen',
              'Donna Masini',
              'Laura Masone',
              'Stephen Massimilla',
              'Leonard Matin',
              'Yoichiro Matsumura',
              'Michael Mauel',
              'Davesh Maulik',
              'Gita May',
              'Morgan May',
              'Mark Mazower',
              "E'mett McCaskill",
              'Robert McCaughey',
              'Tyler McCormick',
              'Marilyn McCoy',
              'Koleen McCrink',
              'Rachel McDermott',
              'Dusa McDuff',
              'Donovan McFeron',
              'David McKenna',
              'Carin McLain',
              'Jane McMahan',
              'Jerry McManus',
              'John McWhorter',
              'Perry Mehrling',
              'Linn Mehta',
              'Jodi Melnick',
              'Edward Mendelson',
              'Yuan-Yuan Meng',
              'Christia Mercer',
              'Dina Merrer',
              'Maya Mikdashi',
              'Nara Milanich',
              'Jeffrey Milarsky',
              'Matthew Miller',
              'Monica Miller',
              'Elizabeth Miller',
              'Kristina Milnor',
              'Denise Milstein',
              'Masha Mimran',
              'Milan Mincek',
              'Lorraine Minnite',
              'Dan Miron',
              'Gaurav Misra',
              'Dean Mobbs',
              'David Moerman',
              'Oran Moked',
              'Hlonipha Mokoena',
              'Catherine Monk',
              'Roosevelt Montas',
              'Carlos Montes-Galdon',
              'Michele Moody-Adams',
              'Rosalind Morris',
              'Ted Mosby',
              'Irene Motyl',
              'Solomon Mowshowitz',
              'Jose Moya',
              'Samuel Moyn',
              'Ovidiu Munteanu',
              'Francoise Murail',
              'Ann Murphy',
              'Chris Murphy',
              'Stephen Murray',
              'Molly Murray',
              'Tobias Myers',
              'Kristin Myers',
              'Ioannis Mylonopoulos',
              'Premilla Nadasen',
              'Shahid Naeem',
              'Paola Nastri',
              'Shree Nayar',
              'Fumiko Nazikian',
              'Kathryn Neckerman',
              'Robert Neel',
              'Evan Neely',
              'Robert Neer',
              'Duncan Neilson',
              'Alondra Nelson',
              'Catharine Nepomnyashchy',
              'Anahid Nersessian',
              'Oded Netzer',
              'Frederick Neuhouser',
              'Aimee Ng',
              'Serena Ng',
              'Fay Ng',
              'Mae Ngai',
              'Jason Nieh',
              'Nicola Nino',
              'Miharu Nittono',
              'Valentina Nocentini',
              'Daniela Noe',
              'Samuel North',
              'Lisa Northrop',
              'Jack Norton',
              'Ismail Noyan',
              'Marcel Nutz',
              "Brian O'Keeffe",
              "Robert O'Meally",
              "Jeffrey O'Neal",
              "Bethany O'Shea",
              'Samuel Oak',
              'Andrew Obus',
              'Jennifer Offill',
              'Keiko Okamoto',
              'Gary Okihiro',
              'Virginia Oliveros',
              'Rachel Ollivier',
              'Pietro Ortoleva',
              'Irina Oryshkevich',
              'Niels Ostbye',
              'Elizabeth Ouyang',
              'Frederik Paerels',
              'John Pagano',
              'Matthew Palmer',
              'Patrizia Palumbo',
              'Neni Panourgia',
              'Anargyros Papageorgiou',
              'Jennifer Pardo',
              'Joseph Parent',
              'So Park',
              'Jisuk Park',
              'Gerard Parkin',
              'John Parsons',
              'Coilin Parsons',
              'Esther Pasztory',
              'Joseph Patterson',
              'Julie Patterson',
              'Elliot Paul',
              'Elizabeth Pearlman',
              'Philip Pechukas',
              'Stefan Pedatella',
              'John Pemberton',
              'Richard Pena',
              'Terence Pender',
              'Serrano, PerÃ©z',
              'Gustavo Perez-Firmat',
              'Javier Perez-Zapatero',
              'Alexandra Perisic',
              'Julie Peters',
              'Jason Petrulis',
              'Douglas Pfeiffer',
              'Stephanie Pfirman',
              'Gregory Pflugfelder',
              'Justin Phillips',
              'Lindsay Piechnik',
              'Anatoly Pinsky',
              'Pablo Pinto',
              'Richard Pious',
              'Peter Platt',
              'Jonathan Platt',
              'Attila Pok',
              'Lorenzo Polvani',
              'Cathy Popkin',
              'Gabrielle Popoff',
              'Olaf Post',
              'Laurie Postlewate',
              'Elizabeth Povinelli',
              'Amy Powell',
              'Olivia Powell',
              'Amit Prakash',
              'Anne Prescott',
              'Quandra Prettyman',
              'Wayne Proudfoot',
              'Thibaut Pugin',
              'Shaoyan Qi',
              'Sophie Queuniet',
              'Vincent Racaniello',
              'Eshkol Rafaeli',
              'Dalpat Rajpurohit',
              'Anupama Rao',
              'Stuart Raphael',
              'Anna Ratner',
              'Sanjay Reddy',
              'Ricardo Reis',
              'Irina Reyfman',
              'Jonathan Reynolds',
              'Frances Richard',
              'Jonathan Rick',
              'Jonathan Rieder',
              'Kristy Riggs',
              'Carl Riskin',
              'Ryan, Rivers',
              'Bruce Robbins',
              'Lucy Robinson',
              'Lorena Rodas',
              'Christian Rojas',
              'Sarah Roland',
              'Thomas Roma',
              'Russell Romeo',
              'Patricia Romero',
              'Luci Rosalia',
              'Nelly Rosario',
              'Louise Rose',
              'Margo Rosen',
              'Rosalind Rosenberg',
              'John Rosenberg',
              'Harry Rosenblum',
              'Jennifer Rosenthal',
              'Victoria Rosner',
              'David Rosner',
              'Todd Rouhe',
              'Perla Rozencvaig',
              'Zipora Rubin',
              'James Runsdorf',
              'Alessandra Russo',
              'Emmanuelle Saada',
              'Jeffrey Sachs',
              'Richard Sacks',
              'Xavier Sala-i-Martin',
              'Edgardo Salinas',
              'Shelley Saltzman',
              'Arthur Salvo',
              'John Salyer',
              'Hiie Saumaa',
              'Ovidiu Savin',
              'James Schamus',
              'Caleb Scharf',
              'Elizabeth Scharffenberger',
              'David Schiminovich',
              'Conrad Schirokauer',
              'Maximillian Schmeder',
              'Jutta Schmiers-Heller',
              'Stephanie Schmitt-Grohe',
              'Wendy Schor-Haim',
              'Selby Schwartz',
              'Madeline Schwartzman',
              'Paul Scolieri',
              'David Scott',
              'Stephen Scott',
              'Joanna Scutts',
              'Michael Seidel',
              'Ann Senghas',
              'Neslihan Senocak',
              'Natasa Sesum',
              'Rajiv Sethi',
              'Michael Shaevitz',
              'Steven Shaklan',
              'Wei Shang',
              'James Shapiro',
              'Matthew Sharpe',
              'David Shatz',
              'Allyson Sheffield',
              'Nathanael Shelley',
              'Kristen Shepard',
              'Yuri Shevchuk',
              'Zhongqi Shi',
              'Emily Shortslef',
              'Erica Siegel',
              'Paul Siegel',
              'Julia Siemon',
              'Karl Sigman',
              'Cristobal Silva',
              'Elaine Sisman',
              'Michael Skelly',
              'Samuel Skippon',
              'Joseph Slaughter',
              'Joanna Smith',
              'Kathleen Smith',
              'Tatiana Smoliarova',
              'Alla Smyslova',
              'Scott Snyder',
              'Jeffrey Snyder',
              'Richard So',
              'Adam Sobel',
              'Alexis Soloski',
              'Robert Somerville',
              'Roxanna Sooudi',
              'Katharine Soper',
              'Ben Soskis',
              'Betsy Sparrow',
              'Marc Spiegelman',
              'Barbara Spinelli',
              'Samuel Spinner',
              'Matthew Spooner',
              'Joanna Stalnaker',
              'Piero Stanig',
              'Rebecca Stanton',
              'Jessica Stanton',
              'David Stark',
              'Elliott Stein',
              'Deborah Steiner',
              'Jon Steinsson',
              'Paul Stephens',
              'David Sterritt',
              'Patricia Stokes',
              'Shilarna Stokes',
              'Horst Stormer',
              'Dawn Strickland',
              'Steven Stroessner',
              'Martin Stute',
              'Jesus Suarez-Garcia',
              'Harold Sultan',
              'Abigail Susik',
              'Peter Susser',
              'Timea Szell',
              'Xiaoxi Tai',
              'Ichiro Takayoshi',
              'Bernard Tamas',
              'Qiuyu Tan',
              'Todd Tarantino',
              'Naofumi Tatsumi',
              'Ezra Tawil',
              'Edward Tayler',
              'Michael Thaddeus',
              'Susan Thames',
              'Robert Thomas',
              'Robin Thomas',
              'Andrea Thomas',
              'Erin Thompson',
              'Lisa Tiersten',
              'Zoe Tobier',
              'Antonio Tomas',
              'Valentino Tosatti',
              'Yannis Tsividis',
              'Michael Tuts',
              'Victoria Tzotzkova',
              'James Uden',
              'Joseph Ulichny',
              'Katherine Underwood',
              'Isabelle Urban',
              'Martin Uribe',
              'Phillip Usher',
              'Lucie Vagnerova',
              'Simona Vaidean',
              'Margaret Vail',
              'Deborah Valenze',
              'Mario Valero',
              'Dyck, Van',
              'Margaret Vandenburg',
              'Achille Varzi',
              'Diane Vaughan',
              'Melanie Ventilla',
              'Christina Viereck-Hunter',
              'Xavier Vila',
              'Vlad Vintila',
              'Paul Violi',
              'Gauri Viswanathan',
              'Katja Vogt',
              'Katharina Volk',
              'Mucke, von',
              'Ostenfeld, von',
              'Eugene Vydrin',
              'Haim Waisman',
              'Joshua Walden',
              'Charles Walls',
              'Caroline Wamsler',
              'Zhirong Wang',
              'Mu-Tao Wang',
              'Feng Wang',
              'Jian Wang',
              'Dorian Warren',
              'Christopher Washburne',
              'Duncan Watts',
              'Philip Watts',
              'Mari Webel',
              'Caroline Weber',
              'Anthony Webster',
              'Paul Weinfield',
              'Sheldon Weinig',
              'David Weinstein',
              'Christopher Weiss',
              'Paige West',
              'Veronica White',
              'Josh Whitford',
              'Chris Wiggins',
              'Tobias Wilke',
              'Tyler Williams',
              'Christopher Williams',
              'Emma Winter',
              'Meaghan Winter',
              'Clarice Wirkala',
              'Karla Wolfangle',
              'Eliza Woo',
              'Christopher Wood',
              'Frank Wood',
              'Leslie Woodard',
              'Michael Woodbury',
              'Yvonne Woon',
              'Nancy Workman',
              'Nancy Worman',
              'Richard Wortman',
              'Chen Wu',
              'Eric Wubbels',
              'Xin Yan',
              'Ling Yan',
              'Alan Yang',
              'David Yao',
              'Alan Yeung',
              'Hyunkyu Yi',
              'Timothy Youker',
              'Doris Zahner',
              'Homa Zarghamee',
              'Taryn Zarrillo',
              'Anton Zeitlin',
              'Wei Zhang',
              'Xiangwen Zhang',
              'Tian Zheng',
              'Alan Ziegler',
              'Patrick Zimerli',
              'Patrick Zimmerli',
              'Ralph Zito',
              'Charles Zukowski']

    def __init__(self, text, semester):
        try:
            self.semester = semester

            soup = BeautifulSoup(text, 'html.parser')
            course = soup.find_all(text=re.compile(self.semester))

            if len(course) != 0:
                self.is_header = True
                self.header = course[0].next.text

                self.professor = ""
                self.section = ""
                self.data = ""
                self.enrollment = ""

                return

            else:
                self.professor = soup.find_all(text=self.keywords['professor'])[0].parent.next.next.strip()
                self.section = soup.find_all(text=self.keywords['section'])[0]
                self.date = soup.find_all(text=self.keywords['date'])[0].next.strip()

                raw_enrollment = soup.find_all(text=self.keywords['enrollment'])[0].next.strip()
                p = re.compile('([[0-9]+).+\(([0-9]+).+')
                self.enrollment = p.sub(r'\1/\2', raw_enrollment)

                self.is_header = False
                self.header = ""

        except:
            raise ValueError("String could not be parsed into a Section object.")

    def nugget(self):
        p = re.compile('(\S+)\s\S\s(\S+)')

        if (self.professor in self.gold or p.sub("\\1 \\2", self.professor) in self.gold):
            return "gold"
        elif (self.professor in self.silver or p.sub("\\1 \\2", self.professor) in self.silver):
            return "silver"
        else:
            return ""

    def to_string(self):
        if self.is_header:
            string = self.header
        else:
            if len(self.nugget()) != 0:
                string = self.section + " " + self.date + " " + "(" + self.enrollment + ") " + self.professor + " (" + self.nugget() + ")"
            else:
                string = self.section + " " + self.date + " " + "(" + self.enrollment + ") " + self.professor

        return string

    def __str__(self):
        return self.to_string()


import requests

if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except:
        print("Please enter a valid web URL to the course directory page as the only command line argument.")
        exit(1)

    try:
        message = requests.get(path)
        assert( message.status_code == 200 )

    except:
        print("Your path was invalid. Please enter a valid path.")
        exit(1)

    html = BeautifulSoup(message.text, 'html.parser')

    data = []

    p = re.compile('^\S+_([a-zA-Z]+)([0-9]+).html')
    semester = p.sub('\\1 \\2', path)

    elems = html.find_all('tr')
    for e in elems:
        try:
            s = Section(e.encode_contents(), semester)
            data.append(s)
        except:
            continue


    with open("courses.txt", 'w') as f:
        for i, section in enumerate(data):

            if section.is_header and i is not 0:
                f.write("\n")

            f.write(section.to_string() + '\n')

            if section.is_header:
                f.write("\n")
