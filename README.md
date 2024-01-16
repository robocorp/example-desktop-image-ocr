# Desktop automation using images templates and OCR

![GnuCash Logo](https://www.gnucash.org/images/gnc-download.png)

This robot demonstrates automating a desktop application with image recognition and OCR.
The system being automated is a cross-platform free accounting software called [GnuCash](https://www.gnucash.org/).
This demo uses a mock account.

Most of the interaction happens by locating a desired text by OCR. Regions and offsets are involved too,
e.g. when you want to type text into an input field with a text label next to it,
you first find the label, then get a region or offset relative to that text and click there.

## Note about OCR

OCR refers to recognizing characters, words, and text in general. Image recognition is more
generic (and simpler) and might refer to the recognition of, e.g. colors and shapes.

OCR or image recognition based automation is usually the last resort in automation.
When thinking whether you should use OCR to automate your application, first investigate if you could:

- Read the raw data programmatically
- Use native UI selectors
- Use UI hotkeys
- Use the clipboard

Usually image recognition must be used when dealing with Citrix (or similar).
Even then hotkeys and the clipboard are oftentimes more reliable than pure OCR.

Another use case for OCR is reading text from documents (PDF, JPEG),
this demo does not consider that use case at all.

## Requirements

This robot assumes the running environment has a functional installation
of [GnuCash](https://www.gnucash.org/). All other dependencies are
handled by RCC and conda.yaml.
