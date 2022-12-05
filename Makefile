DAY:=
YEAR:=
SOLUTION_DIR:=solutions/$(YEAR)/$(DAY)

.PHONY: day
day:
	[ -n "$(DAY)" ] # Make sure DAY is set
	[ -n "$(YEAR)" ] # Make sure YEAR is set
	[ ! -d $(SOLUTION_DIR) ] # Make sure the solution doesn't exist
	mkdir -p $(SOLUTION_DIR)
	cp -a template/python $(SOLUTION_DIR)/python

