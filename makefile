FILE=fey.py
COMMAND=pyinstaller

all:
	$(COMMAND) $(FILE) --onefile

clean:
	rm -rf build dist fey
