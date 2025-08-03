display pki whitelist (all views)
=================================

display pki whitelist (all views)

Function
--------



The **display pki whitelist** command displays the content of certificate whitelist files on the device.




Format
------

**display pki whitelist** { **filename** *file-name* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **filename** *file-name* | Specifies the name of a certificate whitelist file. | It must be the name of an existing certificate whitelist file. |
| **all** | Displays the content of all certificate whitelist files. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After certificate whitelist files are imported to the device, you can run this command to check the content.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the content of all certificate whitelist files.
```
<HUAWEI> display pki whitelist all

 Whitelist filename : a40                                                      
 Imported whitelist count : 1                                       
 -------------------------------------------------------------------------------     
 Items   Whitelist value                                                            
 -------------------------------------------------------------------------------    
 1       CN-on-Certificate_of-RBS-3

 Whitelist filename : 0000
 Imported whitelist count : 6
 -------------------------------------------------------------------------------     
 Items   Whitelist value                                                            
 -------------------------------------------------------------------------------    
 1       CN-on-Certificate_of-RBS-1CN-on-Certificate_of-RBS-1CNCN-on-Certificate_of-RBS-
1CN-on-Certificate_of-RBS-1CNaaaaaaaaaaaaaaaaa
 2       CN-on-Certificate_of-RBS-4
 2       CN-on-Certificate_of-RBS-1
 1       CN-on-Certificate_of-RBS-2

```

**Table 1** Description of the **display pki whitelist (all views)** command output
| Item | Description |
| --- | --- |
| Whitelist filename | Name of a certificate whitelist file. To set a name for a certificate whitelist file, run the pki import whitelist command. |
| Whitelist value | Content in the certificate whitelist files. |
| Imported whitelist count | Number of imported certificate whitelist files. |
| Items | Number of certificate whitelist files with the same content. |