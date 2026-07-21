#1783728000

-- This file is part of Hercules.
-- http://herc.ws - http://github.com/HerculesWS/Hercules
--
-- Copyright (C) 2026 Hercules Dev Team
--
-- Hercules is free software: you can redistribute it and/or modify
-- it under the terms of the GNU General Public License as published by
-- the Free Software Foundation, either version 3 of the License, or
-- (at your option) any later version.
--
-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU General Public License for more details.
--
-- You should have received a copy of the GNU General Public License
-- along with this program.  If not, see <http://www.gnu.org/licenses/>.

ALTER TABLE `char`
	ADD COLUMN `pow` SMALLINT UNSIGNED NOT NULL DEFAULT '0' AFTER `luk`,
	ADD COLUMN `sta` SMALLINT UNSIGNED NOT NULL DEFAULT '0' AFTER `pow`,
	ADD COLUMN `wis` SMALLINT UNSIGNED NOT NULL DEFAULT '0' AFTER `sta`,
	ADD COLUMN `spl` SMALLINT UNSIGNED NOT NULL DEFAULT '0' AFTER `wis`,
	ADD COLUMN `con` SMALLINT UNSIGNED NOT NULL DEFAULT '0' AFTER `spl`,
	ADD COLUMN `crt` SMALLINT UNSIGNED NOT NULL DEFAULT '0' AFTER `con`,
	ADD COLUMN `max_ap` INT UNSIGNED NOT NULL DEFAULT '0' AFTER `sp`,
	ADD COLUMN `ap` INT UNSIGNED NOT NULL DEFAULT '0' AFTER `max_ap`,
	ADD COLUMN `trait_point` INT UNSIGNED NOT NULL DEFAULT '0' AFTER `skill_point`;

INSERT INTO `sql_updates` (`timestamp`) VALUES (1783728000);
