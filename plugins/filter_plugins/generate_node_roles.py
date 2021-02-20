#!/user/bin/python3

from ansible import errors

ELASTICSEARCH_NODE_ROLE_MAP = {
  'master_nodes': 'master',
  'data_nodes': 'data',
  'data_content_nodes': 'data_content',
  'data_hot_nodes': 'data_hot',
  'data_warm_nodes': 'data_warm',
  'data_cold_nodes': 'data_cold',
  'ingest_nodes': 'ingest',
  'machine_learning_nodes': 'ml',
  'remote_elgible_nodes': 'remote_cluster_client',
  'transform_nodes': 'transform'
}

def generate_node_roles(group_names):
  # Return empty list if coordinating only node
  if 'coord_only_nodes' in group_names:
    return 'node.roles: []'

  roles = []
  for group in group_names:
    role = ELASTICSEARCH_NODE_ROLE_MAP.get(group, None)
    if role is not None:
      roles.append(role)
  return f'node.roles: {roles}'


class FilterModule(object):
  def filters(self):
    return {
      'generate_node_roles': generate_node_roles
    }