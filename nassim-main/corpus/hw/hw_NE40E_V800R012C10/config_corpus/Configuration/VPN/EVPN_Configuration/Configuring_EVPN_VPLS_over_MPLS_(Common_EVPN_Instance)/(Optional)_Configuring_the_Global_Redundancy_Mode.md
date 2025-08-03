(Optional) Configuring the Global Redundancy Mode
=================================================

A PE's global redundancy mode determines whether the PE can work with other PEs in load-balancing mode.

#### Context

By default, EVPN PEs work in all-active mode. If a CE is multi-homed to several EVPN PEs, these PEs will load-balance traffic. If you do not want to transmit traffic in load balancing mode, you can switch the global redundancy mode of a PE from all-active to single-active. When PEs work in all-active mode, each PE is in the active state. When PEs work in single-active mode, one PE is in the active state, and the other PEs are in the standby state.

In a scenario where a CE is multi-homed to PEs, an Eth-Trunk interface needs to be configured on the CE to connect to the PEs, and an Eth-Trunk interface also needs to be configured on the PEs to connect to the CE. Currently, only E-Trunk can be used to determine the active/standby status of PEs. Perform the following steps on a multi-homed PE:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
   
   
   
   An E-Trunk is configured, and its view is displayed.
3. Run [**priority**](cmdqueryname=priority) *priority*
   
   
   
   An E-Trunk priority value is set.
4. Run [**peer-address**](cmdqueryname=peer-address) *peer-ip-address* **source-address** *source-ip-address*
   
   
   
   IP addresses are configured for the local and peer ends of the E-Trunk.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
   
   
   
   The Eth-Trunk interface view is displayed.
7. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
   
   
   
   The Eth-Trunk interface is added to the E-Trunk.
   
   An Eth-Trunk interface can be added to only one E-Trunk.
8. (Optional) Run [**e-trunk mode**](cmdqueryname=e-trunk+mode) **force-master**
   
   
   
   The E-Trunk member interface is forced to work in master mode.
   
   In an all-active scenario, you need to run this command to set the status of multiple PEs to master to implement load balancing. In single-active scenarios, this command cannot be run on PEs.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
10. Run [**lacp e-trunk system-id**](cmdqueryname=lacp+e-trunk+system-id) *mac-address*
    
    
    
    An E-Trunk Link Aggregation Control Protocol (LACP) system ID is set.
    
    The LACP system IDs for the same E-Trunk must be the same.
11. (Optional) Run [**lacp e-trunk priority**](cmdqueryname=lacp+e-trunk+priority) *priority*
    
    
    
    An E-Trunk LACP system priority value is set.
    
    The LACP system priority values for the same E-Trunk must be the same.
12. (Optional) Run [**evpn redundancy-mode single-active**](cmdqueryname=evpn+redundancy-mode+single-active)
    
    
    
    The global redundancy mode is set to single-active.
    
    In single-active scenarios, this command must be configured on PEs. In all-active scenarios, this command cannot be configured on PEs.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.