from django.db import models

# Create your models here.

#組織成員
class Member(models.Model):
    MemberID = models.IntegerField()
    CheckIn = models.BooleanField(default=False)
    StartTime = models.DateTimeField()

    def __str__(self):
        return f"{self.MemberID}"

#請假(補假)申請、紀錄
class LeaveApply(models.Model):
    MemberID = models.IntegerField()
    Start = models.DateTimeField()
    End = models.DateTimeField()
    Info = models.TextField()
    Applied = models.BooleanField(default=False)

    def __str__(self):
        return f"ID {self.id} / {self.Start} ~ {self.End} / {self.Info}"

#出缺勤紀錄
class Attendant(models.Model):
    MemberID = models.IntegerField()
    Start = models.DateTimeField()
    End = models.DateTimeField()
    Info = models.TextField(default="")

    def __str__(self):
        return f"ID {self.id} / {self.Start} ~ {self.End} / {self.Info}"

# #請假補假申請
# class LeaveApply(models.Model):
#     ApplierID = models.IntegerField()
#     AttendantID = models.IntegerField()
#     LeaveType = models.BooleanField()
#     LeaveInfo = models.TextField()

#     def __str__(self):
#         return f"ID {self.id} / ApplierID {self.ApplierID} / LeaveInfo {self.LeaveInfo}"
