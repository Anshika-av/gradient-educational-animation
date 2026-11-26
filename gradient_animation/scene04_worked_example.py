"""
==============================================================
 SCENE 04 — Step-by-Step Worked Example
 Subject : Mathematics 3 — Linear Algebra and Calculus
 Topic   : The Gradient
 Student : Anshika Verma | E25B070603
 College : Newton School of Technology
 Target  : ~80 seconds
==============================================================
"""

from manim import *
import numpy as np

# Colour palette
NAVY        = ManimColor("#003087")
ROYAL_BLUE  = ManimColor("#4169E1")
DEEP_PURPLE = ManimColor("#6A0DAD")
STEEL_BLUE  = ManimColor("#4682B4")
LIGHT_BLUE  = ManimColor("#B0C4DE")
ORANGE_VEC  = ManimColor("#FF6600")
POINT_RED   = ManimColor("#E63946")
BG_LIGHT    = ManimColor("#F4F6FF")


class Scene04WorkedExample(Scene):
    """
    Scene 4: Step-by-Step Mathematical Computation
    - Problem Statement: f(x, y) = x² + y² at P(1, 2)
    - Step 1: ∂f/∂x = 2x
    - Step 2: ∂f/∂y = 2y
    - Step 3: ∇f = (2x, 2y)
    - Step 4: ∇f(1, 2) = (2, 4)
    - Step 5: |∇f(1, 2)| = √(2² + 4²) = 2√5 ≈ 4.47
    """

    def construct(self):
        self.camera.background_color = BG_LIGHT

        # ── 1. Scene Header ──
        header = Text(
            "Step-by-Step Worked Example",
            font_size=28, color=NAVY, weight=BOLD
        )
        problem_box = Rectangle(
            width=10.0, height=0.9,
            fill_color=NAVY, fill_opacity=0.08,
            stroke_color=ROYAL_BLUE, stroke_width=2
        )
        problem_text = Text(
            "Find the gradient vector and its magnitude for   f(x, y) = x² + y²   at point   P(1, 2)",
            font_size=20, color=NAVY, weight=BOLD
        )
        problem_grp = VGroup(problem_box, problem_text)
        top_grp = VGroup(header, problem_grp).arrange(DOWN, buff=0.25).to_edge(UP, buff=0.35)

        self.play(FadeIn(header), Create(problem_box), Write(problem_text), run_time=1.5)
        self.wait(1.0)

        # ── 2. Steps Panel (Left Side) ──
        # Step 1
        s1_title = Text("Step 1: Partial Derivative with respect to x", font_size=18, color=ROYAL_BLUE, weight=BOLD)
        s1_note  = Text("• Treat y as a constant; derivative of y² is 0", font_size=16, color=GREY_A)
        s1_math  = Text("∂f/∂x = d/dx (x²) + 0  =  2x", font_size=20, color=DEEP_PURPLE, weight=BOLD)
        s1_grp   = VGroup(s1_title, s1_note, s1_math).arrange(DOWN, buff=0.12, aligned_edge=LEFT)

        # Step 2
        s2_title = Text("Step 2: Partial Derivative with respect to y", font_size=18, color=ROYAL_BLUE, weight=BOLD)
        s2_note  = Text("• Treat x as a constant; derivative of x² is 0", font_size=16, color=GREY_A)
        s2_math  = Text("∂f/∂y = 0 + d/dy (y²)  =  2y", font_size=20, color=DEEP_PURPLE, weight=BOLD)
        s2_grp   = VGroup(s2_title, s2_note, s2_math).arrange(DOWN, buff=0.12, aligned_edge=LEFT)

        # Step 3
        s3_title = Text("Step 3: Assemble the General Gradient Vector", font_size=18, color=ROYAL_BLUE, weight=BOLD)
        s3_math  = Text("∇f(x, y) = ( ∂f/∂x ,  ∂f/∂y )  =  ( 2x ,  2y )", font_size=20, color=NAVY, weight=BOLD)
        s3_grp   = VGroup(s3_title, s3_math).arrange(DOWN, buff=0.12, aligned_edge=LEFT)

        # Step 4
        s4_title = Text("Step 4: Substitute Point P(1, 2)", font_size=18, color=ROYAL_BLUE, weight=BOLD)
        s4_math  = Text("∇f(1, 2) = ( 2(1) ,  2(2) )  =  ( 2 ,  4 )", font_size=22, color=ORANGE_VEC, weight=BOLD)
        s4_box   = SurroundingRectangle(s4_math, color=ORANGE_VEC, buff=0.15, stroke_width=2.5)
        s4_grp   = VGroup(s4_title, VGroup(s4_math, s4_box)).arrange(DOWN, buff=0.12, aligned_edge=LEFT)

        steps_column = VGroup(s1_grp, s2_grp, s3_grp, s4_grp).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        steps_column.to_edge(LEFT, buff=0.8).shift(DOWN * 0.4)

        # Animate steps sequentially
        self.play(FadeIn(s1_grp, shift=RIGHT * 0.2), run_time=1.8)
        self.wait(1.0)
        self.play(FadeIn(s2_grp, shift=RIGHT * 0.2), run_time=1.8)
        self.wait(1.0)
        self.play(FadeIn(s3_grp, shift=RIGHT * 0.2), run_time=1.8)
        self.wait(1.0)
        self.play(FadeIn(s4_title), Write(s4_math), Create(s4_box), run_time=2.0)
        self.wait(1.5)

        # ── 3. Step 5: Magnitude Calculation Card (Right Side) ──
        mag_card_bg = RoundedRectangle(
            width=5.2, height=4.2, corner_radius=0.2,
            fill_color=WHITE, fill_opacity=1,
            stroke_color=ROYAL_BLUE, stroke_width=2
        )
        mag_title = Text("Step 5: Compute Magnitude", font_size=20, color=NAVY, weight=BOLD)
        mag_desc  = Text("Maximum Rate of Increase:", font_size=16, color=ROYAL_BLUE)
        mag_f1    = Text("|∇f(1, 2)| = √( (∂f/∂x)² + (∂f/∂y)² )", font_size=17, color=NAVY)
        mag_f2    = Text("= √( 2² + 4² )", font_size=19, color=DEEP_PURPLE, weight=BOLD)
        mag_f3    = Text("= √( 4 + 16 ) = √20", font_size=19, color=DEEP_PURPLE, weight=BOLD)
        mag_final = Text("= 2√5  ≈  4.47", font_size=24, color=ORANGE_VEC, weight=BOLD)
        mag_box   = SurroundingRectangle(mag_final, color=ORANGE_VEC, buff=0.12, stroke_width=2)

        mag_content = VGroup(
            mag_title, mag_desc, mag_f1, mag_f2, mag_f3, VGroup(mag_final, mag_box)
        ).arrange(DOWN, buff=0.22)

        mag_grp = VGroup(mag_card_bg, mag_content)
        mag_grp.to_edge(RIGHT, buff=0.8).shift(DOWN * 0.4)

        self.play(FadeIn(mag_card_bg), FadeIn(mag_content), run_time=2.5)
        self.wait(3.5)

        # ── 4. Summary Takeaway Banner at the bottom ──
        takeaway = Text(
            "Result: Gradient direction = (2, 4)   |   Maximum rate of climb = 2√5 ≈ 4.47",
            font_size=18, color=NAVY, weight=BOLD
        )
        takeaway.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(takeaway, shift=UP * 0.2), run_time=1.2)
        self.wait(3.0)

        # ── 5. Clean Exit ──
        self.play(
            FadeOut(top_grp),
            FadeOut(steps_column),
            FadeOut(mag_grp),
            FadeOut(takeaway),
            run_time=1.5
        )
