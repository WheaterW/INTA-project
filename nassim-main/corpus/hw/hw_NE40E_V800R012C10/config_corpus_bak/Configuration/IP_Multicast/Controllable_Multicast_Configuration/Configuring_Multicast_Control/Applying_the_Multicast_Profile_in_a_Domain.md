Applying the Multicast Profile in a Domain
==========================================

After a multicast profile is bound to a domain, the users in this domain have the rights to access the multicast lists bound to the multicast profile.

#### Context

Perform the following steps on the Router:

Choose one of the following configurations as required:

* Binding a multicast profile to a domain on an IPv4 network
* Binding a multicast profile to a domain on an IPv6 network

#### Procedure

* Binding a multicast profile to a domain on an IPv4 network
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**domain**](cmdqueryname=domain) *domain-name*
     
     
     
     The domain view is displayed.
  4. Run [**multicast-profile**](cmdqueryname=multicast-profile) *profile-name*
     
     
     
     An IPv4 multicast profile is bound to the domain.
     
     
     
     After a multicast profile is bound to a domain, the users in this domain have the rights to access the multicast lists bound to the multicast profile. One domain can use only one multicast profile. If multiple multicast profiles are bound to the domain, the latest binding takes effect.
* Binding a multicast profile to a domain on an IPv6 network
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**domain**](cmdqueryname=domain) *domain-name*
     
     
     
     The domain view is displayed.
  4. Run [**multicast-profile ipv6**](cmdqueryname=multicast-profile+ipv6) *profile-name*
     
     
     
     An IPv6 multicast profile is bound to the domain.
     
     
     
     After a multicast profile is bound to a domain, the users in this domain have the rights to access the multicast lists bound to the multicast profile. One domain can use only one multicast profile. If multiple multicast profiles are bound to the domain, the latest binding takes effect.