============
Installation
============

Installing django-pjax-middleware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Install using pip::

    pip install git+https://github.com/bbrik/django-pjax-middleware.git

#. Add ``PjaxMiddleware`` to your ``MIDDLEWARE_CLASSES`` in settings.py:

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        ...
        'pjax.middleware.PjaxMiddleware',
    )

#. Add ``jquery`` and ``jquery_pjax`` to your static files


Usage
~~~~~

#. Add a template for full page render, default name is ``base.html``:

.. code-block:: html

    {% load staticfiles %}

    <!DOCTYPE html>
    <html>
      <head>
        <title>
          {% block title %}
          {% endblock title %}
        </title>
        
        {# should set layout version through a template context processor #}
        {# see PJAX_VERSION bellow #}
        <meta http-equiv="x-pjax-version" content="{{ version }}">
      </head>

      <body>
        <div id="pjax-container">
          {% block content %}
          {% endblock content %}
        </div>

        <script type="text/javascript" src="{% static 'js/jquery-1.9.1.min.js' %}"></script>
        <script type="text/javascript" src="{% static 'js/jquery.pjax.js' %}"></script>
        <script type="text/javascript">
          $document = $(document);
          
          $document.on('ready pjax:end', function() {
            // Use this for document ready code
          });
        
          $document.pjax('a[data-pjax]', '#pjax-container', {
            timeout: 3000
          });
        </script>
      </body>
    </html>


#. Add a template for pjax render, default name is ``pjax_base.html``:

.. code-block:: html

    {% load staticfiles %}

    <title>
      {% block title %}
      {% endblock title %}
    </title>

    {% block content %}
    {% endblock content %}


#. Use the variable ``base`` as the base for your templates:

.. code-block:: html

    {% extends base %}

    {% block title %}
      ...
    {% endblock title %}

    {% block content %}
      ...
    {% endblock content %}

#. Add ``data-pjax`` to any link you want to load using pjax:

.. code-block:: html

    <a data-pjax href="{% url 'home' %}">
      Home
    </a>


Custom settings
***************

BASE_TEMPLATE
+++++++++++++

Sets the full reload base template name. Default is ``base.html``.

PJAX_BASE_TEMPLATE
++++++++++++++++++

Sets the pjax reload template name. Default is ``pjax_base.html``.

PJAX_VERSION
++++++++++++

Sets the layout version for your site.
When you update your site layout, you should update this.
Should be the same value of the meta attribute in your base.html head.
This is a mechanism to trigger a full page reload when the site layout changes.
See pjax docs.

