# The Gradient — M3 Mathematics Animation Video

**Student:** Anshika Verma | E25B070603
**Subject:** Mathematics 3 — Linear Algebra and Calculus
**College:** Newton School of Technology

---

## What This Project Is

This project produces an educational animation video explaining the concept of the **Gradient** in multivariable calculus. The video is carefully timed for **approximately 5 minutes (target: ~5:00, strictly under the 7-minute maximum)**. The animation is built with **Manim Community Edition** (a Python animation library) and covers six scenes: a 3D mountain hook, multivariable function intro, visual gradient explanation, step-by-step worked example, real-world applications, and a summary.

---

## Project File Structure

```
MATHS animation video/
│
├── gradient_animation/              ← All animation Python files
│   ├── scene01_hook.py              ← Scene 1: Mountain + Title card
│   ├── scene02_multivariable.py     ← Scene 2: f(x,y) = x²+y² surface
│   ├── scene03_gradient_visual.py  ← Scene 3: Gradient formula + contour
│   ├── scene04_worked_example.py   ← Scene 4: Step-by-step calculation
│   ├── scene05_applications.py     ← Scene 5: Real-world applications
│   ├── scene06_summary.py           ← Scene 6: Summary + credits
│   └── main_video.py                ← Combines all 6 scenes → Video.mp4
│
├── docs/
│   ├── Storyboard.md                ← Six-scene storyboard with visual descriptions
│   └── Narration_Script.txt         ← Full narration with timestamps (~5 min target)
│
├── output/
│   └── Video.mp4                    ← Final rendered video (created later)
│
├── README.md                        ← This file
└── Credits_and_AI_Disclosure.md    ← References and AI tools used
```

---

## Step-by-Step Setup Instructions (Beginner Friendly)

Follow these steps **in order**. Everything is typed into the **Terminal** app on your Mac.

### How to open Terminal
Press **Command + Space**, type **Terminal**, press **Enter**.

---

### STEP 1 — Install Homebrew (Mac package manager)

Homebrew lets you install developer tools easily. Paste this single command and press Enter:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

> It will ask for your Mac password (you won't see characters as you type — that is normal). Press Enter when done.
> This takes about 2–5 minutes.

**Check it worked:**
```bash
brew --version
```
You should see something like `Homebrew 4.x.x`.

---

### STEP 2 — Install FFmpeg

FFmpeg converts animation frames into an MP4 video file. Run:

```bash
brew install ffmpeg
```

> This downloads and installs FFmpeg. It may take 3–10 minutes depending on your internet speed.

**Check it worked:**
```bash
ffmpeg -version
```
You should see `ffmpeg version 7.x.x ...`

---

### STEP 3 — Install Python Libraries

Run this single command to install Manim and all required Python libraries:

```bash
pip3 install manim numpy matplotlib scipy
```

> This installs four libraries. It takes about 2–5 minutes.

**Check it worked:**
```bash
manim --version
```
You should see something like `Manim Community v0.18.x`

---

### STEP 4 — Navigate to the Project Folder

In Terminal, type this command to go to your project folder:

```bash
cd "/Users/anshikaverma/Downloads/MATHS animation video/gradient_animation"
```

> `cd` means "change directory" — it moves Terminal into your project folder.

---

### STEP 5 — Render a Scene Preview

To render **Scene 1** as a quick low-quality preview (renders in ~30 seconds):

```bash
manim -pql scene01_hook.py Scene01Hook
```

> - `-p` = play the video automatically when it's done
> - `-q` = quality setting
> - `l` = low quality (480p) — fast for previewing
> - The video opens automatically in QuickTime.

To render Scene 1 in **full 1080p HD** (takes longer):

```bash
manim -pqh scene01_hook.py Scene01Hook
```

---

### STEP 6 — Render All Scenes (Final Video)

After all scenes are complete and approved, run:

```bash
manim -pqh main_video.py GradientFullVideo
```

This renders the complete animation video (targeted at ~5 minutes, strictly under the 7-minute limit) at 1920×1080 resolution.

---

## Where Do Rendered Videos Go?

Manim automatically creates a folder:
```
gradient_animation/media/videos/scene01_hook/
```
Inside, it places the MP4 file. For the preview (low quality), look in:
```
media/videos/scene01_hook/480p15/
```
For high quality (1080p):
```
media/videos/scene01_hook/1080p60/
```

---

## Common Errors and Fixes

| Error Message | What It Means | Fix |
|---|---|---|
| `command not found: manim` | Manim is not installed | Run Step 3 again |
| `command not found: ffmpeg` | FFmpeg is not installed | Run Step 2 again |
| `ModuleNotFoundError: No module named 'numpy'` | NumPy missing | Run `pip3 install numpy` |
| `FileNotFoundError` on render | Wrong folder in Terminal | Re-run Step 4 |
| Black screen in video | Camera orientation issue | Contact your instructor |

---

## Narration Instructions

1. Open `docs/Narration_Script.txt` in any text editor or Notes app.
2. Record each scene as a separate audio file.
3. Save them as:
   - `narration_scene01.mp3`
   - `narration_scene02.mp3` ... through `narration_scene06.mp3`
4. Put all audio files in the `assets/` folder.
5. In Phase 3, we will merge audio and video using FFmpeg.

---

## Mathematical Content Summary

| Scene | Concept | Key Formula |
|---|---|---|
| 1 | Introduction | — |
| 2 | Multivariable function | f(x, y) = x² + y² |
| 3 | Gradient definition | ∇f = (∂f/∂x, ∂f/∂y) |
| 4 | Worked example at P=(1,2) | ∇f(1,2) = (2, 4), \|∇f\| = 2√5 |
| 5 | Applications | Gradient Descent, Heat flow |
| 6 | Summary | Three key takeaways |

---

## Render Settings Reference

| Flag | Meaning | Quality |
|---|---|---|
| `-ql` | Low quality | 480p 15fps — fast preview |
| `-qm` | Medium quality | 720p 30fps |
| `-qh` | High quality | 1080p 60fps — final submission |
| `-p` | Auto-play after render | Recommended |
| `-v WARNING` | Suppress verbose output | Optional |
