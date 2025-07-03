from .models import Feedback

class FeedbackService:
    def create_feedback(self, data):
        """
        create a feedback object from form data
        :param data:
        :return:
        """
        employee = data.get("employee")
        comment = data.get("comment")
        subject = data.get("subject")

        return Feedback.objects.create(
            employee = employee,
            comment = comment ,
            subject = subject
        )