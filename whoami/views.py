from django.shortcuts import render

STUDENT_ID = '10957050'
NAME = '林欣鈺'

def whoamI(request):
    context = {
        'line1': '台北商業大學',
        'line2': '五專資管科',
        'line3': STUDENT_ID,
        'line4': NAME,
    }
    return render(request, 'whoamI.html', context)
