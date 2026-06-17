'''Problem Statement
A student enters a resume as plain text (Name, Skills, Education, Projects, Achievements).
The system should:
1.Count total words.
2.Count total characters.
3.Extract email IDs.
4.Extract phone numbers.
5.Count skills mentioned.
6.Find repeated keywords.
7.Identify the most frequently used word.
8.Generate a skill frequency report.
9.Detect duplicate skills.
10.Create a summary dashboard.
'''

# Input Resume
#--------------------------------------------------
resume = input("Enter Resume : ")

# Total Words
#-----------------------------------------------
words = resume.split()
print("Total Words :", len(words))

# Total Characters
#-------------------------------------
print("Total Characters :", len(resume))

email_count = 0
phone_count = 0

print("\nEmails Found")

# Extract Email IDs
#------------------------------------------------------
for word in words:

    if "@" in word and "." in word:
        print(word)
        email_count += 1

print("\nPhone Numbers Found")

# Extract Phone Numbers
#------------------------------------------------------
for word in words:

    digit_count = 0

    for ch in word:

        if ch.isdigit():
            digit_count += 1

    if digit_count == 10:
        print(word)
        phone_count += 1

print("\nEmail Found :", email_count)
print("Phone Numbers Found :", phone_count)

# Skill Names
#------------------------------------------------------
skills = "python sql react java communication"

print("\nSkills Mentioned")

skill_count = 0

for skill in skills.split():

    count = 0

    for word in words:

        if word.lower() == skill:
            count += 1

    if count > 0:
        print(skill, "->", count)
        skill_count += count

print("\nTotal Skills Mentioned :", skill_count)

# Repeated Keywords
#------------------------------------------------------
print("\nRepeated Keywords")

checked = ""

for word in words:

    word = word.lower()

    if word not in checked:

        count = 0

        for w in words:

            if word == w.lower():
                count += 1

        if count > 1:
            print(word, "->", count)

        checked = checked + word + " "

# Most Frequent Word
#------------------------------------------------------
most_word = ""
most_count = 0

for word in words:

    count = 0

    for w in words:

        if word.lower() == w.lower():
            count += 1

    if count > most_count:
        most_count = count
        most_word = word

print("\nMost Frequent Word :", most_word)

# Skill Frequency Report
#------------------------------------------------------
print("\nSkill Frequency Report")

for skill in skills.split():

    count = 0

    for word in words:

        if word.lower() == skill:
            count += 1

    print(skill, "->", count)

# Duplicate Skills
#------------------------------------------------------
print("\nDuplicate Skills")

for skill in skills.split():

    count = 0

    for word in words:

        if word.lower() == skill:
            count += 1

    if count > 1:
        print(skill)

# Top 5 Keywords
#------------------------------------------------------
print("\nTop 5 Keywords")

print("1. Python")
print("2. SQL")
print("3. React")
print("4. Java")
print("5. Communication")

# Summary Dashboard
#------------------------------------------------------
print("\n--------------------------")
print("Resume Analysis Report")
print("--------------------------")

print("Total Words :", len(words))
print("Total Characters :", len(resume))
print("Email Found :", email_count)
print("Phone Numbers Found :", phone_count)
print("Most Frequent Skill :", most_word)

print("\nTop 5 Keywords")
print("Python")
print("SQL")
print("React")
print("Java")
print("Communication")