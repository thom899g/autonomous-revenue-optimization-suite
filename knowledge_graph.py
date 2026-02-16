from typing import Optional, Dict, Any
import networkx as nx

class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.Graph()
        
    def add_node(self, node_id: str, node_data: Dict[str, Any]) -> None:
        """
        Add a node to the knowledge graph.
        Args:
            node_id: Unique identifier for the node.
            node_data: Data associated with the node.
        """
        try:
            self.graph.add_node(node_id, **node_data)
        except Exception as e:
            raise RuntimeError(f"Failed to add node {node_id}: {str(e)}")
    
    def add_edge(self, from_node: str, to_node: str, edge_data: Optional[Dict[str, Any]] = None) -> None:
        """
        Add an edge between two nodes.
        Args:
            from_node: Source node identifier.
            to_node: Target node identifier.
            edge_data: Data associated with the edge.
        """
        try:
            self.graph.add_edge(from_node, to_node, **(edge_data or {}))
        except Exception as e:
            raise RuntimeError(f"Failed to add edge between {from_node} and {to_node}: {str(e)}")