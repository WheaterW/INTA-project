force insert option
===================

force insert option

Function
--------

The **force insert option** command configures a DHCP server to forcibly insert an Option field specified in the global address pool or DHCP Option template to a DHCP Response packet that it sends to a DHCP client.

The **undo force insert option** command deletes the Option field forcibly inserted to a DHCP Response packet that a DHCP server sends to a DHCP client.

By default, a DHCP server does not forcibly insert an Option field to a DHCP Response packet that it sends to a DHCP client.



Format
------

**force insert option** *value* &<1-254>

**undo force insert option** *value* &<1-254>



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the code for a forcibly replied option. You can configure a DHCP server to forcibly reply one or more options. | The value is an integer that ranges from 1 to 254. |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

When a DHCP client applies for an IP address from a DHCP server, parameters contained in the DHCP Request packet specify the options the client requires. The DHCP server inserts the required options to a DHCP Response packet.

When a device functions as a DHCP server on the live network, the DHCP request packets sent by DHCP clients may not carry expected options. However, the DHCP clients still expect the DHCP server to reply with options configured in the global address pool. Run the force insert option code & <1-254> command to configure the DHCP server to forcibly insert an Option field to a DHCP Response packet.

**Prerequisites**

1. The global address pool has been created using the ip pool command.
2. The Option field has been configured in the global address pool by running the **option** command in the global address pool view.


Example
-------

# Configure a DHCP server to forcibly insert Option 4 to a DHCP Response packet in the address pool pool1.
```
<HUAWEI> system-view
[~HUAWEI] ip pool pool1
[*HUAWEI-ip-pool-pool1] option 4 hex 11
[*HUAWEI-ip-pool-pool1] force insert option 4

```