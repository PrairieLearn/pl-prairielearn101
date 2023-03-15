class ProbeMinus extends PLDrawingBaseElement {
  static generate(canvas, options, submittedAnswer) {
    fabric.Image.fromURL(options.image_url, (obj) => {
      /* Generate a unique ID for this object if it doesn't have one */
      if (!('id' in obj)) {
        obj.id = PLDrawingApi.generateID();
      }

      /* Set the Fabric object's values from what we loaded */
      obj.set({
        left: options.left,
        top: options.top,
        angle: options.angle,
        originX: 'center',
        originY: 'center',
      });

      /* Disable the scaling and rotate controls */
      obj.setControlsVisibility({
        mt: false,
        mb: false,
        ml: false,
        mr: false,
        bl: false,
        br: false,
        tl: false,
        tr: false,
        mtr: false
      });

      canvas.add(obj);
      submittedAnswer.registerAnswerObject(options, obj);
    });
  }

  static get_button_tooltip() {
    return 'Add negative probe';
  }

  static get_button_icon() {
    return 'probe-minus-icon.svg';
  }
}

PLDrawingApi.registerElements('probe-minus', {
  'pl-probe-minus': ProbeMinus,
});
