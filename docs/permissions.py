from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_authenticated
        )


# class IsOwnerPermission(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return bool(
#             request.method in SAFE_METHODS or
#             (
#                     request.user and request.user.is_authenticated and request.user.employees == obj.employees)
#         )
