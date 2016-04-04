PANDOC=pandoc
PANDOC_OPTS=--no-tex-ligatures --chapters
SCRIPT_PATH=../../scripts
CLEANMD=$(SCRIPT_PATH)/cleantex.py
MARKDOWN_PATH=../markdown
MARKDOWN_FILES=chapter01.md chapter02.md chapter03.md chapter04.md\
    chapter05.md chapter06.md chapter07.md chapter08.md\
    chapter09.md chapter10.md chapter11.md chapter12.md\
    chapter13.md chapter14.md chapter15.md chapter16.md\
    chapter17.md chapter18.md copyright.md dedication.md\
	preface.md abbreviations.md
LATEX_FILES=$(MARKDOWN_FILES:.md=.tex)

all: $(LATEX_FILES)

%.tex: $(MARKDOWN_PATH)/%.md
	$(PANDOC) $(PANDOC_OPTS) $< -t latex | $(CLEANMD) > $@

clean:
	rm -rf $(LATEX_FILES)
