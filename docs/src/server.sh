#!/usr/bin/env Rscript
# https://bookdown.org/yihui/bookdown/serve-the-book.html

bookdown::serve_book(dir = ".", output_dir = "_book", preview = TRUE, in_session = TRUE)