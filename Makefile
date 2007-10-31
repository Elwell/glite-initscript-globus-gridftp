prefix=/
package=glite-initscript-globus-gridftp

.PHONY: configure install clean rpm

all: configure

install: 
	@echo installing ...
	@mkdir -p $(prefix)/etc/init.d/ $(prefix)/etc/logrotate.d/
	@install -m 0755 src/globus-gridftp $(prefix)/etc/init.d/
	@install -m 0644 src/logrotate/globus-gridftp $(prefix)/etc/logrotate.d/

clean::
	rm -f *~ test/*~ etc/*~ doc/*~ src/*~  
	rm -rf rpmbuild 

rpm:
	@mkdir -p  RPMS
	@mkdir -p  rpmbuild/RPMS/noarch
	@mkdir -p  rpmbuild/SRPMS/
	@mkdir -p  rpmbuild/SPECS/
	@mkdir -p  rpmbuild/SOURCES/
	@mkdir -p  rpmbuild/BUILD/
	@tar --gzip --exclude='*CVS*' -cf rpmbuild/SOURCES/${package}.src.tgz *
	rpmbuild -ba ${package}.spec




