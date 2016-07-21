=====
Django Slider Flickity
=====

Заготовка под слайдер

Как установить:
-----------
0. Установить через pip:

pip install https://raw.githubusercontent.com/LastDreamer/django-common-apps/master/slider/dist/slider-0.1.tar.gz

1. Добаить "slides" в settings.py

INSTALLED_APPS = [
  ...
  'slides',
  ...
]

2. Унаследовать модель в главном модуле приложения:

from slides.models import Slide as VendorSlide

class Slide(VendorSlide):
    class Meta(VendorSlide.Meta):
        pass

3. Вставить слайдер на страницу:

{% include "slider.djhtml" with slides=slides %}

4. Добавить подгрузку статики в нужный шаблон:

{% block css %}
	<link href="/static/css/carousel.css" rel="stylesheet"/>
{% endblock %}

{% block scripts %}
	<link href="/static/css/flickity.css" rel="stylesheet"/>
	<script src="/static/js/flickity.min.js"></script>
{% endblock scripts %}
