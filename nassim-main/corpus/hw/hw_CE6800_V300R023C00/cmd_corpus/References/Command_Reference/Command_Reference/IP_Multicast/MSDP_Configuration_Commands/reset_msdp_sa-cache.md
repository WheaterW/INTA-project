reset msdp sa-cache
===================

reset msdp sa-cache

Function
--------



The **reset msdp sa-cache** command clears (S, G) information in the source active (SA) cache.




Format
------

**reset msdp vpn-instance** *vpn-instance-name* **sa-cache** [ *group-address* ]

**reset msdp sa-cache** [ *group-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-address* | Specifies the group address in (S, G) information. | The value ranges from 224.0.0.0 to 239.255.255.255, in dotted decimal notation. If this parameter is not specified, all (S, G) information in the SA cache is cleared. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name "\_public\_" cannot be used. The string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To clear (S, G) information in the SA cache, run the **reset msdp sa-cache** command.

**Configuration Impact**

After the (S, G) information in the SA cache is cleared, the previous (S, G) information cannot be restored. Exercise caution when performing this operation.

**Precautions**

If vpn-instance is not specified, only (S, G) information in the SA cache of the public network instance is cleared.


Example
-------

# Clear (S, G) information about group 225.5.4.3 from the SA cache of the public network instance.
```
<HUAWEI> reset msdp sa-cache 225.5.4.3

```