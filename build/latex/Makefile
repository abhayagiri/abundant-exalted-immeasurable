LATEX=lualatex
LATEX_OPTS=-interaction=nonstopmode -halt-on-error
LATEX_FILES=print.tex web.tex
PDF_FILES=$(LATEX_FILES:.tex=.pdf)

all: $(PDF_FILES)

%.pdf: %.tex
	$(LATEX) $(LATEX_OPTS) $<

clean:
	rm -rf *.aux *.log *.out *.toc *.pdf
