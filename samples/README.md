#Samples

This folder contains some file samples from different stages input and output of using libJSHOL in an attempt
to demonstrate the use and provide a basic spec for how HTML will be formatted and how JSON objects will be returned.
Each of the files is annotated below.

##[sample.html.json](./sample.html.json)

This file contains the plaintext representation that would be expected by JSHOL.
An object just like this could be created with any language that has a JSON binding or with any libJSHOL JSON wrapper.
This file demonstrates how I'd probably manually write JSON.
This file maps very closely (visually) to [sample-clean.html](./sample-clean.html),
but will not necessarily output HTML like this when given to JSHOL.

##[sample-alt.html.json](./sample-alt.html.json)

This file contains a slightly shorter version of the sample.html.json text.
This version may be more preferable to some people and will result in the same output using JSHOL.
It should be noted that padding and non-content whitespace in the JSON file will not affect JSHOL html output.
This file closely maps (visually) to [sample-clean-false.html](./sample-clean-false.html),
but it should be noted that JSHOL does not consider sample-clean-false.html to be the same document.
This is explained below.

##[sample-ugly.html.json](./sample-ugly.html.json)

A computer might create JSON object like this. They're not very readable, but it's the same object.
This file will closely map (visually) to [sample.html](./sample.html).
Like the above JSON files, this file will result in the same output HTML.


##[sample.html](./sample.html)

This is the most literal output that JSHOL can create from JSON objects.
Computers will read it fine and the lack out unneccesary whitespace may result in a smaller file size.
It's not very human readable, but it's correct.

##[sample-clean.html](./sample-clean.html)

People (in general) hate this file.
This file is a literal output HTML created from above JSON samples.
It's ugly (to some) and weird because all of the non-content whitespace is inside of tags.
Whitespace outside of tags **IS CONTENT** in HTML.
libJSHOL **will not** (by defualt) create content, whitespace or otherwise.
libJSHOL does not care if your tags are `<pre>` tags or if your css says to handle them as if they
were preformatted.
If you want whitespace and a more vertical, tabulated HTML output, this is how it will be (correctly) returned.
If you accept the risks of adding whitespace because you're sure you have only sane CSS, you may eventually
get an option for the next style of output.

##[sample-clean-false.html](./sample-clean-false.html)

This is the type of HTML people are used to seeing.
Lots of fake whitespace that is usually (and fortunately) ignored when rendering the page.
libJSHOL may eventually get an option to output this.
Don't expect me to write it, because I hate adding false content.
I put this example here because I know many people read HTML best this way.
While it's not likely to be what is produced from the above JSON, it may be in the future and still
somewhat accurately represents the output.
