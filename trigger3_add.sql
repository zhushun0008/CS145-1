--Add a trigger to block insertion (before) on bids table where time in bids table is before or after the 'started' and 'ends' in the 'items' table for same item_id.This trigger is added as 'trigger3_add.sql'. 

PRAGMA foreign_keys= ON;
drop trigger if exists trigger3;
create trigger trigger3
before insert on bids
for each row
when exists (select * from items where item_id=new.item_id and (new.time>ends or new.time<started))
begin
     SELECT raise(rollback, "The bid should be made between the start and end times designated for the item. The bid is either before the start or after the end time. Hence, error!");
end;