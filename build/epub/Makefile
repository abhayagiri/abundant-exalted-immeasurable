ZIP=zip
OUTFILE=out.epub
CHECK=epubcheck
PANDOC=pandoc
PANDOC_OPTS=--template=template.xhtml
MARKDOWN_PATH=../../manuscripts/markdown
MARKDOWN_FILES=chapter01.md chapter02.md chapter03.md chapter04.md\
    chapter05.md chapter06.md chapter07.md chapter08.md\
    chapter09.md chapter10.md chapter11.md chapter12.md\
    chapter13.md chapter14.md chapter15.md chapter16.md\
    chapter17.md chapter18.md copyright.md dedication.md\
    foreword.md abbreviations.md credits.md about_the_author.md
XHTML_PATH=root/OEBPS/text
XHTML_FILES=$(MARKDOWN_FILES:.md=.xhtml)

all: $(OUTFILE) check

$(OUTFILE): clean
	cd root; \
	zip -o ../$(OUTFILE) -X -0 mimetype; \
	zip -o ../$(OUTFILE) -X -x mimetype -r *

%.xhtml: $(MARKDOWN_PATH)/%.md
	$(PANDOC) $(PANDOC_OPTS) $< -o $(XHTML_PATH)/$@

xhtml: $(XHTML_FILES)

clean_xhtml:
	cd $(XHTML_PATH); \
	rm -f $(XHTML_FILES)

check:
	$(CHECK) $(OUTFILE)

clean:
	rm -f $(OUTFILE)
