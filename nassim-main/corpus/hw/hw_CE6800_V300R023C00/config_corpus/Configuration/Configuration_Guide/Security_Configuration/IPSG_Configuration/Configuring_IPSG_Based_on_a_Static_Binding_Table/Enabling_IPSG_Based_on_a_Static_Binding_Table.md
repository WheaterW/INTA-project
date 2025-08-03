Enabling IPSG Based on a Static Binding Table
=============================================

Enabling IPSG Based on a Static Binding Table

#### Context

IPSG based on a static binding table is applicable to LANs that contain only a few hosts with fixed IP addresses. After creating a static binding table, you need to enable IPSG on an interface or in a VLAN for IPSG to take effect.

* Enabling IPSG on an interface: IPSG checks all packets received by the interface against binding entries. Use this method if you want to perform an IPSG check on specified interfaces and trust other interfaces. This method is suitable for scenarios in which an interface belongs to multiple VLANs, because it eliminates the need to enable IPSG in each VLAN.
* Enabling IPSG in a VLAN: IPSG checks the packets received by all interfaces in the VLAN against binding entries. Use this method if you want to perform an IPSG check in specified VLANs and trust other VLANs. This method is suitable for scenarios in which multiple interfaces belong to the same VLAN, because it eliminates the need to enable IPSG on each interface.

![](public_sys-resources/note_3.0-en-us.png) 

* If you configure IPSG both in VLANs and on interfaces, only the one that is configured first takes effect.

* If ACL resources are insufficient, IPSG configurations exist on the device but the binding table may fail to be delivered. To check whether IPSG takes effect, run the [**display ip source check user-bind status**](cmdqueryname=display+ip+source+check+user-bind+status) **static** [ [ { **interface** *interface-type* *interface-number* | **ip-address** *ip-address* | **mac-address** *mac-address* | **vlan** *vlan-id* } \* ] [ **valid** | **invalid** ] | **summary** ] [ **slot** *slot-id* ] command and check the value of **Status** in the command output.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure static binding entries. 
   
   
   * Configure IPv4 static binding entries.
   
   
   ```
   [user-bind static](cmdqueryname=user-bind+static) { ip-address { start-ip [ to end-ip ] } &<1-10> | mac-address mac-address } * [ interface { interface-type interface-number | interface-name } ] [ vlan vlan-id [ ce-vlan ce-vlan-id ] ]
   ```
   
   By default, no static binding table is configured.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   IPSG matches packets against all items in static binding entries. Ensure that the created binding table is correct and contains all the items to check. The device forwards the packets from hosts only when the packets match all items in binding entries, and discards all other packets.
   
   The device can bind IP addresses or IP address segments in batches. For example, it can bind multiple IP addresses to the same interface or MAC address.
   
   * To bind non-contiguous IP addresses, enter 1 to 10 IP addresses in *start-ip*. For example, run the **user-bind static ip-address 10.0.0.1 10.0.0.3 10.0.0.5 interface 100GE 1/0/1** command to bind IP addresses 10.0.0.1, 10.0.0.3, and 10.0.0.5 to the same interface.
   * To bind contiguous IP addresses, enter 1 to 10 IP address segments using *start-ip* **to** *end-ip*. When the keyword **to** is used, the IP address segments cannot overlap. For example, run the **user-bind static ip-address 10.0.0.1 to 10.0.0.4 mac-address 00e0-fc12-3456** command to bind IP addresses 10.0.0.1 to 10.0.0.4 to the MAC address 00e0-fc12-3456.
3. (Optional) Configure a trusted interface.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the hosts on the network use static IP addresses, you do not need to configure trusted interfaces. However, if the upstream interface is in an IPSG-enabled VLAN, you need to configure the interface as a trusted interface. Otherwise, the return packets will be discarded due to mismatched binding entries. For details, see [IP Packets Are Discarded Because the Upstream Interface Is Not Trusted](galaxy_IPSG_cfg_0019.html). After the upstream interface is configured as trusted, the device forwards the packets received by the interface without checking them against the binding entries.
   
   
   
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
        [dhcp snooping trusted](cmdqueryname=dhcp+snooping+trusted)
        [quit](cmdqueryname=quit)
        ```
      * Configure a trusted interface in the VLAN view.
        ```
        [vlan](cmdqueryname=vlan) vlan-id
        [dhcp snooping trusted interface](cmdqueryname=dhcp+snooping+trusted+interface) interface-type interface-number 
        [quit](cmdqueryname=quit)
        ```
      
      By default, an interface is untrusted.
4. Enable IPSG.
   
   
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
   
   The CE6885-LL in low latency mode does not support **ipv4 source check user-bind enable**.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display ip source check user-bind statistics**](cmdqueryname=display+ip+source+check+user-bind+statistics) [ **interface** *interface-type* *interface-number* ] command to check statistics on packets discarded due to IPSG.
* Run the [**display ip source check user-bind status**](cmdqueryname=display+ip+source+check+user-bind+status) [ [ **static** [ { **interface** *interface-type* *interface-number* | **ip-address** *ip-address* | **mac-address** *mac-address* | **vlan** *vlan-id* } \* ] [ **valid** | **invalid** ] ] | **summary** ] [ **slot** *slot-id* ] command to check information and status of IPSG static binding entries.