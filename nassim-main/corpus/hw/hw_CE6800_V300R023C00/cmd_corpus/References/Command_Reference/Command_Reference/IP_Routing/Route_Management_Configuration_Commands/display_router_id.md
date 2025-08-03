display router id
=================

display router id

Function
--------

The **display router id** command displays the configured router ID.



Format
------

**display router id** [ **vpn-instance** *vpn-instance-name* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

You can run the **display router id** command to view the router ID of the public network configured on the device, and run the **display router id vpn-instance** command to view the router ID of the VPN instance configured on the device.

**Prerequisites**

The VPN instance has been configured.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display the configured router ID of the VPN instance named vpna.
```
<HUAWEI> display router id vpn-instance vpna
RouterID:10.1.1.1

```

# Display the configured router ID.
```
<HUAWEI> display router id
RouterID:1.1.1.1

```


**Table 1** Description of the
**display router id** command output

| Item | Description |
| --- | --- |
| RouterID | Router ID. |