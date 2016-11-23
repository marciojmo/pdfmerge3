# pdfmerge3
`pdfmerge3` is a simple command-line utility for merging PDF files.

## Getting Started
### Install
The easiest way to install `pdfmerge3` is to use `pip`:

    $ pip install https://github.com/marciojmo/pdfmerge3.git

### Contribute
If you want to play around with the code, start by cloning
the repository:

    $ git clone git://github.com/marciojmo/pdfmerge3.git

Install the dependencies (specifically PyPDF2) using `pip`:

    $ pip install -r requirements.txt


## Usage

    $ pdfmerge3 [-h] [-o output_file] [file1.pdf file2.pdf file3.pdf ...]

  * `-o`, `--output` output file (default: `output.pdf`).
    **Must not exist in the current folder.**


## Command-line Example
    $ pdfmerge3 -o output.pdf
    Merges all pdf files from the current folder in lexicographic order and put the result in output.pdf
    
    $ pdfmerge3 -o output.pdf file1.pdf file2.pdf file3.pdf
    Merges file1.pdf, file2.pdf, file3.pdf (in this order) and put the result in output.pdf


## Python Module Usage
`pdfmerge3` can also be imported into python scripts.

    import pdfmerge3
    pdfmerge3.merge( "output.pdf", [ "file1.pdf", "file2.pdf", "file3.pdf"] )

## License
Licensed under the MIT License.