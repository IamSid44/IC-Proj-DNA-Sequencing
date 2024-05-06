from manim import *

class ShowImage(Scene):
  def construct(self):
    # Replace "path/to/your/image.jpg" with the actual path to your image file
    image = ImageMobject("deamer-notebook.png")

    # You can adjust the position and scale of the image here (optional)
    image.scale(2)  # Scale down the image by half
    image.move_to(ORIGIN)  # Move the image to the center of the screen

    # Add the image to the scene
    self.play(FadeIn(image))
    self.wait(1.5)
    self.play(image.animate.scale(0.5).move_to(DOWN*1.5))
    self.wait(3)

    text = Text("This shows Professor David Deamer's initial sketch for\n  sequencing DNA using a nanopore. He drew it after\n          pulling over to the side of the road during\n           a one-hour drive from one part of Oregon\n    to another. The text reads: 'Sunday June 25 1989.\n  Driving back from Eugene -> Belmont Lodge, had\n         an idea on how to sequence DNA directly.", color=RED).scale(0.6)
    text.to_edge(UP)
    self.play(Write(text))
    self.wait(7.5)
