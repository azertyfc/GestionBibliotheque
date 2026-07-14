from fastapi import status

class ApiException(Exception):

    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code

        super().__init__(message)


class NotFoundException(ApiException):

    def __init__(self, message: str):

        super().__init__(
            message,
            status.HTTP_404_NOT_FOUND
        )


class ConflictException(ApiException):

    def __init__(self, message: str):

        super().__init__(
            message,
            status.HTTP_409_CONFLICT
        )


class BadRequestException(ApiException):

    def __init__(self, message: str):

        super().__init__(
            message,
            status.HTTP_400_BAD_REQUEST
        )


class LivreIndisponible(NotFoundException):
    pass

class LimiteEmpruntDepasse(NotFoundException):
    pass


class EmpruntEnCours(NotFoundException):
    pass


class UnauthorizedException(NotFoundException):
    pass


class RapportIntrouvable(NotFoundException):
    pass

class EmailDejaUtilise(ConflictException):
    pass

class SoldeInsuffisant(BadRequestException):
    pass

class ForbiddenException(BadRequestException):
    pass

class MontantInvalide(BadRequestException):
    pass