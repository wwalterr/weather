from fastapi import FastAPI, status

from fastapi.responses import RedirectResponse

application = FastAPI(
    title='Zapata',
    description='Weather API',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redoc'
)

@application.get('/', status_code=status.HTTP_308_PERMANENT_REDIRECT, include_in_schema=False)
async def index():
    return RedirectResponse('/docs')