============
Installation
============

Installing django-pjax-middleware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Install using pip::

    pip install git+ssh://git@github.com/bbrik/django-pjax-middleware.git

#. Add ``pjax`` to your ``INSTALLED_APPS`` in settings.py::

    INSTALLED_APPS = (
        ...
        'pjax',
    )

#. Add ``jquery`` and ``jquery_pjax`` to your static files


Usage
~~~~~

#. Add a template for full page render, default name is ``base.html``::

    {% load staticfiles %}

    <!DOCTYPE html>
    <html>
      <head>
        <title>
          {% block title %}
          {% endblock title %}
        </title>
      </head>

      <body>
        <div id="pjax-container">
          {% block content %}
          {% endblock content %}
        </div>

        <script type="text/javascript" src="{% static 'js/jquery-1.9.1.min.js' %}"></script>
        <script type="text/javascript" src="{% static 'js/jquery.pjax.js' %}"></script>
        <script type="text/javascript">
          $(document).pjax('a[data-pjax]', '#pjax-container', {
            timeout: 3000
          });
        </script>
      </body>
    </html>


#. Add a template for pjax render, default name is ``pjax_base.html``::

    {% load staticfiles %}

    <title>
      {% block title %}
      {% endblock title %}
    </title>

    {% block content %}
    {% endblock content %}


#. Use the variable ``base`` as the base for your templates::

    {% extends base %}

    {% block title %}
      ...
    {% endblock title %}

    {% block content %}
      ...
    {% endblock content %}


#. The middleware will set ``base`` variable to the correct template name,
based on the request header

#. Add ``data-pjax`` to any link you want to load using pjax::

    <a data-pjax href="{% url 'home' %}">
      Home
    </a>
