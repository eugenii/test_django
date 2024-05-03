from django.shortcuts import render


def law_list(request):
    template_name = 'catalog/law_list.html'
    title = 'список законов'
    context = {
        'laws': phys_laws_catalog,
        'title': title,
    }
    return render(request, template_name, context)


def law_detail(request, pk):
    template_name = "catalog/law_detail.html"
    context = {
        'law_detail': phys_laws_catalog[pk]
    }
    return render(request, template_name, context)


phys_laws_catalog = [
    {
        'id': 1,
        'title': 'Закон Ома для участка цепи',
        'section': 'Электродинамика',
        'author': 'Георг Ом',
        'year': 1857,
        'text': 'Сила тока в участке цепи прямо пропорциональна напряжению'
                ' на концах этого участка и обрато пропорциональна'
                ' сопротивлению этого участка',
        'country': 'Германия',
    },
    {
        'id': 2,
        'title': '1 закон Ньютона',
        'section': 'Механика',
        'author': 'Исаак Ньютон',
        'year': 1687,
        'text': 'Существуют такие системы отсчёта, в которых тела сохраняют '
                'состояние покоя или прямоленейного и равномерного двжения'
                ' если равнодействующая всех сил, приложенных к телу'
                ' равна нулю',
        'country': 'Англия',
    },
    {
        'id': 3,
        'title': 'Закон Архимеда',
        'section': 'Механика',
        'author': 'Архимед',
        'year': -300,
        'text': 'На тело, погружённое в жидкость или в газ действует'
                ' выталкивающая сила, равная весу вытесненной жидкости (газа)',
        'country': 'Греция',
    },
    {
        'id': 4,
        'title': 'Закон электромагнитной индукции',
        'section': 'Электродинамика',
        'author': 'Майкл Фарадей',
        'year': 1857,
        'text': 'ЭДС индукции в замкнутом контуре равна и противоположна'
                ' по знаку скорости изменения магнитного потока через'
                ' поверхность, ограниченную контуром.',
        'country': 'Англия',
    },
    {
        'id': 5,
        'title': 'Давление смеси газов',
        'section': 'МКТ и Т/Д',
        'author': 'Джон Дальтон',
        'year': 1801,
        'text': 'Давление смеси газов равно сумме'
                ' парциальных давлений газов смеси',
        'country': 'Англия',
    },
]
