build:
	docker build . -t school_test_assignment

run:
	docker run --name school_test_assignment -t school_test_assignment $(filter-out $@,$(MAKECMDGOALS))
	docker rm school_test_assignment

clean:
	docker rmi school_test_assignment

%:
	@:
