"""
TODO
"""

from django.test.client import Client
from django.test import TestCase
from django.test.utils import override_settings
from django.conf import settings
from django.core.urlresolvers import reverse

from xmodule.modulestore.tests.factories import CourseFactory
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from courseware.tests.tests import TEST_DATA_MONGO_MODULESTORE
from student.tests.factories import UserFactory, CourseEnrollmentFactory
from student.models import CourseEnrollment
from course_modes.models import CourseMode
from verify_student.models import SoftwareSecurePhotoVerification


@override_settings(MODULESTORE=TEST_DATA_MONGO_MODULESTORE)
class TestProfEdVerification(TestCase):
    """
    TODO
    """

    def setUp(self):
        self.user = UserFactory.create(username="rusty", password="test")
        self.client.login(username="rusty", password="test")
        self.course_key = SlashSeparatedCourseKey('Robot', '999', 'Test_Course')
        CourseFactory.create(org='Robot', number='999', display_name='Test Course')
        prof_ed_mode = CourseMode(
            course_id=self.course_key,
            mode_slug="professional",
            mode_display_name="Professional Certificate",
            min_price=50,
            suggested_prices=""
        )
        prof_ed_mode.save()

    def test_new_user_flow(self):
        # self.client.get(url, query_dict)
        # reverse: course-specific-register
        # reverse: verify_student_show_requirements
        # reverse: verify_student_verify
        # reverse: payment (?)
        pass

    def test_already_verified_user_flow(self):
        # Already verified: SoftwareSecurePhotoVerificationModel
        pass

    def test_registered_user_flow(self):
        # Register the user for the course
        # CourseRegistrationFactory
        pass