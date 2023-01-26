from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    assert encrypt_message('SAPO', 2) == 'OP_AS'
    assert encrypt_message('SAPO', 3) == 'PAS_O'
    assert encrypt_message('SAPO', 8) == 'OPAS'

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('SAPO', '1')

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(2, 3)
