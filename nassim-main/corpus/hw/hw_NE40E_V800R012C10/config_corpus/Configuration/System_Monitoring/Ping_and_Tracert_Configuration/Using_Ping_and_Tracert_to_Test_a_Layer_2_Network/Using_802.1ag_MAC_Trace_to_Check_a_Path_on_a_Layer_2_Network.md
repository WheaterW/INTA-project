Using 802.1ag MAC Trace to Check a Path on a Layer 2 Network
============================================================

802.1ag MAC trace monitors the connectivity between MEPs or between MEPs and MIPs within an MA and provides information used to locate faults.

#### Context

Similar to traceroute or tracert, 802.1ag MAC trace tests the path between the local device and a destination device or locates failure points by sending test packets and receiving reply packets.

Before performing 802.1ag MAC trace, ensure that 802.1ag has been configured. For details, see [Configuring Basic Ethernet CFM Functions](dc_vrp_cfm_cfg_000004.html).


#### Procedure

1. A device is usually configured with multiple MDs and MAs. To determine the forwarding path for sending packets from a MEP to another MEP or a MIP in an MA or failure points, perform either of the following operations on the Router with a MEP at one end of the link to be tested.
   
   
   * In the MA view:
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. (Optional) Run [**cfm portid-tlv type**](cmdqueryname=cfm+portid-tlv+type) { ****interface-name**** | ****local**** }
        
        The portid-tlv type in trace packets is configured.
     3. Run the [**cfm enable**](cmdqueryname=cfm+enable) command to globally enable the CFM function on the device.
     4. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     5. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     6. Run the [**trace mac-8021ag**](cmdqueryname=trace+mac-8021ag) **mep** **mep-id** *mep-id* [ **md** *md-name* **ma** *ma-name* ] { **mac** *mac-address* | **remote-mep** **mep-id** *mep-id* } [ **-t** *timeout* | **ttl** *ttl* ] \* command to locate the connectivity fault between the local and peer devices.
        + Run the **trace mac-8021ag** command without **md** *md-name* **ma** *ma-name* specified in the MA view to monitor a forwarding path or locate a failure point in the current MA.
        + Run the **trace mac-8021ag** **md** *md-name* **ma** *ma-name* command in the MA view to monitor a forwarding path or locate a failure point in the specified MA.
          
          An example is as follows:
          
          ```
          <HUAWEI> system-view 
          [~HUAWEI] cfm enable
          [*HUAWEI] cfm md md1 
          [*HUAWEI-md-md1] ma ma1 
          [*HUAWEI-md-md1-ma-ma1] trace mac-8021ag mep mep-id 1 md md1 ma ma1 remote-mep mep-id 8
          Tracing the route to 00e0-fc12-3458 over a maximum of 64 hops: 
           Hops  Ingress Mac    Ingress Port                Ingress Action    Relay Action
                 Egress Mac     Egress Port                 Egress Action     Ismep 
           1     00e0-fc23-3459 GigabitEthernet0/1/1        IngOK             RlyFDB
                 00e0-fc22-3459 GigabitEthernet0/1/2        EgrOK             NoMep 
           2     --             --                          --                RlyHit
                 00e0-fc12-3458 GigabitEthernet0/1/3        EgrOK             IsMep 
          Info: Succeeded in tracing the destination address 00e0-fc12-3458. 
          ```
   * In all views except the MA view:
     
     1. (Optional) Run [**cfm portid-tlv type**](cmdqueryname=cfm+portid-tlv+type) { **interface-name** | **local** }
        
        The portid-tlv type for trace packets is set.
     2. Run [**trace mac-8021ag**](cmdqueryname=trace+mac-8021ag) **mep** **mep-id** *mep-id* **md** *md-name* **ma** *ma-name* { **mac** *mac-address* | **remote-mep** **mep-id** *mep-id* } [ **-t** *timeout* | **ttl** *ttl* ] \*
        
        The connectivity fault between the local and the remote devices is located.
   
   When implementing 802.1ag MAC trace, ensure that:
   
   * The MEP is configured in the MA.
   * If the destination node is an RMEP, either **mac** *mac-address* or **remote-mep** **mep-id** *mep-id* can be specified. If **remote-mep** **mep-id** *mep-id* is selected, the RMEP must already be created using the [**remote-mep**](cmdqueryname=remote-mep) command.
   * If the destination node is a MIP, select **mac** *mac-address*.
   * If the forwarding entry of the destination node does not exist in the MAC address table, **interface** *interface-type* *interface-number* must be specified.
2. (Optional) Run the [**display cfm statistics lblt**](cmdqueryname=display+cfm+statistics+lblt) command to check 802.1ag protocol packet statistics.
   
   
   
   If the test using the [**trace mac-8021ag**](cmdqueryname=trace+mac-8021ag) command fails, you can run this command to check whether a link fault or a device fault occurs.
3. (Optional) Run the [**reset cfm statistics lblt**](cmdqueryname=reset+cfm+statistics+lblt) command to clear the 802.1ag protocol packet statistics.