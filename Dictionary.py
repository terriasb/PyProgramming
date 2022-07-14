monthConversions = {  # "KEY": "Value"
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthConversions["Jan"])
print(monthConversions.get("Jan"))
print(monthConversions.get("LOVE", "Not an Applicable Key")) # You can include a default value for when a key isnt in the dictionary