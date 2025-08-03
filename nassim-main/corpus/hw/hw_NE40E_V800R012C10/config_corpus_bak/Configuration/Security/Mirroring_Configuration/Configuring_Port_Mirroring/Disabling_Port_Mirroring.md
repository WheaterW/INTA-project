Disabling Port Mirroring
========================

When the port mirroring function is not required, disable it so that it does not adversely affect user services.

#### Context

When disabling port mirroring, you can delete the observing port configuration of the involved board, the observing port configuration of the involved interface, and the mirrored-port configuration of the involved interface in any sequence.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**undo mirror to observe-index**](cmdqueryname=undo+mirror+to+observe-index) *observe-index*
   
   
   
   The observing port configuration of the board is deleted.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**undo observe user-defined-filter**](cmdqueryname=undo+observe+user-defined-filter) *id*
   
   
   
   The user-defined any-byte matching rule for mirrored packets is deleted.
6. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   This interface functions as the observing port.
7. Run [**undo port-observing observe-index**](cmdqueryname=undo+port-observing+observe-index) *observe-index* [ **without-filter** ]
   
   
   
   The observing port configuration of the interface is deleted.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   This interface functions as the mirrored port.
10. Cancel the following port mirroring configurations as required:
    1. Run the [**undo port-mirroring**](cmdqueryname=undo+port-mirroring) { **inbound** [ **cpu-packet** ] | **outbound** } [ **user-defined-filter** *user-defined-filter-id* ] command to delete the mirrored-port configuration of the interface.
    2. Run the [**undo port-mirroring**](cmdqueryname=undo+port-mirroring) { **inbound** | **outbound** } **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } command to delete the configuration of the Layer 2 mirrored port.
    3. Run the [**undo port-mirroring to**](cmdqueryname=undo+port-mirroring+to) **observe-index** *observe-index* command to delete the configuration used to specify an observing port for the upstream and downstream packets of the mirrored port.
    4. Run the [**undo port-mirroring to**](cmdqueryname=undo+port-mirroring+to) **observe-index** *observe-index* &<2-8> [ **inbound | outbound** ] command to delete the configuration used to specify multiple observing ports for the upstream or downstream packets of the mirrored port.
    5. Run the [**undo port-mirroring to**](cmdqueryname=undo+port-mirroring+to) **null0** command to delete the configuration used to specify the observing port null0 for the upstream and downstream packets of the mirrored port.
    6. Run the [**undo port-mirroring to**](cmdqueryname=undo+port-mirroring+to) **observe-index** *observe-index* { **inbound | outbound** } command to delete the configuration used to specify an observing port for the upstream or downstream packets of the mirrored port.
    7. Run the [**undo port-mirroring instance**](cmdqueryname=undo+port-mirroring+instance) *instance-name* { **inbound** | **outbound** } **pe-vid** *pe-vlan-id* **ce-vid** *ce-vlan-id-begin* [**to** *ce-vlan-id-end* ] command to delete the port mirroring configuration.
    8. Run the [**undo port-mirroring instance**](cmdqueryname=undo+port-mirroring+instance) *instance-name* { **inbound** | **outbound** } **vid** *vlan-id-begin* [**to** *vlan-id-end* ] command to delete the port mirroring configuration.
    9. Run the [**undo port-mirroring instance**](cmdqueryname=undo+port-mirroring+instance) *instance-name* { **inbound** | **outbound** } command to delete the port mirroring configuration.
    10. Run the [**undo mirror instance**](cmdqueryname=undo+mirror+instance) *instance-name* command to delete the mirroring instance configuration.
    11. Run the [**undo port-mirroring to**](cmdqueryname=undo+port-mirroring+to) { **null0** | **interface** *interface-type* *interface-number* **observe-index** *observe-index* } { **inbound** | **cpu-packet** | **outbound** } [ **user-defined-filter** *user-defined-filter-id* ] command to delete the port mirroring in integrated mode configuration.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.