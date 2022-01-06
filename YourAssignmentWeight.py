
class Grades:
    """
        A script to calculate percentage of marks obtained based on weightage of the assignment.
    """
    totalGrades ={}
    def __init__(self, theSubject, theMarks, theWeightage, theTotalWeightage, theCa):
        self.subject = theSubject
        self.marks = theMarks
        self.weightage = theWeightage
        self.totalweightage = theTotalWeightage
        self.ca = theCa
    
    def __str__(self):
        return "this program calculates your grades for the assignment no.{self.ca} for the subject {self.subject}".format(self=self)

    def Marks(self):
        return self.marks

    def assignmentGrade(self):
        num = ((self.marks)*(self.weightage/self.totalweightage))
        self.totalGrades.update({self.ca:num})
        return self.totalGrades

    def subGrade(self):
        values = self.totalGrades.values()
        total = sum(values) 
        return total

CA1 = Grades("Maths", 99, 10, 100, "CA1")
CA2 = Grades("Maths", 94, 10, 100, "CA2")
CA3 = Grades("Maths", 100, 10, 100, "CA3")
print(CA1.assignmentGrade())
print(CA2.assignmentGrade())
print(CA3.assignmentGrade())
print(CA3.subGrade())


