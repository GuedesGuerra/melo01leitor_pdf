# views.py
from django.shortcuts import render, redirect
from .forms import PastaForm
from a00main import LeitorDeGia
def minha_interface(request):
    if request.method == 'POST':
        form = PastaForm(request.POST)
        if form.is_valid():
            caminho_da_pasta = form.cleaned_data['caminho']
            print(f'Caminho da pasta: {caminho_da_pasta}')

            for  i in caminho_da_pasta:
                print(i)
                print(type(i))
            print(type(form))
            form.save()
            leitor_gia = LeitorDeGia()
            leitor_gia._ininicializador(caminho_da_pasta, caminho_da_pasta)
            leitor_gia._captura_de_gia()
            return redirect('minha_interface')  # Redireciona para a mesma página após o envio do formulário
    else:
        form = PastaForm()

    return render(request, 'minha_interface.html', {'form': form})
