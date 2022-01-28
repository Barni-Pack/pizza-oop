import sqlite3
import pathlib


conn = sqlite3.connect('app/pizza_storage.db')


def create_pizza_storage_table():
    sql = '''
            CREATE TABLE PIZZA_STORAGE
                (name TEXT NOT NULL PRIMARY KEY,
                amount INTEGER NOT NULL)
            
            '''
    with conn:
        conn.execute(sql)


def init_pizza():
    '''Inits '''
    sql = 'INSERT INTO PIZZA_STORAGE (name, amount) values(?, ?)'
    data = [
        ('Pepperoni', 100),
        ('Barbecue', 80),
        ('Seafood', 60),
    ]

    with conn:
        conn.executemany(sql, data)


def add_pizza(pizza_name: str) -> None:
    update_value = 1
    update_pizza(
        pizza_name=pizza_name,
        update_value=update_value
    )


def take_pizza(pizza_name: str) -> None:
    update_value = -1
    update_pizza(
        pizza_name=pizza_name,
        update_value=update_value
    )


def update_pizza(pizza_name: str, update_value: int) -> None:
    pizza_amount = get_pizza_amount(pizza_name=pizza_name)
    new_pizza_amount = pizza_amount + update_value
    sql = f'''
    UPDATE PIZZA_STORAGE
    SET amount = {new_pizza_amount}
    WHERE name == "{pizza_name}"
    '''
    conn.execute(sql)


def get_pizza_amount(pizza_name: str) -> int:
    '''Returns amount of pizza left in the storage'''
    sql = f'SELECT * FROM PIZZA_STORAGE WHERE name == "{pizza_name}"'
    data = conn.execute(sql)
    amount = data.fetchone()[1]
    return amount


if __name__ == "__main__":
    # Create database with table if it doesn't exist
    db_file = list(pathlib.Path('.').glob('*.db'))
    if not db_file:
        create_pizza_storage_table()
        init_pizza()
        
    pizza_name = 'Pepperoni'    
    print(get_pizza_amount(pizza_name=pizza_name))
    
    take_pizza(pizza_name=pizza_name)
    print(get_pizza_amount(pizza_name=pizza_name))
    
    add_pizza(pizza_name=pizza_name)
    print(get_pizza_amount(pizza_name=pizza_name))
