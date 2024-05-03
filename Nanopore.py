from manim import *
import random

class TwoRectangles(ThreeDScene):
    def construct(self):
        # Define rectangle dimensions and gap size
        rectangle_width = 8
        rectangle_height = 1
        gap_width = 2

        # Create rectangles
        left_rectangle = Rectangle(width=rectangle_width, height=rectangle_height, color=GRAY, fill_opacity=1)
        right_rectangle = Rectangle(width=rectangle_width, height=rectangle_height, color=GRAY, fill_opacity=1)

        # Position rectangles with gap in between
        left_rectangle.move_to(LEFT * (rectangle_width + gap_width) / 2)
        right_rectangle.move_to(RIGHT * (rectangle_width + gap_width) / 2)

        rectangles = VGroup(left_rectangle, right_rectangle)

        curve1 = ParametricFunction(
            lambda u: np.array([
                0.6 * np.cos(u),
                -0.5 * u,
                0.6 * np.sin(u)
            ]), color=RED, t_range = np.array([-12*TAU, 1.25*TAU, 0.01])
        ).set_shade_in_3d(True)

        lines = VGroup()
        for u in range(-75, 10):
            l = Line([0.6 * np.cos(u), u * -0.5, 0.6 * np.sin(u)], [0.2 * np.cos(u), u * -0.5, 0.2 * np.sin(u)])
            lines.add(l)

        # Animate rectangles appearing on screen
        # self.add_fixed_in_frame_mobjects(rectangles)
        self.add_fixed_in_frame_mobjects(rectangles)

        Posve = ImageMobject("Positive_Charge.png")
        self.play(FadeIn(Posve))
        Posve.generate_target()
        Posve.target.move_to(LEFT*4.5+DOWN*1.9)
        self.play(MoveToTarget(Posve))
        Negve = ImageMobject("Negative_Charge.png")
        self.play(FadeIn(Negve))
        Negve.generate_target()
        Negve.target.move_to(LEFT*4.5+UP*1.9)
        self.play(MoveToTarget(Negve))

        self.play(Create(curve1))
        self.play(Create(lines))
        myGroup = VGroup(curve1, lines)
        self.wait(1)
        
        self.play(myGroup.animate.shift(DOWN*50))
        self.remove(myGroup)
        # Keep the scene on screen for a bit
        self.wait(2)
        image = ImageMobject("Nanopore_image.png").scale(1.1)
        self.play(FadeIn(image))
        # database1.generate_target()
        # database1.target.move_to(LEFT*3.9+UP*1.9)

        curve2 = ParametricFunction(
            lambda u: np.array([
                0.3 * np.cos(u),
                -0.25 * u,
                0.3 * np.sin(u)
            ]), color=RED, t_range = np.array([-12*TAU, 3*TAU, 0.01])
        ).set_shade_in_3d(True)

        lines2 = VGroup()
        for u in range(-75, 20):
            l = Line([0.3 * np.cos(u), u * -0.25, 0.3 * np.sin(u)], [0.1 * np.cos(u), u * -0.25, 0.1 * np.sin(u)])
            lines2.add(l)

        myGroup2 = VGroup(curve2, lines2)

        self.play(Create(curve2))
        self.play(Create(lines2))

         # Parameters
        num_periods = 5
        max_width = 0.5
        max_height = 0.01

        # Create axes
        axes = Axes(
            x_range=[num_periods * 3.5 * PI, num_periods * 5 * PI, 0.1 * PI],
            y_range=[-max_height, max_height, max_height / 8],
            axis_config={"color": BLUE},
        )

        # Generate random points for the square signal
        points = [(0, 0)]
        for i in range(num_periods):
            width = random.uniform(0.3, max_width)
            height = random.uniform(0.001, max_height)
            points.extend([
                (i * 2 * PI, height),
                ((i + width) * 2 * PI, height),
                ((i + width) * 2 * PI, -height),
                ((i + 1) * 2 * PI, -height),
                ((i + 1) * 2 * PI, 0),
            ])

        # Convert points to coordinates
        coords = [axes.coords_to_point(x, y) for x, y in points]

        # Create the graph
        graph = VGroup()
        for i in range(len(coords) - 1):
            graph.add(Line(coords[i], coords[i + 1]))

        # Add axes and final graph to scene
        self.add(graph)
        
        self.play(
            myGroup2.animate(run_time=5, rate_func=rate_functions.linear).shift(DOWN*5), 
            graph.animate(run_time=5, rate_func = rate_functions.linear).shift(RIGHT * axes.x_range[1])
        )
        # self.remove(myGroup2)
        # Keep the scene on screen for a bit
        # self.wait(2)
