const CREDITS = 'Web interface adapted from <a href="https://github.com/ShawnZhong/JsSpim">JsSpim</a> by Shawn Zhong.';

class PLMipsDebugger {
  // Initialize static vars that others (e.g. wasm.js) can easily access and use.
  static init(elementFilesUrl, questionFilesUrl, questionMainFile, editorId, options) {
    PLMipsDebugger.options = Object.freeze(options);
    PLMipsDebugger.elementFilesUrl = elementFilesUrl;
    PLMipsDebugger.questionFilesUrl = questionFilesUrl;
    PLMipsDebugger.questionMainFile = questionMainFile;
    PLMipsDebugger.editorId = editorId;
    PLMipsDebugger.mainCode = null;
    PLMipsDebugger.highlightWorker = new Worker(elementFilesUrl + '/highlight.min.js');
    PLMipsDebugger.highlightWorker.onmessage = (event) => {
      event.data.forEach((e, i) => InstructionUtils.instructionList[i].instructionElement.innerHTML = e);
    };
  }

  // After WASM module is setup, load current code into the simulator.
  static postModuleLoad() {
    PLMipsDebugger.reload(false);
  }

  // Fetch code from the editor and load into the debugger.
  static reload(scroll = true) {
    const code = PLMipsDebugger.getCode(PLMipsDebugger.editorId);
    if (code != null) {
      PLMipsDebugger.fetchMainCode()
        .then(() => {
          const source = PLMipsDebugger.prepareCode(code);
          PLMipsDebugger.run(source, scroll);
        });
    }
  }

  // Feed the code to SPIM and set up initial state.
  static run(source = "", scroll = true) {
    let data = new TextEncoder().encode(source);

    const stream = FS.open('input.s', 'w+');
    FS.write(stream, data, 0, data.byteLength, 0);
    FS.close(stream);

    Execution.init();
    if (scroll) {
      InstructionUtils.highlightScrollIntoView(true);
    }

    // Since we've overwritten things, need to sync up the toggles.
    PLMipsDebugger.syncToggles();
  }

  static fetchMainCode() {
    if (PLMipsDebugger.mainCode != null) {
      return new Promise((resolve, reject) => resolve());
    }
    const path = `${PLMipsDebugger.questionFilesUrl}/${PLMipsDebugger.questionMainFile}`;
    return fetch(path)
      .then(response => response.text())
      .then(text => PLMipsDebugger.mainCode = text)
      .catch(error => console.error('Error while fetching question main file', error));
  }

  static getCode(editorId) {
    const elements = $(`#${editorId} .editor`);
    if (elements.length !== 1) {
      console.error("Unable to find code editor within container with id:", editorId);
      return null;
    }
    const editor = ace.edit(elements[0]);
    return editor.getValue();
  }

  static prepareCode(code) {
    // We put the student's code first so that the source line numbers
    // match up better to what the student sees in the code editor.
    return code + "\n" + PLMipsDebugger.mainCode;
  }

  static syncToggles() {
    InstructionUtils.toggleSourceCode(Elements.sourceToggle.checked);
    InstructionUtils.toggleKernelText(Elements.kernelTextToggle.checked);
    InstructionUtils.toggleBinary(Elements.instrValueToggle.checked);
    MemoryUtils.toggleKernelData(Elements.kernelDataToggle.checked);
  }

  static adjustSpeed(value) {
    $('#speed-selector').val(value).trigger('input');
  }

  static currentSpeed() {
    const value = $('#speed-selector').val();
    return parseInt(value);
  }
}

