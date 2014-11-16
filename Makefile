all: pull devel test

devel: dev_buildout

production: prod_buildout

dev_buildout: bin/buildout

prod_buildout: bin/buildout
	[ -d develop-eggs ] && rm -rf develop-eggs || true
	bin/buildout -N -c production.cfg

pull:
	@echo "=================== $@ ======================="
	@git checkout master
	@git pull origin master
	@[ -x bin/develop ] && bin/develop up || true
	@[ -x bin/release ] && bin/release git -- fetch --tags || true

clean:
	rm -f bin/* .installed.cfg 

bin/buildout: bin/python2.6
	@wget http://downloads.buildout.org/1/bootstrap.py
	@bin/python2.6 bootstrap.py
	@bin/buildout
	@bin/python setup.py develop
	@rm bootstrap.*

bin/python2.6:
	@virtualenv --clear -p python2.6 --no-site-packages .

dev-reload:
	bin/pserve --reload development.ini
