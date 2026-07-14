from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from core.exceptions import ApiException
from core.logger import logger


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(ApiException)
    async def api_exception_handler(
        request: Request,
        exc: ApiException
    ):

        logger.warning(
            "%s %s - %s",
            request.method,
            request.url.path,
            exc.message
        )

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": exc.message
            }
        )