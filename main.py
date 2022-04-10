from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from models import Customer, Agent, Order
from database import engine
from sqlmodel import Session, select
from typing import List
app = FastAPI(debug=True, title="TEST_JOMAA_API", version="V1.0")


# ******************* customer
@app.get('/customers', response_model=List[Customer])
def get_customers():
    with Session(engine) as session:
        customers = session.exec(select(Customer)).all()
    return customers


@app.post('/customer', response_model=Customer, status_code=status.HTTP_201_CREATED)
def create_customer(customer: Customer):
    new_cust = Customer(id=customer.id, name=customer.name, country=customer.country,
                        phone=customer.phone, agent_code=customer.agent_code)
    with Session(engine) as session:
        check_agt = session.exec(select(Agent).where(Agent.id == customer.agent_code)).one_or_none()
        if check_agt is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id agent not found in table")
        session.add(new_cust)
        session.commit()
        session.refresh(new_cust)
    return new_cust


@app.put('/customer/{customer_id}', response_model=Customer)
def modify_customer(customer_id: int, customer: Customer):
    with Session(engine) as session:
        result = session.exec(select(Customer).where(Customer.id == customer_id)).first()
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        result.name = customer.name
        result.country = customer.country
        result.phone = customer.phone
        session.commit()
        session.refresh(result)
    return result


@app.delete('/customer/{customer_id}', status_code=status.HTTP_200_OK)
def delete_customer(customer_id: int):
    with Session(engine) as session:
        result = session.exec(select(Customer).where(Customer.id == customer_id)).one_or_none()
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found")
        session.delete(result)
        session.commit()
    return "Delete success"


#  ******************* order
@app.get('/orders', response_model=List[Order])
def get_orders():
    with Session(engine) as session:
        orders = session.exec(select(Order)).all()
    return orders


@app.post('/order', response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(order: Order):
    new_cust = Order(num=order.num, date=order.date, description=order.description,
                     cust_code=order.cust_code, agent_code=order.agent_code)
    with Session(engine) as session:
        check_cust = session.exec(select(Customer).where(Customer.id == order.cust_code)).one_or_none()
        if check_cust is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id customer not found in table")
        check_agt = session.exec(select(Agent).where(Agent.id == order.agent_code)).one_or_none()
        if check_agt is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id agent not found in table")
        session.add(new_cust)
        session.commit()
        session.refresh(new_cust)
    return new_cust


@app.put('/order/{order_num}', response_model=Order)
def modify_order(order_num: int, order: Order):
    with Session(engine) as session:
        result = session.exec(select(Order).where(Order.num == order_num)).first()
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        result.date = order.date
        result.description = order.description
        session.commit()
        session.refresh(result)
    return result


@app.delete('/order/{order_num}', status_code=status.HTTP_200_OK)
def delete_order(order_num: int):
    with Session(engine) as session:
        result = session.exec(select(Order).where(Order.num == order_num)).one_or_none()
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found")
        session.delete(result)
        session.commit()
    return "Delete success"


# ******************* agent
@app.post('/agent', response_model=Agent, status_code=status.HTTP_201_CREATED)
async def create_agent(agent: Agent):
    new_agent = Agent(id=agent.id, name=agent.name, working_area=agent.working_area, commission=agent.commission)
    with Session(engine) as session:
        session.add(new_agent)
        session.commit()
        session.refresh(new_agent)
    return new_agent


@app.get('/agents', response_model=List[Agent])
def get_agents():
    with Session(engine) as session:
        customers = session.exec(select(Agent)).all()
    return customers


@app.put('/agent/{agent_id}', response_model=Agent)
def modify_agent(agent_id: int, agent: Agent):
    with Session(engine) as session:
        result = session.exec(select(Agent).where(Agent.id == agent_id)).first()
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        result.name = agent.name
        result.working_area = agent.working_area
        result.commission = agent.commission
        session.commit()
        session.refresh(result)
    return result


@app.delete('/agent/{agent_id}', status_code=status.HTTP_200_OK)
def delete_agent(agent_id: int):
    with Session(engine) as session:
        result = session.exec(select(Agent).where(Agent.id == agent_id)).one_or_none()
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found")
        session.delete(result)
        session.commit()
    return "delete success"
