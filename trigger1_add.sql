--Updates the currently attribute on the 'items' table to the newly inserted 'bid_amount' after each insert on 'bids'

PRAGMA foreign_keys= ON;
drop trigger if exists trigger1;
create trigger trigger1
after insert on bids
for each row
begin
     update items set currently = new.bid_amount where new.item_id=item_id;
end;