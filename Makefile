# Default target executed when no arguments are given to make.
default_target: all

#The .PHONY line declares all and clean as phony targets. A phony target is one that does not represent a file; it purely represents a command to be executed.
.PHONY: all clean run dev debug deploy submit

all:
	./build.sh

clean:
	./build.sh clean

run:
	./build.sh web

dev:
	[ -z $$CODESPACES ] && ./build.sh local_dev; [ -n $$CODESPACES ] && (./build.sh; ./build.sh web)

debug:
	./build.sh; ./build.sh debug

deploy:
	./build.sh deploy

submit:
	juniorit submit