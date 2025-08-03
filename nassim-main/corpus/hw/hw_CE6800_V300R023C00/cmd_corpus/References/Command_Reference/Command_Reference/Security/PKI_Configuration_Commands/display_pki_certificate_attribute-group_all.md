display pki certificate attribute-group all
===========================================

display pki certificate attribute-group all

Function
--------



The **display pki certificate attribute-group all** command displays the information of all attribute groups.




Format
------

**display pki certificate attribute-group all**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To display the information of all attribute groups, run the **display pki certificate attribute-group all** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the information of all attribute groups.
```
<HUAWEI> display pki certificate attribute-group all
pki certificate attribute-group mygroup                                         
                                                                                
pki certificate attribute-group m                                               
                                                                                
pki certificate attribute-group group1                                          
                                                                                
pki certificate attribute-group aaa_a                                           
                                                                                
pki certificate attribute-group aaa_                                            
                                                                                
pki certificate attribute-group aaa-a                                           
                                                                                
pki certificate attribute-group aaa-,                                           
                                                                                
pki certificate attribute-group aaa-"                                           
                                                                                
pki certificate attribute-group aaa                                             
                                                                                
 Total Number: 9

```

**Table 1** Description of the **display pki certificate attribute-group all** command output
| Item | Description |
| --- | --- |
| Total Number | Total number of certificate attribute groups. |