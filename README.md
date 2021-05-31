# cuda_lint_raku

Raku language linter for cudatext. Uses "raku -c"

To the moment it supports the following error messages

1.
```
===SORRY!=== Error while compiling file.raku
Undeclared routines:
    asd used at line 8
    basd used at line 10
```

2.
```
===SORRY!=== Error while compiling file.raku
Variable '$a' is not declared
at file.raku:12
```

3.
```
===SORRY!=== Error while compiling file.raku
Unsupported use of ?  and : for the ternary conditional operator.  In
Raku please use: ??  and !!.
at file:11
```