all: master.odt

master.odt: master.rst
	rst2odt.py $< $@
	#pandoc -t odt -o $@ $<

clean:
	rm -f master.tex master.pdf master.odt master.html *.aux *.log
