display stp vlan instance
=========================

display stp vlan instance

Function
--------



The **display stp vlan instance** command displays the mapping between VLANs and instances.




Format
------

**display stp vlan instance**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After a network designer deploys VBST configurations, you can run this command to check the mapping between VLANs and instances.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the mapping between VLANs and instances on the device running VBST.
```
<HUAWEI> display stp vlan instance
--------------------------------------------------------------------------------                                                    
Instance Mode    VLANs Mapped                                                                                                       
--------------------------------------------------------------------------------                                                    
       0 default 2 to 4, 6 to 99, 101 to 110, 112 to 154, 156 to 4094                                                               
       1 dynamic 1                                                                                                                  
       2 dynamic 100                                                                                                                
       3 dynamic 111                                                                                                                
       4 dynamic 155                                                                                                                
       5 dynamic 5                                                                                                                  
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display stp vlan instance** command output
| Item | Description |
| --- | --- |
| Instance | Instance.   * 0: instance that does not take effect. |
| Mode | Mapping mode between VLANs and instances:   * Static: The mapping between VLANs and instances is statically configured. * Dynamic: The mapping between VLANs and instances is dynamically assigned. * Default: Others. |
| VLANs Mapped | VLANs mapped. |