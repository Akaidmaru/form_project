from django.shortcuts import render
from .forms import OrderForm

initial = {"email": "user@example.com"}


# Create your views here.
def form_example(request):
	for name in request.POST:
		print(f"{name}: {request.POST.getlist(name)}")
	return render(request, "form-example.html", {"method": request.method})


def form_example(request):
	if request.method == "POST":
		form = OrderForm(request.POST, initial=initial)
		if form.is_valid():
			for name, value in form.cleaned_data.items():
													print(f"{name}: ({type(value)}) {value}")

	else:
		form = OrderForm(initial=initial)

	return render(request, "form-example.html", 
		{"method": request.method, "form": form})
