from django.shortcuts import render, redirect
from django.http import HttpResponse
from docx import Document
import os

# Função para exibir a página inicial e redirecionar conforme a escolha
def home(request):
    if request.method == 'POST':
        modalidade = request.POST.get('modalidade')
        tipo = request.POST.get('tipo')
        if modalidade == 'dispensa':
            return redirect('dispensa_form')
        # Outros redirecionamentos podem ser adicionados aqui
    return render(request, 'home.html')

# Função para o formulário de dispensa
def dispensa_form(request):
    if request.method == 'POST':
        # Coleta dos dados do formulário
        objeto = request.POST.get('objeto')
        justificativa = request.POST.get('justificativa')
        processo_administrativo = request.POST.get('processo_administrativo')
        prazo_vigencia = request.POST.get('prazo_vigencia')

        # Carrega o modelo base da AGU
        modelo_path = os.path.join(os.path.dirname(__file__), 'modelos', 'dispensa.docx')
        doc = Document(modelo_path)

        # Preenche os campos no documento
        for paragraph in doc.paragraphs:
            if '<<Objeto>>' in paragraph.text:
                paragraph.text = paragraph.text.replace('<<Objeto>>', objeto)
            if '<<Justificativa>>' in paragraph.text:
                paragraph.text = paragraph.text.replace('<<Justificativa>>', justificativa)
            if '<<ProcessoAdministrativo>>' in paragraph.text:
                paragraph.text = paragraph.text.replace('<<ProcessoAdministrativo>>', processo_administrativo)
            if '<<PrazoVigencia>>' in paragraph.text:
                paragraph.text = paragraph.text.replace('<<PrazoVigencia>>', prazo_vigencia)

        # Gera o arquivo para download
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename="Termo_de_Referencia_Dispensa.docx"'
        doc.save(response)
        return response

    return render(request, 'dispensa_form.html')
