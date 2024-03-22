## `pl-mips-debugger` element

### Usage

We'll need a few things in order to use the MIPS debugger. Note that this
element is only supported in the question panel.

1. Create assembly file for the main function to use (e.g. `main.s`) and place
   it in your question's `clientFilesQuestion` directory.

2. Add an editor element to your question panel and wrap it in a container. The
   editor is where the students will write their code. Give the container an
   `id` attribute, which will be used to locate the editor and fetch the code
   for the debugger.

    ```html
    <div id="my-editor">
      <pl-file-editor ...></pl-file-editor>
    </div>
    ```

3. Add the debugger element and customize as desired.

    ```html
    <pl-mips-debugger
        editor-id="my-editor"
        question-main-file="main.s"
        ...>
    </pl-mips-debugger>
    ```

### Element Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `editor-id` | string (required) | ID for the container that holds the editor where code will be fetched from. |
| `question-main-file` | string (default: "main.s") | Name of file that contains the bootstrapping code to use when reloading. |
| `default-view` | string (default: "run") | The view to start with, can be `run` or `column`. |
| `show-float-registers` | bool (default: false) | Whether to show the floating-point registers in the registers panel. |
| `show-kernel-toggles` | bool (default: false) | Whether to show toggles for kernel text and data. |
| `show-data-panel` | bool (default: false) | Whether to show the data panel (displayed beneath the register/text panels). |
| `show-stack-panel` | bool (default: false) | Whether to show the stack panel (displayed beneath the data panel). |
| `show-output-panel` | bool (default: true) | Whether to show the output panel (displayed beneath the stack panel). |

Note: the attributes for toggling the panels are only effective for the
`column` view. The Run View will always display the output and log panels. And
the Full View will display all the panels.

### Customize Inner HTML

You may customize what gets rendered above the panels by putting html inside
the element tags. If not provided, then this element will render the default
introductory message.

```html
<pl-mips-debugger ...>
  <h4>The Debugger</h4>
  <p>Custom message here!</p>
</pl-mips-debugger>
```

### Developer Notes

Majority of the functionality is derived from [JsSpim][jsspim] with minimal
changes. The files needed for JsSpim are located in this element's `jsspim`
directory. This helps consolidate the code for JsSpim into one place, and helps
isolate it from the element's own code.

JsSpim provides functionality on top of SPIM, which is loaded into the browser
as a WebAssembly (WASM) module. Given the way that WASM loads its dependencies,
these files are placed in `clientFilesElement` instead so we can better control
how those files are loaded. Likewise, the `highlight.js` library is placed in
`clientFilesElement` for similar reasons.

[jsspim]: https://github.com/ShawnZhong/JsSpim
