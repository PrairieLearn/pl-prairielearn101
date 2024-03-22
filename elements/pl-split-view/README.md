## `pl-split-view` element

A custom element for showing page elements in a side-by-side view. A typical
use-case is to show a `pl-code` element on the left pane, while having a
`pl-file-editor` element on the right pane, to allow students to more easily
work on code (such as when translating C code to MIPS). However, this custom
element is general enough so that we can put any elements we want on the left
and right of the split view.

### Usage

1. Identity the HTML elements you want for the split view.

2. Wrap the elements in a container and assign them an id. E.g.:

    ```html
    <div id="my-code">
      <pl-code>...</pl-code>
    </div>
    ...
    <div id="my-editor">
      <pl-file-editor ...></pl-file-editor>
    </div>
    ...
    <div id="my-debugger">
      <pl-mips-debugger ...></pl-mips-debugger>
    </div>
    ```

3. Add this element to the question's HTML template and customize as desired.
   This can go anywhere in the question template, and it will render a button
   that opens the split view (see tips below for how to customize button).

    ```html
    <pl-split-view
        left-ids="my-code my-debugger"
        right-ids="my-editor"
        ...>
    </pl-split-view>
    ```

### Element Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `left-ids` | string (required) | Space-separated list of IDs for elements to show on the left side of the split view. |
| `right-ids` | string (required) | Space-separated list of IDs for elements to show on the right side of the split view. |
| `title` | string (default: "Split View") | Title for the split view popup modal. |

Note that the order of IDs in the `left-ids` and `right-ids` lists will be the
order of elements shown in the pane from top to bottom. Also note that this
custom element is only supported in the question panel.

### Tip: Customize View Styles

Sometimes you might want to customize the look & feel of the split view for
certain questions. Although this might not be a common use case, it is possible
by targeting specific CSS used by the split view.

The split view popup is implemented using Bootstrap's modal component, and has
a certain hierarchy. Here's a rough layout of the important elements in the
hierarchy that you can try targeting:

```
#split-modal
└── ...
  └── #split-container
    ├── #split-pane-left
    ├── .gutter
    └── #split-pane-right
```

For example, if you want to make the left pane more colorful for a certain
question, you can add the following in the question's template:

```html
<style>
  #split-pane-left {
    background-color: aquamarine;
    padding: 1rem;
  }
</style>
```

### Tip: Customize Button

By default, the split view button will show the text `Open split view`. You can
customize what the button says by providing your own inner HTML for the custom
element. This means you can put any HTML inside, such as icons:

```html
<pl-split-view left-ids="id1 id2" right-ids="id3">
  <i class="fa fa-expand"></i> Open Sesame
</pl-split-view>
```

You can also customize the styles of the button by targeting the
`#split-button` CSS selector.

### Tip: Relocating Button

One use-case might be showing the split view button in a specific location on
the page. This might be desirable for MIPS programming questions, where it will
be nice to have the split view button in the footer right below the text
editor, inline with the other editor buttons.

This can be done by adding a bit of JavaScript in the question's template:

```html
<script>
  $(document).ready(() => {
    $('#split-button').prependTo('<editor-id-here> .card .card-footer');
  });
</script>
```

Although this could be something offered by this custom element, we're trying
to keep it more general. In fact, we don't impose where the split view button
needs to go, so you can put the button anywhere. For example, you can put the
button inline beside a header like so:

```html
<div>
  <h2 style="display: inline-block; margin-right: 10px;">Some Header</h2>
  <pl-split-view left-ids="id1 id2" right-ids="id3"></pl-split-view>
</div>
```

### Developer Notes

We use the [SplitJS][splitjs] library for managing the splits, which also
provides the resizable gutter functionality. We use our own copy of the
minified version of the library instead of loading from external source (e.g.
from CDN) so that we can keep everything within PrairieLearn and avoid the
possibility of external requests getting blocked (e.g. when student is taking
quiz in CBTF). It also ensures we always use the same version of the library.
To get a new copy or new version, download the JS file from here:

```
https://unpkg.com/split.js/dist/split.min.js
```

The split view is created by "moving" the page elements into the modal. In
order to restore the elements when the modal closes, hidden "marker" elements
are created and inserted at the original location of those elements.

[splitjs]: https://split.js.org/
