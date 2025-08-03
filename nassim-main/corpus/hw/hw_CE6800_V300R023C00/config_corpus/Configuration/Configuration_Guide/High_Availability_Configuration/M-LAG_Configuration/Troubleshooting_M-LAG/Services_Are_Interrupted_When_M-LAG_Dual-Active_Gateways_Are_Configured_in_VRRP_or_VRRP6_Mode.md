Services Are Interrupted When M-LAG Dual-Active Gateways Are Configured in VRRP or VRRP6 Mode
=============================================================================================

Services Are Interrupted When M-LAG Dual-Active Gateways Are Configured in VRRP or VRRP6 Mode

#### Fault Symptom

When M-LAG dual-active gateways are configured in VRRP or VRRP6 mode, service traffic cannot be forwarded.


#### Common Causes

Currently, the device does not support VRRP/VRRP6 dual-active gateways in an M-LAG scenario.


#### Procedure

Configure M-LAG dual-active gateways using the same IP address and MAC address. The configuration procedure is as follows:

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLANIF or VBDIF interface view.
   * Enter the VLANIF interface view.
     ```
     [interface](cmdqueryname=interface) vlanif vlan-id
     ```
   * Enter the VBDIF interface view.
     ```
     [interface](cmdqueryname=interface) vbdif bd-id
     ```
3. Configure an IP address for the interface.
   * Configure an IPv4 address.
     ```
     [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ]
     ```
   * Configure an IPv6 address.
     1. Enable IPv6 on the interface.
        ```
        [ipv6 enable](cmdqueryname=ipv6+enable)
        ```
     2. Configure a global unicast address for the interface.
        ```
        [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length | ipv6-address/prefix-length } [ eui-64 ]
        ```![](../public_sys-resources/note_3.0-en-us.png) 
   
   VLANIF or VBDIF interfaces corresponding to M-LAG member interfaces of M-LAG master and backup devices must be configured with the same IP address.
   
   For the CE6885-LL (low latency mode): IPv6-related configurations are not supported.
4. Configure a virtual MAC address for the VLANIF or VBDIF interface.
   ```
   [mac-address](cmdqueryname=mac-address) mac-address
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   VLANIF or VBDIF interfaces corresponding to M-LAG member interfaces of M-LAG master and backup devices must be configured with the same virtual MAC address.
   
   A virtual MAC address is in the format of 0000-5E00-01XX or 0000-5E00-02XX.
5. Commit the configuration.
   ```
   commit
   ```