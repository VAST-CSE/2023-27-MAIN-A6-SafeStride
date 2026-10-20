# Multi-Agent Voice-Based Assistive Navigation for Visually Impaired

Main Project 2026-2027
Department of Computer Science and Engineering
Vidya Academy of Science and Technology

Class: S7 CSE | Batch: A | Group No.: 06
Project Guide: Ms. Anjana B

## Group Members

| Name | Roll No. |
|---|---|
| Abinav K Binesh | 10 |
| Abhijith K S | 5 |
| Anandakrishnan K | 44 |
| Alokh M K | 36 |

## Abstract

Visually impaired people often find it hard to understand and move around unfamiliar indoor places on their own. Most existing tools do only one job at a time: detecting objects, giving directions, or answering questions, but not all together. This project builds a Multi-Agent Voice-Based Assistive Navigation System in which four AI agents work together in real time. A central controller manages all four agents and makes sure obstacle warnings always come before any other message, so safety comes first.

## Problem Statement

Visually impaired individuals struggle to navigate unfamiliar indoor spaces safely and independently, because existing assistive tools handle only one function at a time rather than working together. This lack of integration causes delayed obstacle warnings, limited scene awareness and no real-time interactive support, making everyday indoor navigation difficult and often unsafe without human assistance.

## Proposed Solution

A multi-agent AI system that combines computer vision and voice interaction. A central controller coordinates four agents in real time:

| Agent | Role | Technology |
|---|---|---|
| Scene-Description Agent | Detects objects around the user and describes the surroundings in simple spoken sentences | YOLOv8 |
| Obstacle-Alert Agent | Watches the camera feed for nearby hazards and warns immediately, interrupting any other speech | YOLOv8 |
| Route-Guidance Agent | Gives step-by-step voice directions to a destination using a simple indoor map | A* algorithm on a pre-loaded map |
| Query-Response Agent | Lets the user ask questions aloud (for example "Is there a chair near me?") and answers from information the other agents have gathered | Whisper |

All feedback is delivered as speech (pyttsx3), designed to run fully offline on a smartphone.

## System Architecture

```
        Camera                  Microphone
           \                      /
            v                    v
          +-------------------------+
          |    Central Controller   |
          |   (coordinates agents,  |
          |  obstacle alerts first) |
          +-------------------------+
           /      |        |       \
          v       v        v        v
      Scene    Obstacle  Route    Query
      agent    agent     agent    agent
   (describes) (hazards) (A* path) (Whisper
                                    + answers)
          \       |        |       /
           v      v        v      v
            +-------------------+
            |  Voice output (TTS) |
            +-------------------+
```

## Use Cases

The visually impaired user can:

1. View (hear) their surroundings
2. Get obstacle alerts
3. Navigate to a destination
4. Ask a voice question

## Key Merits

- Combines scene description, obstacle alerts, route guidance and voice Q&A in one integrated system
- Prioritizes obstacle warnings in real time to keep the user safe
- Works entirely on a smartphone, with no IoT devices or beacons required
- Voice interaction makes it accessible and easy to use
- The multi-agent design lets each function work efficiently without interfering with the others

## Area of the Project

Artificial Intelligence, Natural Language Processing, Computer Vision, Deep Learning, Multi-Agent Systems, Speech Recognition and Synthesis, Assistive Technology, Human-Computer Interaction

## SDG Mapping

- SDG 3 (Good Health and Well-being): prevents avoidable injury through real-time obstacle detection and supports the autonomy that comes with independent navigation
- SDG 10 (Reduced Inequalities): narrows the accessibility gap through AI-powered environmental awareness
- SDG 11 (Sustainable Cities and Communities): makes indoor spaces more navigable without costly physical infrastructure changes

## Literature Review

| No. | Paper | Authors | What inspired us | Limitation |
|---|---|---|---|---|
| 1 | Navigation and Interaction for Blind Users via a Cognitive Architecture (Mar 2026) | Oscar J. Romero, Anthony Tomasic | Obstacle alerts take priority over navigation and conversation; inspired our controller's priority rule | Needs pre-placed AR anchors; we use a simple indoor map |
| 2 | NaVIP: A Computer Vision-Based Indoor Navigation Solution for Visually Impaired Persons (Feb 2026) | Jun Yu, Yitian Yang | Computer vision for indoor localization and distance- and direction-based voice navigation | Struggles in unfamiliar or featureless places; voice prompts can become outdated as the user moves |
| 3 | Enhanced Accessibility for Mobile Indoor Navigation (Jan 2026) | Johannes Wortmann, Bernd Schaufele | Event-based, adaptive voice/haptic feedback without continuous speaking | Feedback can be late or skipped at different walking speeds |
| 4 (base paper) | Scene-Aware Vectorized Memory Multi-Agent Framework with Cross-Modal Differentiated Quantization VLMs for Visually Impaired Assistance (Jan 2026) | Xiangxiang Wang, Xuanyu Wang | Specialized agents coordinated by a central controller with voice interaction; inspired our four-agent architecture | Relies on heavy GPU/server models; ours uses lightweight on-device models |

## Current Progress

Phase 1 (laptop prototype): real-time object detection with YOLOv8 from the webcam, with detected object names shown under the video and spoken aloud.

### Run Phase 1

1. Create and activate a virtual environment:

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install the requirements:

   ```
   pip install -r requirements.txt
   ```

3. Run:

   ```
   python main.py
   ```

   The first run downloads the `yolov8n.pt` model, so internet is needed once. Press `q` in the video window to quit.

## Roadmap

- Query-Response agent: answer spoken questions about what the camera sees
- Obstacle-Alert agent with priority interruption of other speech
- Scene-Description agent producing spoken summaries
- Route-Guidance agent using A* on an indoor map
- Central controller tying all four agents together
- Android app so the whole system runs on a smartphone
- Custom-trained model for indoor obstacles such as doors and stairs

## Future Scope

Extend the system from indoor to outdoor environments.
