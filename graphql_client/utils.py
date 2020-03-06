def _get_updated_headers(primary_headers, headers):
    h = dict(**primary_headers)
    if headers and isinstance(headers, dict):
        h.update(headers)
    return h
