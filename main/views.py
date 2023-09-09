from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Vinka Alrezky As',
        'id': '2206820200',
        'class': 'PBP A'
    }

    return render(request, "main.html", context = context)
