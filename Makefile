package=glite-initscript-globus-gridftp

.PHONY: configure install clean rpm dist

all: configure

install: 
	@echo installing ...
	@mkdir -p $(DESTDIR)/etc/init.d/ $(DESTDIR)/etc/logrotate.d/
	@install -m 0755 src/globus-gridftp $(DESTDIR)/etc/init.d/
	@install -m 0644 src/logrotate/globus-gridftp $(DESTDIR)/etc/logrotate.d/

clean::
	rm -f *~ test/*~ etc/*~ doc/*~ src/*~  
	rm -rf rpmbuild 


dist:
	echo ${package}-`sed \
		-e '/^Version:/!d' \
		-e 's/[^0-9.]*\([0-9.]*\).*/\1/' \
		-e q \
		${package}.spec` > .fname
	-rm -rf `cat .fname`
	mkdir `cat .fname`
	cp -lvr src/ Makefile LICENSE `cat .fname`
	tar chzf `cat .fname`.tar.gz `cat .fname`
	-rm -rf `cat .fname` .fname

rpm:
	@mkdir -p  RPMS
	@mkdir -p  rpmbuild/RPMS/noarch
	@mkdir -p  rpmbuild/SRPMS/
	@mkdir -p  rpmbuild/SPECS/
	@mkdir -p  rpmbuild/SOURCES/
	@mkdir -p  rpmbuild/BUILD/
	@tar --gzip --exclude='*CVS*' -cf rpmbuild/SOURCES/${package}.src.tgz *
	rpmbuild -ba ${package}.spec




