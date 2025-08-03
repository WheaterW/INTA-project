display bridge-domain
=====================

display bridge-domain

Function
--------



The **display bridge-domain** command displays bridge domain (BD) configurations.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bridge-domain** [ **binding-info** | *bdid* [ **verbose** | **brief** | **binding-info** ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **binding-info** | Displays the binding information between BDs and VNIs, VSIs, and EVPN instances. | - |
| *bdid* | Displays information about a BD with a specified ID. | The value is an integer ranging from 1 to 16777215. |
| **verbose** | Displays detailed BD information. | - |
| **brief** | Displays brief BD information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After BDs are configured on a device, to view BD information, run the **display bridge-domain** command. The command output contains bridge domain configurations. The command output helps verify the configuration and analyze faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the binding information between BDs and VNIs, VSIs, and EVPN instances.
```
<HUAWEI> display bridge-domain binding-info
--------------------------------------------------------------------------------  
BDID     VNI      VSI              EVPN
--------------------------------------------------------------------------------
1        1                         vpntest1        
2        2                         vpntest2
3        3                         vpntest3

```

# Display the brief configurations of BD 10.
```
<HUAWEI> display bridge-domain 10 brief
--------------------------------------------------------------------------------
*down: Administratively down;           U:Up;            D:Down;
--------------------------------------------------------------------------------

BDID       State Ports
--------------------------------------------------------------------------------
10         up    Eth-Trunk1.10(U)              Eth-Trunk2.1(U)

```

# Display the binding relationships between all BDs and EVPN instances.
```
<HUAWEI> display bridge-domain binding-info
--------------------------------------------------------------------------------  
BDID     VNI      VSI              EVPN
--------------------------------------------------------------------------------
1                                  vpntest1        
2                                  vpntest2
3                                  vpntest3

```

# Display the configurations of all BDs configured on a device.
```
<HUAWEI> display bridge-domain
The total number of bridge-domains is : 2
--------------------------------------------------------------------------------
MAC_LRN: MAC learning;         STAT: Statistics;         SPLIT: Split-horizon;
BC: Broadcast;                 MC: Unknown multicast;    UC: Unknown unicast;
*down: Administratively down;  FWD: Forward;             DSD: Discard;
--------------------------------------------------------------------------------

BDID  State MAC-LRN STAT    BC  MC  UC  SPLIT   Description
--------------------------------------------------------------------------------
10    up    enable  enable  FWD FWD DSD disable VLAN
20    up    enable  disable FWD FWD FWD disable VLAN

```

# Display the configurations of BD 10 configured on a device.
```
<HUAWEI> display bridge-domain 10
--------------------------------------------------------------------------------
MAC_LRN: MAC learning;         STAT: Statistics;         SPLIT: Split-horizon;
BC: Broadcast;                 MC: Unknown multicast;    UC: Unknown unicast;
*down: Administratively down;  FWD: Forward;             DSD: Discard;
U: Up;         D: Down;
--------------------------------------------------------------------------------

BDID         Ports                                                          
--------------------------------------------------------------------------------
10                                                                               

BDID  State MAC-LRN STAT    BC  MC  UC  SPLIT   Description
--------------------------------------------------------------------------------
10    down  enable  disable FWD FWD FWD disable                                 

BDID         VLANIDs                                                          
--------------------------------------------------------------------------------
10           1(D)

```

# Display detailed configurations of BD 10.
```
<HUAWEI> display bridge-domain 10 verbose
Bridge-domain ID        : 10
  Description             : vni 5010
  State                   : Up
  MAC Learning            : Enable
  Statistics              : Disable
  Broadcast               : Forward
  Unknown-unicast         : Forward
  Unknown-multicast       : Forward
  Split-horizon           : Disable
  Vxlan Vni               : 5010
  VSI                     : 
  EVPN                    :
  ----------------
Interface                                State
  100GE1/0/1.1                           up

```

**Table 1** Description of the **display bridge-domain** command output
| Item | Description |
| --- | --- |
| BDID | ID of each BD.  A BD can be configured using the bridge-domain bd-id command in the system view. |
| VNI | VNI bound to a BD.  A VNI can be bound to a BD using the vxlan vni vni-id command in the BD view. |
| VSI | VSI bound to a BD. |
| EVPN | EVPN instance bound to a BD. |
| State | BD status:   * up: An EVC Layer 2 sub-interface is added to a BD, and the EVC Layer 2 sub-interface status is Up. * down: its meaning is as follows:   + No EVC Layer 2 sub-interface is added to a BD.   + An EVC Layer 2 sub-interface is added to a BD, and the EVC Layer 2 sub-interface status is Down.   A BD goes Up when at least one member interface in the BD is Up. |
| Ports | The status of an EVC Layer 2 sub-interface in a BD can be:   * UP: The data link layer protocol of the EVC Layer 2 sub-interface starts properly. * Down: The data link layer protocol of the EVC Layer 2 sub-interface starts is abnormal. |
| The total number of bridge-domains is | Total number of BDs configured on a device. |
| MAC Learning | Whether the MAC address learning function is enabled in a BD:   * disable. * enable. |
| MAC-LRN | Whether the MAC address learning function is enabled in a BD:   * disable. * enable. |
| STAT | Whether a device is enabled to collect statistics about packets transmitted in a BD:   * disable. * enable. |
| BC | Whether a device forwards broadcast packets in a BD:   * FWD: The device forwards broadcast packets in a BD. * DSD: The device discards broadcast packets in a BD. |
| MC | Whether a device forwards multicast packets in a BD:   * FWD: The device forwards multicast packets in a BD. * DSD: The device discards multicast packets in a BD. |
| UC | Whether a device forwards unknown unicast packets in a BD:   * FWD: The device forwards unknown unicast packets in a BD. * DSD: The device discards unknown unicast packets in a BD. |
| SPLIT | Whether split horizon is enabled in a BD:   * disable. * enable. |
| Description | Description of a BD.  To configure a bridge domain description, run the description command in the BD view. |
| VLANIDs | ID of the VLAN bound to a BD. |
| Bridge-domain ID | ID of each BD.  A BD can be configured using the bridge-domain bd-id command in the system view. |
| Statistics | Whether a device is enabled to collect statistics about packets transmitted in a BD:   * disable. * enable. |
| Broadcast | Whether a device forwards broadcast packets in a BD:   * FWD: The device forwards broadcast packets in a BD. * DSD: The device discards broadcast packets in a BD. |
| Unknown-unicast | Whether a device forwards unknown unicast packets in a BD:   * FWD: The device forwards unknown unicast packets in a BD. * DSD: The device discards unknown unicast packets in a BD. |
| Unknown-multicast | Whether a device forwards multicast packets in a BD:   * FWD: The device forwards multicast packets in a BD. * DSD: The device discards multicast packets in a BD. |
| Split-horizon | Whether split horizon is enabled in a BD:   * disable. * enable. |
| Vxlan Vni | VNI bound to a BD. |
| Interface | Interface bound to the BD. |