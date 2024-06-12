from flask import jsonify
from service import app
from service.common import status

############################################################
# Error Handlers
############################################################
@app.errorhandler(status.HTTP_404_NOT_FOUND)
def not_found(error):
    """Handles 404 Not Found errors"""
    app.logger.warning("404 Error: %s", error)
    return (
        jsonify(
            status=status.HTTP_404_NOT_FOUND,
            error="Not Found",
            message=str(error),
        ),
        status.HTTP_404_NOT_FOUND,
    )

@app.errorhandler(status.HTTP_400_BAD_REQUEST)
def bad_request(error):
    """Handles 400 Bad Request errors"""
    app.logger.warning("400 Error: %s", error)
    return (
        jsonify(
            status=status.HTTP_400_BAD_REQUEST,
            error="Bad Request",
            message=str(error),
        ),
        status.HTTP_400_BAD_REQUEST,
    )

@app.errorhandler(status.HTTP_500_INTERNAL_SERVER_ERROR)
def internal_server_error(error):
    """Handles 500 Internal Server errors"""
    app.logger.error("500 Error: %s", error)
    return (
        jsonify(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error="Internal Server Error",
            message=str(error),
        ),
        status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
