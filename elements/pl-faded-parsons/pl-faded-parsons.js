
// fetch char_width_in_px
let context = document.createElement("canvas").getContext("2d");
context.font = "monospace";
const char_width_in_px = context.measureText("0").width;

class ParsonsCodeLine {
    constructor(elem, widget) {

        this.widget = widget;
        this.elem = elem;
        let code_indent = NaN;

        if (elem.style !== null) {
          let raw_indent = parseInt(elem.style.marginLeft, 10);
          code_indent = raw_indent / widget.options.x_indent;
        } 

        this.code_indent = isNaN(code_indent) ? 0 : code_indent;
    }
    elem () { return this.elem; }
    asText () { 
        let elemClone = $(this.elem).clone();
        elemClone.find("input").each(function (_, inp) {
            inp.replaceWith(inp.value);
        });
        elemClone[0].innerText = elemClone[0].innerText.trimRight();

        let spaceCount = this.widget.options.x_indent * this.code_indent;
        return " ".repeat(spaceCount) + elemClone[0].innerText;
    }
    asSegments () {
        let elemClone = $(this.elem).clone();
        let blank_values = []
        elemClone.find("input").each(function (_, inp) {
            blank_values.push(inp.value);
            inp.replaceWith("!BLANK");
        });
        return {
          given_segments : elemClone.text().split("!BLANK"),
          blank_values   : blank_values
        }
    }
    markCorrect() {}
    markIncorrectPosition() {}
    markIncorrectIndent() {}
}

