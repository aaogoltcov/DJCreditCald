from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"
    common_result = float()
    result = float()
    form = CalcForm
    if request.method == 'GET':
        form = CalcForm(request.GET)
        if form.is_valid():
            print(form)
            print(request.GET)
            common_result = float(request.GET.get('initial_fee')) + \
                            float(request.GET.get('initial_fee')) * \
                            float(request.GET.get('rate')) / 100
            result = common_result / int(request.GET.get('months_count'))
    else:
        form = form
    context = {
        'form': form,
        'common_result': int(common_result),
        'result': int(result),
    }
    return render(request, template, context)
