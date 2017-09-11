from unittest.mock import _get_target, _patch, DEFAULT


class MockTypeError(ValueError):
    pass


def _check_type(value, argument_name, expected_types):
    if argument_name in expected_types:
        expected_type = expected_types[argument_name]

        if not isinstance(value, expected_type):
            raise MockTypeError(
                f'Expected {argument_name}'
                f' to have type {expected_type},'
                f' however `{repr(value)}` was passed'
                f' with type {type(value)}.'
            )


# TODO weird use of a closure
def call_mocker(old_mock_call, original_function):

    argument_names = original_function.__code__.co_varnames
    expected_types = original_function.__annotations__

    def mock_call(*args, **kwargs):

        for arg, argument_name in zip(args, argument_names):
            _check_type(arg, argument_name, expected_types)

        for kwarg_name, value in kwargs.items():
            _check_type(value, kwarg_name, expected_types)

        return old_mock_call(*args, **kwargs)

    return mock_call


class _typed_patch(_patch):

    def __init__(self, getter, attribute, new, *args, **kwargs):
        super().__init__(getter, attribute, new, *args, **kwargs)

        original_function = getattr(getter(), attribute)

        new._mock_call = call_mocker(new._mock_call, original_function)


def patch(
    target, new=DEFAULT, spec=None, create=False,
    spec_set=None, autospec=None, new_callable=None, **kwargs
):
    getter, attribute = _get_target(target)

    return _typed_patch(
        getter, attribute, new, spec, create,
        spec_set, autospec, new_callable, kwargs
    )
