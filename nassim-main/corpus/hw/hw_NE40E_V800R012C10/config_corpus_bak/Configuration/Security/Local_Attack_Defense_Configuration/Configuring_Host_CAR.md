Configuring Host CAR
====================

You can configure host CAR to control the rate at which packets are sent to the CPU.

#### Usage Scenario

The system defines a default bandwidth for user-side packets to be sent to the CPU. You can configure host CAR to enable the system to adjust the traffic rate in either of the following scenarios:

* Excessive user-side packets are sent to the CPU, congesting the links and reducing the CPU efficiency.
* Some user-side packets to be sent to the CPU are dropped due to tight rate limits.

In VS mode, this feature is supported only by the admin VS.


#### Pre-configuration Tasks

None


#### Context

To protect against packet attacks, a device implements three levels of CAR: host CAR/HTTP Host CAR, VLAN Host CAR, and CP CAR. For details about CP CAR configurations, see [Configuring the CAR](dc_ne_sysattack_cfg_0017.html).

* Host CAR is implemented based on the source MAC addresses, source IP addresses, or Session IDs carried in PPPoE, DHCP, L2TP, and DHCPv6 packets, IP packets for triggering user access, and ARP packets for triggering user access. HTTP Host CAR is implemented based on the source MAC addresses and source IP addresses carried in web packets. Both host CAR and HTTP Host CAR limit the number of packets to be sent to the CPU from the same host. Therefore, host CAR and HTTP Host CAR are on the same level.
* VLAN Host CAR limits the number of user packets sent to the CPU from hosts in the same VLAN based on the VLAN ID. After VLAN Host CAR is enabled, the device limits the rate at which packets are sent to the CPU from hosts in the same VLAN.
* CP CAR is implemented based on user access modes to limit the number of packets to be sent to the CPU from hosts that access the network in the same mode (for example, PPPoE/DHCP) in a specified period.

Perform the following steps to configure host CAR.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**hostcar**](cmdqueryname=hostcar+cir+pir+cbs+pbs) **cir** *cir-value* [ **pir** *pir-value* ] [ **cbs** *cbs-value* **pbs** *pbs-value* ]
   
   
   
   Host CAR is configured.
4. Run [**hostcar drop-rate enable**](cmdqueryname=hostcar+drop-rate+enable)
   
   
   
   Automatic bandwidth adjustment is enabled.
5. Run [**hostcar attack-detect drop-rate**](cmdqueryname=hostcar+attack-detect+drop-rate) *rate-value*
   
   
   
   The attack detection threshold for the rate at which packets are dropped by host CAR is configured. After the threshold is exceeded, attack detection is started.
6. Run [**hostcar logging**](cmdqueryname=hostcar+logging+interval+discard-threshold) { **interval** *interval-value* | **discard-threshold** *threshold-value* }\*
   
   
   
   Parameters are configured for host CAR logging.
7. Run [**http-hostcar**](cmdqueryname=http-hostcar+cir+pir+cbs+pbs) **cir** *cir-value* [ **pir** *pir-value* ] [ **cbs** *cbs-value* **pbs** *pbs-value* ]
   
   
   
   HTTP Host CAR is configured for web packets to be sent to the CPU.
8. Run [**http-hostcar drop-rate enable**](cmdqueryname=http-hostcar+drop-rate+enable)
   
   
   
   HTTP Host CAR automatic bandwidth adjustment is enabled for web packets.
9. Run [**http-hostcar attack-detect drop-rate**](cmdqueryname=http-hostcar+attack-detect+drop-rate) *rate-value*
   
   
   
   The threshold for the rate at which packets are dropped by HTTP-Host-CAR is configured.
10. Run [**http-hostcar logging**](cmdqueryname=http-hostcar+logging+interval+discard-threshold) { **interval** *interval-value* | **discard-threshold** *threshold-value* }\*
    
    
    
    Parameters are configured for HTTP Host CAR logging.
11. Run [**vlan-host-car**](cmdqueryname=vlan-host-car+cir+pir+cbs+pbs) **cir** *cir-value* [ **pir** *pir-value* ] [ **cbs** *cbs-value* **pbs** *pbs-value* ]
    
    
    
    VLAN Host CAR is configured.
    
    VLAN Host CAR limits the bandwidth of the user-side packets to be sent to the CPU from hosts in the same VLAN.
12. Run [**vlan-host-car drop-rate enable**](cmdqueryname=vlan-host-car+drop-rate+enable)
    
    
    
    VLAN Host CAR automatic bandwidth adjustment is enabled.
13. Run [**vlan-host-car attack-detect drop-rate**](cmdqueryname=vlan-host-car+attack-detect+drop-rate) *rate-value*
    
    
    
    The threshold for the rate at which packets are dropped by VLAN-Host-CAR is configured.
14. Run [**vlan-host-car logging**](cmdqueryname=vlan-host-car+logging+interval+discard-threshold) { **interval** *interval-value* | **discard-threshold** *threshold-value* }\*
    
    
    
    Parameters are configured for VLAN Host CAR logging.
15. (Optional) Run [**ignore-hostcar**](cmdqueryname=ignore-hostcar+ipv6+acl+name) [ **ipv6** ] **acl** { *aclnum* | **name** *aclname* }
    
    
    
    Host CAR and VLAN-Host-CAR do not apply to packets matching the ACL rule.
16. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
17. Run [**quit**](cmdqueryname=quit)
    
    
    
    The system view is displayed.
18. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
    
    
    
    The GE or trunk interface view is displayed.
19. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Checking the Configurations

After configuring host CAR, check the configurations.

* Run the [**display cpu-defend**](cmdqueryname=display+cpu-defend+hostcar+vlan-host-car+http-hostcar+config) { **hostcar** | **vlan-host-car** | **http-hostcar** } **config** **slot** *slot-id* command to check the default and actual rate limiting parameters configured for packets to be sent to the CPU.
* Run the [**display cpu-defend hostcar**](cmdqueryname=display+cpu-defend+hostcar+all+auto-adjust+dropped+non-dropped) { *carid* | **all** | **auto-adjust** | **dropped** | **non-dropped** } **statistics** **slot** *slot-id* command to check host CAR statistics.
* Run the [**display cpu-defend http-hostcar**](cmdqueryname=display+cpu-defend+http-hostcar+all+auto-adjust+dropped) { *carid* | **all** | **auto-adjust** | **dropped** | **non-dropped** } **statistics** **slot** *slot-id* command to check HTTP Host CAR statistics.
* Run the [**display cpu-defend vlan-host-car**](cmdqueryname=display+cpu-defend+vlan-host-car+all+auto-adjust+dropped) { *carid* | **all** | **auto-adjust** | **dropped** | **non-dropped** } **statistics** **slot** *slot-id* command to check VLAN Host CAR statistics.
* Run the [**display cpu-defend hostcar**](cmdqueryname=display+cpu-defend+hostcar+access-user-info+slot) *car-id* **access-user-info** **slot** *slot-id* command to check statistics about a specified host CAR and the information about access users limited by the host CAR, such as MAC addresses, IP addresses, and online status.