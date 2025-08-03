Configuring Fast Convergence for a Multi-Area Adjacency Interface
=================================================================

Configuring fast convergence for a multi-area adjacency interface improves network performance.

#### Procedure

* Configure the interval at which a multi-area adjacency interface sends Hello packets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The OSPF interface view is displayed.
  3. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
     
     
     
     OSPF is enabled on the interface.
  4. Run [**ospf enable multi-area**](cmdqueryname=ospf+enable+multi-area) *area-id*
     
     
     
     OSPF is enabled on the multi-area adjacency interface.
  5. Run [**ospf timer hello**](cmdqueryname=ospf+timer+hello) *interval* **multi-area** *area-id*
     
     
     
     The interval at which Hello packets are sent is configured on the multi-area adjacency interface.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the dead interval of OSPF neighbor relationships for a multi-area adjacency interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The OSPF interface view is displayed.
  3. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
     
     
     
     OSPF is enabled on the interface.
  4. Run [**ospf enable multi-area**](cmdqueryname=ospf+enable+multi-area) *area-id*
     
     
     
     OSPF is enabled on the multi-area adjacency interface.
  5. Run [**ospf timer dead**](cmdqueryname=ospf+timer+dead) *interval* **multi-area** *area-id*
     
     
     
     The dead interval of OSPF neighbor relationships is configured for the multi-area adjacency interface.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an LSA retransmission interval on a multi-area adjacency interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The OSPF interface view is displayed.
  3. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
     
     
     
     OSPF is enabled on the interface.
  4. Run [**ospf enable multi-area**](cmdqueryname=ospf+enable+multi-area) *area-id*
     
     
     
     OSPF is enabled on the multi-area adjacency interface.
  5. Run [**ospf timer retransmit**](cmdqueryname=ospf+timer+retransmit) *interval* **multi-area** *area-id*
     
     
     
     An LSA retransmission interval is configured on the multi-area adjacency interface.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an LSA transmission delay on a multi-area adjacency interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The OSPF interface view is displayed.
  3. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
     
     
     
     OSPF is enabled on the interface.
  4. Run [**ospf enable multi-area**](cmdqueryname=ospf+enable+multi-area) *area-id*
     
     
     
     OSPF is enabled on the multi-area adjacency interface.
  5. Run [**ospf trans-delay**](cmdqueryname=ospf+trans-delay) *delayValue* **multi-area** *area-id*
     
     
     
     An LSA transmission delay is configured on the multi-area adjacency interface.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure smart-discover on a multi-area adjacency interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The OSPF interface view is displayed.
  3. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
     
     
     
     OSPF is enabled on the interface.
  4. Run [**ospf enable multi-area**](cmdqueryname=ospf+enable+multi-area) *area-id*
     
     
     
     OSPF is enabled on the multi-area adjacency interface.
  5. Run [**ospf smart-discover**](cmdqueryname=ospf+smart-discover) **multi-area** *area-id*
     
     
     
     Smart-discover is enabled on the multi-area adjacency interface.
     
     
     
     Without smart-discover, if the neighbor status of a device on a P2P network changes or the DR or BDR on a multi-access network (broadcast or NBMA network) changes, Hello packets are not sent to neighbors until the Hello timer expires. This slows down the establishment of neighbor relationships. With smart-discover, Hello packets are sent to neighbors immediately in this case, regardless of the Hello timer. This speeds up neighbor relationship establishment and network convergence.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an OSPF multi-area adjacency interface to filter the LSAs to be sent.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The OSPF interface view is displayed.
  3. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
     
     
     
     OSPF is enabled on the interface.
  4. Run [**ospf enable multi-area**](cmdqueryname=ospf+enable+multi-area) *area-id*
     
     
     
     OSPF is enabled on the multi-area adjacency interface.
  5. Run **[**ospf filter-lsa-out**](cmdqueryname=ospf+filter-lsa-out)** { **all** | { **ase** [ **acl** { *ase-acl-num* | *ase-acl-name* } ] | **nssa** [ **acl** { *nssa-acl-num* | *nssa-acl-name* } ] | **summary** [ **acl** { *sum-acl-num* | *sum-acl-name* } ] } \* } **multi-area** *area-id*
     
     
     
     The device is configured to filter the OSPF LSAs to be sent.
     
     
     
     If multiple links exist between two devices, you can configure this filtering function to ensure that the matched LSAs are not transmitted through some of the links. This prevents unnecessary retransmissions and saves bandwidth resources.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.