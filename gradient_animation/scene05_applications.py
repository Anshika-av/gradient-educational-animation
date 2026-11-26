"""
==============================================================
 SCENE 05 — Interpretation and Real-Life Applications
 Subject : Mathematics 3 — Linear Algebra and Calculus
 Topic   : The Gradient
 Student : Anshika Verma | E25B070603
 College : Newton School of Technology
 Target  : ~50 seconds
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


class Scene05Applications(Scene):
    """
    Scene 5: Intuitive Interpretation and Real-World Applications
    - Recap of mountain intuition (direction & steepness)
    - 4 Applied Domains:
      1. Machine Learning: Gradient Descent
      2. Physics: Heat flow & Temperature Gradients
      3. Geography: Topographic slope analysis
      4. Engineering: Structural & Circuit Optimization
    - Brief mention of Directional Derivatives
    """

    def construct(self):
        self.camera.background_color = BG_LIGHT

        # ── 1. Header ──
        header = Text(
            "Physical Meaning & Real-World Applications",
            font_size=28, color=NAVY, weight=BOLD
        )
        sub = Text(
            "Direction: Where to step for fastest climb   |   Magnitude: How steep the slope is",
            font_size=19, color=ROYAL_BLUE
        )
        top_grp = VGroup(header, sub).arrange(DOWN, buff=0.18).to_edge(UP, buff=0.4)

        self.play(FadeIn(header), FadeIn(sub), run_time=1.2)
        self.wait(1.0)

        # ── 2. Create 4 Application Cards (2x2 Grid) ──
        def make_card(title_txt, bullet_txt, color_accent):
            bg = RoundedRectangle(
                width=5.8, height=2.0, corner_radius=0.15,
                fill_color=WHITE, fill_opacity=1,
                stroke_color=color_accent, stroke_width=2
            )
            t = Text(title_txt, font_size=18, color=color_accent, weight=BOLD)
            b = Text(bullet_txt, font_size=15, color=NAVY, line_spacing=1.2)
            content = VGroup(t, b).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
            card = VGroup(bg, content)
            content.move_to(bg.get_center())
            return card

        card_ml = make_card(
            "[1] Machine Learning & AI",
            "• Gradient Descent follows -∇L to minimize loss\n• Powers training in neural networks & LLMs",
            ROYAL_BLUE
        )
        card_phys = make_card(
            "[2] Physics & Thermodynamics",
            "• Heat flows opposite to temperature gradient: q = -k∇T\n• Governs fluid flow, diffusion, and potential fields",
            DEEP_PURPLE
        )
        card_geo = make_card(
            "[3] Geography & GIS Mapping",
            "• Identifies steep terrain slopes on topographic maps\n• Used in flood analysis and landslide hazard assessment",
            STEEL_BLUE
        )
        card_eng = make_card(
            "[4] Engineering Optimization",
            "• Minimizes stress, drag, or cost in multi-parameter designs\n• Aerodynamic shaping and circuit layout optimization",
            ORANGE_VEC
        )

        grid_top = VGroup(card_ml, card_phys).arrange(RIGHT, buff=0.5)
        grid_bot = VGroup(card_geo, card_eng).arrange(RIGHT, buff=0.5)
        grid = VGroup(grid_top, grid_bot).arrange(DOWN, buff=0.35).shift(DOWN * 0.1)

        self.play(
            LaggedStart(
                FadeIn(card_ml, shift=UP * 0.15),
                FadeIn(card_phys, shift=UP * 0.15),
                FadeIn(card_geo, shift=DOWN * 0.15),
                FadeIn(card_eng, shift=DOWN * 0.15),
                lag_ratio=0.35
            ),
            run_time=3.2
        )
        self.wait(2.5)

        # ── 3. Directional Derivative Teaser Banner ──
        dd_box = Rectangle(
            width=12.2, height=0.8,
            fill_color=NAVY, fill_opacity=0.08,
            stroke_color=ROYAL_BLUE, stroke_width=1.5
        )
        dd_text = Text(
            "Extension Concept: Directional Derivative   Du f = ∇f · u   (Rate of change in any unit direction u)",
            font_size=17, color=NAVY, weight=BOLD
        )
        dd_grp = VGroup(dd_box, dd_text)
        dd_grp.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(dd_grp, shift=UP * 0.2), run_time=1.2)
        self.wait(3.0)

        # ── 4. Clean Exit ──
        self.play(
            FadeOut(top_grp),
            FadeOut(grid),
            FadeOut(dd_grp),
            run_time=1.5
        )
