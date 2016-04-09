PANDOC=pandoc
PANDOC_OPTS=--no-wrap
SCRIPT_PATH=../../scripts
CLEANMD=$(SCRIPT_PATH)/cleanmd.py
HTML_PATH=../../source/html
HTML_FILES=chapter01.html chapter02.html chapter03.html chapter04.html\
    chapter05.html chapter06.html chapter07.html chapter08.html\
    chapter09.html chapter10.html chapter11.html chapter12.html\
    chapter13.html chapter14.html chapter15.html chapter16.html\
    chapter17.html chapter18.html preface.html
MARKDOWN_FILES=$(HTML_FILES:.html=.md)

all: $(MARKDOWN_FILES)

%.md: $(HTML_PATH)/%.html
	$(PANDOC) $(PANDOC_OPTS) $< -t markdown | $(CLEANMD) > $@

clean:
	rm -rf *.md
