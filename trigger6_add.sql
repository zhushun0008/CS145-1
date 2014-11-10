--All new bids must be placed at the time which matches the current time of your AuctionBase system.
--Check whether time is same as current time. This trigger is added as 'trigger6_add.sql'.

PRAGMA foreign_keys= ON;
drop trigger if exists trigger6;
create trigger trigger6
before insert on bids
for each row
when exists (select * from CurrentTime where time<>new.time)
begin
     SELECT raise(rollback, "Bid time must match current system time");
end;