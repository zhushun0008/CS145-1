--The current time of your AuctionBase system can only advance forward in time, not backward in time.
--Add a trigger to block updates (before) to CurrentTime table where time updated is less than already existing time in the table. This trigger is added as 'trigger7_add.sql'.


PRAGMA foreign_keys= ON;
drop trigger if exists trigger7;
create trigger trigger7
before update on CurrentTime
for each row
when old.time>new.time
begin
     --select raise(ignore);
     SELECT raise(rollback, "Can't go back in time. Can only update with time greater than current time");
end;