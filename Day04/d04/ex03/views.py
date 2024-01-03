from django.shortcuts import render
 
def color(request):
    color = {'Black': [], 'Red': [], 'Green': [], 'Blue': []}
    for i in range(0, 256, 5):
        hexa = format(i, '02x')
        color['Black'].append('#' + hexa + hexa + hexa)
        color['Red'].append('#' + hexa + '0000')
        color['Green'].append('#00' + hexa + '00')
        color['Blue'].append('#0000' + hexa)

    color_list = list(zip(color['Black'], color['Red'], color['Green'], color['Blue']))

    return render(request, 'color.html', {'color_list': color_list})
