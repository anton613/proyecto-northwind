-- Desactivar claves foráneas
SET FOREIGN_KEY_CHECKS = 0;

-- Truncar en orden correcto (tablas hijas primero, luego padres)
TRUNCATE TABLE `northwind`.`purchase_order_details`;
TRUNCATE TABLE `northwind`.`order_details`;
TRUNCATE TABLE `northwind`.`invoices`;
TRUNCATE TABLE `northwind`.`inventory_transactions`;
TRUNCATE TABLE `northwind`.`purchase_orders`;
TRUNCATE TABLE `northwind`.`orders`;
TRUNCATE TABLE `northwind`.`employee_privileges`;
TRUNCATE TABLE `northwind`.`products`;
TRUNCATE TABLE `northwind`.`suppliers`;
TRUNCATE TABLE `northwind`.`shippers`;
TRUNCATE TABLE `northwind`.`customers`;
TRUNCATE TABLE `northwind`.`employees`;
TRUNCATE TABLE `northwind`.`privileges`;
TRUNCATE TABLE `northwind`.`inventory_transaction_types`;
TRUNCATE TABLE `northwind`.`orders_tax_status`;
TRUNCATE TABLE `northwind`.`orders_status`;
TRUNCATE TABLE `northwind`.`purchase_order_status`;
TRUNCATE TABLE `northwind`.`order_details_status`;
TRUNCATE TABLE `northwind`.`sales_reports`;
TRUNCATE TABLE `northwind`.`strings`;

-- Reactivar claves foráneas
SET FOREIGN_KEY_CHECKS = 1;