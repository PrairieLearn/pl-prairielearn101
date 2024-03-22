class Execution {
    static init(reset = false) {
        Execution.maxSpeed = Elements.speedSelector.max;
        Execution.speed = Elements.speedSelector.value;

        Execution.started = false;
        Execution.playing = false;
        Execution.skipBreakpoint = false;

        Elements.stepButton.disabled = false;
        Elements.playButton.disabled = false;
        Elements.playButton.innerHTML = (Execution.speed === Execution.maxSpeed) ? "Run" : "Play";

        Elements.output.innerHTML = '';
        Elements.log.innerHTML = '';

        Module.printCredits();
        Module.init();

        RegisterUtils.init();
        MemoryUtils.init();

        if (reset) {
            // After Module.init(), breakpoints are gone, so let's re-register them, if any.
            InstructionUtils.registerAllBreakpoints();
            InstructionUtils.highlightCurrentInstruction();
            InstructionUtils.highlightScrollIntoView(true);
        } else {
            InstructionUtils.init();
            InstructionUtils.highlightCurrentInstruction();
        }
    }

    static step(stepSize = 1) {
        const result = Module.step(stepSize, Execution.playing ? Execution.skipBreakpoint : true);

        let finished = false;
        if (result === 0) {  // finished
            Execution.finish();
            finished = true;
        } else if (result === -1) {  // break point encountered
            Execution.skipBreakpoint = true;
            Execution.playing = false;
            Elements.playButton.innerHTML = "Continue";
        } else if (result === 1) { // break point not encountered
            Execution.skipBreakpoint = false;
        }

        RegisterUtils.update();
        MemoryUtils.update();
        InstructionUtils.highlightCurrentInstruction();
        InstructionUtils.highlightScrollIntoView();

        // When we go at max speed, execution will step through multiple
        // instructions, and that messes with highlighting in the UI. Once
        // we're done, let's clear the highlighting.
        if (finished) {
            RegisterUtils.removeHighlight();
            MemoryUtils.removeHighlight();
        }
    }

    static togglePlay() {
        Execution.started = true;
        if (Execution.playing) {
            Execution.playing = false;
            Elements.playButton.innerHTML = "Continue"
        } else {
            Execution.playing = true;
            Elements.playButton.innerHTML = "Pause";
            Execution.play();
        }
    }

    static play() {
        if (!Execution.playing) return;
        if (Execution.speed === Execution.maxSpeed) {
            // Passing step size of 0 will run the whole thing, but that tends
            // to crash the client web browser. Instead, we try to simulate
            // very fast execution while keeping the browser somewhat
            // responsive in case there's infinite loops or other errors.
            Execution.step(1024);
            setTimeout(Execution.play, 0.5);
        } else {
            Execution.step();
            setTimeout(Execution.play, Execution.maxSpeed - Execution.speed);
        }
    }

    static finish() {
        Execution.playing = false;

        Elements.playButton.disabled = true;
        Elements.stepButton.disabled = true;

        Elements.playButton.innerHTML = (Execution.speed === Execution.maxSpeed) ? "Run" : "Play";
    }

    static setSpeed(newSpeed) {
        Execution.speed = newSpeed;
        if (Execution.started) return;
        Elements.playButton.innerHTML = (Execution.speed === Execution.maxSpeed) ? "Run" : "Play";
    }
}
