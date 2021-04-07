# -*- coding: utf-8 -*-
"""

Justin Berg
Akhil Kumar Reddy Gopireddy
Tyler C. O'Brien
IE 8030 Final Project Model
Dr.Emily Tucker
4/26/21

"""
# Set up packages
from pyomo.environ import *
import pandas as pd

# Set 1 (Set of API sites)
model.S = Set(initialize["USA", "Mexico", "Puerto Rico", "Ireland", "Italy", 
                         "Hungary", "Croatia", "Israel", "India", "China"])
print(S)

# Set 2 (Set of Manufacturing Sites)
model.F = Set(initialize["USA", "Mexico", "Puerto Rico", "Ireland", "Italy", 
                         "Hungary", "Croatia", "Israel", "India", "Canada", 
                         "Venezuela", "Peru", "Chile", "Brazil", "Argentina", 
                         "Iceland", "Netherlands", "Spain", "UK", "Poland", 
                         "Germany", "Malta", "Lithuania", "Russia", "Serbia", 
                         "Czech", "Hungary", "Romania", "Bulgaria", "Greece", 
                         "Japan", "Thailand", "Singapore", "Indonesia"])
print(F)

# Set 3 (Set of Countries)
model.C = Set(initialize["China", "India", "United States", "Indonesia",
                         "Pakistan", "Brazil", "Nigeria", "Bangladesh",	
                         "Russia",	"Mexico", "Japan","Ethiopia",	
                         "Philippines",	"Egypt", "Vietnam",	"DR Congo",	
                         "Turkey",	"Iran",	"Germany", "Thailand",	
                         "United Kingdom",	"France", "Italy",	
                         "Tanzania", "South Africa", "Myanmar",	
                         "Kenya", "South Korea", "Colombia", 
                         "Spain", "Uganda",	"Argentina",	
                         "Algeria",	"Sudan", "Ukraine",	"Iraq",	
                         "Afghanistan",	"Poland", "Canada",	"Morocco",	
                         "Saudi Arabia", "Uzbekistan", "Peru", "Angola", 
                         "Malaysia", "Mozambique", "Ghana",	"Yemen", "Nepal", 
                         "Venezuela", "Madagascar", "Cameroon",	
                         "Côte d'Ivoire", "North Korea", "Australia", "Niger",	
                         "Taiwan", "Sri Lanka",	"Burkina Faso",	"Mali",	
                         "Romania",	"Malawi", "Chile", "Kazakhstan", 
                         "Zambia",	"Guatemala", "Ecuador",	
                         "Syria", "Netherlands", "Senegal",	"Cambodia",	
                         "Chad",	"Somalia",	"Zimbabwe",	"Guinea",	
                         "Rwanda",	"Benin",	"Burundi",	"Tunisia",	
                         "Bolivia",	"Belgium", "Haiti", "Cuba",	"South Sudan",	
                         "Dominican Republic",	"Czech Republic (Czechia)",	
                         "Greece",	"Jordan",	"Portugal",	"Azerbaijan", 
                         "Sweden",	"Honduras",	"United Arab Emirates",	
                         "Hungary",	"Tajikistan",	"Belarus",	"Austria", 
                         "Papua New Guinea",	"Serbia",	"Israel", 
                         "Switzerland",	"Togo",	"Sierra Leone",	"Hong Kong", 
                         "Laos",	"Paraguay",	"Bulgaria",	"Libya", 
                         "Lebanon",	"Nicaragua",	"Kyrgyzstan", 
                         "El Salvador",	"Turkmenistan",	"Singapore", 
                         "Denmark",	"Finland",	"Congo",	"Slovakia",	
                         "Norway",	"Oman",	"State of Palestine", 
                         "Costa Rica",	"Liberia",	"Ireland", 
                         "Central African Republic", 
                         "New Zealand",	"Mauritania", "Panama",	"Kuwait", 
                         "Croatia",	"Moldova",	"Georgia",	"Eritrea", 
                         "Uruguay",	"Bosnia and Herzegovina", 
                         "Mongolia",	"Armenia",	"Jamaica", 
                         "Qatar",	"Albania",	"Puerto Rico", 
                         "Lithuania",	"Namibia",	"Gambia", 
                         "Botswana", "Gabon", "Lesotho", "North Macedonia",	
                         "Slovenia", "Guinea-Bissau", "Latvia", "Bahrain", 
                         "Equatorial Guinea",	"Trinidad and Tobago", 
                         "Estonia",	"Timor-Leste",	"Mauritius", "Cyprus", 
                         "Eswatini", "Djibouti", "Fiji", "Réunion",	
                         "Comoros",	"Guyana", "Bhutan", "Solomon Islands", 
                         "Macao", "Montenegro", "Luxembourg", 
                         "Western Sahara",	"Suriname",	"Cabo Verde", 
                         "Micronesia",	"Maldives",	"Malta", "Brunei", 
                         "Guadeloupe", "Belize", "Bahamas", "Martinique",	
                         "Iceland",	"Vanuatu",	"French Guiana", "Barbados", 
                         "New Caledonia", "French Polynesia", "Mayotte", 
                         "Sao Tome & Principe",	"Samoa", "Saint Lucia",	
                         "Channel Islands",	"Guam",	"Curaçao",	"Kiribati",	
                         "Grenada",	"St. Vincent & Grenadines",	"Aruba", 
                         "Tonga", "U.S. Virgin Islands", "Seychelles", 
                         "Antigua and Barbuda",	"Isle of Man", "Andorra", 
                         "Dominica", "Cayman Islands", "Bermuda", 
                         "Marshall Islands", "Northern Mariana Islands", 
                         "Greenland", "American Samoa",	"Saint Kitts & Nevis", 
                         "Faeroe Islands", "Sint Maarten", "Monaco", 
                         "Turks and Caicos", "Saint Martin", 
                         "Liechtenstein", "San Marino",	"Gibraltar", 
                         "British Virgin Islands", "Caribbean Netherlands", 
                         "Palau", "Cook Islands", "Anguilla", "Tuvalu", 
                         "Wallis & Futuna",	"Nauru", "Saint Barthelemy", 
                         "Saint Helena", "Saint Pierre & Miquelon",	
                         "Montserrat", 
                         "Falkland Islands", "Niue", "Tokelau",	"Holy See"])
