ZIP=zip
OUTFILE=out.epub
CHECK=epubcheck

all: $(OUTFILE) check

$(OUTFILE): clean
	cd root; \
	zip -o ../$(OUTFILE) -X -0 mimetype; \
	zip -o ../$(OUTFILE) -X -x mimetype -r *

check:
	$(CHECK) $(OUTFILE)

clean:
	rm -f $(OUTFILE)
