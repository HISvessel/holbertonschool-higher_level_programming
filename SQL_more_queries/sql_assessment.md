SQL assessment test

Q1 Basic DDL
1) create a categories table.
> CREATE TABLE categories VALUES(
    id INT AUTO_INCREMENT PRIMARY_KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

2) add a column called category_id inside of the products table,
and have it placed after the name column. 
> ALTER TABLE PRODUCTS ADD COLUMN category_id INT AFTER NAME;

3) Explain why foreign keys should always reference a primary key or unique column.
> Foreign keys serve as the direct linking betwen tables, they should reference a primary key or unique data for normalization and atomicity.

Q2 Basic DML
1) Log in the rows 'Electronics' 'Office Supplies' 'Toys' in the name column of the category table.
>INSERT INTO categories(name) VALUES (
('Electronics'),
('Office Supplies'),
('Toys')
); 
-------------------------------------------------------------------
** corrections: after VALUES, you do not need to wrap the values in an extra set of parenthesis. 
-------------------------------------------------------------------

2) Change the name of the 'Toys' row to 'Children's Toys'.
>UPDATE categories SET name = "Children'S Toys" WHERE name = 'Toys';

3) Delete a category only if it has no products referencing it with foregin keys.
>DELETE FROM products IF NOT FOREIGN_KEY WHERE name = 'Office Supplies'; 
-----------------------------------------------------------------
**correction: SQl does not have an IF not FOREIGN KEY prompt. THis is invalid.
here is the corrected query:
DELETE FROM categories WHERE name == 'Office Supplies' AND id NOT IN (SELECT DISTINCT category_id FROM products);
-----------------------------------------------------------------

Q3 Triggers
1) Create a trigger that acts when data is inserted on the products table. If the new product's price is above 1000, it should insert a row into premium log(product_id, flagged_at) table.
>DELIMITER $
CREATE TRIGGER insert_into_premium
AFTER INSERT INTO products
FOR EACH ROW
BEGIN
    UPDATE premium_log
    SET premium_stock = premium_stock + NEW.quantity
    WHERE premium_stock_id = NEW.quantity
    IF NEW.stock > 1000; //FLAG//
END$
-----------------------------------------------------------------
** correction: the trigger conditions are correct, but the trigger action needs to insert, not delete. So the query looks more like this:
CREATE TRIGGER insert_into_premium
AFTER INSERT ON products
FOR EACH ROW
BEGIN
    IF NEW.price > 1000 THEN
        INSERT INTO premium_log (product_id, flagged_at)
        VALUES (NEW.id, NOW());
    END IF;
------------------------------------------------------------------

2) True or False: Triggers can reference multiple rows at once from a multiple insert.
> True. For consistency, sql handles each reference separately, allowing for accurate tracking. **correction, it is false, not true.

3) What kind of trigger would you use if you wanted to cancel a deleting action from a registered user that has an existing order?
>I would use a BEFORE, since I would want to block the query beore it is finalized. Inside the trigger, I should write a clause that specifies IF orders = True.
CREATE TRIGGER prevent_user_delete
BEFORE DELETE ON users
FOR EACH ROW
BEGIN
    IF EXISTS (SELECT 1 FROM orders WHERE user_id = OLD.id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot delete user with existing orders.';
    END IF;
END$$

Q4: Normalization
1) List three separate tables where you would want to split the following table to better comply with 3nf formalization:

order_id customer_name customer_email product_name	product_price
1	Kevin Sanchez	kevin@email.com	Laptop	1200.00
2	Kevin Sanchez	kevin@email.com	Mouse	25.00

>List orders table, customers table and products table. //FLAG//

2) Is storing a username inside an orders table consider normalized or denormalized? Eexplain why.
> It is denormalized, and the reason being is that it becomes redundant information, that would still be put in a report when using joins. The norm would be to leave it for the topic of joins when performing reports and analisis.
----------------------------------------------------------
Areas to improve and practice:
1) Multi-row INSERT syntax and escaping strings

2) Writing precise conditional logic inside BEGIN...END blocks for triggers

3) DELETE safeguards with subqueries (e.g., NOT IN, LEFT JOIN IS NULL)

4) Use of SIGNAL SQLSTATE to cancel operations in BEFORE triggers

