from django.shortcuts import render


def main(request):
    context = {'data': 'some text'}
    return render(request, 'base/main.htm', context=context)
