# Storyboard: The Gradient
### Mathematics 3 — Linear Algebra and Calculus
**Student:** Anshika Verma | **Student ID:** E25B070603  
**College:** Newton School of Technology  
**Target Duration:** ~5 minutes (Strict maximum: 7 minutes) | **Resolution:** 1080p (1920×1080, 16:9)

---

## Scene 1: Hook and Introduction
- **Target Duration:** 0:00 – 0:35 (~35 seconds)
- **Visual Description:**
  - Opens on a 3D mountain-like surface (an inverted paraboloid $z = 4 - x^2 - y^2$).
  - Camera rotates smoothly while a glowing red dot moves along the surface.
  - Overlay question text appears: *"Imagine standing on a mountain. Which direction leads to the steepest climb?"*
  - The teaser *"The answer: THE GRADIENT"* resolves.
  - Transitions to a title card displaying student name (Anshika Verma), Student ID (E25B070603), subject, and college.
- **Key Concepts:** Qualitative intuition of steepest ascent; project introduction.

---

## Scene 2: Introduction to Multivariable Functions
- **Target Duration:** 0:35 – 1:20 (~45 seconds)
- **Visual Description:**
  - Transition to clean 3D coordinate system.
  - Introduces $f(x, y) = x^2 + y^2$.
  - Demonstrates independent variables $(x, y)$ in the horizontal plane generating dependent output $z = f(x, y)$.
  - Shows the 3D surface (paraboloid bowl) forming mesh line by mesh line.
  - Clearly labelled color-coded axes: $x$ (royal blue), $y$ (purple), $z$ (navy).
  - Highlights origin $(0, 0, 0)$ as the minimum point.
- **Key Concepts:** Multivariable mapping $\mathbb{R}^2 \to \mathbb{R}$, 3D surface geometry, coordinate axes.

---

## Scene 3: Understanding Gradient Visually
- **Target Duration:** 1:20 – 2:25 (~65 seconds)
- **Visual Description:**
  - Formula introduced: $\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$.
  - Split view / synchronized representation: 3D surface on one side, 2D contour plot (level curves $x^2 + y^2 = c$) on the other.
  - Test point $P = (1, 2)$ plotted in red on both representations.
  - Gradient vector $\nabla f(1, 2)$ drawn as an orange arrow starting from $P$.
  - Right-angle indicator visually proves the gradient vector is perpendicular to the tangent of the level curve at $P$.
  - Animated vector demonstrates how magnitude reflects slope steepness.
- **Key Concepts:** Gradient as a 2D vector, orthogonality to level sets, direction of steepest ascent, magnitude as maximum rate of increase.

---

##Scene 4: Step-by-Step Worked Example

Target Duration: 2:25 – 3:45 (~80 seconds)

Visual Description:

Structured math panel with clear sequential steps:

Base function: (f(x,y)=x^2+y^2)

Partial derivative w.r.t. (x): (\frac{\partial f}{\partial x}=2x) (treating (y) as constant)

Partial derivative w.r.t. (y): (\frac{\partial f}{\partial y}=2y) (treating (x) as constant)

General gradient vector: (\nabla f=(2x,2y))

Evaluation at (P(1,2)): (\nabla f(1,2)=(2(1),2(2))=(2,4))

Magnitude calculation: (|\nabla f(1,2)|=\sqrt{2^2+4^2}=\sqrt{20}=2\sqrt{5}\approx4.47)

Vector ((2,4)) dynamically connected to the 3D surface at point ((1,2,5)) to reinforce spatial meaning.

Key Concepts: Partial differentiation rules, vector evaluation, distinguishing vector direction from scalar magnitude.
---

## Scene 5: Interpretation and Real-Life Applications
- **Target Duration:** 3:45 – 4:35 (~50 seconds)
- **Visual Description:**
  - Mountain metaphor recap: direction indicates where to step; length indicates steepness.
  - Animated 4-quadrant application showcase:
    - **Machine Learning:** Loss surface showing Gradient Descent (moving opposite to gradient $-\nabla L$).
    - **Physics:** Heat transfer / temperature gradient ($\vec{q} = -k \nabla T$).
    - **Geography:** Topographic contour maps and steepest slope analysis.
    - **Engineering:** Multivariable optimization in structural and circuit design.
  - Brief graphical mention of directional derivatives $D_{\vec{u}} f = \nabla f \cdot \hat{u}$.
- **Key Concepts:** Practical applications across modern STEM fields, intuitive synthesis.

---

## Scene 6: Summary and Credits
- **Target Duration:** 4:35 – 5:05 (~30 seconds)
- **Visual Description:**
  - Three distinct summary takeaway cards animate on screen:
    1. **Vector of partials:** $\nabla f = (\partial f/\partial x, \partial f/\partial y)$
    2. **Steepest ascent:** Points in the direction of maximum increase (when non-zero)
    3. **Magnitude:** $\|\nabla f\|$ gives the maximum instantaneous rate of change
  - Thank You card, academic references (Stewart, Thomas/Finney), and AI tools disclosure.
- **Key Concepts:** Knowledge consolidation, academic integrity, closing credits.