class ParsonsWidget {
    constructor(options) {
        const defaults = {
            source_tray: false,
            source_tray: "starter-code",
            solution_tray: "parsons-solution",
            x_indent: 4,
            can_indent: true,
            onSortableUpdate: (_event, _ui) => {},
            onBlankUpdate: (_event, _codeline) => {},
            
            // TODO: reimplement support (tagged with TODO:FB)
            incorrectSound: false,
            feedback_cb: false,
            first_error_only: true,
            max_wrong_lines: 10, // maybe not needed?
            lang: "en",
        };

        this.options = jQuery.extend({}, defaults, options);

        if ( window.prettyPrint &&
            ( typeof this.options.prettyPrint === "undefined" ||
              this.options.prettyPrint )
        ) {
            prettyPrint();
        }


        const that = this;
        const sortable = $("#ul-" + this.options.solution_tray).sortable({
            start: function () {
                that.clearFeedback();
            },
            stop: function (event, ui) {
                if ($(event.target)[0] != ui.item.parent()[0]) {
                    return;
                }
                
                if (that.options.can_indent) {
                    that.updateIndent(
                        that.calculateCodeIndent(
                            ui.position.left - ui.item.parent().position().left, 
                            ui.item[0] ), 
                        ui.item[0] );
                }
                
                that.addLogEntry({ type: "moveOutput", target: ui.item[0].id }, true);
            },
            receive: function (_event, ui) {
                that.updateIndent(
                    that.calculateCodeIndent(
                        ui.position.left - ui.item.parent().position().left, // TODO: check if this left distance calc is correct
                        ui.item[0] ), 
                    ui.item[0] );

                that.addLogEntry({ type: "addOutput", target: ui.item[0].id }, true);
            },
            update: that.options.onSortableUpdate,
            grid: that.options.can_indent ? [that.options.x_indent, 1] : false,
        });
        sortable.addClass("output");

        if (this.options.source_tray) {
            const sourceTray = $("#ul-" + this.options.source_tray).sortable({
                connectWith: sortable,
                start: function () {
                    that.clearFeedback();
                },
                receive: function (_event, ui) {
                    // that.getLineById(ui.item[0].id).indent = 0;
                    that.updateIndent(0, ui.item[0].id);
                    that.addLogEntry(
                        { type: "removeOutput", target: ui.item[0].id },
                        true
                    );
                },
                stop: function (event, ui) { 
                    if ($(event.target)[0] != ui.item.parent()[0]) { 
                        // line moved to output and logged there 
                        return;
                    }
                    that.addLogEntry({ type: "moveInput", target: ui.item[0].id }, true);
                },
            });
            sortable.sortable("option", "connectWith", sourceTray);
        }

        // set up event listeners on input fields for blanks
        $("input.parsons-blank").each(function (_index, item) {
            item.addEventListener("input", function (e) {
                that.options.onBlankUpdate(e, item);
            });
        });

        // when blanks are filled, adjust their width
        $('input.text-box').on('input', function() {
            $(this).width( this.value.length.toString() + 'ch');
        });

        // Log the original codelines in the exercise in order to be able to
        // match the input/output hashes to the code later on. We need only a
        // few properties of the codeline objects
        /*
        const bindings = this.modified_lines
            .map(line => { return { code: line.code, distractor: line.distractor }; }); // * /
        this.addLogEntry({ type: "init", time: new Date(), bindings: bindings }); // */
        
        /* TODO:FB
            /////////////////
            this.feedback_exists = false; 
            this.FEEDBACK_STYLES = { 
                correctPosition: "correctPosition",
                incorrectPosition: "incorrectPosition",
                correctIndent: "correctIndent",
                incorrectIndent: "incorrectIndent",
            };
            
            // use grader passed as an option if defined and is a function
            if (this.options.grader && _.isFunction(this.options.grader)) {
                this.grader = new this.options.grader(this);
            } else {
                this.grader = new LineBasedGrader(this);
            }
        // */

    }
    getSourceLines() {
        let source_tray = document.getElementById("ul-" + this.options.source_tray);
        if (source_tray === null) { return []; }

        let trayHTMLLines = Array.from( source_tray.children);
        return trayHTMLLines.map((elem, _) => new ParsonsCodeLine(elem, this));
    }
    getSolutionLines () {
        let solution_tray = document.getElementById("ul-" + this.options.solution_tray);
        if (solution_tray === null) { return []; }

        let trayHTMLLines = Array.from( solution_tray.children);
        return trayHTMLLines.map((elem, _) => new ParsonsCodeLine(elem, this));
    }
    calculateCodeIndent(dist_in_px, elem) {
        let dist = dist_in_px / char_width_in_px;
        let old_code_indent = (new ParsonsCodeLine(elem, this)).code_indent;
        let new_code_indent = old_code_indent + Math.floor(dist / this.options.x_indent);
         
        return Math.max(0, new_code_indent);
    }
    solutionCode() {
        const solution_lines = this.getSolutionLines();
        
        let solutionCode = ""
        let codeMetadata = "";
        let blankText = "";
        let originalLine = "";
        for (const line of solution_lines) {
            const yamlConfigClone = $(line.elem).clone();
            
            blankText = "";
            yamlConfigClone.find("input").each(function (_, inp) {
                inp.replaceWith("!BLANK");
                blankText += " #blank" + inp.value;
            });
            yamlConfigClone[0].innerText = yamlConfigClone[0].innerText.trimRight();

            if (yamlConfigClone[0].innerText != line.asText()) {
                originalLine = " #!ORIGINAL" + yamlConfigClone[0].innerText + blankText;
            } else {
                originalLine = yamlConfigClone[0].innerText + blankText;
            }

            solutionCode += line.asText() + "\n";
            codeMetadata += originalLine + "\n";
        }

        return [solutionCode, codeMetadata];
    }

