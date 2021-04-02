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
model.S = Set(initialize["USA", "Mexico", "Puerto Rico", "Ireland", "Italy", "Hungary", "Croatia", "Israel", "India", "China"])
print(S)

# Set 2 (Set of Manufacturing Sites)
model.F = Set(initialize["USA", "Mexico", "Puerto Rico", "Ireland", "Italy", "Hungary", "Croatia", "Israel", "India", "Canada", "Venezuela", "Peru", "Chile", "Brazil", "Argentina", "Iceland", "Netherlands", "Spain", "UK", "Poland", "Germany", "Malta", "Lithuania", "Russia", "Serbia", "Czech", "Hungary", "Romania", "Bulgaria", "Greece", "Japan", "Thailand", "Singapore", "Indonesia"])
print(F)

# Set 3 (Set of Countries)
model.C = Set(initialize["China",	"India",	"United States",	"Indonesia",	"Pakistan",	"Brazil",	"Nigeria",	"Bangladesh",	"Russia",	"Mexico",	"Japan",	"Ethiopia",	"Philippines",	"Egypt",	"Vietnam",	"DR Congo",	"Turkey",	"Iran",	"Germany",	"Thailand",	"United Kingdom",	"France",	"Italy",	"Tanzania",	"South Africa",	"Myanmar",	"Kenya",	"South Korea",	"Colombia",	"Spain",	"Uganda",	"Argentina",	"Algeria",	"Sudan",	"Ukraine",	"Iraq",	"Afghanistan",	"Poland",	"Canada",	"Morocco",	"Saudi Arabia",	"Uzbekistan",	"Peru",	"Angola",	"Malaysia",	"Mozambique",	"Ghana",	"Yemen",	"Nepal",	"Venezuela",	"Madagascar",	"Cameroon",	"Côte d'Ivoire",	"North Korea",	"Australia",	"Niger",	"Taiwan",	"Sri Lanka",	"Burkina Faso",	"Mali",	"Romania",	"Malawi",	"Chile",	"Kazakhstan",	"Zambia",	"Guatemala",	"Ecuador",	"Syria",	"Netherlands",	"Senegal",	"Cambodia",	"Chad",	"Somalia",	"Zimbabwe",	"Guinea",	"Rwanda",	"Benin",	"Burundi",	"Tunisia",	"Bolivia",	"Belgium",	"Haiti",	"Cuba",	"South Sudan",	"Dominican Republic",	"Czech Republic (Czechia)",	"Greece",	"Jordan",	"Portugal",	"Azerbaijan",	"Sweden",	"Honduras",	"United Arab Emirates",	"Hungary",	"Tajikistan",	"Belarus",	"Austria",	"Papua New Guinea",	"Serbia",	"Israel",	"Switzerland",	"Togo",	"Sierra Leone",	"Hong Kong",	"Laos",	"Paraguay",	"Bulgaria",	"Libya",	"Lebanon",	"Nicaragua",	"Kyrgyzstan",	"El Salvador",	"Turkmenistan",	"Singapore",	"Denmark",	"Finland",	"Congo",	"Slovakia",	"Norway",	"Oman",	"State of Palestine",	"Costa Rica",	"Liberia",	"Ireland",	"Central African Republic",	"New Zealand",	"Mauritania",	"Panama",	"Kuwait",	"Croatia",	"Moldova",	"Georgia",	"Eritrea",	"Uruguay",	"Bosnia and Herzegovina",	"Mongolia",	"Armenia",	"Jamaica",	"Qatar",	"Albania",	"Puerto Rico",	"Lithuania",	"Namibia",	"Gambia",	"Botswana",	"Gabon",	"Lesotho",	"North Macedonia",	"Slovenia",	"Guinea-Bissau",	"Latvia",	"Bahrain",	"Equatorial Guinea",	"Trinidad and Tobago",	"Estonia",	"Timor-Leste",	"Mauritius",	"Cyprus",	"Eswatini",	"Djibouti",	"Fiji",	"Réunion",	"Comoros",	"Guyana",	"Bhutan",	"Solomon Islands",	"Macao",	"Montenegro",	"Luxembourg",	"Western Sahara",	"Suriname",	"Cabo Verde",	"Micronesia",	"Maldives",	"Malta",	"Brunei",	"Guadeloupe",	"Belize",	"Bahamas",	"Martinique",	"Iceland",	"Vanuatu",	"French Guiana",	"Barbados",	"New Caledonia",	"French Polynesia",	"Mayotte",	"Sao Tome & Principe",	"Samoa",	"Saint Lucia",	"Channel Islands",	"Guam",	"Curaçao",	"Kiribati",	"Grenada",	"St. Vincent & Grenadines",	"Aruba",	"Tonga",	"U.S. Virgin Islands",	"Seychelles",	"Antigua and Barbuda",	"Isle of Man",	"Andorra",	"Dominica",	"Cayman Islands",	"Bermuda",	"Marshall Islands",	"Northern Mariana Islands",	"Greenland",	"American Samoa",	"Saint Kitts & Nevis",	"Faeroe Islands",	"Sint Maarten",	"Monaco",	"Turks and Caicos",	"Saint Martin",	"Liechtenstein",	"San Marino",	"Gibraltar",	"British Virgin Islands",	"Caribbean Netherlands",	"Palau",	"Cook Islands",	"Anguilla",	"Tuvalu",	"Wallis & Futuna",	"Nauru",	"Saint Barthelemy",	"Saint Helena",	"Saint Pierre & Miquelon",	"Montserrat",	"Falkland Islands",	"Niue",	"Tokelau",	"Holy See"])
print(C)

# Set up Distance Matrices
# Distance from API site to Manufacturing Site
r_
# Distance from Manufacturing Site to Country
k_

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
