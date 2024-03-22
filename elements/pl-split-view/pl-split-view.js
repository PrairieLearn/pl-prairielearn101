class PLSplitView {
  static init(leftIds, rightIds) {
    PLSplitView.leftIds = Object.freeze(leftIds);
    PLSplitView.rightIds = Object.freeze(rightIds);

    PLSplitView.relocateModal();
    PLSplitView.injectMarkers();
    PLSplitView.setupEventHandlers();

    const panes = ['#split-pane-left', '#split-pane-right'];
    PLSplitView.split = window.Split(panes, {
      sizes: [50, 50],
    });
  }

  static relocateModal() {
    // Due to how PL custom elements are expanded in-place and that the only
    // visible thing from this element is the button, we need to move the modal
    // to somewhere else (e.g. the "top level") in order to avoid weird
    // parent-child/recursion issues.
    $('#split-modal').appendTo('.question-block');
  }

  static injectMarkers() {
    // Note: question template can be duplicated across PL's three different
    // panels (question, submission, answer). So it is possible that the
    // element ID is not unique on the page, but it should be unique within the
    // question panel so we scope the selector to that.
    PLSplitView.leftIds.forEach(elemId => {
      const marker = `<div id="split-marker-${elemId}" class="d-none"></div>`;
      $(marker).insertBefore(`.question-block #${elemId}`);
    });
    PLSplitView.rightIds.forEach(elemId => {
      const marker = `<div id="split-marker-${elemId}" class="d-none"></div>`;
      $(marker).insertBefore(`.question-block #${elemId}`);
    });
  }

  static setupEventHandlers() {
    $('#split-button').click(event => {
      event.preventDefault();
      PLSplitView.moveElements();
      PLSplitView.hideButton();
      PLSplitView.showModal();
    });
    $('#split-modal').on('hide.bs.modal', () => {
      PLSplitView.restoreElements();
      PLSplitView.showButton();
    });
  }

  static moveElements() {
    PLSplitView.leftIds.forEach(elemId => {
      $(`.question-block #${elemId}`).appendTo('#split-pane-left');
    });
    PLSplitView.rightIds.forEach(elemId => {
      $(`.question-block #${elemId}`).appendTo('#split-pane-right');
    });
  }

  static restoreElements() {
    PLSplitView.leftIds.forEach(elemId => {
      $(`.question-block #${elemId}`).insertAfter(`#split-marker-${elemId}`);
    });
    PLSplitView.rightIds.forEach(elemId => {
      $(`.question-block #${elemId}`).insertAfter(`#split-marker-${elemId}`);
    });
  }

  static hideButton() {
    $('#split-button').addClass('d-none');
  }

  static showButton() {
    $('#split-button').removeClass('d-none');
  }

  static showModal() {
    // Hide all other modals before showing this one.
    $('.modal').modal('hide');
    $('#split-modal').modal('toggle');
  }
}
