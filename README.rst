============
Model Server
============

The Model Server aims to simplifying the process of serving a model.

Install
=======

.. code-block::

    pip install model_server

Usage
=====

.. code-block:: python

    import model_server

    def bottle_configuration_function(bottle):
      # Configure bottle
      pass

    plugins = [
      SomePlugin,
      ...
    ]

    app, run_server = model_server(plugins, bottle_configuration_function)

