# py-cooperhewitt-roboteyes-atkinson

Functions for generating black and white images using Bill Atkinson's dithering
algorithm.

## Usage

### Simple

	import sys
	import cooperhewitt.roboteyes.atkinson as atkinson

	source = sys.argv[1]
	dest = sys.argv[2]

	atkinson.dither(source, dest)

### Fancy

By default `cooperhewitt.roboteyes.atkinson` try to use the faster C-based `atk`
library to dither images falling back to a pure-Python version if necessary. You
can for the issue like this:

	import sys
	import cooperhewitt.roboteyes.atkinson as atkinson

	source = sys.argv[1]
	dest1 = sys.argv[2]
	dest2 = sys.argv[3]

	atkinson.dither_atk(source, dest1)
	atkinson.dither_python(source, dest2)

## See also

* https://github.com/migurski/atkinson
