bfd bind vxlan peer-ip
======================

bfd bind vxlan peer-ip

Function
--------



The **bfd bind vxlan peer-ip** command creates BFD for VXLAN session binding information and displays the BFD session view.



By default, no BFD for VXLAN sessions are created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bfd** *session-name* **bind** **vxlan** **peer-ip** *peer-ip-address* **source-ip** *source-ip-address* **peer-mac** *peer-mac-address* **auto**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *session-name* | Specifies·the·name·of·a·BFD·session. | The·value·is·a·string·of·1·to·64·case-sensitive·characters·without·spaces.·When·double·quotation·marks·are·used·around·the·string,·spaces·are·allowed·in·the·string. |
| **peer-ip** *peer-ip-address* | Specifies the destination VTEP IP address of a VXLAN tunnel to be monitored by a BFD session. | The value is in dotted decimal notation. |
| **source-ip** *source-ip-address* | Specifies the source VTEP IP address of a VXLAN tunnel to be monitored by a BFD session. | The value is a unicast address in dotted decimal notation. |
| **peer-mac** *peer-mac-address* | Specifies the destination VTEP MAC address of a VXLAN tunnel to be monitored by a BFD session. | The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H is 4 digits. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0.A MAC address cannot be all 0s, all 1s, or a multicast MAC address. |
| **auto** | Enables the auto-negotiation function for static discriminators. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To use BFD to monitor VXLAN tunnel connectivity for VXLAN tunnel protection switching, create a BFD for VXLAN session on a VXLAN gateway.peer-ip-address and source-ip-address respectively represent the destination and source VTEP IP addresses of a VXLAN tunnel to be monitored by a BFD session and are written into the inner IP headers of BFD packets.A destination VTEP bridge MAC address or multicast MAC address must be specified for peer-mac-address. The value of this parameter is written into the inner destination MAC address field of BFD packets, so that the peer VTEP can receive and process the BFD packets.

**Prerequisites**

BFD has been enabled globally using the **bfd** command run in the system view.

**Follow-up Procedure**

After a static BFD session with automatically negotiated discriminators is created, optionally perform the following operations in the BFD view:

* Run the **min-tx-interval** command to set a desired minimum interval at which BFD packets are sent.
* Run the **min-rx-interval** command to set a desired minimum interval at which BFD packets are received.
* Run the **detect-multiplier** command to set a local detection multiplier for the BFD session.
* Run the **wtr** command to set the WTR time for the BFD session.

**Precautions**



When configuring a BFD for VXLAN session, you do not need to configure the local and remote discriminators.Only one BFD for VXLAN session can be established between a pair of VTEPs, and the VNI for the VXLAN must be 0.If M-LAG devices have the same VTEP address, BFD cannot be used to detect VXLAN tunnel connectivity.This function applies only to IPv4 VXLAN tunnels.




Example
-------

# Create a BFD for VXLAN session named atob to monitor the VXLAN tunnel with the source VTEP IP address 2.2.2.2, destination VTEP IP address 4.4.4.4, and destination VTEP MAC address 00e0-fc12-3456.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd atob bind vxlan peer-ip 4.4.4.4 source-ip 2.2.2.2 peer-mac 00e0-fc12-3456 auto

```