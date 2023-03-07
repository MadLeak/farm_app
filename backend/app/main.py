"""Importing Packages"""
from fastapi import FastAPI
from prisma import Prisma

from prisma.models import User
from prisma.partials import CreateUser, UpdateUser, DeleteUser
from prisma.types import UserUpdateInput, UserCreateInput

app = FastAPI()
data_base = Prisma()


@app.get('/users')
async def list_users() -> list[User] | None:
    """List all users"""
    await data_base.connect()  # Wating for database to connect
    listed_users = await data_base.user.find_many(
        order=[
            {'firstName': 'asc'},
            {'lastName': 'asc'}
        ]
    )
    await data_base.disconnect()  # Wating for database to disconnect
    return listed_users


@app.post('/users')
async def create_user(user: CreateUser) -> User | None:
    """Create a new user"""
    user_input = {key: value for (key, value) in user if value is not None}
    await data_base.connect()  # Wating for database to connect
    new_user = await data_base.user.create(
        data=UserCreateInput(**user_input)
    )
    await data_base.disconnect()  # Wating for database to disconnect
    return new_user


@app.get('/users/{user_id}')
async def get_user(user_id: int) -> User | None:
    """Read a user"""
    await data_base.connect()  # Wating for database to connect
    user = await data_base.user.find_unique(
        where={
            'id': user_id,
        }
    )
    await data_base.disconnect()  # Wating for database to disconnect
    return user


@app.put('/users')
async def update_user(user: UpdateUser) -> User | None:
    """Update a user"""
    user_input = {key: value for (key, value) in user if value is not None}
    await data_base.connect()  # Wating for database to connect
    updated_user = await data_base.user.update(
        where={
            'id': user.id,
        },
        data=UserUpdateInput(**user_input)
    )
    await data_base.disconnect()  # Wating for database to disconnect
    return updated_user


@app.delete('/users')
async def delete_user(user: DeleteUser) -> User | None:
    """Delete a user"""
    data_base = Prisma()
    await data_base.connect()  # Wating for database to connect
    deleted_user = await data_base.user.delete(
        where={
            'id': user.id,
        }
    )
    await data_base.disconnect()  # Wating for database to disconnect
    return deleted_user
