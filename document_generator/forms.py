from django import forms

class CamposDinamicosForm(forms.Form):
    processo_administrativo = forms.CharField(label="Número do Processo Administrativo", max_length=50)
    objeto = forms.CharField(label="Descrição do Objeto", max_length=200)
    tipo_vigencia = forms.ChoiceField(
        label="Prazo de Vigência",
        choices=[
            ("a", "Entrega única (Art. 105)"),
            ("b", "Entrega contínua (Art. 106)"),
            ("c", "Emergencial (Art. 75, VIII)"),
        ],
    )
    num_criterios = forms.IntegerField(label="Quantidade de Critérios de Sustentabilidade", min_value=1, initial=1)
    luxury_item = forms.ChoiceField(
        label="O objeto é um bem de luxo?",
        choices=[("no", "Não"), ("yes", "Sim")],
    )
    justificativa = forms.CharField(
        label="Justificativa da Contratação",
        widget=forms.Textarea,
        required=False,
        help_text="Deixe em branco para usar a justificativa padrão."
    )
    plano_contratacoes = forms.ChoiceField(
        label="A contratação está prevista no PCA?",
        choices=[("sim", "Sim"), ("nao", "Não")],
    )

class ItensForm(forms.Form):
    num_itens = forms.IntegerField(label="Quantidade de Itens", min_value=1, initial=1)
    num_lotes = forms.IntegerField(label="Quantidade de Lotes", min_value=1, initial=1)
