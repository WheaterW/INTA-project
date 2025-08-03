dhcp client request option-list exclude
=======================================

dhcp client request option-list exclude

Function
--------



The **dhcp client request option-list exclude** command configures a list of default request options that are not carried in the Option55 field of DHCP Request messages.

The **undo dhcp client request option-list exclude** command deletes the list of default request options that are not carried in the Option55 field of DHCP Request messages.



By default, the device does not configure the option to be excluded from the DHCP client request list.


Format
------

**dhcp client request option-list exclude** *option-code* &<1-8>

**undo dhcp client request option-list exclude** *option-code* &<1-8>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *option-code* | Specifies a list of default request options that are excluded from the Option55 field. | The value is of enumerated type and can be:   * 3 * 6 * 15 * 28 * 33 * 44 * 121 * 184 |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The Option55 field in DHCP Request messages is used to set the request option list. DHCP clients use this option to specify network configuration parameters that need to be obtained from the DHCP server. You can run the **dhcp client request option-list exclude** command to configure a list of default options that are excluded from the Option55 field based on network requirements.


Example
-------

# Configure the default request option 3 to be excluded from the Option55 field in DHCP Request messages on interface 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcp client request option-list exclude 3

```