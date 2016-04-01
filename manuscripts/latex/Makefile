PANDOC=pandoc
PANDOC_OPTS=--no-tex-ligatures --chapters
SCRIPT_PATH=../../scripts
CLEANMD=$(SCRIPT_PATH)/cleantex.py
MARKDOWN_PATH=../markdown
MARKDOWN_FILES=chapter01.md
LATEX_FILES=$(MARKDOWN_FILES:.md=.tex)

all: $(LATEX_FILES)

%.tex: $(MARKDOWN_PATH)/%.md
	$(PANDOC) $(PANDOC_OPTS) $< -t latex | $(CLEANMD) > $@

clean:
	rm -rf *.tex
