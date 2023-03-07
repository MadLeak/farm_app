"""Importing packages"""
from prisma.models import User

# Partial type for create a user
User.create_partial(
    'CreateUser',
    include={
        'firstName',
        'lastName',
        'email',
        'password',
        'role',
    }
)

# Partial type for read a user
User.create_partial(
    'ReadUser',
    include={'id'}
)

# Partial type for update a user
User.create_partial(
    'UpdateUser',
    required={'id'},
    exclude={'createdAt', 'updatedAt'},
    optional={
        'firstName',
        'lastName',
        'email',
        'password',
        'role',
        'dateOfBirth',
        'profileImage',
        'addressOne',
        'addressTwo',
        'zipCode',
        'phoneNumer',
    }
)

# Partial type for delete a user
User.create_partial(
    'DeleteUser',
    include={'id'}
)
