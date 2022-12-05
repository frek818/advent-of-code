DAY:=
YEAR:=
SOLUTION_DIR:=solutions/$(YEAR)/$(DAY)

.PHONY: variables
variables:
	[ -n "$(DAY)" ] # Make sure DAY is set
	[ -n "$(YEAR)" ] # Make sure YEAR is set

$(SOLUTION_DIR):
	mkdir -p $(SOLUTION_DIR)

.PHONY: day
day: variables $(SOLUTION_DIR)
	echo "Day created"

.PHONY: python
python: variables $(SOLUTION_DIR)
	[ ! -d $(SOLUTION_DIR)/python ]
	cp -a template/python $(SOLUTION_DIR)/python

.PHONY: golang
golang: variables $(SOLUTION_DIR)
	[ ! -d $(SOLUTION_DIR)/golang ]
	cp -a template/golang $(SOLUTION_DIR)/golang

