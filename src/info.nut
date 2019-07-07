/*
 * This file is part of MinimalGS, which is a GameScript for OpenTTD
 * Copyright (C) 2012-2013  Leif Linse
 *
 * MinimalGS is free software; you can redistribute it and/or modify it 
 * under the terms of the GNU General Public License as published by
 * the Free Software Foundation; version 2 of the License
 *
 * MinimalGS is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with MinimalGS; If not, see <http://www.gnu.org/licenses/> or
 * write to the Free Software Foundation, Inc., 51 Franklin Street, 
 * Fifth Floor, Boston, MA 02110-1301 USA.
 *
 */

require("version.nut");

class FMainClass extends GSInfo {
	function GetAuthor()		{ return "Kyle Smith"; }
	function GetName()			{ return SELF_NAME; }
	function GetDescription() 	{ return "Provides alternative ways to boost town and city growth."; }
	function GetVersion()		{ return SELF_VERSION; }
	function GetDate()			{ return SELF_DATE; }
	function CreateInstance()	{ return "TBMain"; }
	function GetShortName()		{ return "ITTB"; } // Replace this with your own unique 4 letter string
	function GetAPIVersion()	{ return "1.2"; }
	function GetURL()			{ return "https://github.com/internet-trains/town-booster"; }

	function GetSettings() {
	}
}

RegisterGS(FMainClass());
