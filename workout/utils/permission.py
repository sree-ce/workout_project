from rest_framework.permissions import BasePermission


class IsAuthenticatedTrainer(BasePermission):

    def has_permission(self, request, view):

        try:
            return request.user.is_trainer
        except:
            return False


class IsAuthenticatedCustomer(BasePermission):

    def has_permission(self, request, view):

        try:
            return request.user.is_customer
        except:
            return False