print(C)

# Set up Distance Matrices

# Distance from API site to Manufacturing Site
r = [[0, 1632525, 3529005, 6678610,	8619053, 8652055, 8553872, 10860041, 
      13576673,	2261533, 4507991, 5580330, 8466841, 7316912, 9017673, 5713533, 
      7506086, 7588915, 6830403, 8279733, 7861470, 9163371,	8265566, 
      8886096, 8976453,	8234385, 8652055, 9045856, 9332647, 9408874, 
      10150452,	13871490, 15289912, 14961819], [ 1632525, 0, 3773273,	
      8237885, 10147771, 10240927, 10116809, 12429344, 15094401, 3626619, 
      4290260, 4720117, 7357677, 6928280, 8004596, 7337691, 9085849, 9025731, 
      8414579, 9888562, 9447558, 10649721, 9890795, 10222488, 10553673, 
      9825661, 10240927, 10644897, 10919083, 10959586, 10798152, 
      14931656, 16034577, 15335255], [ 3529005, 3773273, 0, 6339188, 
      7785444, 8244015, 7950951, 10008660, 14294651, 5359214, 1311774, 
      3185135, 6015643, 3950744, 6305374, 6262785, 7188639, 6427711, 
      6664178, 8135081, 7543894,	8037758,	8383246,	11118695,	
      8424526,	7908683,	8244015,	8680688,	8809693,	
      8610720,	13423388,	15987850,	17598929,	18075983],[ 6678610,	
      8237885,	6339188,	0,	1959296,	2033889,	1879108,	
      4191525,	7971287,	5795162,	7403646,	9366175,	
      11629768,	8595444,	11511342,	1460258,	882025,	1440823,	
      371651,	1809749,	1253620,	2570978,	2050333,	5974986,	
      2321272,	1638441,	2033889,	2463442,	2697142,	2730265,	
      9550904,	9791113,	11296975,	12119197], [8619053,	10147771,	
      7785444,	1959296,	0,	804656,	417016,	2317704,	6569030,	
      7705256,	8634324,	10489607,	12131167,	9069620,	11785185,	
      3243382,	1265829,	1372634,	1898048,	1222707,	1045901,	
      678124,	1692405,	6146030,	726672,	911530,	804656,	1090055,	
      1065667,	841988,	9728696,	8710328,	10010862,	11004050],[8652055,	
      10240927,	8244015,	2033889,	804656,	0,	403091,	2219591,	
      6055086,	7476354,	9189311,	11095818,	12894051,	9819040,	
      12572579,	3023369,	1160137,	1999475,	1826437,	529576,	
      793668,	1318326,	940739,	5345117,	368817,	418660,	0,	439113,	
      680895,	918776,	8924052,	8084293,	9467788,	10405807],
      [8553872,	10116809,	7950951,	1879108,	417016,	403091,	0,	
       2312536,	6363696,	7508147,	8858231,	10746600,	12494492,	
       9421987,	12169528,	3033210,	1066812,	1625599,	1740242,	
       811762,	760596,	1021188,	1277046,	5731175,	475396,	524960,	
       403091,	766165,	864153,	864099,	9319773,	8440352,	9792724,	
       10753229],[ 10860041,	12429344, 10008660,	4191525,	
                  2317704,	2219591,	2312536,	0,	4534437,	
                  9649896,	10717347,	12420709,	13322836,	10518564,	
                  12764173,	5234517,	3354165,	3605377,	4030499,	
                  2651487,	3002474,	1970904,	2818551,	5987770,	
                  1884230,	2638024,	2219591,	1863100,	1541344,	
                  1481596,	9084352,	6858708,	7935274,	9013885],
                  [ 13576673,	15094401,	14294651,	7971287,	6569030,	
                   6055086,	6363696,	4534437,	0,	11469120,	15200128,	
                   16951278,	16691796,	14775294,	15926642,	8307640,	
                   7110443,	7941645,	7662647,	6165671,	6752184,	
                   6436034,	5949395,	4985663,	5895258,	6385983,	
                   6055086,	5620746,	5517143,	5779106,	5959300,	
                   2382920,	3443647,	4484994], [ 11647274,	12826358,	
                                                13923587,	8149522,	
                                                7566260,	6813837,	
                                                7210939,	6319667,	
                                                2983793,	9385871,	
                                                15215569,	17048254,	
                                                19630051,	16632845,	
                                                18898955,	7777686,	
                                                7486398,	8788264,	
                                                7779561,	6640304,	
                                                7223887,	7757407,	
                                                6230291,	2854613,	
                                                6845532,	6967766,	
                                                6813837,	6476236,	
                                                6567578,	7013859,	
                                                3046756,	2245546,	
                                                3837482,	4198121]]

r_sf = pd.DataFrame(data = r, columns = model.F, index = model.S)
r_val = r_sf.stack().to_dict() #convert to dictionary

# Distance from Manufacturing Site to Country
k = 
k_fc = pd.DataFrame(data = k, columns = model."", index = model."")
k_val = k_fc.stack().to_dict() #convert to dictionary

# Parameters
# Count of Manufacturing Sites

Count_F = len(F)
print(Count_F)

#Count of Countries
Count_C = len(C)
print(Count_C)

# Create the model
model = ConcreteModel(name = "Team 3 Final Project Model-Teva Supply Chain")

#  Variables

# Decision Variables
model.x = Var(model.S,model.F, within=NonNegativeReals)
model.y = Var(model.F,model.C, within=NonNegativeReals)

# Objective Function

# Amount Sent from API Site (in set S) to Manufacturing Site (in set F)
