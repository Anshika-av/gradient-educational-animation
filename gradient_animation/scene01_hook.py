"""
==============================================================
 SCENE 01 — Hook and Introduction
 Subject : Mathematics 3 — Linear Algebra and Calculus
 Topic   : The Gradient
 Student : Anshika Verma | E25B070603
 College : Newton School of Technology
 Duration: ~45 seconds
==============================================================

 NOTE: This scene uses ONLY the Text() class with Unicode
 mathematical symbols.  No LaTeX installation is required.

 To render a quick preview (480p):
     manim -pql scene01_hook.py Scene01Hook

 To render final HD (1080p 60fps):
     manim -pqh scene01_hook.py Scene01Hook
==============================================================
"""

from manim import *
import numpy as np

# ──────────────────────────────────────────────
# Project-wide colour palette (used in all scenes)
# ──────────────────────────────────────────────
NAVY        = ManimColor("#003087")   # dark navy  – titles, backgrounds
ROYAL_BLUE  = ManimColor("#4169E1")   # royal blue – axes, accents
DEEP_PURPLE = ManimColor("#6A0DAD")   # purple     – gradient vectors, highlights
STEEL_BLUE  = ManimColor("#4682B4")   # steel blue – level curves
LIGHT_BLUE  = ManimColor("#B0C4DE")   # pale blue  – subtitles on dark bg
ORANGE_VEC  = ManimColor("#FF6600")   # bright orange – gradient arrows
POINT_RED   = ManimColor("#E63946")   # red        – point P
BG_LIGHT    = ManimColor("#F4F6FF")   # near-white background


