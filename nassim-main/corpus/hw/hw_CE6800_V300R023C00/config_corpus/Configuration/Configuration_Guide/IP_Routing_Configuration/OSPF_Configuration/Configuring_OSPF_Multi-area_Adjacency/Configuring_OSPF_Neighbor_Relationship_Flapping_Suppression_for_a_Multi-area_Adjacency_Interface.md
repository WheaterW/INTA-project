Configuring OSPF Neighbor Relationship Flapping Suppression for a Multi-area Adjacency Interface
================================================================================================

Configuring OSPF Neighbor Relationship Flapping Suppression for a Multi-area Adjacency Interface

#### Prerequisites

Before configuring OSPF neighbor relationship flapping suppression for a multi-area adjacency interface, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

If an interface carrying OSPF services frequently alternates between up and down, OSPF neighbor relationship flapping will occur on the interface. In this case, OSPF quickly sends Hello packets to re-establish neighbor relationships, synchronizes LSDBs, and triggers route calculation. As a result, a large number of packets are exchanged, compromising the stability of existing neighbor relationships, OSPF services, and other OSPF-dependent services (such as BGP). OSPF neighbor relationship flapping suppression can be used to address this issue. If OSPF neighbor relationships flap frequently, this function delays the re-establishment of the relationships or prevents service traffic from passing through flapping links.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Disable OSPF neighbor relationship flapping suppression globally.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   [suppress-flapping peer disable](cmdqueryname=suppress-flapping+peer+disable)
   [quit](cmdqueryname=quit)
   ```
   
   By default, OSPF neighbor relationship flapping suppression is enabled globally. That is, this function is enabled on each interface in an OSPF process. To disable this function globally, perform this step.
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Enable OSPF on the interface.
   
   
   ```
   [ospf enable](cmdqueryname=ospf+enable) [ process-id ] area area-id
   ```
5. Configure a multi-area adjacency interface and enable OSPF for it.
   
   
   ```
   [ospf enable multi-area](cmdqueryname=ospf+enable+multi-area) area-id
   ```
6. (Optional) Disable OSPF neighbor relationship flapping suppression on the multi-area adjacency interface.
   
   
   ```
   [ospf suppress-flapping peer disable multi-area](cmdqueryname=ospf+suppress-flapping+peer+disable+multi-area) area-id
   ```
   
   By default, OSPF neighbor relationship flapping suppression is enabled globally. That is, this function is enabled on each multi-area adjacency interface in an OSPF process. To disable OSPF neighbor relationship flapping suppression on a specified interface, perform this step.
7. Enable the Hold-down mode and set a corresponding duration for the multi-area adjacency interface.
   
   
   ```
   [ospf suppress-flapping peer hold-down](cmdqueryname=ospf+suppress-flapping+peer+hold-down) interval multi-area area-id
   ```
   
   OSPF neighbor relationship flapping suppression operates in two modes:
   
   * Hold-down mode: If flooding and topology changes frequently occur during the establishment of neighbor relationships, re-establishment of these relationships is disabled during Hold-down suppression. This minimizes LSDB synchronization attempts and packet exchanges.
   * Hold-max-cost mode: If the traffic forwarding path changes frequently, interfaces use 65535 (maximum value) as the cost of the flapping link during Hold-max-cost suppression. This prevents traffic from passing through the flapping link.
   
   By default, the Hold-max-cost mode is enabled. If both modes are enabled, flapping suppression initially works in Hold-down mode (until its duration expires) and then in Hold-max-cost mode.
8. (Optional) Disable the Hold-max-cost mode.
   
   
   ```
   [ospf suppress-flapping peer](cmdqueryname=ospf+suppress-flapping+peer) hold-max-cost disable multi-area area-id
   ```
9. (Optional) Configure detection parameters for neighbor relationship flapping suppression on the OSPF multi-area adjacency interface.
   
   
   ```
   [ospf suppress-flapping peer](cmdqueryname=ospf+suppress-flapping+peer) { detecting-interval detecting-interval | threshold threshold | resume-interval resume-interval } * multi-area area-id
   ```
   
   Parameters in this command are described as follows:
   
   * **detecting-interval**: indicates the detection interval for OSPF neighbor relationship flapping suppression. When configured with OSPF neighbor relationship flapping suppression, an OSPF interface starts a flapping counter. If the interval between two successive neighbor relationship states (changing from Full to a non-Full state) is shorter than the *detecting-interval*, a valid flapping\_event is recorded, and the flapping\_count is incremented by 1.
   * **threshold**: indicates the threshold for OSPF neighbor relationship flapping suppression. When the flapping\_count reaches or exceeds the *threshold* value, flapping suppression occurs.
   * **resume-interval**: indicates the interval for exiting OSPF neighbor relationship flapping suppression. If the interval between two successive neighbor relationship states (changing from Full to a non-Full state) is longer than the *resume-interval*, the flapping\_count is reset. If OSPF neighbor relationship flapping suppression works in Hold-max-cost mode, the value of *resume-interval* indicates the duration of this mode.
   * The value of *resume-interval* must be greater than that of *detecting-interval*.
   
   You can configure detection parameters for OSPF neighbor relationship flapping suppression on specific interfaces according to network conditions. However, using the default values of these parameters is recommended. By default, the detection interval for OSPF neighbor relationship flapping suppression is 60 seconds, the suppression threshold is 10, and the interval for exiting flapping suppression is 120 seconds.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```
11. (Optional) Configure the OSPF multi-area adjacency interface to exit neighbor relationship flapping suppression.
    
    
    ```
    [quit](cmdqueryname=quit)
    [quit](cmdqueryname=quit)
    [reset ospf](cmdqueryname=reset+ospf) process-id suppress-flapping peer [ interface-name [ all-areas | area area-id ] | interface-type interface-number [ all-areas | area area-id ] ] [ notify-peer ]
    ```
    
    
    ![](../public_sys-resources/note_3.0-en-us.png) 
    
    Interfaces exit flapping suppression in the following scenarios:
    
    * The suppression timer expires.
    * The corresponding OSPF process is reset.
    * An OSPF neighbor relationship is reset using the [**reset ospf peer**](cmdqueryname=reset+ospf+peer) command.
    * OSPF neighbor relationship flapping suppression is disabled globally using the [**suppress-flapping peer disable**](cmdqueryname=suppress-flapping+peer+disable) command in the OSPF view.