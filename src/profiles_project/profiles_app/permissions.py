from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to update their own profile """

    def has_object_permission(self, request, view, obj):
        """check whether user is triing to edit his own profile
        and returns True/False"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnProfileFeed(permissions.BasePermission):
    """one thing anonymous user can post the status (we use SAFE_METHODS)
        second only authorized user can update their own status"""

    def has_object_permission(self, request, view, obj):
        """return True if request.method in SAFE_METHODS
            return True if the user is trying update his own"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
