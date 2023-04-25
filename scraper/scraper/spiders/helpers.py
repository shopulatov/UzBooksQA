def xpath_text_blocks():
    tags = ['ul', 'blockquote', 'p', 'ol', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div']
    internal = "or".join([f"name()='{tag}'" for tag in tags])
    return f'*[{internal}]'