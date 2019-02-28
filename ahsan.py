def create_slideshow_from_slides(slides):
    return Slideshow(slides)

def create_slides_from_photos(photos):
    slides = []
    for i, photo in enumerate(photos):
        if photo.orientation == 'H':
            slide = Slide(photo.tags, [i])
            slides.append(slide)
    return slides 
