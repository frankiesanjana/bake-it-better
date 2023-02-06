from django.shortcuts import render

"""
These views enable customised error pages to be provided
for easier navigation back to the main site
"""


def page_not_found_view(request, exception):
    """
    404 Page Not Found
    """
    return render(request, '404.html', status=404)


def server_error_view(request):
    """
    500 Internal Server Error
    """
    return render(request, '500.html', status=500)


def permission_denied_view(request, exception):
    """
    403 Forbidden
    """
    return render(request, '403.html', status=403)


def bad_request_view(request, exception):
    """
    400 Bad Request
    """
    return render(request, '400.html', status=400)