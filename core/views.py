# @Date:   2017-05-20T19:44:50+05:30
# @Last modified time: 2017-05-21T12:21:10+05:30



from django.shortcuts import render

# Create your views here.
from core.models import TestData

def getTestData(request):
    """returns the test data from all the databases"""
    databases=('testdb1','testdb2','testdb3','testdb4','testdb5')
    data=[]
    for database in databases:
        data.append(TestData.objects.using(database).values_list('desc',flat=True))
    return render(request,'index.html',{"title":"TestData",'data':data})
