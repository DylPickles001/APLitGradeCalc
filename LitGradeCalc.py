print('Welcome! With this program, you can find out what your overall AP Lit grade is.')
print('For the following questions, simply type out the percentages as numbers.')
print('Example: "48.2% in a category", just type out 48.2 ')
print('Make sure you have also have AERIES open to see the %s you have for each category')
ask = input('First of all, which semester of AP Lit are you in? Type 1 or 2 : ')
if ask == '1':
  QT = float(input('What % do you have for the Quotation Test category? '))
  APT = float(input('What % do you have for the AP-style Tests/Quizzes category? : '))
  SUM = float(input('What % do you have for the Summer Assignment category? : '))
  HW = float(input('What % do you have for the T-Notes/Critical Sources category? : '))
  P = float(input('What % do you have for the Participation category? : '))
  askF = input('Have you taken the final yet? Type either "yes" or "no". ')
  if askF == 'yes':
    F = float(input('What % do you have for the Final Exam category? '))
    def gwF ():
      grade = (QT /100)*35 + (APT/100)*25 + (SUM /100)*10 + (HW /100)*10 + (P /100)*10 + (F /100)*10
      print ('Your AP Lit grade is:',grade)
    gwF()
  if askF == 'no':
    def gwoF ():
      tot = (QT /100)*35 + (APT /100)*25 + (SUM /100)*10 + (HW /100)*10 + (P /100)*10
      grade = (tot /90)*100
      print ('Your AP Lit grade is:', grade)
    gwoF()
if ask == '2':
  QT = float(input('What % do you have for the Quotation Test category? '))
  APT = float(input('What % do you have for the AP-style Tests/Quizzes category? : '))
  HW = float(input('What % do you have for the T-Notes/Critical Sources category? : '))
  P = float(input('What % do you have for the Participation category? : '))
  askF = input('Have you completed the Senior Project yet? Type either "yes" or "no". ')
  if askF == 'yes':
    F = float(input('What % do you have for the Senior Project category? '))
    def gwF ():
      grade = (QT /100)*15 + (APT/100)*45 + (HW /100)*5 + (P /100)*20 + (F /100)*15
      print ('Your AP Lit grade is:',grade)
    gwF()
  if askF == 'no':
    def gwoF ():
      tot = (QT /100)*15 + (APT /100)*45 + (HW /100)*5 + (P /100)*20
      grade = (tot /85)*100
      print ('Your AP Lit grade is:', grade)
    gwoF()
