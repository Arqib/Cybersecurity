#!/usr/bin/awk -f
{ 
	gsub("," ,"\n"); 
	gsub("*.", "");
	#print 
}
{
	#gsub("a", "45");
	print
}
