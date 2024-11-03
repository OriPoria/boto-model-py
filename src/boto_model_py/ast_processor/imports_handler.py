import ast
import astor
from typing import Union

from boto_model_py.consts_source_code import base_response_code, datatime_import, enum_import


def append_source_imports_based_on_field_types_required(source_code: str,
                                                        map_from_value_of_temp_datetime_to_list_of_path,
                                                        map_from_value_of_temp_enum_to_list_of_path,
                                                        enum_classes_ast):
    base_response_code_ast = ast.parse(base_response_code).body
    ast_object = ast.parse(source_code)

    for b_r in base_response_code_ast:
        if isinstance(b_r, ast.ImportFrom):
            ast_object.body.insert(1, b_r)
        else:
            ast_object.body.insert(3, b_r)
    if map_from_value_of_temp_datetime_to_list_of_path:
        ast_object.body.insert(1, ast.parse(datatime_import).body[0])
    if map_from_value_of_temp_enum_to_list_of_path:
        ast_object.body.insert(1, ast.parse(enum_import).body[0])

    for e_c in enum_classes_ast:
        ast_object.body.insert(3, e_c)
    return ast_object


def merge_imports(import_nodes) -> list[Union[ast.Import, ast.ImportFrom]]:
    imports_dict = {}
    import_from_dict = {}

    for node in import_nodes:
        if isinstance(node, ast.Import):
            # Handle ast.Import: Key on the module being imported
            for alias in node.names:
                if alias.name not in imports_dict:
                    imports_dict[alias.name] = alias
                elif alias.asname:  # Replace if alias is present
                    imports_dict[alias.name] = alias

        elif isinstance(node, ast.ImportFrom):
            # Handle ast.ImportFrom: Key on the module and aggregate names
            module_key = (
                node.module,
                node.level,
            )  # Use both module and level for relative imports
            if module_key not in import_from_dict:
                import_from_dict[module_key] = {}

            for alias in node.names:
                if alias.name not in import_from_dict[module_key]:
                    import_from_dict[module_key][alias.name] = alias
                elif alias.asname:  # Replace if alias is present
                    import_from_dict[module_key][alias.name] = alias

    new_imports = (
        [ast.Import(names=list(imports_dict.values()))] if imports_dict else list()
    )

    import_from_collection = []
    for (module, level), names in import_from_dict.items():
        import_from = ast.ImportFrom(
            module=module, names=list(names.values()), level=level
        )
        import_from_collection.append(import_from)
    return new_imports + import_from_collection


def _transform(node):
    imports = list()
    body = list()
    for n in node.body:
        if isinstance(n, ast.ImportFrom) or isinstance(n, ast.Import):
            imports.append(n)
        else:
            body.append(n)
    imports = merge_imports(imports)
    imports.extend(body)
    node.body = imports
    return node


def sort_imports(ast_object) -> str:
    _transform(ast_object)
    return astor.to_source(ast_object)
