dict = {
    "name" : "Karthikeya Mannem",
    "SGPA" : 9.0,
    "Subjects" : {
        "Maths" : 100,
        "Phy" : 95,
        "Chem" : 90
    }
}
print(dict)

print(dict["name"])
print(dict["SGPA"])
print(dict["Subjects"])

dict["name"] = "karthik"
print(dict)

print(dict["Subjects"]["Chem"])

print(list(dict.keys()))
print(list(dict.values()))
print(list(dict.items()))
print(list(dict.get("Subjects")))