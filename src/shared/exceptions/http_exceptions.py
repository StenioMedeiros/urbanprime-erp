from fastapi import HTTPException, status


def not_found(detail: str = "Registro nao encontrado") -> HTTPException:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
