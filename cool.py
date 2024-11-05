import manim

class shush(Scene):
    def construct(self):
        colors = ["#132930","#006494","#247BA0","#1B98E0"]
        g = VGroup()
        for i in range(5):
            d = Dot(color = colors(i),
                    sheen_factor = -0.25,
                    ). scale (30-i*4)
            g.add (d)
        t = Text("Yoink")
        self.play(Write(d), run_time = 0.5)
        self.wait()
        self.play(ReplacementTransform(g, t))
        self.wait(3)