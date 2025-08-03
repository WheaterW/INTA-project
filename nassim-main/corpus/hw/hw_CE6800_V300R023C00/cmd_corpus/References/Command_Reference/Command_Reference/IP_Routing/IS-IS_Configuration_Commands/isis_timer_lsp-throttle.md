isis timer lsp-throttle
=======================

isis timer lsp-throttle

Function
--------



The **isis timer lsp-throttle** command sets the minimum interval at which LSPs are sent on an IS-IS interface and the maximum number of LSPs to be sent each time.

The **undo isis timer lsp-throttle** command restores the default setting.



By default, the minimum interval at which LSPs are sent on an interface is 50 milliseconds, and the maximum number of LSPs to be sent each time is 10.


Format
------

**isis timer lsp-throttle** *throttle-interval* [ **count** *count* ]

**undo isis timer lsp-throttle**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *throttle-interval* | Specifies the minimum interval at which LSPs are sent. | The value ranges from 1 to 10000, in milliseconds. |
| **count** *count* | Specifies the maximum number of LSPs to be sent each time. | The value ranges from 1 to 1000. |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can specify throttle-interval in the isis timer lsp-throttle command to set the delay between two successive LSPs and the interval at which fragments of a CSNP are sent.


Example
-------

# Set the interval at which LSPs are sent on 100GE1/0/1 to 500 milliseconds.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis timer lsp-throttle 500

```