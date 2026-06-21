def test_permission_tuple_contract():
    permission = ("financeiro", "visualizar")
    assert permission[0] == "financeiro"
    assert permission[1] == "visualizar"
