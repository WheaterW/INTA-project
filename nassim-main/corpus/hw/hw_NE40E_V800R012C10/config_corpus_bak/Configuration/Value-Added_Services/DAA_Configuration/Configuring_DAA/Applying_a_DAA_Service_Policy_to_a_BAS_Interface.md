Applying a DAA Service Policy to a BAS Interface
================================================

Applying a DAA service policy to a BAS interface allows access control between users in an enterprise as well as policy sharing between users in different enterprises.

#### Context

When enterprise users access the Router over a Layer 3 leased line, each enterprise belongs to a VPN. You can apply a DAA service policy to a BAS interface to allow access control between users in an enterprise as well as policy sharing between users in different enterprises. When Layer 2 or Layer 3 leased line users are not authenticated, applying a DAA service policy to a BAS interface is also required to allow access control between Layer 2 or Layer 3 leased line users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**bas**](cmdqueryname=bas)
   
   
   
   The BAS interface view is displayed.
4. Run [**access-type**](cmdqueryname=access-type) **layer2-leased-line** **user-name** *uname* **password** { **cipher** *password* | **simple** *password* } [ **bas-interface-name** *bname* | **default-domain** **authentication** *dname* | **accounting-copy** **radius-server** *rd-name* | **nas-port-type** { **async** | **sync** | **isdn-sync** | **isdn-async-v120** | **isdn-async-v110** | **virtual** | **piafs** | **hdlc** | **x.25** | **x.75** | **g.3-fax** | **sdsl** | **adsl-cap** | **adsl-dmt** | **idsl** | **ethernet** | **xdsl** | **cable** | **wireless-other** | **802.11** } ] \* or [**access-type**](cmdqueryname=access-type) **layer3-leased-line** { **user-name** *uname* | **user-name-template** } **password** { **cipher** *password* | **simple** *password* } [ **default-domain** **authentication** *dname* | **bas-interface-name** *bname* | **accounting-copy** **radius-server** *rd-name* | **nas-port-type** { **async** | **sync** | **isdn-sync** | **isdn-async-v120** | **isdn-async-v110** | **virtual** | **piafs** | **hdlc** | **x.25** | **x.75** | **g.3-fax** | **sdsl** | **adsl-cap** | **adsl-dmt** | **idsl** | **ethernet** | **xdsl** | **cable** | **wireless-other** | **802.11** } | **mac-address** *mac-address* | **client-id** *client-id* ] \*
   
   
   
   The BAS interface is configured as a Layer 2 or Layer 3 leased line interface.
5. Run [**value-added-service policy**](cmdqueryname=value-added-service+policy) *policy-name*
   
   
   
   A DAA service policy is applied to the BAS interface.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.