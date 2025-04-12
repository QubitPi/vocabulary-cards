TEX_ENGINE=xelatex
REMOVE_AUXILIARY=make clean

GREEK_PROJECT=ancient-greek
BUILDTEX_GREEK=$(TEX_ENGINE) -shell-escape $(GREEK_PROJECT).tex

GERMAN_PROJECT=german
BUILDTEX_GERMAN=$(TEX_ENGINE) -shell-escape $(GERMAN_PROJECT).tex

all:
	make greek
	make german

greek:
	$(REMOVE_AUXILIARY)
	$(BUILDTEX_GREEK)
	$(BUILDTEX_GREEK)
	$(BUILDTEX_GREEK)
	$(REMOVE_AUXILIARY)

# this target cannot be named "german" which collides with the $GERMAN_PROJECT and therefore won't trigger compilation
# unless forced by PHONY
.PHONY: german
german:
	$(REMOVE_AUXILIARY)
	$(BUILDTEX_GERMAN)
	$(BUILDTEX_GERMAN)
	$(BUILDTEX_GERMAN)
	$(REMOVE_AUXILIARY)

clean:
	find . -name "*.aux" -type f -delete
	find . -name "*.log" -type f -delete
	find . -name "*.out" -type f -delete
	find . -name "*.bbl" -type f -delete
	find . -name "*.blg" -type f -delete
	find . -name "*.toc" -type f -delete
	find . -name "*.tdo" -type f -delete
	find . -name "*.bcf" -type f -delete
	find . -name "*.glo" -type f -delete
	find . -name "*.idx" -type f -delete
	find . -name "*.ist" -type f -delete
	find . -name "*.nlo" -type f -delete
	find . -name "*.run.xml" -type f -delete
