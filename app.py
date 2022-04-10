from fastapi import FastAPI
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
import uvicorn

# TODO not used file
class Settings:
    def __init__(self):
        self.api_version = "v1"
        self.api_name = "TEST_API"
        self.DEBUG = True


settings = Settings()
app = FastAPI(debug=settings.DEBUG, title=settings.api_name, version=settings.api_version)
router = InferringRouter()


@cbv(router)
class RunModel:
    @router.get('/customers')
    def get_customers(self):
        pass

    @router.post('/customers')
    def create_customers(self):
        pass

    @router.get('/customer/{customer_id}')
    def get_customer(self, customer_id: int):
        pass

    @router.put('/customer/{customer_id}')
    def modify_customer(self, customer_id: int):
        pass

    @router.delete('/customer/{customer_id}')
    def delete_customer(self, customer_id: int):
        pass


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
