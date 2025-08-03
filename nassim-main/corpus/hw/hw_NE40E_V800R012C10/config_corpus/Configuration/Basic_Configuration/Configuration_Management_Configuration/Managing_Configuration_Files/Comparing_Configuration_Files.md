Comparing Configuration Files
=============================

You can compare the current configuration file with the configuration file for the next startup or a specified configuration file.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The compared configuration file name extension must be .cfg or .zip.



#### Procedure

1. Run [**compare configuration**](cmdqueryname=compare+configuration) [ *configuration-file* ]
   
   
   
   The current configuration is compared with the configuration file for the next startup or a specified configuration file.
   
   
   
   After a series of operations are performed, you can run the [**compare configuration**](cmdqueryname=compare+configuration) command to compare whether the current configurations are identical with the next startup or a specified configuration file from the first line. The command output helps decide whether to save and set the current configurations as the next startup configuration file.
   
   The command output respectively displays nine lines of the current configurations and the next startup or a specified configuration file from the line that contains differences. If the lines from the differences to the end of the configuration file are less than nine, the command displays the content till the end of the configuration file.