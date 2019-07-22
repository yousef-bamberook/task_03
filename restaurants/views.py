from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    		'my_list': [
    			{"restaurant_name": "Maasoub Al-sultan", "food_type": "Maasoub Cream and Milk"},
    			{"restaurant_name": "Al-bailk", "food_type": "Chicken"},
    			{"restaurant_name": "Maqram restaurant", "food_type": "Kabsaa"}
    		]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
		'my_object':
			{"restaurant_name": "Maasoub Al-sultan", "food_type": "Maasoub Cream and Milk"},}
    return render(request, 'detail.html', context)
