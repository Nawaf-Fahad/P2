
class RouteTrieNode:
    def __init__(self, handler = None):
        self.handler = handler
        self.children = {}
    
    def insert(self, path_piece, handler):
         self.children[path_piece] = RouteTrieNode(handler)
         
    def __repr__(self):
        return str(self.children)

 
class RouteTrie:
    def __init__(self,root_handler = None):
        self.root = RouteTrieNode(root_handler)

     
    def insert(self, path_pieces, handler):
        
        current_node = self.root
        
        for path_piece in path_pieces:
            if path_piece not in current_node.children:
                current_node.children[path_piece] = RouteTrieNode(None)
            
            current_node = current_node.children[path_piece]
        
        current_node.handler = handler
        

    def find(self, path_pieces):
        
        if len(path_pieces) == 0:
            return self.root.handler
        
        current_node = self.root
        for path_piece in path_pieces:
            if path_piece not in current_node.children:
                return None 
            
            current_node =  current_node = current_node.children[path_piece]
        
        return current_node.handler



      
class Router:
    def __init__(self, handler):
        self.route_trie = RouteTrie(handler)
        self.route_trie.root.handler = handler

    def add_handler(self, path, handler):
        
        path_pieces = self.split_path(path)
        self.route_trie.insert(path_pieces , handler)
        

    def lookup(self,path):
        
        path_pieces = self.split_path(path)
        return  self.route_trie.find(path_pieces)
    
    def split_path(self, path):
        if path == "/":
            return []
        path_pieces = path.split('/')
        
        path_pieces.remove('')
        return path_pieces


router1 = Router("root handler") 
router1.add_handler("/", "root handler") 

print(router1.lookup("/")) # will print 'root handler'

router2 = Router("root handler") 
router2.add_handler("/home/about", "about handler")  # add a route

print(router2.lookup("/")) # 'root handler'
print(router2.lookup("/home")) #  None 
print(router2.lookup("/home/about")) # about handler
print(router2.lookup("/home/about/")) # None
print(router2.lookup("/home/about/me")) # None