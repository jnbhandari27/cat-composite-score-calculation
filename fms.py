composite_score = 0
gender = int(input("Enter 1 if Male or 2 if Female: "))
if gender == 2:
    composite_score+=5
varc = float(input("Enter VARC Scaled Score: "))
dilr = float(input("Enter DILR Scaled Score: "))
qa = float(input("Enter QA Scaled Score: "))
composite_score+= varc*40/72 + dilr*30/60 + qa*30/66
print("Your composite score is: ", composite_score)
