(Optional) Configuring Gateway Unnumbered
=========================================

(Optional)_Configuring_Gateway_Unnumbered

#### Context

Generally, a RADIUS server delivers IP addresses in the domain address pool to common Layer 2 DHCP users. If the delivered IP addresses are not in the domain address pool, users cannot go online. To enable common Layer 2 DHCP users to go online with IP addresses delivered by the RADIUS server but not in the domain address pool, configure gateway unnumbered.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**access gateway unnumbered loopback user-type ipoe**](cmdqueryname=access+gateway+unnumbered+loopback+user-type+ipoe)
   
   
   
   Gateway unnumbered is enabled.
3. (Optional) Run [**access frame-ip lease manage pool-exclude**](cmdqueryname=access+frame-ip+lease+manage+pool-exclude)
   
   
   
   Lease management is enabled for IP addresses delivered by the RADIUS server but not in the domain address pool.
4. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
   
   
   
   The loopback interface view is displayed.
5. Run [**access gateway unnumbered**](cmdqueryname=access+gateway+unnumbered)
   
   
   
   Gateway unnumbered is enabled on the loopback interface.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.