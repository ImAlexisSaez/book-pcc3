def make_car(manufacturer, model, **kwargs):
    """Imprime información del coche a fabricar."""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    print("\nInformación del modelo:")
    for k, v in kwargs.items():
        print(f"\t- {k.title()}: {v}")

car = make_car('subaru', 'outback', color='blue', tow_package=True)
