# py-cooperhewitt-roboteyes-atkinson

## Usage

### Simple

	import sys
	import cooperhewitt.roboteyes.atkinson as atkinson

	source = sys.argv[1]
	dest = sys.argv[2]

	atkinson.dither(source, dest)

### Fancy

	import sys
	import cooperhewitt.roboteyes.atkinson as atkinson

	source = sys.argv[1]
	dest1 = sys.argv[2]
	dest2 = sys.argv[3]

	atkinson.dither_atk(source, dest1)
	atkinson.dither_python(source, dest2)

## See also

* https://github.com/migurski/atkinson
