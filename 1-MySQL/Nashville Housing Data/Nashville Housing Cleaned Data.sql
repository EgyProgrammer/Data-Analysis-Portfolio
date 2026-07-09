use new_schema;

# change table name to a convinent one, easier and faster in typeing
alter table `nashville housing data for data cleaning`
rename  to `nh`;
------------------------------------------------------------------------
# change comlumn name
alter table `nashville housing data for data cleaning`
rename column `ï»¿UniqueID` to `ID`
;
------------------------------------------------------------------------
# to see the whole data everytime if needed
select *
from nh;
------------------------------------------------------------------------
# exploring the empty addresses
select nh1.parcelid,nh1.propertyaddress,nh2.propertyaddress
from nh as nh1
join nh as nh2
on nh1.parcelid=nh2.parcelid
where nh2.propertyaddress='' and nh1.propertyaddress!=''
;
------------------------------------------------------------------------
# update the empty addresses based on parcelid
update nh as nh1
join nh as nh2
on nh1.parcelid=nh2.parcelid
set nh1.propertyaddress=nh2.propertyaddress
where nh1.propertyaddress='' and nh2.propertyaddress!=''
;
------------------------------------------------------------------------
# seperating property address and city
select propertyaddress, 
trim(substring_index(propertyaddress,',',1)) as address, 
trim(substring_index(propertyaddress,',',-1)) as city 
from nh;

# adding new column for address, then updating its values
alter table nh
add column propertysplitaddress char(150);
update nh
set propertysplitaddress=trim(substring_index(propertyaddress,',',1));

# adding new column for city, then updating its values
alter table nh
add column propertysplitcity char(150);
update nh
set propertysplitcity=trim(substring_index(propertyaddress,',',-1));
------------------------------------------------------------------------
# seperating owner address and city
select owneraddress, 
trim(substring_index(owneraddress,',',1)) as address, 
trim(substring_index(substring_index(owneraddress,',',-2),',',1)) as city,
trim(substring_index(owneraddress,',',-1)) as state
from nh;

# adding new column for address, then updating its values
alter table nh
add column ownersplitaddress char(150);
update nh
set ownersplitaddress=trim(substring_index(owneraddress,',',1));

# adding new column for city, then updating its values
alter table nh
add column ownersplitcity char(150);
update nh
set ownersplitcity=trim(substring_index(substring_index(owneraddress,',',-2),',',1));

# adding new column for state, then updating its values
alter table nh
add column ownersplitstate char(150);
update nh
set ownersplitstate=trim(substring_index(owneraddress,',',-1));
------------------------------------------------------------------------
# updating SoldAsVacant to yes and no only
update nh
set SoldAsVacant='Yes'
where SoldAsVacant='Y';

update nh
set SoldAsVacant='No'
where SoldAsVacant='N';
-------------------------------------------------------------------------
# getting the duplicate values
with temp_table as
(select *,
row_number() over (partition by ParcelID,LandUse,PropertyAddress,SaleDate,SalePrice,LegalReference order by id) as ranking
from nh)
select * from temp_table
where ranking>1
;

# deleting the duplicates
delete from nh
where id in (with temp_table as
(select *,
row_number() over (partition by ParcelID,LandUse,PropertyAddress,SaleDate,SalePrice,LegalReference order by id) as ranking
from nh)
select id from temp_table
where ranking>1);

# delete from CTE directly
with temp_table as
(select *,
row_number() over (partition by ParcelID,LandUse,PropertyAddress,SaleDate,SalePrice,LegalReference order by id) as ranking
from nh)
delete 
from temp_table
where ranking>1
;
-------------------------------------------------------------------------
# delete unused columns
alter table nh
drop column propertyaddress,
drop column owneraddress,
drop column taxdistrict,
drop column saledate;