Using GMAC Trace to Check a Path on a Layer 2 Network
=====================================================

Generic MAC (GMAC) trace can be used to monitor paths and locate faults in a part of or a whole network without configuring an MD, MA, or MEP.

#### Context

GMAC trace has principles similar to those of 802.1ag MAC trace. The difference is that a source device does not need to be a MEP, and a destination device does not need to be a MEP or MIP. In other words, GMAC trace can be implemented without the need to configure an MD, MA, or MEP on the source, intermediate, or destination device.

Enable the GMAC trace function on the source, intermediate, and destination devices.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**trace mac enable**](cmdqueryname=trace+mac+enable)
   
   
   
   The GMAC trace function is enabled globally.
   
   
   
   If the GMAC trace function is enabled:
   
   * A source device starts the GMAC trace function by sending a linktrace message (LTM) to a destination device.
   * After receiving the LTM, the destination device replies to the source device with a linktrace reply (LTR).
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
4. (Optional) In a VLAN scenario: Run [**trace mac**](cmdqueryname=trace+mac) *mac-address* **vlan** *vlan-id* [ **interface** *interface-type interface-number* | **-t** *timeout* ] \*
   
   
   
   Paths on a VLAN are checked.
   
   
   
   The following is an example:
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] trace mac enable 
   [*HUAWEI] commit 
   [~HUAWEI] trace mac 00e0-fc23-3459 vlan 2
   Tracing the route to 00e0-fc23-3459 over a maximum of 255 hops: 
   ------------------------------------------------------------------------------- 
   Hops     Mac                Ingress                     Ingress Action      Relay Action
             Forwarded         Egress                      Egress Action                    
   -------------------------------------------------------------------------------- 
   1     00e0-fc12-3459      gigabitethernet0/2/1      IngOK                 RlyFDB 
         Forwarded            gigabitethernet0/1/1       EgrOK       
   2     00e0-fc12-3457      gigabitethernet0/1/1       IngOK                RlyFDB         
         Forwarded            gigabitethernet0/1/0       EgrOk         
   3     00e0-fc23-3459      gigabitethernet0/1/0       IngOK                RlyHit        
         Not Forwarded 
   Info: Succeed in tracing the destination address 00e0-fc23-3459. 
   ```
5. (Optional) In a VLL scenario: Run [**trace mac**](cmdqueryname=trace+mac) *mac-address* **l2vc** *l2vc-id* { **raw** | **tagged** } [ **interface** *interface-type* *interface-number* | { [ **pe-vid** *pe-vid* **ce-vid** *ce-vid* ] | [ **dot1q-vlan** *vlan-id* ] } | **-t** *timeout* | **-h** ] \*
   
   
   
   The VLL network connectivity is checked.
   
   
   
   The following shows an example:
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] trace mac enable 
   [*HUAWEI] commit
   [~HUAWEI] trace mac 00e0-fc12-3458 l2vc 1 raw
   Tracing the route to 00e0-fc12-3458 over a maximum of 255 hops:
    Hops  Host Name (IP Address)
          Mac             Ingress                   Ingress Action    Relay Action
          Forwarded       Egress                    Egress Action   
   1     HUAWEIA (10.10.10.16)
         00e0-fc22-3459  GigabitEthernet0/2/1           IngOK             RlyFDB
         Forwarded       GigabitEthernet0/1/1.1         EgrOK               
   2     HUAWEIB (10.10.10.13)
         00e0-fc12-3458  GigabitEthernet0/3/1           IngOK             RlyHit
         Not Forwarded 
   Info: Succeeded in tracing the destination address 00e0-fc12-3458.
   ```
6. (Optional) In a VPLS scenario: Run [**trace mac**](cmdqueryname=trace+mac) *mac-address* **vsi** *vsi-name* [ **interface** *interface-type* *interface-number* | { [ **pe-vid** *pe-vid* **ce-vid** *ce-vid* ] | [ **dot1q-vlan** *vlan-id* ] } | **-t** *timeout* | **-h** ] \*
   
   
   
   The VPLS network connectivity is checked.
   
   
   
   The following shows an example:
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] trace mac enable 
   [*HUAWEI] commit 
   [~HUAWEI] trace mac 00e0-fc12-3458 vsi vsi1 -h
   Tracing the route to 00e0-fc12-3458 over a maximum of 255 hops:
    Hops  Host Name (IP Address)
           Mac             Ingress                   Ingress Action    Relay Action
           Forwarded       Egress                    Egress Action    
   1     HUAWEIA (10.10.10.16)        
         00e0-fc22-3459  GigabitEthernet0/2/1           IngOK             RlyFDB
         Forwarded       GigabitEthernet0/1/1.1         EgrOK                
   2     HUAWEIB (10.10.10.13)
         00e0-fc12-3458  GigabitEthernet0/3/1           IngOK             RlyHit
         Not Forwarded  
   Info: Succeeded in tracing the destination address 00e0-fc12-3458. 
   ```