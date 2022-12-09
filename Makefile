DAY =
YEAR =
PYTEST_ARGS =
SOLUTION_PATH:=solutions/$(YEAR)/$(DAY)
GOLANG_PATH:=$(SOLUTION_PATH)/golang
PYTHON_PATH:=$(SOLUTION_PATH)/python

.PHONY: check-env
check-env:
ifndef DAY
	$(error DAY is undefined)
endif
ifneq "$(strip $(shell echo $(DAY)|wc -c))" "3"
	$(error DAY must be a two digit string)
endif
ifndef YEAR
	$(error YEAR is undefined)
endif
ifneq "$(strip $(shell echo $(YEAR)|wc -c))" "5"
	$(error YEAR must be a four digit string)
endif

.PHONY: pytest
pytest: check-env | $(PYTHON_PATH)
	cd $(PYTHON_PATH) && python -mpytest $(PYTEST_ARGS)

.PHONY: pyanswer
pyanswer: check-env pytest | $(PYTHON_PATH)
	cd $(PYTHON_PATH) && python solution.py

$(PYTHON_PATH): | $(SOLUTION_PATH)
	cp -a template/python $(SOLUTION_PATH)/

$(GOLANG_PATH): | $(SOLUTION_PATH)
	cp -a template/golang $(SOLUTION_PATH)/

$(SOLUTION_PATH): | check-env
	git checkout -b feature/$(YEAR)/$(DAY)
	mkdir -p $(SOLUTION_PATH)
	touch $(SOLUTION_PATH)/problem.md

