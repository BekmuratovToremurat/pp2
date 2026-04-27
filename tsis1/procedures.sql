-- ADD PHONE
CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE v_id INT;
BEGIN
    SELECT id INTO v_id FROM contacts WHERE name = p_contact_name;

    IF v_id IS NULL THEN
        RAISE NOTICE 'Contact not found';
        RETURN;
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES (v_id, p_phone, p_type);
END;
$$;


-- MOVE TO GROUP (auto-create group)
CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INT;
    v_group_id INT;
BEGIN
    SELECT id INTO v_contact_id FROM contacts WHERE name = p_contact_name;

    IF v_contact_id IS NULL THEN
        RAISE NOTICE 'Contact not found';
        RETURN;
    END IF;

    SELECT id INTO v_group_id FROM groups WHERE name = p_group_name;

    IF v_group_id IS NULL THEN
        INSERT INTO groups(name)
        VALUES (p_group_name)
        RETURNING id INTO v_group_id;
    END IF;

    UPDATE contacts SET group_id = v_group_id
    WHERE id = v_contact_id;
END;
$$;


-- SEARCH (name + email + phones)
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE (
    id INT,
    name VARCHAR,
    email VARCHAR,
    phone VARCHAR,
    group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.email, p.phone, g.name
    FROM contacts c
    LEFT JOIN phones p ON p.contact_id = c.id
    LEFT JOIN groups g ON g.id = c.group_id
    WHERE c.name ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%';
END;
$$;