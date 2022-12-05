DAY:=
YEAR:=
SOLUTION_DIR:=solutions/$(YEAR)/$(DAY)
GOLANG_DIR:=$(SOLUTION_DIR)/golang
PYTHON_DIR:=$(SOLUTION_DIR)/python

.PHONY: variables
variables:
	[ -n "$(DAY)" ] # Make sure DAY is set
	[ -n "$(YEAR)" ] # Make sure YEAR is set

$(SOLUTION_DIR): variables
	mkdir -p $@

.PHONY: day
day: variables $(SOLUTION_DIR)
	echo "Day created"

.PHONY: python
python: variables $(SOLUTION_DIR)
	[ ! -d $(PYTHON_DIR) ]
	cp -a template/python $(SOLUTION_DIR)/

.PHONY: golang
golang: variables $(SOLUTION_DIR)
	[ ! -d $(GOLANG_DIR) ]
	cp -a template/golang $(SOLUTION_DIR)/

.PHONY: pytest
pytest: variables python
	@cd $(PYTHON_DIR) && python -mpytest

.PHONY: pyanswer
pyanswer: variables pytest
	@cd $(PYTHON_DIR) && python solution.py
