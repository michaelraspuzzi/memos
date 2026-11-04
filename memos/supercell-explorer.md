# Supercell Explorer: feedback memo

*Nov 4, 2026. A one-page review of [murkatopiya/supercell](https://github.com/murkatopiya/supercell) ([live app](https://supercell.iryna.online/)), read from two seats: a research meteorologist who runs storm simulations, and an ML engineer who builds weather models. Based on the code and docs as of commit `18823fc`.*

## What it is today

- **A kinematic lab, not a storm model.** Real wind profiles from four historical soundings (Goshen, Prospect Valley, Dumas, Moore), plus seven hand-built storm shapes (Gaussian updraft, rotation, inflow, outflow, downdraft) added together. Passive tracers drift through the sum.
- **Built with unusual honesty.** The README says plainly what the model is not: no buoyancy, pressure, moisture, or mass conservation. Few science apps are this careful. Keep that.
- **Shape of the repo:** about 23K lines of TypeScript (React + Three.js), 52K lines of tests, 221 Markdown docs, 238 commits in under three months, one author.
- **The key result failed on numerics, not physics.** The trajectory experiment (Phase P) closed as *INVALID CONTROL, numerical convergence*. Production still steps tracers with forward Euler, and RK2 exists only in tests.

> **Bottom line:** The interface and the scientific habits are strong. The airflow behind them is hand-drawn. The 10x move is to put real storm dynamics behind the same interface, first from simulations and then from a learned model that runs in the browser.

## 1. Top 3 things to 10x this

1. **Replace the hand-built shapes with simulated storms.** Run [CM1](https://www2.mmm.ucar.edu/people/bryan/cm1/), the standard research storm model, once for each of the four soundings, and ship the 4D wind fields as compressed 3D textures. That gives mass-conserving, buoyancy-driven storms that change over time, with real updraft–shear interaction, rear-flank downdrafts, and cold pools. The tracers and the tilting diagnostic then mean something physical. Goshen (VORTEX2, 5 June 2009) also has published radar and EnKF analyses to check against.
2. **Fix the integrator so the evidence can pass.** Move production to RK4, or adaptive RK45 with error control, and use smooth (C¹) interpolation between sounding levels. The H3 control failed where trajectories crossed a sounding-segment boundary, which is what you'd expect from Euler on a piecewise-linear profile. Build the convergence ladder (dt, dt/2, dt/4 with an observed order of accuracy) into the test harness, and make every authored field divergence-free by deriving it from a stream function. Then move tracers to WebGPU compute so 10⁵–10⁶ particles can run, not dozens.
3. **Train an emulator: hodograph in, 3D storm out.** The hodograph can't be edited today because nothing could respond to it. Sweep CM1 across hodographs and CAPE, as Weisman and Klemp did by hand in 1982, then train a small conditional diffusion model or neural operator on the runs. Users draw a hodograph and get a plausible evolving supercell in seconds. That's the product nobody else has: a storm-scale counterpart to GraphCast or GenCast that anyone can play with.

## 2. Research to read

- **Weisman & Klemp (1982), [The dependence of numerically simulated convective storms on vertical wind shear and buoyancy](https://doi.org/10.1175/1520-0493(1982)110<0504:TDONSC>2.0.CO;2).** *Why:* the original shear-by-buoyancy parameter sweep, and the template for the emulator's training set.
- **Dahl, Parker & Wicker (2014), [Imported and storm-generated near-ground vertical vorticity in a simulated supercell](https://doi.org/10.1175/JAS-D-13-0123.1).** *Why:* the reference method for trajectory vorticity budgets, including how trajectory integration error can fake a result. It's exactly what T1 is reaching for.
- **Coffer & Parker (2017), [Simulated supercells in nontornadic and tornadic VORTEX2 environments](https://doi.org/10.1175/MWR-D-16-0226.1).** *Why:* runs CM1 from VORTEX2 soundings, the same campaign as Goshen, and shows how much the lowest 500 m of the hodograph matters.
- **Pathak et al. (2024), [StormCast: kilometer-scale convection-allowing model emulation using generative diffusion](https://arxiv.org/abs/2408.10958).** *Why:* evidence that diffusion models can emulate convection-resolving physics, and the closest ML blueprint for item 3.
- **Price et al. (2025), [GenCast: probabilistic weather forecasting with machine learning](https://doi.org/10.1038/s41586-024-08252-9).** *Why:* storms are chaotic, so an emulator should sample an ensemble of storms, not one deterministic answer. GenCast shows how to do that and score it (CRPS, spread–skill).

## 3. Other considerations

- **Process is outgrowing the product.** About 70% of the repo is governance: a decision doc, an authorization, and an acceptance for each UI slice. That rigor fits scientific claims, but applying it to scroll behavior slows down the science. Keep it for physics gates and drop it for UI.
- **Get outside eyes.** V1 evaluation was done by the author alone. Five educators and one storm researcher (OU, NSSL, Penn State, or NC State) would tell you more than another protocol would.
- **Pick the primary user.** Educators want a few curated storms that look right. Researchers want CM1 output and trajectory budgets. Serving both is fine, but the roadmap should say which one comes first.
- **Show what forecasters read.** Streamwise vorticity, storm-relative helicity (0–1 and 0–3 km), and critical angle come straight from the hodograph you already have. They're cheap to add and connect the app to real practice.
- **Data plumbing for real fields.** Use Zarr or chunked binary with quantized float16 3D textures, streamed by time step. One CM1 run at 250 m spacing compresses to roughly tens of MB, which is fine for the web.
- **The bigger risk is credibility, not code.** The careful labeling of what's observed and what's prescribed is the app's moat. Carry it over to simulated and learned fields as well, for example with labels like "simulated from this sounding" and "emulated, ensemble of N".