class PLMipsViews {
  // Initialize various aspects of the user interface.
  static init() {
    PLMipsViews.previousSpeed = null;

    // Initialized some toggles based on configuration.
    let enable = !!PLMipsDebugger.options.enableFloatRegs;
    $('#float-regs-container').toggleClass('d-none', !enable);
    enable = !!PLMipsDebugger.options.enableKernelToggles;
    $('#toggle-kernel-text').parent().toggleClass('d-none', !enable);
    $('#toggle-kernel-data').parent().toggleClass('d-none', !enable);
    $('#kernel-text-container').toggleClass('d-none', !enable);
    $('#kernel-data-container').toggleClass('d-none', !enable);

    // Setup click handlers for main buttons.
    Elements.resetButton.onclick = (event) => {
      event.preventDefault();
      Execution.init(true);
    };
    Elements.stepButton.onclick = (event) => {
      event.preventDefault();
      Execution.step(1);
    };
    Elements.playButton.onclick = (event) => {
      event.preventDefault();
      Execution.togglePlay();
    };
    $('#sync-button').click(event => {
      event.preventDefault();
      PLMipsDebugger.reload();
    });

    // Setup handlers for switching views.
    $('#mips-run-view').click(() => {
      PLMipsViews.showRunView();
    });
    $('#mips-col-view').click(() => {
      PLMipsViews.showColumnView();
    });
    $('#mips-full-view').click(() => {
      PLMipsViews.showFullView();
    });

    // Setup handler to open help modal.
    $('#mips-help').click(() => {
      PLMipsViews.showHelp();
    });

    // Whenever the full modal is closed, re-activate the previous view.
    $('#mips-full-modal').on('hide.bs.modal', (event) => {
      $('#mips-navbar .nav-link.active').click();
    })
  }

  // Activate the default view based on configuration. Falls back to run view.
  static showDefaultView() {
    if (PLMipsDebugger.options.defaultView === 'column') {
      PLMipsViews.setActiveView('col');
    } else {
      PLMipsViews.setActiveView('run');
    }
  }

  // Activate the given view, or fallback to the run view.
  static setActiveView(view) {
    if (view === 'full') {
      $('#mips-full-view').click();
    } else if (view === 'col') {
      $('#mips-col-view').click();
    } else {
      $('#mips-run-view').click();
    }
  }

  static showRunView() {
    PLMipsViews.move('#mips-run-buttons', '#play-button');
    PLMipsViews.move('#mips-run-buttons', '#reset-button');
    PLMipsViews.move('#mips-run-buttons', '#sync-button');
    PLMipsViews.move('#mips-run-panels', '#output-panel');
    PLMipsViews.move('#mips-run-panels', '#log-panel');

    PLMipsViews.show('#output-panel');
    PLMipsViews.show('#mips-run-view-container');
    PLMipsViews.hide('#mips-col-view-container');

    $('#mips-run-view').addClass('active');
    $('#mips-col-view').removeClass('active');
    $('#mips-full-view').removeClass('active');

    PLMipsViews.setMaxSpeed();
  }

  static showColumnView() {
    PLMipsViews.move('#text-panel-buttons', '#play-button');
    PLMipsViews.move('#text-panel-buttons', '#step-button');
    PLMipsViews.move('#text-panel-buttons', '#reset-button');
    PLMipsViews.move('#text-panel-buttons', '#sync-button');
    PLMipsViews.move('#mips-col-main-panels', '#regs-panel');
    PLMipsViews.move('#mips-col-main-panels', '#text-panel');
    PLMipsViews.move('#mips-col-more-panels', '#data-panel');
    PLMipsViews.move('#mips-col-more-panels', '#stack-panel');
    PLMipsViews.move('#mips-col-more-panels', '#output-panel');
    PLMipsViews.move('#mips-col-more-panels', '#log-panel');

    PLMipsViews.toggleColumnPanels();
    PLMipsViews.rebuildColumnGrid();
    PLMipsViews.hide('#mips-run-view-container');
    PLMipsViews.show('#mips-col-view-container');

    if ($('#mips-run-view').hasClass('active')) {
      PLMipsViews.restoreSpeed();
    }

    $('#mips-run-view').removeClass('active');
    $('#mips-col-view').addClass('active');
    $('#mips-full-view').removeClass('active');
  }

