"""
==============================================================
 SCENE 06 — Summary and Credits
 Subject : Mathematics 3 — Linear Algebra and Calculus
 Topic   : The Gradient
 Student : Anshika Verma | E25B070603
 College : Newton School of Technology
 Target  : ~30 seconds
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


class Scene06Summary(Scene):
    """
    Scene 6: Summary and Closing Credits
    - 3 Main Takeaways
    - Thank You Screen
    - Academic Credits & AI Disclosure
    """

    def construct(self):
        self.camera.background_color = BG_LIGHT

        # ── 1. Header ──
        header = Text(
            "Summary: Three Key Takeaways",
            font_size=28, color=NAVY, weight=BOLD
        )
        header.to_edge(UP, buff=0.5)
        self.play(FadeIn(header, shift=DOWN * 0.2), run_time=1.0)

        # ── 2. Three Takeaway Cards ──
        def make_takeaway(num_str, title_str, detail_str, accent_color):
            card_bg = RoundedRectangle(
                width=11.5, height=1.1, corner_radius=0.15,
                fill_color=WHITE, fill_opacity=1,
                stroke_color=accent_color, stroke_width=2
            )
            badge = Text(num_str, font_size=20, color=WHITE, weight=BOLD)
            badge_bg = Dot(radius=0.35, color=accent_color)
            badge_grp = VGroup(badge_bg, badge)

            t = Text(title_str, font_size=18, color=NAVY, weight=BOLD)
            d = Text(detail_str, font_size=15, color=GREY_A)
            text_grp = VGroup(t, d).arrange(DOWN, buff=0.08, aligned_edge=LEFT)

            row = VGroup(badge_grp, text_grp).arrange(RIGHT, buff=0.35)
            row.move_to(card_bg.get_center())
            return VGroup(card_bg, row)

        card1 = make_takeaway(
            "1",
            "The Gradient is a Vector of Partial Derivatives",
            "∇f = ( ∂f/∂x ,  ∂f/∂y ) — one component for each input variable",
            ROYAL_BLUE
        )
        card2 = make_takeaway(
            "2",
            "Points Towards Maximum Rate of Increase",
            "When non-zero, it identifies steepest ascent and is perpendicular to level curves",
            DEEP_PURPLE
        )
        card3 = make_takeaway(
            "3",
            "Magnitude Equals the Maximum Rate of Change",
            "|∇f| = √( (∂f/∂x)² + (∂f/∂y)² ) — length represents slope steepness",
            ORANGE_VEC
        )

        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.3).shift(DOWN * 0.2)

        self.play(
            LaggedStart(
                FadeIn(card1, shift=UP * 0.2),
                FadeIn(card2, shift=UP * 0.2),
                FadeIn(card3, shift=UP * 0.2),
                lag_ratio=0.45
            ),
            run_time=3.0
        )
        self.wait(3.5)

        # ── 3. Fade to Closing Credits Screen ──
        self.play(FadeOut(header), FadeOut(cards), run_time=1.2)

        # Navy closing card
        closing_bg = Rectangle(
            width=16, height=10,
            fill_color=NAVY, fill_opacity=1, stroke_width=0
        )
        ty_text = Text("Thank You!", font_size=48, color=WHITE, weight=BOLD)
        course_text = Text(
            "Mathematics 3 — Linear Algebra and Calculus",
            font_size=24, color=LIGHT_BLUE
        )
        sep_line = Line(LEFT * 4, RIGHT * 4, color=ROYAL_BLUE, stroke_width=2)

        author_name = Text("Anshika Verma", font_size=22, color=WHITE, weight=BOLD)
        author_id   = Text("Student ID: E25B070603", font_size=18, color=LIGHT_BLUE)
        college     = Text("Newton School of Technology", font_size=18, color=LIGHT_BLUE)

        ref_title   = Text("References & Integrity:", font_size=16, color=LIGHT_BLUE, weight=BOLD)
        ref_text    = Text(
            "Stewart Multivariable Calculus (Ch. 14)  •  Thomas & Finney (Ch. 11)\nAI Tooling: Google Antigravity (Scaffolding & Scripts) | Code: Manim CE",
            font_size=14, color=GREY_B, line_spacing=1.2
        )

        credits_grp = VGroup(
            ty_text,
            course_text,
            sep_line,
            author_name,
            author_id,
            college,
            VGroup(ref_title, ref_text).arrange(DOWN, buff=0.1)
        ).arrange(DOWN, buff=0.25).move_to(ORIGIN)

        self.play(FadeIn(closing_bg), FadeIn(credits_grp), run_time=1.5)
        self.wait(3.0)
