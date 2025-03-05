-- Prints the description of the table first_table
SELECT 
    table_name AS TABLE_NAME, 
    column_name AS COLUMN_NAME, 
    column_type AS COLUMN_TYPE, 
    is_nullable AS IS_NULLABLE, 
    column_default AS COLUMN_DEFAULT
FROM 
    information_schema.columns
WHERE 
    table_name = 'first_table'
    AND table_schema = 'hbtn_0c_0';
