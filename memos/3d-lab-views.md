# Lab robots are black boxes. So I took 17 apart.

![3D Lab Views in 30 seconds](assets/3d-lab-views/hype.mp4)
*30 seconds through the site: the slideshow of all 17 machines, the Opentrons Flex running DNA prep, then Liverpool's robot chemist and the parts inside it.*

*Nov 3, 2026. Draft for an X article. It introduces [3D Lab Views](https://michaelraspuzzi.github.io/labautomationin3d/): 17 lab automation systems taken apart in 3D, from a desktop pipetting robot to a room-sized cell factory. Every number below is from a card on the site, and each card links its sources.*

## Summary

- **The problem:** Lab robots are sold as brochures and quotes. You rarely see what science a machine actually runs, what software drives it, or what's inside.
- **What I built:** 17 machines in four sizes (benchtop, workstation, work cell, lab and room). Each film covers five layers: the science, the models, the software, the hardware and the components.
- **What I found:** The arms and pipettes are mostly solved. The hard part is the hand-off: a tool swap, a plate passed between instruments, a grasp nobody checks.
- **The gap:** Almost nobody publishes how often those hand-offs fail. Every card ends with the one log that would settle it.

> **Bottom line:** If you want to know where lab automation is stuck, don't look at the robot. Look at the moment it hands something off, and ask for the log.

## Every lab robot ships as a black box

If you've ever tried to buy, use or just understand a lab robot, you know how it goes. There's a product page, a spec sheet, a sales call. What you don't get is the thing you actually want to know: what happens inside when it runs.

So I took 17 of them apart, in 3D. Some are the robots you'd find in any biology lab, like the Opentrons Flex, a Hamilton STAR or a Tecan Fluent. Some are whole rooms: Berkeley's A-Lab, Multiply Labs' cell therapy towers, Cellares. And one is a robot that walks around a chemistry lab on wheels.

Each machine gets the same five layers, top to bottom:

1. **Science:** what it actually runs, played step by step on the 3D model.
2. **Models:** the machine learning that picks what to try next, where there is any.
3. **Software:** what schedules the run and talks to the instruments.
4. **Hardware:** the arms, grippers, decks and tracks.
5. **Components:** one level further down, cut open, such as a gripper lock, a torque sensor or a six-touch calibration routine.

## Three machines, three scales

**Opentrons Flex, the benchtop.** It's an 87 cm steel-and-aluminium box with one gantry. The science card plays Illumina DNA Prep for 48 samples: tagmentation, washes, PCR and a bead cleanup, with the gripper moving the plate between the thermocycler and the magnetic block by itself. Here's the catch. A person screws each pipette onto the gantry by hand. Changing a pipette stops the run, and Opentrons publishes no time for it.

**Liverpool's mobile robot chemist, the whole lab.** Andy Cooper's group put a KUKA arm on a mobile base and let it run a lab built for people. It drives to the solid dispenser, the liquid station, the light box and the gas chromatograph, then back to its charger. It ran 688 experiments in 8 days and found a catalyst mix six times more active than where it started. But the robot never checks its grasps. When a station fails, a person watching CCTV restarts the run, often remotely.

**Inside the parts.** The Liverpool robot finds each station by touch. Six taps on a black cube tell it exactly where it is, to within 0.12 mm. Its gripper fingers open outward to lock into a rack. Each of the arm's seven joints has a torque sensor, which is how the arm feels the cube at all.

## The hard part is the hand-off

Once you lay 17 machines side by side, the same thing shows up in nearly every one. The robot can move. What breaks is the moment it hands something off.

| Machine | What's known | The log that would settle it |
|---|---|---|
| Berkeley A-Lab | Over 1.5 years, 3.9% of 2,455 samples hit an exception, 89% of them mechanical | How each exception was cleared |
| Maholo LabDroid | Over 185 days, 25 of 28 stoppages needed a person; 11 were tips that failed to load or eject | A force check on every tip pickup |
| Liverpool chemist | Grasps are never checked; a person on CCTV restarts failed runs | Grasp checks and a self-restart |
| Opentrons Flex | A pipette change stops the run | A dock that changes pipettes mid-run |
| Chemspeed | 57 tools listed, no swap time, no failure rate | One unedited log of tool swaps |
| Tecan Fluent | 8 to 10 s for a 384-head adapter swap; nothing for a finger swap | 100 finger swaps, unedited |
| Multiply Labs | Every bag, syringe and vial gets a snap-on adapter by hand first | Human touches per batch |

The few numbers that do exist come from academic labs (A-Lab, Maholo, Liverpool), because papers have to report them. The companies mostly don't. That's the real black box: not the hardware, but the failure rate.

## How it's built

I built it with Claude, working through papers, patents, firmware, manuals and videos, one machine at a time. A few rules kept it honest:

- **Every card carries its sources.** A mark on each card shows how a fact is known: verified by a third party, shown in docs or video, or claimed by the company.
- **Simulated means simulated.** Component cutaways are drawn from firmware and docs, not a teardown, and each says so. The shapes are ours and the numbers are cited.
- **Stand-ins are labelled.** A photo marked "stand-in" shows the same kind of machine, not the company's own.

The whole thing is one static HTML page with three.js. You can link straight to one machine, for example [#liverpool-mobile-chemist](https://michaelraspuzzi.github.io/labautomationin3d/#liverpool-mobile-chemist).

## The ask

If you run one of these machines, the most useful thing you could share is one unedited log: every tool swap, plate hand-off and grasp in a real run, including the ones that failed and who fixed them. One log like that would tell the field more than another spec sheet.

**Open the box:** [michaelraspuzzi.github.io/labautomationin3d](https://michaelraspuzzi.github.io/labautomationin3d/)

---

*Draft notes (cut before posting):*

- *For X: lead with the video, then the first two sections. The hand-off table is the part people will share; consider turning it into an image.*
- *Check the A-Lab exception figure and the Maholo eLife figures against their papers before posting. Both come from the sources linked on their cards.*
- *The catalyst figure is from Burger et al., Nature 2020.*
