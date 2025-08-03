Enabling IPSG Based on a Dynamic Binding Table
==============================================

Enabling IPSG Based on a Dynamic Binding Table

#### Context

IPSG based on a dynamic binding table is applicable to LANs that contain many hosts or the hosts obtain IP addresses through DHCP. The interfaces directly or indirectly connected to the DHCP server are configured as trusted interfaces, and other interfaces are untrusted. The device forwards the packets received by the trusted interfaces without checking them against the binding entries. In this case, authorized hosts can obtain IP addresses only from valid DHCP servers. After enabling DHCP snooping on an interface connected to users or in the VLAN, configure the interface connected to the DHCP server as a trusted interface, so that the dynamic DHCP snooping binding table is generated.

After creating a dynamic binding table, you need to enable IPSG on an interface or in a VLAN for IPSG to take effect.

* Enabling IPSG on an interface: IPSG checks all packets received by the interface against binding entries. Use this method if you want to perform an IPSG check on specified interfaces and trust other interfaces. This method is suitable for scenarios in which an interface belongs to multiple VLANs, because it eliminates the need to enable IPSG in each VLAN.
* Enabling IPSG in a VLAN: IPSG checks the packets received by all interfaces in the VLAN against binding entries. Use this method if you want to perform an IPSG check in specified VLANs and trust other VLANs. This method is suitable for scenarios in which multiple interfaces belong to the same VLAN, because it eliminates the need to enable IPSG on each interface.

![](public_sys-resources/note_3.0-en-us.png) 

* If you use both of the preceding methods, only the one that is configured first takes effect.

* If ACL resources are insufficient, IPSG configurations exist on the device but the binding table may fail to be delivered. To check whether IPSG takes effect, run the [**display ip source check user-bind status**](cmdqueryname=display+ip+source+check+user-bind+status) **dynamic** [ { **interface** *interface name* | *interface-type* *interface-number* | **ip-address** *ip-address* | **mac-address** *mac-address* | **vlan** *vlan-id* } \* ] [ **valid** | **invalid** ] [ **slot** *slot-id* ] command and check the value of **Status** in the command output.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure DHCP snooping so that a dynamic binding table is generated.
   
   
   1. Enable DHCP globally.
      ```
      [dhcp enable](cmdqueryname=dhcp+enable)
      ```
      
      By default, DHCP is disabled globally.
   2. Enable DHCP snooping globally.
      ```
      [dhcp snooping enable](cmdqueryname=dhcp+snooping+enable)
      ```
      
      By default, DHCP snooping is disabled globally.
   3. Configure a trusted interface.
      * Configure a trusted interface in the interface view.
        ```
        [interface](cmdqueryname=interface) interface-type interface-number
        [dhcp snooping enable](cmdqueryname=dhcp+snooping+enable)
        [dhcp snooping trusted](cmdqueryname=dhcp+snooping+trusted)
        [quit](cmdqueryname=quit)
        ```
      * Configure a trusted interface in the VLAN view.
        ```
        [vlan](cmdqueryname=vlan) vlan-id
        [dhcp snooping enable](cmdqueryname=dhcp+snooping+enable)
        [dhcp snooping trusted interface](cmdqueryname=dhcp+snooping+trusted+interface) interface-type interface-number 
        [quit](cmdqueryname=quit)
        ```
3. Enable IPSG.
   
   
   * Enable IPSG in the interface view.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [ipv4 source check user-bind enable](cmdqueryname=ipv4+source+check+user-bind+enable)
     [quit](cmdqueryname=quit)
     ```
   * Enable IPSG in the VLAN view.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [ipv4 source check user-bind enable](cmdqueryname=ipv4+source+check+user-bind+enable)
     [quit](cmdqueryname=quit)
     ```
   
   
   
   By default, IPSG is disabled.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The CE6885-LL in low latency mode does not support [**ipv4 source check user-bind enable**](cmdqueryname=ipv4+source+check+user-bind+enable).
4. (Optional) Configure the IP packet check items.
   
   
   
   After IPSG is enabled, the device checks received IP packets against the binding table and forwards only those that match the binding entries. Among the four check items of IP packets, the interface is mandatory, and the source IP address, source MAC address, and VLAN are optional.
   
   
   
   * Configure IP packet check items in the interface view.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [ip source check user-bind check-item](cmdqueryname=ip+source+check+user-bind+check-item) { ip-address | mac-address | vlan } *
     [quit](cmdqueryname=quit)
     ```
   * Configure IP packet check items in the VLAN view.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [ip source check user-bind check-item](cmdqueryname=ip+source+check+user-bind+check-item) { ip-address | mac-address | interface } *
     [quit](cmdqueryname=quit)
     ```
   
   
   
   By default, the IP packet check items include the IP address, MAC address, VLAN, and interface. If some items are trusted or unfixed (for example, packets from hosts may be received by different interfaces), you can perform this step. The default items are recommended.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The CE6885-LL in low latency mode does not support **ip source check user-bind check-item**.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display ip source check user-bind configuration**](cmdqueryname=display+ip+source+check+user-bind+configuration) [ **vlan** *vlan-id* | **interface** *interface-type* *interface-number* ] command to check the IPSG configuration on an interface or in a VLAN.
* Run the [**display ip source check user-bind statistics**](cmdqueryname=display+ip+source+check+user-bind+statistics) [ **interface** *interface-type* *interface-number* ] command to check statistics on packets discarded due to IPSG.
* Run the [**display ip source check user-bind status**](cmdqueryname=display+ip+source+check+user-bind+status) [ [ **dynamic** [ { **interface** *interface-type* *interface-number* | **ip-address** *ip-address* | **mac-address** *mac-address* | **vlan** *vlan-id* } \* ] [ **valid** | **invalid** ] ] | **summary** ] [ **slot** *slot-id* ] command to check information and status of IPSG dynamic binding entries.