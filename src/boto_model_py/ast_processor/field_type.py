import ast


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
