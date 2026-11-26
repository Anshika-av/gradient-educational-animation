"""
==============================================================
 MAIN VIDEO — The Gradient (Full 6-Scene Feature)
 Subject : Mathematics 3 — Linear Algebra and Calculus
 Topic   : The Gradient
 Student : Anshika Verma | E25B070603
 College : Newton School of Technology
 Target Duration: ~5 minutes (Strict maximum: 7 minutes)
==============================================================

To render this full video:
    cd "/Users/anshikaverma/Downloads/MATHS animation video/gradient_animation"

Quick preview render (480p):
    manim -pql main_video.py GradientFullVideo

Final high-definition submission render (1080p 60fps):
    manim -pqh main_video.py GradientFullVideo
==============================================================
"""

from manim import *
import numpy as np

# Import all individual scenes
from scene01_hook import Scene01Hook
from scene02_multivariable import Scene02Multivariable
from scene03_gradient_visual import Scene03GradientVisual
from scene04_worked_example import Scene04WorkedExample
from scene05_applications import Scene05Applications
from scene06_summary import Scene06Summary


class GradientFullVideo(ThreeDScene):
    """
    Master Scene: Assembles Scenes 1 through 6 into a continuous,
    seamless ~5-minute educational video on the Gradient.
    """

    def mountain_z(self, u: float, v: float) -> float:
        """Helper function required by Scene 1 mountain surface."""
        return max(4.0 - u**2 - v**2, 0.0)

    def construct(self):
        # ══════════════════════════════════════════════════════
        # SCENE 1: Hook and Introduction (~35s)
        # ══════════════════════════════════════════════════════
        Scene01Hook.construct(self)
        self.wait(1.0)
        self.clear()

        # ══════════════════════════════════════════════════════
        # SCENE 2: Multivariable Functions (~45s)
        # ══════════════════════════════════════════════════════
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        Scene02Multivariable.construct(self)
        self.wait(1.0)
        self.clear()

        # ══════════════════════════════════════════════════════
        # SCENE 3: Understanding Gradient Visually (~65s)
        # ══════════════════════════════════════════════════════
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        Scene03GradientVisual.construct(self)
        self.wait(1.0)
        self.clear()

        # ══════════════════════════════════════════════════════
        # SCENE 4: Step-by-Step Worked Example (~80s)
        # ══════════════════════════════════════════════════════
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        Scene04WorkedExample.construct(self)
        self.wait(1.0)
        self.clear()

        # ══════════════════════════════════════════════════════
        # SCENE 5: Interpretation & Applications (~50s)
        # ══════════════════════════════════════════════════════
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        Scene05Applications.construct(self)
        self.wait(1.0)
        self.clear()

        # ══════════════════════════════════════════════════════
        # SCENE 6: Summary & Credits (~30s)
        # ══════════════════════════════════════════════════════
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        Scene06Summary.construct(self)
        self.wait(2.0)
