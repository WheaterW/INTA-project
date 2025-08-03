Specifying an IPv4 Address Pool for a Domain and a BAS Interface
================================================================

Users in a domain can obtain addresses from an IPv4 address pool only after the pool is specified for the domain.

#### Context

The IPv4 address pool specified for a domain can be a local or remote address pool.

A maximum of 1024 IPv4 address pools can be specified for a domain, and one address pool can be used for multiple domains. The IPv4 address pools configured for a domain can be moved according to the number of address pools configured in the domain. For example, if 10 address pools are configured in the domain, each address pool can be moved in the range between 1 and 10.

When different users go online through the same domain, to configure different IP address segments for these users, run this command on a BAS interface to limit the IPv4 address range for users in the domain. A maximum of eight address pools can be configured.


#### Procedure

* Specifying an IPv4 address pool for a domain
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**domain**](cmdqueryname=domain) *domain-name*
     
     
     
     The domain view is displayed.
  4. Run [**ip-pool**](cmdqueryname=ip-pool) *pool-name* [ **move-to** *new-position* ]
     
     
     
     An IPv4 address pool is specified for the domain.
  5. Run [**ip-pool-group**](cmdqueryname=ip-pool-group) *group-name*
     
     
     
     An IPv4 address pool group is specified for the domain.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Specifying an IPv4 address pool for a BAS interface
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
     
     
     
     The interface view is displayed.
  3. Run [**bas**](cmdqueryname=bas)
     
     
     
     The BAS interface view is displayed.
  4. Run [**access-type**](cmdqueryname=access-type) **layer2-subscriber** [ **default-domain** { **pre-authentication** *predname* | **authentication** [ **force** | **replace** ] *dname* } \* ]
     
     
     
     The access type and related attributes are configured for Layer 2 common users.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  6. Run [**ip-pool**](cmdqueryname=ip-pool) *pool-name*
     
     
     
     One or more IPv4 address pools are specified for the BAS interface. A maximum of eight address pools can be configured.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.