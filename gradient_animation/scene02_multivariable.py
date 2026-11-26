"""
==============================================================
 SCENE 02 — Introduction to Multivariable Functions
 Subject : Mathematics 3 — Linear Algebra and Calculus
 Topic   : The Gradient
 Student : Anshika Verma | E25B070603
 College : Newton School of Technology
 Target  : ~45 seconds
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


class Scene02Multivariable(ThreeDScene):
    """
    Scene 2: Multivariable Functions
    - Introduces f(x, y) = x² + y²
    - Explains inputs (x, y) producing output z = f(x, y)
    - Animates 3D axes and the paraboloid surface
    """

    def construct(self):
        self.camera.background_color = BG_LIGHT

        # ── 1. Title and Formula banner (Fixed in camera frame) ──
        header = Text(
            "Multivariable Functions: Inputs and Outputs",
            font_size=28, color=NAVY, weight=BOLD
        )
        formula = Text(
            "f(x, y) = x² + y²",
            font_size=36, color=DEEP_PURPLE, weight=BOLD
        )
        subtitle = Text(
            "Two independent inputs (x, y)  →  One height output:  z = f(x, y)",
            font_size=22, color=ROYAL_BLUE
        )
        top_group = VGroup(header, formula, subtitle).arrange(DOWN, buff=0.25)
        self.add_fixed_in_frame_mobjects(top_group)
        top_group.to_edge(UP, buff=0.4)

        self.play(FadeIn(header, shift=DOWN * 0.2), run_time=1.0)
        self.play(Write(formula), run_time=1.2)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.0)
        self.wait(2.0)

        # ── 2. 3D Coordinate Axes ──
        axes_3d = ThreeDAxes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            z_range=[0, 6, 1],
            x_length=5.0,
            y_length=5.0,
            z_length=4.0,
            axis_config={"color": GREY_B, "stroke_width": 2},
        )

        # Labels for axes
        x_label = axes_3d.get_x_axis_label(
            Text("x (Input)", font_size=18, color=ROYAL_BLUE),
            direction=RIGHT
        )
        y_label = axes_3d.get_y_axis_label(
            Text("y (Input)", font_size=18, color=DEEP_PURPLE),
            direction=UP
        )
        z_label = axes_3d.get_z_axis_label(
            Text("z = f(x, y) (Output)", font_size=18, color=NAVY),
            direction=OUT
        )
        labels = VGroup(x_label, y_label, z_label)

        # Set 3D perspective
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        self.play(Create(axes_3d), run_time=1.5)
        self.play(FadeIn(labels), run_time=1.0)
        self.wait(1.5)

        # ── 3. Paraboloid Surface z = x² + y² ──
        surface = Surface(
            lambda u, v: axes_3d.c2p(u, v, u**2 + v**2),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(24, 24),
            fill_opacity=0.80,
            stroke_color=WHITE,
            stroke_width=0.4,
        )
        surface.set_fill_by_value(
            axes=axes_3d,
            colorscale=[
                (NAVY, 0.0),
                (ROYAL_BLUE, 2.0),
                (DEEP_PURPLE, 5.0),
                (LIGHT_BLUE, 8.0)
            ],
            axis=2
        )

        surface_note = Text(
            "Elliptic Paraboloid: Bowl-shaped surface",
            font_size=20, color=NAVY, weight=BOLD
        )
        self.add_fixed_in_frame_mobjects(surface_note)
        surface_note.to_edge(DOWN, buff=0.8)

        # Sweep-in build of the surface
        self.play(Create(surface), FadeIn(surface_note), run_time=2.5)

        # ── 4. Origin Minimum Point ──
        origin_dot = Dot3D(point=axes_3d.c2p(0, 0, 0), radius=0.12, color=POINT_RED)
        origin_text = Text("Minimum: (0, 0, 0)", font_size=18, color=POINT_RED, weight=BOLD)
        self.add_fixed_in_frame_mobjects(origin_text)
        origin_text.next_to(surface_note, UP, buff=0.2)

        self.play(FadeIn(origin_dot), FadeIn(origin_text), run_time=1.0)

        # Slow orbital pan to show 3D geometry
        self.begin_ambient_camera_rotation(rate=0.08)
        self.wait(4.0)
        self.stop_ambient_camera_rotation()
        self.wait(1.5)

        # ── 5. Clean Exit ──
        self.play(
            FadeOut(top_group),
            FadeOut(surface_note),
            FadeOut(origin_text),
            FadeOut(origin_dot),
            FadeOut(surface),
            FadeOut(axes_3d),
            FadeOut(labels),
            run_time=1.5
        )
