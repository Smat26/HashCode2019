from problem import Slideshow, Slide
def create_slideshow_from_slides(slides):
    return Slideshow(slides)

def create_slides_from_photos(photos):
    slides = []
    for i, photo in enumerate(photos):
        if photo.orientation == 'H':
            slide = Slide(photo.tags, [i])
            slides.append(slide)
    return slides 

## Bubble Sort
        # index = 0
        # innerIndex = 0
        # for _ in range(len(self.slides)):
        #     while index < len(self.slides):
        #         maxScore = 0
        #         while innerIndex < len(self.slides):
        #             if self.slides[index].calculate_interest(self.slides[innerIndex]) > maxScore:
        #                 print("Found max score at index:" + str(innerIndex) + " " + str(maxScore) )
        #                 maxScore = self.slides[index].calculate_interest(self.slides[innerIndex])
        #                 ejectedSlide = self.slides[index + 1]
        #                 self.slides[index + 1] = self.slides[innerIndex]
        #                 self.slides[innerIndex] = ejectedSlide
        #             innerIndex = innerIndex + 1
        #         index = index + 1

## Random Mutations

        # trail = 0
        # while trail < 100:
        #     print(str(trail) + " out of " + str(len(self.slides)))
        #     oldScore = self.calculateScore()
        #     indexA = random.randint(0,len(self.slides) - 1)
        #     indexB = random.randint(0,len(self.slides) - 1)
        #     self.slides[indexA], self.slides[indexB] = self.slides[indexB], self.slides[indexA]
        #     if self.calculateScore() < oldScore:
        #         self.slides[indexA], self.slides[indexB] = self.slides[indexB], self.slides[indexA]
        #     trail = trail + 1