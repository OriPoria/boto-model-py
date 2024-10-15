import ast
from typing import Union


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


class ImportSorter(ast.NodeTransformer):

    def transform(self, node):
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


def change_ast_field_type(
    ast_object_, dict_of_values: dict, actual_type: str, main_class_name: str
):
    for list_of_path in dict_of_values.values():
        next_class = main_class_name
        list_of_path.insert(0, main_class_name)
        len_of_path = len(list_of_path)
        for index in range(0, len_of_path - 1):
            for node in ast.walk(ast_object_):
                if isinstance(node, ast.ClassDef) and node.name == next_class:
                    next_attribute = list_of_path[index + 1]
                    for class_body_item in node.body:
                        if (
                            isinstance(class_body_item, ast.AnnAssign)
                            and class_body_item.target.id == next_attribute
                        ):

                            def get_root_type(
                                class_body_item_, iteration_until_value: int
                            ):
                                if "slice" in class_body_item_.__dict__:
                                    iteration_until_value += 1
                                    return get_root_type(
                                        class_body_item_.slice, iteration_until_value
                                    )
                                else:
                                    assert isinstance(class_body_item_, ast.Name)
                                    return class_body_item_.id, iteration_until_value

                            next_class, iterations = get_root_type(
                                class_body_item.annotation, 0
                            )
                            if next_class == "str":
                                if iterations == 1:
                                    class_body_item.annotation.slice.id = actual_type
                                elif iterations == 2:
                                    class_body_item.annotation.slice.slice.id = (
                                        actual_type
                                    )
                                else:
                                    raise NotImplemented(
                                        "More than 2 iteration until value is not supported"
                                    )
