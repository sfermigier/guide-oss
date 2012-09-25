all: master.odt master.pdf

master.odt: master.rst
	rst2odt.py $< $@
	#pandoc -t odt -o $@ $<

master.tex: master.rst
	rst2latex.py $< $@

master.pdf: master.tex
	pdflatex $<

clean:
	rm -f master.tex master.pdf master.odt master.html *.aux *.log
