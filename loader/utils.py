
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def save_picture(picture) -> str:
    filename = picture.filename

    path = f'./uploads/images/{filename}'

    picture.save(path)

    return path


def is_picture(picture) -> bool:
    extension = picture.filename.split(".")[-1]

    if extension in ALLOWED_EXTENSIONS:
        return True
    else:
        return False
