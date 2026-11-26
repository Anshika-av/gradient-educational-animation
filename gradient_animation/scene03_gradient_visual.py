"""
==============================================================
 SCENE 03 — Understanding Gradient Visually
 Subject : Mathematics 3 — Linear Algebra and Calculus
 Topic   : The Gradient
 Student : Anshika Verma | E25B070603
 College : Newton School of Technology
 Target  : ~65 seconds
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


class Scene03GradientVisual(Scene):
    """
    Scene 3: Visualising the Gradient Vector and Level Curves
    - Del / Nabla definition: ∇f = (∂f/∂x, ∂f/∂y)
    - 2D Level curves (contours: x² + y² = c)
    - Evaluated at Point P(1, 2)
    - Shows gradient points in direction of steepest increase
    - Visually confirms perpendicularity to the level curve
    """

    def construct(self):
        self.camera.background_color = BG_LIGHT

        # ── 1. Gradient Header & Definition ──
        title = Text(
            "What is the Gradient Vector?",
            font_size=28, color=NAVY, weight=BOLD
        )
        formula = Text(
            "∇f = ( ∂f/∂x ,  ∂f/∂y )",
            font_size=34, color=DEEP_PURPLE, weight=BOLD
        )
        subtitle = Text(
            "A vector of partial derivatives pointing in the direction of steepest increase",
            font_size=20, color=ROYAL_BLUE
        )
        header_grp = VGroup(title, formula, subtitle).arrange(DOWN, buff=0.22)
        header_grp.to_edge(UP, buff=0.4)

        self.play(FadeIn(title), run_time=1.0)
        self.play(Write(formula), run_time=1.2)
        self.play(FadeIn(subtitle), run_time=1.0)
        self.wait(1.5)

        # ── 2. Contour Plot Coordinate Plane ──
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-1, 4, 1],
            x_length=5.5,
            y_length=4.5,
            background_line_style={"stroke_color": GREY_C, "stroke_width": 1},
            axis_config={"color": NAVY, "stroke_width": 2},
        )
        plane.to_edge(LEFT, buff=0.8).shift(DOWN * 0.4)

        x_lbl = plane.get_x_axis_label(Text("x", font_size=18, color=NAVY), direction=RIGHT)
        y_lbl = plane.get_y_axis_label(Text("y", font_size=18, color=NAVY), direction=UP)
        plane_grp = VGroup(plane, x_lbl, y_lbl)

        self.play(Create(plane_grp), run_time=1.5)

        # ── 3. Draw Level Curves (Concentric Circles: x² + y² = c) ──
        # c = 1, 3, 5, 8
        circles = VGroup()
        c_values = [1.0, 3.0, 5.0, 8.0]
        for c in c_values:
            r = np.sqrt(c)
            circ = plane.plot_parametric_curve(
                lambda t, r=r: np.array([r * np.cos(t), r * np.sin(t), 0]),
                t_range=[0, TAU],
                color=STEEL_BLUE,
                stroke_width=2.5,
            )
            circles.add(circ)

        curve_label = Text(
            "Level Curves: x² + y² = c\n(Curves of constant height)",
            font_size=17, color=STEEL_BLUE, line_spacing=1.2
        )
        curve_label.next_to(plane, DOWN, buff=0.25)

        self.play(Create(circles), FadeIn(curve_label), run_time=2.0)
        self.wait(1.0)

        # ── 4. Point P(1, 2) ──
        p_coords = np.array([1.0, 2.0, 0.0])
        p_dot = Dot(plane.c2p(*p_coords), color=POINT_RED, radius=0.1)
        p_label = Text("P(1, 2)", font_size=18, color=POINT_RED, weight=BOLD)
        p_label.next_to(p_dot, DL, buff=0.15)

        self.play(FadeIn(p_dot), Write(p_label), run_time=1.0)

        # ── 5. Gradient Vector ∇f(1, 2) = (2, 4) ──
        # Scaled visually for clean diagram display (factor 0.4)
        scale_fac = 0.35
        grad_endpoint = p_coords + np.array([2.0 * scale_fac, 4.0 * scale_fac, 0.0])
        grad_arrow = Arrow(
            start=plane.c2p(*p_coords),
            end=plane.c2p(*grad_endpoint),
            color=ORANGE_VEC,
            buff=0,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.25,
        )
        grad_label = Text("∇f(1, 2) = (2, 4)", font_size=18, color=ORANGE_VEC, weight=BOLD)
        grad_label.next_to(grad_arrow.get_end(), UR, buff=0.15)

        self.play(GrowArrow(grad_arrow), Write(grad_label), run_time=1.5)

        # ── 6. Perpendicular Marker and Tangent Line ──
        # At P(1, 2), level curve is x² + y² = 5.
        # Tangent vector to circle at (1, 2) is (-2, 1).
        tangent_vec = np.array([-2.0, 1.0, 0.0]) * 0.45
        t_start = p_coords - tangent_vec
        t_end   = p_coords + tangent_vec
        tangent_line = Line(
            plane.c2p(*t_start),
            plane.c2p(*t_end),
            color=GREY_A,
            stroke_width=2.5
        )
        tangent_lbl = Text("Tangent to level curve", font_size=14, color=GREY_A)
        tangent_lbl.next_to(tangent_line, LEFT, buff=0.1)

        # Right angle indicator (perpendicularity)
        ra_corner = RightAngle(
            Line(plane.c2p(*p_coords), plane.c2p(*t_end)),
            grad_arrow,
            length=0.28,
            color=DEEP_PURPLE,
            stroke_width=2.5,
        )

        self.play(Create(tangent_line), FadeIn(tangent_lbl), run_time=1.2)
        self.play(Create(ra_corner), run_time=1.0)

        # ── 7. Explanatory Callout Cards on the Right ──
        card1 = Text(
            "1. Steepest Ascent Direction:\nPoints straight uphill away from the center.",
            font_size=18, color=NAVY, line_spacing=1.3
        )
        card2 = Text(
            "2. Orthogonal to Level Curves:\nAlways perpendicular to contour line x² + y² = 5.",
            font_size=18, color=DEEP_PURPLE, line_spacing=1.3
        )
        card3 = Text(
            "3. Magnitude Reflects Rate:\nLonger vector = steeper instantaneous slope.",
            font_size=18, color=ORANGE_VEC, line_spacing=1.3
        )
        cards_grp = VGroup(card1, card2, card3).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        cards_grp.to_edge(RIGHT, buff=0.8).shift(DOWN * 0.2)

        self.play(
            LaggedStart(
                FadeIn(card1, shift=LEFT * 0.2),
                FadeIn(card2, shift=LEFT * 0.2),
                FadeIn(card3, shift=LEFT * 0.2),
                lag_ratio=0.5
            ),
            run_time=3.0
        )
        self.wait(3.0)

        # ── 8. Clean Exit ──
        self.play(
            FadeOut(header_grp),
            FadeOut(plane_grp),
            FadeOut(circles),
            FadeOut(curve_label),
            FadeOut(p_dot),
            FadeOut(p_label),
            FadeOut(grad_arrow),
            FadeOut(grad_label),
            FadeOut(tangent_line),
            FadeOut(tangent_lbl),
            FadeOut(ra_corner),
            FadeOut(cards_grp),
            run_time=1.5
        )
