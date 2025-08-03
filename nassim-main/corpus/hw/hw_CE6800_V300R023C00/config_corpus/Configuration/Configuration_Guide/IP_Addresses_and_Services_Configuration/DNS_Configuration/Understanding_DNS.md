Understanding DNS
=================

Understanding DNS

#### DNS over the Internet

Initially, the domain names of devices consisted of a sequence of characters. All of these domain names formed a non-hierarchical domain name structure, which makes it inconvenient for administrators to manage a large number of domain names for the following reasons:

* Domain names consist of characters, which may result in a name conflict.
* The domain name structure is not hierarchical. As the number of hostnames increases, so does the management workload.
* The mappings between domain names and IP addresses frequently change. Therefore, maintaining the domain namespace is a huge undertaking.

To address this, a hierarchical domain name structure was defined for the Internet by the DNS in the TCP/IP protocol stack. The DNS divides the Internet into multiple top-level domains (TLDs). [Table 1](#EN-US_CONCEPT_0000001512830982__tab1) lists the domain name of each TLD. TLDs typically represent either an organization type or a geographical location. Geographic TLDs are used to classify domain names based on countries. Before joining the Internet, each country registers a country code TLD that represents their country with the NIC. For example, "cn" represents China, and "us" represents the United States.

**Table 1** TLDs and their meanings
| TLD | Meaning |
| --- | --- |
| com | Commercial organizations |
| edu | Educational agencies |
| gov | Governmental agencies |
| mil | Military departments |
| net | Main network support centers |
| int | International organizations |
| org | Other organizations |
| Country code | Countries (classified in geography mode) |


![](public_sys-resources/note_3.0-en-us.png) 

The first seven domains are defined in organization mode, and the country code domain is defined in geography mode.

The NIC authorizes management agencies to classify domains into sub-domains. The agencies in charge of this can authorize subordinate agencies to continue classifying domains. As a result, the Internet has a hierarchical domain name structure.


#### Static Domain Name Resolution

The DNS supports dynamic and static domain name resolution. Static domain name resolution is first used to resolve a domain name. If the resolution fails, dynamic domain name resolution is used.

Static domain name resolution requires a static domain name resolution table, which is manually created and holds mappings between commonly used domain names and IP addresses. A DNS client first searches the static domain name resolution table for a domain name to resolve it into an IP address. This is an efficient method for domain name resolution.


#### Dynamic Domain Name Resolution

Dynamic domain name resolution requires a dedicated DNS server. This server runs the domain name resolution program, maps domain names to IP addresses, and receives DNS requests from clients.

**Figure 1** Implementation diagram of dynamic domain name resolution  
![](figure/en-us_image_0000001563750909.png)

In [Figure 1](#EN-US_CONCEPT_0000001512830982__fig01), the DNS client, consisting of the resolver and cache, is used to receive and respond to DNS requests from the user program. Typically, the user program, cache, and resolver are located on the same host, whereas the DNS server is on another host. The dynamic domain name resolution process is as follows:

1. When a user program (such as ping or Telnet) uses a domain name to access the network, it sends a DNS request to the resolver of the DNS client.
2. After receiving the request, the resolver first checks the local cache.
   * If the resolver finds the mapping entry for the domain name in the local cache, it directly returns the mapped IP address to the user program.
   * If the resolver does not find such a mapping entry in the local cache, it sends a request to the DNS server.
3. The DNS server checks whether the requested domain name is within a sub-domain it manages and then responds to the DNS client accordingly.
   * If the requested domain name is within a sub-domain it manages, the DNS server searches for the IP address corresponding to the domain name in its own database.
   * If the requested domain name is not within a sub-domain it manages, the DNS server forwards the request to upper-level DNS servers. After completing the resolution, the corresponding upper-level DNS server returns the result to the DNS client.
4. The resolver receives and resolves the response sent by the DNS server, and returns the result to the user program.

Dynamically resolved mappings between domain names and IP addresses are stored in the cache. If a domain name is searched for again, the DNS client obtains the corresponding IP address from the cache directly instead of sending a request to the DNS server. Mappings stored in the cache will expire and be deleted after a period to ensure that the latest mappings can be obtained from the DNS server.


#### DNS Query Types

The IPv4 DNS supports the following query types:

* A query is the most commonly used type of query, and is used to obtain the IP address corresponding to a specified domain name. For example, when you ping or tracert a domain name, a query is sent to the DNS client for the IP address corresponding to the domain name. If the corresponding IP address does not exist on the DNS client, the DNS client sends an A query to the DNS server for obtaining.
* Pointer record (PTR) query means that the DNS client obtains the corresponding domain name based on the IP address. PTRs constitute the mappings between domain names and IP addresses provided by the DNS server for PTR query.

The IPv6 DNS supports the following query types:

* AAAA query: uses a domain name to query an IPv6 address.
* IPv6 PTR query: uses an IPv6 address to query a domain name.