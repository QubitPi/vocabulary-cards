Vocabulary Cards
================

[![LaTeX Badge][LaTeX Badge]][LaTeX URL]
[![GNU Badge][GNU Badge]][GNU Make]
![Python Badge][Python Badge]
[![Apache License Badge]][Apache License, Version 2.0]

- [Ancient Greek](./ancient-greek.pdf)
- [German](./german.pdf)

Development
-----------

## Setup

1. Install [Tex Live][LaTeX URL] (version ≥ 2021) and Python 3
3. Make sure [GNU Make] is installed with

   ```console
   make --version
   ```
   
   which, when installed, outputs something like this

   ```console
   GNU Make 3.81
   Copyright (C) 2006  Free Software Foundation, Inc.
   This is free software; see the source for copying conditions.
   There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
   PARTICULAR PURPOSE.

   This program built for i386-apple-darwin11.3.0
   ```
   
   `make` should be installed in almost every Linux distribution and Mac user can install via `brew install make`

### Getting Source Code

```console
git clone https://github.com/QubitPi/vocabulary-cards.git
cd vocabulary-cards
```

### Compiling

- Everything: `make`
- Ancient Greek: `make greek`
- German: `make german`

License
-------

The use and distribution terms for [vocabulary-cards]() are covered by the [Apache License, Version 2.0].

[Apache License Badge]: https://img.shields.io/badge/Apache%202.0-F25910.svg?style=for-the-badge&logo=Apache&logoColor=white
[Apache License, Version 2.0]: https://www.apache.org/licenses/LICENSE-2.0

[LaTeX Badge]: https://img.shields.io/badge/LaTeX-TeX%20Live%E2%89%A52021-008080.svg?style=for-the-badge&logo=latex&logoColor=white
[LaTeX URL]: https://tug.org/texlive/

[GNU Badge]: https://img.shields.io/badge/GNU-Make-A42E2B.svg?style=for-the-badge&logo=gnu&logoColor=white
[GNU Make]: http://uploads.mitechie.com/books/Managing_Projects_with_GNU_Make_Third_Edition.pdf

[Python Badge]: https://img.shields.io/badge/Python-3.10-3776AB.svg?style=for-the-badge&logo=python&logoColor=white
