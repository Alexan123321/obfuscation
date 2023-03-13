import ast
import random
import string
import sys

def obfuscate_filename(filename):
    # Read the contents of the file
    with open(filename) as f:
        source = f.read()

    # Parse the source code into an AST
    tree = ast.parse(source)

    # Define a visitor to modify the AST
    class Obfuscator(ast.NodeTransformer):
        def __init__(self):
            self.var_map = {}

        def visit_Name(self, node):
            # Replace variable names with random strings
            if isinstance(node.ctx, ast.Load):
                if node.id not in self.var_map:
                    self.var_map[node.id] = ''.join(random.choices(string.ascii_lowercase, k=10))
                node.id = self.var_map[node.id]
            return node

        def visit_Str(self, node):
            # Replace string literals with their reverse
            node.s = node.s[::-1]
            return node

    # Apply the visitor to the AST
    tree = Obfuscator().visit(tree)

    # Generate the new source code from the modified AST
    new_source = ast.unparse(tree)

    # Write the new source code to the same file
    with open(filename, 'w') as f:
        f.write(new_source)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <filename>')
        sys.exit(1)
    obfuscate_filename(sys.argv[1])
