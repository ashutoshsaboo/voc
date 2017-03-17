from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class NamedTupleTests(TranspileTestCase):
    def test_creation(self):
        self.assertCodeExecution("""
            Point = namedtuple('sad','asd')
            Point1 = namedtuple(Point, ['x', 'y'])
            Point = namedtuple()
            Point = namedtuple('Point')

            """)


