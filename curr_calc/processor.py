from djanotask.curr_calc.models import Currency_Details

def currencies(request):
    return {'currencies': Currency_Details.objects.all()}
