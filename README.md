# ElasticSearch
- Open Source 
- Text search performance

# ElasticStack
- Open Source 
- (Solutions)[https://www.elastic.co/downloads/]
	- SaaS solutions for elastic orquestration
- (Use Cases)[https://www.elastic.co/customers/]

# Kibana
- Data Visualization - (Examples)[https://www.elastic.co/blog/elasticsearch-free-open-limitless]

# Data Indexing
- Inverted index

# Instalation
- For ElasticSearch 5 and later, set the maximum number of mapped memory areas a process can have: `sudo sysctl -w vm.max_map_count=262144`

- Simple docker compose with elastic search and kibana. For this project the configuration `discovery.type=single-node` is used. For more discovery options see [link](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-discovery-settings.html) 

- To run ElasticSearch:
	`docker-compose up`

- To stop the services:
	`docker-compose down`

- More detailed information:
	- [Install ElasticSearch with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/master/docker.html#docker-cli-run-dev-mode)
	- [Install Kibana with Docker](https://www.elastic.co/guide/en/kibana/current/docker.html)