#!/bin/bash
echo '---------------------------Running Tests--------------------------'
python3 -m unittest
echo '---------------------------Running PEP8---------------------------'
for f in $(find ./googleResults -name '*.py' -or -name '*.doc'); do pep8 $f; done
echo '------------------------------------------------------------------'
echo '---------------------Running PEP8 OVER TESTS----------------------'
for f in $(find ./tests -name '*.py' -or -name '*.doc'); do pep8 $f; done