  static showFullView() {
    PLMipsViews.move('#text-panel-buttons', '#play-button');
    PLMipsViews.move('#text-panel-buttons', '#step-button');
    PLMipsViews.move('#text-panel-buttons', '#reset-button');
    PLMipsViews.move('#text-panel-buttons', '#sync-button');
    PLMipsViews.move('#mips-full-view-container', '#regs-panel');
    PLMipsViews.move('#mips-full-view-container', '#text-panel');
    PLMipsViews.move('#mips-full-view-container', '#data-panel');
    PLMipsViews.move('#mips-full-view-container', '#stack-panel');
    PLMipsViews.move('#mips-full-view-container', '#output-panel');
    PLMipsViews.move('#mips-full-view-container', '#log-panel');

    PLMipsViews.hide('#mips-run-view-container');
    PLMipsViews.hide('#mips-col-view-container');
    PLMipsViews.showAllPanels();

    if ($('#mips-run-view').hasClass('active')) {
      PLMipsViews.restoreSpeed();
    }

    // Hide all other modals before showing this one.
    $('.modal').modal('hide');
    $('#mips-full-modal').modal('toggle');
  }

  static showAllPanels() {
    PLMipsViews.show('#data-panel');
    PLMipsViews.show('#stack-panel');
    PLMipsViews.show('#output-panel');
  }

  // Adjust the visibility of panels in column view depending on configuration.
  static toggleColumnPanels() {
    let enable = !!PLMipsDebugger.options.enableDataPanel;
    $('#data-panel').toggleClass('d-none', !enable);

    enable = !!PLMipsDebugger.options.enableStackPanel;
    $('#stack-panel').toggleClass('d-none', !enable);

    enable = !!PLMipsDebugger.options.enableOutputPanel;
    $('#output-panel').toggleClass('d-none', !enable);
  }

  // Reconstruct CSS grid for the panels depending on if things got hidden or not.
  // This approach is very brittle and need to align with the layout we have in CSS.
  static rebuildColumnGrid() {
    let areas = [];
    let rows = [];

    if (!!PLMipsDebugger.options.enableDataPanel) {
      areas.push('"data data"');
      rows.push('26rem');
    }

    if (!!PLMipsDebugger.options.enableStackPanel) {
      areas.push('"stack stack"');
      rows.push('26rem');
    }

    if (!!PLMipsDebugger.options.enableOutputPanel) {
      areas.push('"output log"');
      rows.push('16rem');
    } else {
      areas.push('"log log"');
      rows.push('16rem');
    }

    const container = $('#mips-col-more-panels');
    container.css('grid-template-areas', areas.join(' '));
    container.css('grid-template-rows', rows.join(' '));
  }

  static setMaxSpeed() {
    PLMipsViews.previousSpeed = PLMipsDebugger.currentSpeed();
    PLMipsDebugger.adjustSpeed(100);
  }

  static restoreSpeed() {
    let speed = PLMipsViews.previousSpeed;
    if (speed != null) {
      PLMipsDebugger.adjustSpeed(speed);
    } else {
      PLMipsDebugger.adjustSpeed(90);
    }
  }

  static showHelp() {
    // Hide all other modals before showing this one.
    $('.modal').modal('hide');
    $('#mips-help-modal').modal('toggle');
  }

  static move(target, source) {
    $(source).appendTo(target);
  }

  static show(selector) {
    $(selector).removeClass('d-none');
  }

  static hide(selector) {
    $(selector).addClass('d-none');
  }
}

// This module represents the WASM module for the SPIM simulator.
// The wasm.js script should be loaded after this one, so it will add
// properties to the Module defined here instead of creating a new one.
var Module = {
  postRun: [PLMipsDebugger.postModuleLoad],
  print: (text) => {
    Elements.output.innerHTML += text + "\n";
    Elements.output.scrollTop = Elements.output.scrollHeight;
  },
  printErr: (text) => {
    Elements.log.innerHTML += text + "\n";
    Elements.log.scrollTop = Elements.log.scrollHeight;
  },
  printCredits: () => {
    Elements.log.innerHTML += CREDITS + " ";
    Elements.log.scrollTop = Elements.log.scrollHeight;
  }
};
