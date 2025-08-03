peer extended-open-message(BGP View)(group)
===========================================

peer extended-open-message(BGP View)(group)

Function
--------



The **peer extended-open-message** command enables the capability of extending optional parameters in BGP Open messages.

The **undo peer extended-open-message** command restores the default configuration.



By default, Open messages longer than 255 bytes cannot be packed.


Format
------

**peer** *peerGroupName* **extended-open-message**

**undo peer** *peerGroupName* **extended-open-message**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

With the increase of BGP capabilities, when a BGP session negotiates multiple capabilities, the length of an Open message may exceed 255 bytes. You can run the **peer extended-open-message** command to configure the extended format of an Open message so that the Open message longer than 255 bytes can be packed.

**Precautions**

When the BGP session of the local device negotiates multiple capabilities, the length of the optional parameter in the Open packet exceeds 255. When the local device sends an extended Open packet to the peer device, if the peer device does not support the extended Open packet function, the local device cannot establish a neighbor relationship with the peer device, and the established neighbor relationship may be disconnected. Exercise caution when setting this parameter.


Example
-------

# Enable the extended format of Open messages.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group a internal
[*HUAWEI-bgp] peer a extended-open-message

```