    // Takes the x-axis change of the location of the passed element in `ch` units
    updateIndent(new_code_indent, elem) {
        let line = new ParsonsCodeLine(elem, this);
        let old_code_indent = line.code_indent;
        
        if (old_code_indent !== new_code_indent) {
            this.options.onSortableUpdate(
                {
                    type: "reindent",
                    content: line.asText(),
                    old: old_code_indent,
                    new: new_code_indent,
                },
                $("#ul-" + this.options.sortableId).sortable("toArray")
            );

            $(elem).css(
                "margin-left",
                this.options.x_indent * new_code_indent + "ch"
            );

            this.updateVertLines();
        }

        return new_code_indent;
    }
    updateVertLines() {
        if (!this.options.can_indent) {
            return;
        }

        let max_code_indent = 0;
        this.getSolutionLines().forEach(function (line) {
            max_code_indent = Math.max(max_code_indent, line.code_indent);
        });
        // Get current indents
        const element = $("#ul-" + this.options.solution_tray);
        const backgroundColor = element.css("background-color");
        let backgroundPosition = "";
        for (let i = 1; i <= max_code_indent + 1; i++) {
            backgroundPosition += i * this.options.x_indent + "ch 0, "; 
        }
        element.css({
        background:
            "linear-gradient(#ee0, #ee0) no-repeat border-box, "
                .repeat(max_code_indent)
                .slice(0) 
                + "repeating-linear-gradient(0,#ee0,#ee0 10px," 
                + backgroundColor 
                + " 10px, " 
                + backgroundColor 
                + " 20px) no-repeat border-box",
            "background-size": "1px 100%, ".repeat(max_code_indent + 1).slice(0, -2),
            "background-position": backgroundPosition.slice(0, -2),
            "background-origin": "padding-box, ".repeat(max_code_indent + 1).slice(0, -2),
            "background-color": backgroundColor,
        });
    }

    // getHash() {}
    // solutionHash() {}
    // trashHash() {}
    addLogEntry() {}
    // getLineById() {}
    // normalizeIndents() {} 
    // getModifiedCode() {}
    // hashToIDList() {}
    // updateIndentsFromHash() {}
    // displayError() {}
    // colorFeedback() {}
    // getFeedback() {}
    clearFeedback() {}
    // getRandomPermutation() {}
    // shuffleLines() {}
    // alphabetize() {}
    // createHTMLFromHashes() {}
    // updateHTMLIndent() {}
    // codeLineToHTML () {}
    // codeLinesToHTML() {}
    // createHTMLFromLists() {}
}

/////////////////////////////////////////////////////////////////////////////////////////////
const ParsonsGlobal = {
    makeLogger: false,
    logger: null,
    widget: null,
    /*
     * When form is submitted, capture the state of the student's solution.
     * For now we only submit the actual code, NOT the original metadata of where the blanks were etc.
     */
    submitHandler: function() {
      var starterCode = ParsonsGlobal.widget.getSourceLines();
      const starterElements = [];

      starterCode.forEach(function(line, idx) {
          starterElements.push({ content: line.asText(), indent: line.code_indent, index: idx, segments: line.asSegments() });
      });
      $('#starter-code-order').val(JSON.stringify(starterElements));
      
      var solutionCode = ParsonsGlobal.widget.getSolutionLines();
      const solutionElements = [];
      solutionCode.forEach(function(line, idx) {
          solutionElements.push({content: line.asText(), indent: line.code_indent, index: idx, segments: line.asSegments() });
      });
      $('#parsons-solution-order').val(JSON.stringify(solutionElements));
      
      let out = ParsonsGlobal.widget.solutionCode();
      $('#student-parsons-solution').val(out[0]);
  
      ParsonsGlobal.logger && ParsonsGlobal.logger.onSubmit();
    },
  
    /*
     * Initialize the widget.  Code that goes in left-hand box will be in
     * the hidden form field  named 'code-lines'.
     * For now, no logging of events is done.
     */
    setup: function() {
      ParsonsGlobal.widget = new ParsonsWidget({
        'solution_tray': 'parsons-solution', //  This should be changeable from question.html 
                                          //  in the case of multiple FPPs in one question
        'onSortableUpdate': (event, ui) => {
          ParsonsGlobal.logger && ParsonsGlobal.logger.onSortableUpdate(event, ui);
        },
        'onBlankUpdate': (event, codeline) => {
          ParsonsGlobal.logger && ParsonsGlobal.logger.onTextUpdate(event, codeline);
        },
        'source_tray': 'starter-code',
      });

      ParsonsGlobal.widget.updateVertLines();
      
      // when form submitted, grab the student work and put it into hidden form fields
      $('form.question-form').submit(ParsonsGlobal.submitHandler);
  
      if (ParsonsGlobal.makeLogger && (typeof ParsonsLogger !== 'undefined') && !ParsonsGlobal.logger) {
        ParsonsGlobal.logger = new ParsonsLogger(ParsonsGlobal.widget);
      }
      
    }
  }
  
$(document).ready(ParsonsGlobal.setup);
