from regast.exceptions import ParsingError
from regast.parsing.types.type import Type

def parse_type(ctx) -> Type:    # TypeNameContext
    from regast.parsing.types.array_type import ArrayType
    from regast.parsing.types.elementary_type import ElementaryType
    from regast.parsing.types.function_type import FunctionType
    from regast.parsing.types.mapping_type import MappingType
    from regast.parsing.types.user_defined_type import UserDefinedType

    type_name_function_to_class_name = {
        'elementaryTypeName': ElementaryType,
        'userDefinedTypeName': UserDefinedType,
        'mapping': MappingType,
        'functionTypeName': FunctionType,
    }

    if ctx.PayableKeyword():
        return ElementaryType(ctx, is_address_payable=True)

    for type_name_function, class_name in type_name_function_to_class_name.items():
        type_result = getattr(ctx, type_name_function)()
        if type_result:
            return class_name(type_result)

    # If it does not belong to any of the above types, it is an array type
    return ArrayType(ctx)