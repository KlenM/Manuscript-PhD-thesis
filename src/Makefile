.PHONY: all md2tex latexmk clean rmpdf clear

all: md2tex latexmk

latexmk:
	cd tex && latexmk

md2tex:
	cd md2tex && python main.py

clean:
	-$(MAKE) clear
	-$(MAKE) rmpdf
	-$(MAKE) all
	-$(MAKE) clear

rmpdf:
	rm -f main.pdf

clear:
	cd tex && latexmk -c; rm -rf .aux; rm -rf svg-inkscape; rm -rf converted;
