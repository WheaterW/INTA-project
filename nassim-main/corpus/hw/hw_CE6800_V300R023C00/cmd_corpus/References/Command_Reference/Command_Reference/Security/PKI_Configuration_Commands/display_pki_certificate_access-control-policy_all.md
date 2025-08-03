display pki certificate access-control-policy all
=================================================

display pki certificate access-control-policy all

Function
--------



The **display pki certificate access-control-policy all** command displays the information of the access control policy of certificate attributes.




Format
------

**display pki certificate access-control-policy all**


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

To display the information of the access control policy of certificate attributes, run the **display pki certificate access-control-policy all** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the information of the access control policy of certificate attributes.
```
<HUAWEI> display pki certificate access-control-policy all
pki certificate access-control-policy po                                        
 rule 1 permit m                                                                                                                                                
pki certificate access-control-policy policy1                                                                                                                   
 Total Number: 2

```

**Table 1** Description of the **display pki certificate access-control-policy all** command output
| Item | Description |
| --- | --- |
| Total Number | The total number of access-control-policy. |