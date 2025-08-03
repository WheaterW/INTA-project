Link and Interface Types
========================

Link and Interface Types

#### Link Types

VLAN links can be divided into the following types, as described in [Figure 1](#EN-US_CONCEPT_0000001130782654__fig894838162111):

* Access link: connects to a terminal that cannot or does not need to identify VLAN tags. In [Figure 1](#EN-US_CONCEPT_0000001130782654__fig894838162111), all links between user hosts and devices are access links, and frames transmitted over access links do not carry VLAN tags.
* Trunk link: connects to a network device. Frames transmitted over trunk links carry VLAN tags.

**Figure 1** Link types  
![](figure/en-us_image_0000001176742363.png "Click to enlarge")
#### Interface Types

Only specific interfaces on devices can identify VLAN-tagged frames defined in 802.1Q. Based on their ability to identify frames, interfaces are classified into the following types:

* Access interface: connects to user terminals that cannot or do not need to identify VLAN tags and can connect to access links only. Such interfaces have the following characteristics:
  + Tags frames that do not carry a VLAN tag with its default port VLAN ID (also known as PVID).
  + Accepts VLAN-tagged frames only when they are tagged with a VLAN ID that matches its PVID.
  + Sends all frames as untagged.
* Trunk interface: connects to devices that can identify VLAN tags and can connect to trunk links only. Such interfaces have the following characteristics:
  + Allows frames from multiple VLANs (tagged frames) to pass through.
  + Sends frames as untagged in the default VLAN (VLAN ID = PVID) and sends frames in other VLANs as tagged.
* Hybrid interface: connects to terminals or network devices and can connect to both access and trunk links. Such interfaces have the following characteristics:
  + Accepts tagged and VLAN-tagged frames simultaneously.
  + Accepts VLAN-tagged frames for several VLANs simultaneously. Depending on your configuration, frames sent out from a hybrid interface may be tagged or untagged.
* QinQ interface: uses the QinQ protocol and adds an additional VLAN tag to a VLAN-tagged frame in order to extend the VLAN space, offering sufficient VLANs required by the network. Such an interface is also called an 802.1Q-in-802.1Q interface.