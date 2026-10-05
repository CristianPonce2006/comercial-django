from django.shortcuts import render

def lista_categoria(request):
    lista_categoria = [
        {
            'nombre': 'tv',
            'descripcion': "televisor alta gama"
            
        },
        {
            'nombre': 'tv 2',
            'descripcion': "televisor alta gama 2"
                    
        }
    ]

    return render(request, "categoria/lista.html", context={'categorias': lista_categoria})