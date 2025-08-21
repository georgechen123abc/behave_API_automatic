class AssertHandler:
    @staticmethod
    def equal(actual, expected, msg=None):
        """Assert that actual value equals expected value"""
        assert actual == expected, msg or f"❌ Assertion failed: Expected {expected}, got {actual}"

    @staticmethod
    def not_equal(actual, expected, msg=None):
        """Assert that actual value does not equal expected value"""
        assert actual != expected, msg or f"❌ Assertion failed: Did not expect {expected}, but got {actual}"

    @staticmethod
    def contains(item, container, msg=None):
        """Assert that container contains the item"""
        assert item in container, msg or f"❌ Assertion failed: {item} not found in {container}"

    @staticmethod
    def not_contains(item, container, msg=None):
        """Assert that container does not contain the item"""
        assert item not in container, msg or f"❌ Assertion failed: {item} found in {container}"

    @staticmethod
    def is_true(expr, msg=None):
        """Assert that expression is True"""
        assert expr, msg or "❌ Assertion failed: Expression is not True"

    @staticmethod
    def is_false(expr, msg=None):
        """Assert that expression is False"""
        assert not expr, msg or "❌ Assertion failed: Expression is not False"

    @staticmethod
    def is_none(obj, msg=None):
        """Assert that object is None"""
        assert obj is None, msg or f"❌ Assertion failed: Object {obj} is not None"

    @staticmethod
    def is_not_none(obj, msg=None):
        """Assert that object is not None"""
        assert obj is not None, msg or "❌ Assertion failed: Object is None"

