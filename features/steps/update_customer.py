from behave import when


@when('The customer with id "{customer_id}" updates their name to "{name}"')
def update_customer(context, customer_id, name):
    (first_name, surname) = name.split(' ', 2)
    response = context.web_client.put(
        f'/customers/{customer_id}',
        json={'firstName': first_name, 'surname': surname}
    )
    assert response.status_code == 200, f'{response.status_code} != 200 :: {response.get_json()}'
