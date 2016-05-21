#!/usr/bin/python
#
# author: Bret Rusnak
# email: bret.rusnak@gmail.com
# 
# run by crontab 
# removes files in directory that are older than 7 days
# Copyright GNU GPL V3 2016
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Last updated: 5/21/2016



# Set Days and directory to purge here.
days = 6
myDirectory = '/path/to/files/to/purge/'




####   DO NOT CHANGE PARAMETERS BELOW THIS LINE   ####

import os, time
def purgeFiles(dir, age):
 	for xfile in os.listdir(dir):
 		today = time.time()
 		fileloc = os.path.join(dir, xfile)
 		modified = os.stat(filepath).st_mtime
#  		
        if modified < today - age: 
 			if os.path.isfile(fileloc):
 				os.remove(fileloc)
 				
# folder location for files to be deleted.  be sure to 
# include the trailing forward slash.  ( i.e. /home/user/location/ )


#Call the function purgeFiles and pass the directory and days to delete
purgeFiles(myDirectory, (days * 86400))
