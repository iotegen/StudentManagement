# courses/tests.py
from django.core.cache import cache
from django.test import TestCase
from courses.utils import get_course_model  # Use utility for dynamically fetching the Course model

Course = get_course_model()

class CourseCacheTest(TestCase):
    def setUp(self):
        # Create a course object in the database
        self.course = Course.objects.create(name="Math 101", description="Basic Mathematics")

        # Store the course ID in the cache
        cache.set("course_1", self.course.id)

    def test_cache_fetch(self):
        # Retrieve the course ID from the cache
        course_id = cache.get("course_1")

        # Assert that the course ID was retrieved from the cache
        self.assertIsNotNone(course_id, "Cache did not contain the expected key.")

        # Fetch the actual course object from the database using the cached ID
        cached_course = Course.objects.get(id=course_id)

        # Assert that the cached course is the same as the one in the database
        self.assertEqual(cached_course.name, "Math 101")
