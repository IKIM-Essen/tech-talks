# Working with Docker on IKIM hosts

## Summary

- Overview of containers.
- Lifecycle of a container.
- Making changes in containers.
- Filesystem mounts.
- File ownership.
- Dockerfiles.
- Portability.

## Building the slides

If using the included VSCode devcontainer, execute

```
asciidoctor-revealjs slides.adoc
```

For a custom setup without the devcontainer, see [Asciidoctor docs - reveal.js converter][1].

## Opening the speaker's note

Open `slides.html` in a browser, then type `s`.

## Printing to PDF

Open the generated HTML file by adding `print-pdf` as a query string.
For example:

```
file:///project/slides.html?print-pdf
```

To show the speaker's notes, append `showNotes=true`:

```
file:///project/slides.html?print-pdf&showNotes=true
```

For details, see [reveal.js - PDF export][2].

[1]: https://docs.asciidoctor.org/reveal.js-converter/latest/setup/standalone-executable/
[2]: https://github.com/hakimel/reveal.js/blob/v3.9/README.md#instructions-1
