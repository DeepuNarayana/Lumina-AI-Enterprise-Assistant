from ai.indexing.index_service import IndexService

def test_index_document():

    service = IndexService()

    service.index_document("tests/data/employee_handbook.txt")

    assert True