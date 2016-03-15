# Spackle
Spackle sorts your Coverage.py result report, so you can identify gaps in test coverage faster.

## Install
`pip install spackle`

## Usage
Simply run `spackle` after executing Coverage.py's run command, instead of running `coverage report -m`. Spackle will output the original coverage report and a new report that contains only multi line gaps in coverage, sorted by the amount of lines missing.

## Example

Example usage:

```
coverage run ./manage.py test demo
spackle
```

Example output (shortened):

```
Name                                   Stmts   Miss  Cover   Missing
--------------------------------------------------------------------
demo/querysets.py                         63     27    57%   16, 19, 53, 56-57, 64-101
demo/views.py                            106     84    21%   18-39, 45-46, 55-92, 103-134, 143-153, 162-185
demo/utils/github.py                      48     24    50%   10-49
demo/utils/graphs.py                     100     27    73%   41, 63-64, 68-73, 156-196
--------------------------------------------------------------------
TOTAL                                    317    162    86%

Largest gaps in coverage:

Name                                    Missing                 Miss
--------------------------------------------------------------------
demo/utils/graphs.py                     156-196                  40
demo/utils/github.py                     10-49                    39
demo/querysets.py                        64-101                   37
demo/views.py                            55-92                    37
demo/views.py                            103-134                  31
demo/views.py                            162-185                  23
demo/views.py                            18-39                    21
demo/views.py                            143-153                  10
demo/utils/graphs.py                     68-73                    5
demo/views.py                            45-46                    1
demo/utils/graphs.py                     63-64                    1
demo/querysets.py                        56-57                    1
```
