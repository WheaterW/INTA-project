isis timer lsp-retransmit
=========================

isis timer lsp-retransmit

Function
--------



The **isis timer lsp-retransmit** command configures the LSP retransmission interval over a P2P link.

The **undo isis timer lsp-retransmit** command restores the default value.



By default, the LSP retransmission interval over a P2P link is 5 seconds.


Format
------

**isis timer lsp-retransmit** *retransmit-interval*

**undo isis timer lsp-retransmit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *retransmit-interval* | Specifies an LSP retransmission interval. | The value is an integer ranging from 1 to 300 seconds. The default value is 5. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a point-to-point network, devices at both ends of a link synchronize LSDBs with each other by flooding LSPs. The device at one end of the link sends an LSP. If the device at the other end receives this LSP, it replies with a PSNP. If the device that has sent an LSP does not receive a PSNP from the other end in a period of time, the device will retransmit the LSP.The isis timer lsp-retransmit command is used to set an LSP retransmission interval. Only the devices on a point-to-point network send PSNPs. Therefore, the isis timer lsp-retransmit command will take effect only when it is run on point-to-point interfaces.

**Configuration Impact**

After the isis timer lsp-retransmit command is run on a device, the device starts a timer for retransmit-interval after sending an LSP. If the device receives a PSNP from the other end within the timer, the device will not retransmit the LSP. Otherwise, the device will retransmit the LSP.If the value of retransmit-interval is set too small, an LSP will be retransmitted even though it is not necessary, causing high CPU, memory, and network bandwidth usage.

**Precautions**

If a broadcast interface is emulated as a P2P interface using the **isis circuit-type** command or a P2P interface is restored to a broadcast interface using the **undo isis circuit-type** command, the LSP retransmission interval on a P2P link is restored to the default value.


Example
-------

# Set the LSP retransmission interval to 10 seconds on a specified interface.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable
[*HUAWEI-100GE1/0/1] isis circuit-type p2p
[*HUAWEI-100GE1/0/1] isis timer lsp-retransmit 10

```