display netstream
=================

display netstream

Function
--------



The **display netstream** command displays the NetStream configurations.




Format
------

**display netstream** { **all** | **global** | **interface** { *interface-type* *interface-number* | *interface-name* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays all the NetStream configurations, including:   * NetStream configurations in the system view. * NetStream configurations in the flexible flow statistics view. * NetStream configurations in the interface view. | - |
| **global** | Displays the global NetStream configurations, including:  * NetStream configurations in the system view. * NetStream configurations in the flexible flow statistics view. | - |
| **interface** *interface-type* *interface-number* | Displays the NetStream configurations on a specified interface.  The parameter <interface-type> <interface-number> specifies the interface type and number. | -  - |
| **interface** *interface-name* | Displays the NetStream configurations on a specified interface.  The parameter <interface-name> specifies the name of an interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Displays the NetStream configuration.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all the NetStream configurations.
```
<HUAWEI> display netstream all
system                                                                          
  netstream export ip source 192.168.1.1                                            
  netstream export ip host 192.168.10.1 3000

```

**Table 1** Description of the **display netstream** command output
| Item | Description |
| --- | --- |
| netstream export ip source <ip-address> | The field <ip-address> indicates the source address of the exported packets carrying IPv4 flow statistics. To configure the source address, run netstream export ip source. |
| netstream export ip host <ip-address> <port-number> | The field <ip-address> indicates the destination address of the exported packets carrying IPv4 flow statistics, and <port-number> is the UDP port. To configure the destination address and UDP port, run netstream export ip host. |