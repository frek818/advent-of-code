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

$(PYTHON_DIR): variables
	mkdir -p $@

$(GOLAND_DIR): variables
	mkdir -p $@

.PHONY: day
day: variables $(SOLUTION_DIR)
	echo "Day created"

.PHONY: python
python: variables $(SOLUTION_DIR)
	[ ! -d $(SOLUTION_DIR)/python ]
	cp -a template/python/* $(PYTHON_DIR)/

.PHONY: golang
golang: variables $(SOLUTION_DIR)
	[ ! -d $(SOLUTION_DIR)/golang ]
	cp -a template/golang/* $(GOLANG_DIR)/

.PHONY: pytest
pytest: variables $(PYTHON_DIR)
	@cd $(PYTHON_DIR) && python -mpytest

.PHONY: pyanswer
pyanswer: variables $(PYTHON_DIR)
	@cd $(PYTHON_DIR) && python solution.py
