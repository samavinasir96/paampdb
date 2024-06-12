from django.test import TestCase
from django.utils import timezone

from abampdb.models import PDBQuery


class QuestionModelTests(TestCase):
    def test_instantiate_object(self):
        query = PDBQuery(query_id="test")
        query.save()
        self.assertTrue(query.id is not None)
