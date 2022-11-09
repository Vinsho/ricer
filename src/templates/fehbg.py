class FehbgTemplate:
    path = ".fehbg"

    template = """
    #!/bin/sh
    feh --no-fehbg --bg-scale '{image_path}'"""
