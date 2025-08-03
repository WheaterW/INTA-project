dhcp client request option-list
===============================

dhcp client request option-list

Function
--------



The **dhcp client request option-list** command configures a list of request options that the Option55 field in DHCP Request packets carries besides the default options.

The **undo dhcp client request option-list** command deletes a list of request options that the Option55 field in DHCP Request packets carries besides the default options.



By default, the Option 55 field in DHCP Request packets carries only default request options.


Format
------

**dhcp client request option-list** *option-code* &<1-15>

**undo dhcp client request option-list** *option-code* &<1-15>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *option-code* | Specifies a list of request options that the Option55 field carries besides the default options. | The options are as follows:   * 1 * 4 * 7 * 17 * 42 * 43 * 66 * 67 * 120 * 129 * 143 * 145 * 146 * 148 * 150 |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The Option55 field in DHCP Request packets is used to set the request option list. DHCP clients use this option to specify network configuration parameters that need to be obtained from the DHCP server. Besides the default options, you can run the dhcp client request option-list option-code command to set a list of other request options that the Option55 field carries.


Example
-------

# Configure the Option55 field in DHCP Request packets to carry option 4 on interface 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcp client request option-list 4

```