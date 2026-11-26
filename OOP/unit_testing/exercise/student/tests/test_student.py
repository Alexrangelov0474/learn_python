from unittest import TestCase, main

from project.student import Student


class StudentsTest(TestCase):
    def setUp(self):
        self.student1 = Student('test1', {'Python': ['n1', 'n2', 'n3'],
                                          'JS': ['n1', 'n2']})
        self.student2 = Student('test2')

    def test_init_with_courses(self):
        self.assertEqual('test1', self.student1.name)
        self.assertEqual({'Python': ['n1', 'n2', 'n3'],
                                          'JS': ['n1', 'n2']}, self.student1.courses)

        self.assertIsInstance(self.student1.name, str)
        self.assertIsInstance(self.student1.courses, dict)

    def test_init_without_courses(self):
        self.assertEqual('test2', self.student2.name)
        self.assertEqual({}, self.student2.courses)

        self.assertIsInstance(self.student2.name, str)
        self.assertIsInstance(self.student2.courses, dict)

    def test_enroll_in_existing_courses(self):
        result = self.student1.enroll('Python', ['n4', 'n5'])
        self.assertEqual('Course already added. Notes have been updated.', result)

        self.assertEqual({'Python': ['n1', 'n2', 'n3', 'n4', 'n5'],
                          'JS': ['n1', 'n2']}, self.student1.courses)

        result = self.student1.enroll('Python', ['n6', 'n7'], 'N')
        self.assertEqual('Course already added. Notes have been updated.', result)

        self.assertEqual({'Python': ['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7'],
                          'JS': ['n1', 'n2']}, self.student1.courses)

    def test_enroll_not_existing_course_with_y(self):
        result = self.student1.enroll('Java', ['n1', 'n2'], 'Y')
        self.assertEqual('Course and course notes have been added.', result)
        self.assertIn('Java', self.student1.courses)
        self.assertEqual(['n1', 'n2'], self.student1.courses['Java'])

    def test_enroll_not_existing_course_with_empty_string(self):
        result = self.student1.enroll('Java', ['n1', 'n2'], '')
        self.assertEqual('Course and course notes have been added.', result)
        self.assertIn('Java', self.student1.courses)
        self.assertEqual(['n1', 'n2'], self.student1.courses['Java'])

    def test_enroll_not_existing_course_with_not_adding_notes(self):
        result = self.student1.enroll('Java', ['n1', 'n2'], 'N')
        self.assertEqual('Course has been added.', result)
        self.assertIn('Java', self.student1.courses)
        self.assertEqual([], self.student1.courses['Java'])

    def test_add_notes_to_existing_course(self):
        result = self.student1.add_notes('JS', 'n3')
        self.assertEqual('Notes have been updated', result)
        self.assertEqual(['n1', 'n2', 'n3'], self.student1.courses['JS'])

    def test_add_notes_to_not_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student2.add_notes('JS', 'n1')
        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student1.leave_course('Python')
        self.assertEqual('Course has been removed', result)
        self.assertNotIn('Python', self.student1.courses)

    def test_leave_not_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student1.leave_course('Java')
        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))

if __name__ == '__main__':
    main()