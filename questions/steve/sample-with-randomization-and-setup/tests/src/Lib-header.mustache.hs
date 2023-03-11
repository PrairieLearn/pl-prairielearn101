module Lib where
{{#params}}
data {{TypeName}} = {{#Cases}}{{Constructor}}{{#Types}} {{.}}{{/Types}}
     {{TypeNameSpaces}} | {{/Cases}}{{#LastCase}}{{Constructor}}{{#Types}} {{.}}{{/Types}}{{/LastCase}}
  deriving (Show, Eq)
{{/params}}