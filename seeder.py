import pandas as pd

# Cargar el archivo CSV generado por Mockaroo
businesses = pd.read_csv('businesses.csv')
carts = pd.read_csv('carts.csv')
cart_items = pd.read_csv('cart_items.csv')
customers = pd.read_csv('customers.csv')
employees = pd.read_csv('employees.csv')
employee_types = pd.read_csv('employee_types.csv')
genders = pd.read_csv('genders.csv')
items = pd.read_csv('items.csv')
item_types = pd.read_csv('item_types.csv')
orders = pd.read_csv('orders.csv')
order_items = pd.read_csv('order_items.csv')
users = pd.read_csv('users.csv')

b = open('businesses.txt', 'w')
for index, row in businesses.iterrows():
    b.write(f"DB::table('businesses')->insert([" + f"'name' => '{row['name']}', 'balance' => '{row['balance']}', 'email' => '{row['email']}', 'phone' => '{row['phone']}', 'address' => '{row['address']}' " + "]);\n")
b.close()

b = open('carts.txt', 'w')
for index, row in carts.iterrows():
    b.write(f"DB::table('carts')->insert([" + f"'total' => '{row['total']}', 'Customer_id' => '{row['Customer_id']}', 'Employee_id' => '{row['Employee_id']}' " + "]);\n")
b.close()

b = open('cart_items.txt', 'w')
for index, row in cart_items.iterrows():
    b.write(f"DB::table('cart_items')->insert([" + f"'quantity' => '{row['quantity']}', 'Cart_id' => '{row['Cart_id']}', 'Item_id' => '{row['Item_id']}' " + "]);\n")
b.close()

b = open('customers.txt', 'w')
for index, row in customers.iterrows():
    b.write(f"DB::table('customers')->insert([" + f"'balance' => '{row['balance']}', 'guardian_name' => '{row['guardian_name']}', 'guardian_phone' => '{row['guardian_phone']}', 'User_id' => '{row['User_id']}' " + "]);\n")
b.close()

b = open('employees.txt', 'w')
for index, row in employees.iterrows():
    b.write(f"DB::table('employees')->insert([" + f"'salary' => '{row['salary']}', 'User_id' => '{row['User_id']}', 'Business_id' => '{row['Business_id']}', 'Employee_type_id' => '{row['Employee_type_id']}' " + "]);\n")
b.close()

b = open('employee_types.txt', 'w')
for index, row in employee_types.iterrows():
    b.write(f"DB::table('employee_types')->insert([" + f"'name' => '{row['name']}' " + "]);\n")
b.close()

b = open('genders.txt', 'w')
for index, row in genders.iterrows():
    b.write(f"DB::table('genders')->insert([" + f"'name' => '{row['name']}' " + "]);\n")
b.close()

b = open('items.txt', 'w')
for index, row in items.iterrows():
    b.write(f"DB::table('items')->insert([" + f"'name' => '{row['name']}', 'price' => '{row['price']}', 'description' => '{row['description']}', 'image' => '{row['image']}', 'stock' => '{row['stock']}', 'Item_type_id' => '{row['Item_type_id']}', 'Business_id' => '{row['Business_id']}' " + "]);\n")
b.close()
    
b = open('item_types.txt', 'w')
for index, row in item_types.iterrows():
    b.write(f"DB::table('item_types')->insert([" + f"'name' => '{row['name']}' " + "]);\n")
b.close()

b = open('orders.txt', 'w')    
for index, row in orders.iterrows():
    b.write(f"DB::table('orders')->insert([" + f"'total' => '{row['total']}', 'Customer_id' => '{row['Customer_id']}', 'Employee_id' => '{row['Employee_id']}' " + "]);\n")
b.close()

b = open('order_items.txt', 'w')
for index, row in order_items.iterrows():
    b.write(f"DB::table('order_items')->insert([" + f"'quantity' => '{row['quantity']}', 'Order_id' => '{row['Order_id']}', 'Item_id' => '{row['Item_id']}' " + "]);\n")
b.close()

b = open('users.txt', 'w')
for index, row in users.iterrows():
    b.write(f"DB::table('users')->insert([" + f"'name' => '{row['name']}', 'parent_name' => '{row['parent_name']}', 'age' => '{row['age']}', 'phone' => '{row['phone']}', 'email' => '{row['email']}', 'password' => '{row['password']}', 'Gender_id' => '{row['Gender_id']}' " + "]);\n")
b.close()