from contacts.forms import NameForm


def test_name_form_success():
    # Given
    data = {"your_name": "jonh"}
    form = NameForm(data=data)

    # When
    result = form.is_valid()

    # Then
    assert result is True


def test_name_form_you_name_max_length():
    # Given
    data = {"your_name": "fabio" * 50}
    form = NameForm(data=data)

    # When
    result = form.is_valid()

    # Then
    assert result is False
    assert form.errors == {
        "your_name":
        ["Certifique-se de que o valor tenha no máximo 100 caracteres (ele possui 250)."]
        }


def test_name_form_fail():
    # Given
    data = {}
    form = NameForm(data=data)

    # When
    result = form.is_valid()

    # Then
    assert result is False
