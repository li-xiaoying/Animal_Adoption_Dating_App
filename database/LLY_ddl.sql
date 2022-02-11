--
-- Table structure for table `Customers`
--
USE adoptionproject;
DROP TABLE IF EXISTS `Customers`;
CREATE TABLE `Customers` (
	`customerID` int(11) NOT NULL AUTO_INCREMENT,
	`firstName` varchar(255),
	`lastName` varchar(255),
	`customerPhone` varchar(255),
	`email` varchar(255) NOT NULL,
	`password` varchar(255) NOT NULL,
	PRIMARY KEY (`customerID`),
	CONSTRAINT `email` UNIQUE (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8;

INSERT INTO adoptionproject.Customers (email, password) VALUES ('admin@oregonstate.edu', '1234');

--
-- Table structure for table `Pets`
--
USE adoptionproject;
DROP TABLE IF EXISTS `Pets`;
CREATE TABLE `Pets` (
	`petsID` int(11) NOT NULL AUTO_INCREMENT,
	`type` varchar(255), 
	`name` varchar(255) NOT NULL,
	`img` LONGBLOB NOT NULL,
	`breed` varchar(255),
	`age` int(11),
	`size` varchar(255),
	`gender` varchar(255) NOT NULL,
	`goodWithKids` BOOLEAN,
	`goodWithDogs` BOOLEAN,
	`goodWithCats` BOOLEAN,
	`mustBeLeashed` BOOLEAN,
	`availability` varchar(255) NOT NULL,
	PRIMARY KEY (`petsID`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8;

--
-- Table structure for table `AdminMsg`
--
USE adoptionproject;
DROP TABLE IF EXISTS `AdminMsg`;
CREATE TABLE `AdminMsg` (
	`adminMsgID` int(11) NOT NULL AUTO_INCREMENT,
	`petsID` int(11) NOT NULL,
	`customerEmail` varchar(255) NOT NULL,
	`message` varchar(255),
	`status` varchar(255) NOT NULL,
	CONSTRAINT `AdminMsg_Customers_fk_1` FOREIGN KEY (`customerEmail`) REFERENCES `Customers`(`email`) ON DELETE CASCADE,
	PRIMARY KEY (`adminMsgID`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8;


--
-- Table structure for table `CustomerLikePet`
--
USE adoptionproject;
DROP TABLE IF EXISTS `CustomerLikePet`;
CREATE TABLE `CustomerLikePet` (
	`petsID` int(11) NOT NULL,
	`customerID` int(11) NOT NULL,
	CONSTRAINT `CustomerLikePet_Pets_fk_1` FOREIGN KEY (`petsID`) REFERENCES `Pets`(`petsID`) ON DELETE CASCADE,
	CONSTRAINT `CustomerLikePet_Customers_fk_1` FOREIGN KEY (`customerID`) REFERENCES `Customers`(`customerID`) ON DELETE CASCADE,
	PRIMARY KEY (`petsID`, `customerID` )
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8;



--
-- Add timestamp for Pets
--
USE adoptionproject;
ALTER TABLE Pets
ADD COLUMN `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP