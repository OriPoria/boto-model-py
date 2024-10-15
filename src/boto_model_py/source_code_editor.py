

def _replace_base_model_type(source_code: str) -> str:
    return source_code.replace("(BaseModel):", "(BaseResponse):")


def _replace_default_values(source_code: str) -> str:
    return source_code.replace(" = None", "")

def edit_source_code(source_code: str) -> str:
    source_code = _replace_default_values(source_code)
    return _replace_base_model_type(source_code)