# ══════════════════════════════════════════════════════════════
class Scene01Hook(ThreeDScene):
    """
    Hook and Introduction

    Animation flow
    ──────────────
    A  3D mountain (inverted paraboloid, z = 4 − x² − y²) fades in
       while the camera slowly rotates.
    B  A red dot wanders across the mountain surface.
    C  Overlay text poses the opening question.
    D  Fade-out → navy title card with student details.
    """

    # ----------------------------------------------------------
    # Helpers
    # ----------------------------------------------------------
    def mountain_z(self, u: float, v: float) -> float:
        """Height of the mountain surface at (u, v)."""
        return max(4.0 - u**2 - v**2, 0.0)

    # ----------------------------------------------------------
    def construct(self):
        self.camera.background_color = BG_LIGHT

        # ══════════════════════════════════════════════════════
        # PART A — Build the 3D mountain
        # ══════════════════════════════════════════════════════

        # 3-D axes (kept thin / muted so the surface pops)
        axes_3d = ThreeDAxes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            z_range=[-0.5, 5,   1],
            x_length=5,
            y_length=5,
            z_length=4.5,
            axis_config={"color": GREY_C, "stroke_width": 1.5},
            tips=False,
        )

        # Surface: z = 4 − u² − v²  (inverted paraboloid = mountain peak)
        surface = Surface(
            lambda u, v: axes_3d.c2p(u, v, self.mountain_z(u, v)),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(28, 28),   # grid density – higher = smoother
            fill_opacity=0.82,
            stroke_color=WHITE,
            stroke_width=0.35,
        )

        # Colour: deep blue at base → purple mid → white at peak
        surface.set_fill_by_value(
            axes=axes_3d,
            colorscale=[
                (BLUE_D,   0.0),
                (PURPLE_B, 2.0),
                (WHITE,    4.0),
            ],
            axis=2,          # colour based on z-value
        )

        # Initial camera angle – looking at the mountain from the side
        self.set_camera_orientation(phi=65 * DEGREES, theta=-50 * DEGREES)

        # Animate axes and surface into existence
        self.play(Create(axes_3d), run_time=1.0)
        self.play(Create(surface),  run_time=2.0)

        # ── Moving red dot ──────────────────────────────────
        u_tracker = ValueTracker(-1.5)
        v_tracker = ValueTracker(0.0)

        def get_dot():
            u = u_tracker.get_value()
            v = v_tracker.get_value()
            return Dot3D(
                point=axes_3d.c2p(u, v, self.mountain_z(u, v)),
                radius=0.10,
                color=POINT_RED,
            )

        moving_dot = always_redraw(get_dot)
        self.play(FadeIn(moving_dot), run_time=0.5)

        # Slow camera orbit while the dot wanders
        self.begin_ambient_camera_rotation(rate=0.06)

        self.play(
            u_tracker.animate.set_value(1.5),
            v_tracker.animate.set_value(1.2),
            run_time=3.0, rate_func=smooth,
        )
        self.play(
            u_tracker.animate.set_value(-0.5),
            v_tracker.animate.set_value(-0.9),
            run_time=2.0, rate_func=smooth,
        )

        self.stop_ambient_camera_rotation()
        self.wait(0.5)

        # ══════════════════════════════════════════════════════
        # PART B — Overlay question text  (fixed to camera)
        # ══════════════════════════════════════════════════════

        q_line1 = Text(
            "Imagine standing on a mountain...",
            font_size=30, color=NAVY, weight=BOLD,
        )
        q_line2 = Text(
            "Which direction leads to the steepest climb?",
            font_size=28, color=NAVY,
        )
        q_group = VGroup(q_line1, q_line2).arrange(DOWN, buff=0.35)

        # add_fixed_in_frame_mobjects keeps text flat regardless of 3-D camera
        self.add_fixed_in_frame_mobjects(q_group)
        q_group.to_edge(UP, buff=0.5)

        self.play(FadeIn(q_group, shift=DOWN * 0.25), run_time=1.5)
        self.wait(2.0)

        # Gradient teaser at the bottom
        teaser = Text(
            "The answer:  THE GRADIENT",
            font_size=34, color=DEEP_PURPLE, weight=BOLD,
        )
        self.add_fixed_in_frame_mobjects(teaser)
        teaser.to_edge(DOWN, buff=1.1)

        self.play(Write(teaser), run_time=1.5)
        self.wait(1.5)

        # ══════════════════════════════════════════════════════
        # PART C — Fade out everything
        # ══════════════════════════════════════════════════════
        self.play(
            FadeOut(surface),
            FadeOut(axes_3d),
            FadeOut(moving_dot),
            FadeOut(q_group),
            FadeOut(teaser),
            run_time=1.2,
        )

        # ══════════════════════════════════════════════════════
        # PART D — Title Card  (navy background + student info)
        # ══════════════════════════════════════════════════════

        # Full-screen navy background
        bg = Rectangle(
            width=16, height=10,
            fill_color=NAVY, fill_opacity=1, stroke_width=0,
        )

        # Main title
        title_txt = Text(
            "THE GRADIENT",
            font_size=58, color=WHITE, weight=BOLD,
        )

        # Subtitle
        sub_txt = Text(
            "Direction of Maximum Increase",
            font_size=28, color=LIGHT_BLUE,
        )

        # Thin decorative line
        h_line = Line(LEFT * 4.5, RIGHT * 4.5, color=ROYAL_BLUE, stroke_width=2)

        # Student details
        name_txt    = Text("Anshika Verma",
                           font_size=26, color=WHITE, weight=BOLD)
        id_txt      = Text("E25B070603",
                           font_size=22, color=LIGHT_BLUE)
        subject_txt = Text("Mathematics 3  —  Linear Algebra and Calculus",
                           font_size=20, color=LIGHT_BLUE)
        college_txt = Text("Newton School of Technology",
                           font_size=20, color=LIGHT_BLUE)

        info_grp = VGroup(name_txt, id_txt, subject_txt, college_txt)\
                        .arrange(DOWN, buff=0.22)

        card_grp = VGroup(title_txt, sub_txt, h_line, info_grp)\
                        .arrange(DOWN, buff=0.42)

        # Pin title card elements to the camera frame
        self.add_fixed_in_frame_mobjects(bg, card_grp)
        bg.move_to(ORIGIN)
        card_grp.move_to(ORIGIN)

        # Animate the title card
        self.play(FadeIn(bg), run_time=0.4)
        self.play(Write(title_txt), run_time=1.5)
        self.play(
            FadeIn(sub_txt,  shift=UP * 0.2),
            GrowFromCenter(h_line),
            run_time=1.0,
        )
        self.play(
            LaggedStart(
                FadeIn(name_txt,    shift=RIGHT * 0.3),
                FadeIn(id_txt,      shift=RIGHT * 0.3),
                FadeIn(subject_txt, shift=RIGHT * 0.3),
                FadeIn(college_txt, shift=RIGHT * 0.3),
                lag_ratio=0.4,
            ),
            run_time=2.0,
        )
        self.wait(2.5)

        # END OF SCENE 1
        # (In main_video.py this will transition directly into Scene 2)
