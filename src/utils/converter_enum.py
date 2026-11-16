def converter_enum(enum_class, valor):
    try:
        return enum_class(valor) if valor else None
    except ValueError:
        return None