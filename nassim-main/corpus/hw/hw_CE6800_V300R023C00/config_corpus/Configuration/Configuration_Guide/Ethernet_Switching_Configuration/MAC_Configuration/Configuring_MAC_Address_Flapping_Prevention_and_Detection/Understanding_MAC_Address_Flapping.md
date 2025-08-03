Understanding MAC Address Flapping
==================================

Understanding MAC Address Flapping

#### What Is MAC Address Flapping

MAC address flapping occurs when a MAC address is learned by two or three interfaces in the same VLAN, and a more recently learned MAC address entry overrides the earlier version. Normally, the first interface that learns a MAC address is the correct outbound interface, and is referred to as the original interface. An interface that learns the same MAC address later is called the move interface, and this is usually an interface on a loop (or where its downlink network has a loop). [Figure 1](#EN-US_CONCEPT_0000001176664477__macmove) shows how MAC address flapping occurs. In the MAC address entry with MAC address 00e0-fc12-3456 and VLAN ID 2, the outbound interface is changed from interface 1 to interface 2. MAC address flapping can lead to increased CPU usage on devices.

MAC address flapping frequently occurs on networks where a network loop exists. If this issue frequently occurs on your network, it may be due to a network loop or the result of unauthorized users attacking the network. In such cases, check the alarms and MAC address flapping records to quickly locate and eliminate the loops.

**Figure 1** MAC address flapping  
![](figure/en-us_image_0000001176744413.png)

#### How to Prevent MAC Address Flapping

During network planning, you can use the following methods to prevent MAC address flapping:

* Increase the MAC address learning priority of an interface. If the same MAC addresses are learned by interfaces of different priorities, those learned by the interface with the highest priority overrides any learned by other interfaces.
* Prevent MAC address entries from being overridden on interfaces with the same priority. If an interface connected to an unauthorized network device has the same priority as that connected to an authorized device, any MAC address learned by the former will not override the original correct MAC address. However, if the authorized device is powered off, the MAC address of the unauthorized device will be learned, and that of the authorized device cannot be learned once it is powered on again.

In [Figure 2](#EN-US_CONCEPT_0000001176664477__fig_dc_cfg_mac_macmove2), port 1 of DeviceA is connected to a server. To prevent unauthorized users from connecting to DeviceA using the server's MAC address, set a high MAC address learning priority for port 1.

**Figure 2** Networking of MAC address flapping prevention  
![](figure/en-us_image_0000001130784742.png)

#### How to Detect MAC Address Flapping

MAC address flapping detection checks whether outbound interfaces in MAC address entries flap.

After MAC address flapping detection is enabled, a device can report an alarm when MAC address flapping occurs. The alarm contains the flapping MAC address, VLAN ID, and outbound interfaces between which the MAC address flaps. A loop may exist between the outbound interfaces. You can locate the cause by referring to the alarm's information. Alternatively, you can configure what action the device will take following MAC address flapping detection, and this can include quit-vlan (remove the interface from the VLAN) or error-down (shut down the interface), which ensures the device automatically removes the loop.

**Figure 3** Networking of MAC address flapping detection  
![](figure/en-us_image_0000001130784740.png)

In [Figure 3](#EN-US_CONCEPT_0000001176664477__fig_dc_s_feature_macmove3), a network loop occurs between DeviceB, DeviceC, and DeviceD because DeviceC and DeviceD are mistakenly connected using a network cable. When interface 1 of DeviceA receives a broadcast packet, DeviceA forwards the packet to DeviceB. The packet is then sent to interface 2 of DeviceA. After DeviceA is configured with MAC address flapping detection, it can detect that the source MAC address of the packet flaps from interface 1 to interface 2. If MAC address flapping continuously occurs, DeviceA reports a MAC address flapping alarm to inform users of maintenance.


#### Processing Mechanism After MAC Address Flapping Occurs

If MAC address flapping occurs on an interface, the device automatically suppresses broadcast and unknown unicast packets. As a result, the forwarding rate of the outbound interface where MAC address flapping occurs equals 1% of the inbound interface bandwidth. In such cases, you can run the **storm suppression mac-address flapping** command to configure the committed information rate (CIR) for traffic suppression triggered by MAC address flapping on the interface and configure the interface to forward packets based on the specified CIR.

You can also configure the interface where MAC address flapping occurs to transit to the error-down state. If this function is configured, the interface enters the error-down state and reports an alarm when MAC address flapping is detected.