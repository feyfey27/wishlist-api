from rest_framework.permissions import BasePermission

class IsCreator(BasePermission):
    message = "You must be human."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.item == request.user):
            return True
        else:
            return False