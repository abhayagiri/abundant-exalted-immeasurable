PANDOC=pandoc
PANDOC_OPTS=
SCRIPT_PATH=../../scripts
CLEANMD=$(SCRIPT_PATH)/cleanmd.py
HTML_PATH=../../source/html
HTML_FILES=chapter01.html
MARKDOWN_FILES=$(HTML_FILES:.html=.md)

all: $(MARKDOWN_FILES)

%.md: $(HTML_PATH)/%.html
	$(PANDOC) $(PANDOC_OPTS) $< -t markdown | $(CLEANMD) > $@

clean:
	rm -rf *.md
