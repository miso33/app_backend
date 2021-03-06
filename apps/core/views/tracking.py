from rest_framework_tracking.mixins import LoggingMixin


class TrackingView(LoggingMixin):
    sensitive_fields = {"my_secret_key", "my_secret_recipe"}
    logging_methods = ["POST", "PUT", "PATCH", "DELETE"]
